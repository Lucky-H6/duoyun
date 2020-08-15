from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)


@user_bp.route('/login/')
def login():
    # !TODO return login page
    return render_template('login.html')


@user_bp.route('/register/')
def register():
    # !TODO return register page
    return render_template('register.html')


@user_bp.route('/user/center/')
def user_center():
    # !TODO return user center page
    return render_template('user_center.html')


@user_bp.route('/user/workspace/')
def user_workspace():
    # !TODO return user workspace page
    return "user_workspace"


@user_bp.route('/publisher/center/')
def publisher_center():
    # !TODO return publisher center page
    return render_template('publisher_center.html')


@user_bp.route('/publisher/workspace/')
def publisher_workspace():
    # !TODO return publisher workspace page
    return "publisher_workspace"
