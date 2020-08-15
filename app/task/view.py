from flask import Blueprint

task_bp = Blueprint('task', __name__)


@task_bp.route('/task/new/')
def task_new():
    # 新建task
    # 请求参数:
    #    user_id: user id
    #    task_name: task 名称
    #    task_type: 类型
    #    task_mode: 模式
    pass
