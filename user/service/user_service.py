import json
from django.db import IntegrityError

import user
from user.models import User,Task
from user.data.response.user_response import User_Response
from tasksheet.message import Message,SuccessMessage,SuccessStatus

class User_Service:
    def insert_user(self ,request_obj,obj):
        if 'id' in obj:
            try:
                user = User.objects.filter(id=request_obj.get_id()).update(name=request_obj.get_name(),
                                                                    username = request_obj.get_username(),
                                                                    password = request_obj.get_password(),
                                                                    status = request_obj.get_status())
            except Exception as e:
                print(e)
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj

            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"userid":user.id})
            return msg_obj

        else:
            try:
                user = User.objects.create(
                    name=request_obj.get_name(),
                    username = request_obj.get_username(),
                    password = request_obj.get_password(),
                    status = request_obj.get_status())
            except Exception as e:
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj


            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"userid":user.id})
            return msg_obj

    def get_userdetail(self,id):
        user = User.objects.get(id=id)
        req_data = User_Response()
        req_data.set_id(user.id)
        req_data.set_name(user.name)
        req_data.set_username(user.username)
        req_data.set_password(user.password)
        req_data.set_status(user.status)
        return req_data

    def login_user(self,username,password):
        try:
            user = User.objects.get(username=username,password=password)

        except Exception as e:
            print(e)
            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.ERROR)
            msg_obj.set_message(e)
            return msg_obj

        req_data = User_Response()
        req_data.set_id(user.id)
        req_data.set_name(user.name)
        req_data.set_username(user.username)
        req_data.set_password(user.password)
        req_data.set_status(user.status)

        msg_obj = Message()
        msg_obj.set_status(SuccessStatus.SUCCESS)
        msg_obj.set_message(json.loads(req_data.get()))
        return msg_obj

    def get_user(self):
        user = User.objects.all()
        resp_list = User_Response()
        ar =[]
        for usr in user:
            req_data = User_Response()
            req_data.set_id(usr.id)
            req_data.set_name(usr.name)
            req_data.set_username(usr.username)
            req_data.set_password(usr.password)
            req_data.set_status(usr.status)
            ar.append(json.loads(req_data.get()))
        resp_list.set_data(ar)
        return resp_list

    def insert_task(self ,request_obj,obj,userid):
        if 'id' in obj:
            try:
                task = Task.objects.filter(id=obj['id']).update(name=obj['name'],
                                                                    description = obj['description'],
                                                                    date = obj['date'],
                                                                    updated_by = userid)
            except Exception as e:
                print(e)
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj

            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"taskid":task})
            return msg_obj

        else:
            try:
                task = Task.objects.create(
                    user_id=userid,
                    name=obj['name'],
                    description = obj['description'],
                    date = obj['date'],
                    status = 1)
            except Exception as e:
                print(e)
                msg_obj = Message()
                msg_obj.set_status(SuccessStatus.ERROR)
                msg_obj.set_message(e)
                return msg_obj


            msg_obj = Message()
            msg_obj.set_status(SuccessStatus.SUCCESS)
            msg_obj.set_message({"taskid":task.id})
            return msg_obj



    def get_task(self,userid):
        rate = Task.objects.filter(user_id=userid)
        resp_list = User_Response()
        ar =[]
        for i in rate:
            req_data = User_Response()
            req_data.set_id(i.id)
            req_data.set_name(user.service.user_service.User_Service.get_username(self, i.user_id))
            req_data.set_taskname(i.name)
            req_data.set_taskdesc(i.description)
            req_data.set_taskdate(i.date)
            req_data.set_status(i.status)
            ar.append(json.loads(req_data.get()))
        resp_list.set_data(ar)
        return resp_list

    def get_username(self,userid):
        data = User.objects.get(id=userid)
        return data.name


