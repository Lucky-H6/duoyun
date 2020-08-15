from flask import Blueprint

work_bp = Blueprint('work', __name__)


@work_bp.route('/work/new/')
def work_new():
    # !TODO
    # 检查用户在某task下的work情况, 若存在task下未完成的work, 返回该work_id, 若不存在work, 创建新的work并返回work_id
    # 请求参数：
    #    task_id: task id
    # 响应参数：
    #    work_id: 若exist=1, 返回未完成的work_id, 若exist=0, 返回-1
    pass


@work_bp.route('/work/get/')
def work_get():
    # !TODO
    # 获取当前任务的下一张图片
    # 请求参数：
    #    work_id: work id
    # 响应参数：
    #    img: 下一张图片

    pass


@work_bp.route('/work/save/')
def work_save():
    # !TODO
    # 暂存任务
    # 请求参数：
    #    work_id: work id
    #    data: json, 标注数据
    pass


@work_bp.route('/work/end/')
def work_end():
    # !TODO
    # 结束任务
    # 请求参数：
    #    work_id: work id
    #    data: json, 标注数据
    pass
