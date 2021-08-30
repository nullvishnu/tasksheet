from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from datetime import datetime
from django.shortcuts import render
from user.data.request.user_request import UserRequest
from user.service.user_service import User_Service
import pytz
IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.now(IST)
today = datetime_ist.strftime('%Y-%m-%d')

def login_index(request):
    return render(request, 'login.html')

def signup_index(request):
    return render(request, 'signup.html')

def dashboard_index(request):
    return render(request, 'index.html')

@csrf_exempt
@api_view(['GET','POST'])
def user_fetch(request):
    if request.method == 'GET':
        User_service = User_Service()
        resp_obj = User_service.get_user()
        return HttpResponse(resp_obj.get(), content_type='application/json')

    if request.method == 'POST':
        userdata = json.loads(request.body)
        User_service = User_Service()
        data = UserRequest(userdata)
        resp_obj = User_service.insert_user(data,userdata)
        return HttpResponse(resp_obj.get(), content_type='application/json')

@csrf_exempt
@api_view(['GET'])
def user_detail(request,userid):
    if request.method == 'GET':
        User_service = User_Service()
        resp_obj = User_service.get_userdetail(userid)
        return HttpResponse(resp_obj.get(), content_type='application/json')


@csrf_exempt
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        userdata = json.loads(request.body)
        User_service = User_Service()
        username= userdata['username']
        password= userdata['password']
        resp_obj = User_service.login_user(username, password)
        data = json.loads(resp_obj.get())
        request.session['empid'] = data.get('message').get('id')
        request.session['empname'] = data.get('message').get('name')
        # request.session['Entity_gid'] = data.data.message.get(id)
        return HttpResponse(resp_obj.get(), content_type='application/json')


@csrf_exempt
@api_view(['GET','POST'])
def task_fetch(request):
    if request.method == 'GET':
        service = User_Service()
        emp_id = request.session['empid']
        resp_obj = service.get_task(emp_id)
        return HttpResponse(resp_obj.get(), content_type='application/json')

    if request.method == 'POST':
        userdata = json.loads(request.body)
        service = User_Service()
        # data = UserRequest(userdata)
        emp_id = request.session['empid']
        data = {}
        resp_obj = service.insert_task(data,userdata,emp_id)
        return HttpResponse(resp_obj.get(), content_type='application/json')
