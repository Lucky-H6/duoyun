from flask import Flask, render_template

import settings
from app.api.view import api_bp
from app.task.view import task_bp
from app.user.view import user_bp
from app.work.view import work_bp


def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)  # 导入配置

    app.register_blueprint(api_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(work_bp)

    @app.route('/')
    def index():
        # !TODO
        # return the index page
        return render_template('index.html')

    return app
