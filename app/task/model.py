class Task:
    def __init__(self, task_id):
        pass
        # !TODO
        # connect to database and get task message by task_id

    @classmethod
    def creat_task(cls, publisher, task_name, type, mode, professional):
        pass
        # !TODO
        # connect to database and add a new line of the task

    @classmethod
    def get_task(cls, publisher=None, content=None):
        pass
        # !TODO
        # connect to database and return the query task result about the publisher and content in a list
        # return a list of task_id
