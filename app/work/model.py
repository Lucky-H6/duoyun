class Work:
    def __init__(self, work_id):
        pass
        # !TODO
        # connect to database and get info about work of work_id

    @classmethod
    def get_work(cls, user_id):
        pass
        # !TODO
        # connect to database and get all works of the user.
        # return a list of work_id

    @classmethod
    def check_work(cls, user_id, task_id):
        pass
        # !TODO
        # connect to database and check if the user has a running work of the task
        # if has, return the task id
        # if not, return None
