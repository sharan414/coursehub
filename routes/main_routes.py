from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main_routes', __name__)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'teacher':
        return render_template('teacher_dashboard.html', user=current_user)
    else:
        return render_template('student_dashboard.html', user=current_user)
