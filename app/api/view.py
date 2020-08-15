from flask import Blueprint

api_bp = Blueprint('api', __name__)


@api_bp.route('/api/login/')
def api_login():
    # !TODO
    # 用于登录的POST接口。
    # ​	请求参数：
    # ​		username: 用户名
    # ​		password: 密码
    # ​	响应参数：
    # ​		user-group: int 用户组，0: 普通用户， 1: 任务发布者， -1: 错误
    # ​		(添加cookie)
    #   说明：调用User类check_user方法
    pass


@api_bp.route('/api/check-username/')
def api_check_username():
    # !TODO
    # 用于检查用户名是否已经被注册的GET接口
    #
    # ​    请求参数：
    #
    # ​        username: 用户名
    #
    # ​    响应参数：
    #
    # ​        occupied: boolean 0为未注册，1为已注册
    #     说明：
    #         调用User类check_username方法
    pass


@api_bp.route('/api/register/')
def api_register():
    # !TODO
    # ​    用于注册用户的POST接口
    # ​    请求参数：
    # ​        username: 用户名
    # ​        password: 密码
    # ​        re_password: 确认密码
    # ​    响应参数：
    # ​        user - group: int 用户组，0: 普通用户， 1: 任务发布者， -1: 错误
    #     说明：
    #         创建User对象并调用store方法
    pass


@api_bp.route('/api/get-task/')
def api_get_task():
    # !TODO
    # ​	用于任务检索的GET接口
    #
    # ​	请求参数：
    #
    # ​		type: 任务检索的类型
    #
    # ​				0：用户中心任务大厅通过任务名进行检索
    #
    # ​				1：发布者我的任务，通过发布者和任务名进行检索
    #
    # ​		content: 检索的任务名内容
    #
    # ​	响应参数：
    #
    # ​		tasks: dict 任务的信息
    #   说明：使用Task类get_task方法, 注意get_task方法返回的是task_id
    pass


@api_bp.route('/api/get-work/')
def api_get_work():
    # !TODO
    # ​    用户获取历史标注的接口。
    #
    # ​    响应参数：
    #
    # ​        works: dict 历史work的json
    pass


@api_bp.route('/api/upload-dataset/')
def api_upload_dataset():
    # !TODO
    # 上传数据集的POST接口
    #
    # ​    请求参数:
    #
    # ​        file: 上传的文件
    pass


@api_bp.route('/api/upload-task-instruction/')
def api_upload_task_instruction():
    # !TODO
    # ​    上传任务指导书的POST接口
    #
    # ​    请求参数:
    #
    # ​        file: 上传的文件
    pass


@api_bp.route('/api/logout/')
def api_logout():
    # !TODO
    # 用户登出的接口
    # 清除cookie-session数据，返回首页
    pass
