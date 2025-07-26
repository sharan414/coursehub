from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.models import Quiz, Question, Submission, User
from extensions import db

quiz_bp = Blueprint('quiz_routes', __name__)

@quiz_bp.route('/create_quiz', methods=['GET', 'POST'])
@login_required
def create_quiz():
    if request.method == 'POST':
        title = request.form['title']
        new_quiz = Quiz(title=title)
        db.session.add(new_quiz)
        db.session.commit()
        return redirect(url_for('quiz_routes.add_questions', quiz_id=new_quiz.id))

    # Provide an empty quiz object for initial rendering
    return render_template('create_quiz.html', quiz=Quiz(title=""))


@quiz_bp.route('/add_questions/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def add_questions(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    if request.method == 'POST':
        q_text = request.form['question']
        options = {
            'A': request.form['option_a'],
            'B': request.form['option_b'],
            'C': request.form['option_c'],
            'D': request.form['option_d']
        }
        correct = request.form['correct_option']
        question = Question(
            text=q_text, option_a=options['A'], option_b=options['B'],
            option_c=options['C'], option_d=options['D'],
            correct_option=correct, quiz_id=quiz_id
        )
        db.session.add(question)
        db.session.commit()
    return render_template('add_questions.html', quiz=quiz)

@quiz_bp.route('/available_quizzes')
@login_required
def available_quizzes():
    quizzes = Quiz.query.all()
    return render_template('available_quizzes.html', quizzes=quizzes)

@quiz_bp.route('/take_quiz/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    questions = quiz.questions

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected = request.form.get(f'q{question.id}')
            if selected == question.correct_option:
                score += 1
        submission = Submission(student_id=current_user.id, quiz_id=quiz_id, score=score)
        db.session.add(submission)
        db.session.commit()
        return redirect(url_for('quiz_routes.quiz_result', quiz_id=quiz_id, score=score))

    return render_template('take_quiz.html', quiz=quiz, questions=questions)

@quiz_bp.route('/quiz_result/<int:quiz_id>/<int:score>')
@login_required
def quiz_result(quiz_id, score):
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('quiz_results.html', quiz=quiz, score=score)

@quiz_bp.route('/quiz_results')
@login_required
def quiz_results():
    quizzes = Quiz.query.filter_by(created_by=current_user.id).all()
    results = []
    for quiz in quizzes:
        submissions = Submission.query.filter_by(quiz_id=quiz.id).all()
        results.append({"quiz": quiz, "submissions": submissions})
    return render_template("quiz_results.html", results=results)