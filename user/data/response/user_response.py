
import json
class User_Response:
    id = None
    name = None
    username = None
    password = None
    task_name = None
    task_desc = None
    task_date = None
    status = 1

    data = []

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_password(self, password):
        self.password = password

    def set_username(self, username):
        self.username = username

    def set_taskname(self, task_name):
        self.task_name = task_name

    def set_taskdesc(self, task_desc):
        self.task_desc = task_desc

    def set_taskdate(self, task_date):
        task_date = task_date.strftime("%d-%b-%Y")
        self.task_date = task_date

    def set_status(self, status):
        self.status = status

    def set_data(self, data):
        self.data = data

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_taskname(self):
        return self.task_name

    def get_taskdesc(self):
        return self.task_desc

    def get_taskdate(self):
        return self.task_date

    def get_status(self):
        return self.status

    def get_data(self):
        return self.data
