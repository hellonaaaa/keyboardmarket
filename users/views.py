# from django.shortcuts import render

# # Create your views here.
# from django.http import JsonResponse
# # from .models import User
# from tools.R import R
# from tools.models.userModel import UserModel

from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from tools.R import R
from tools.models.userModel import UserModel
import json


# def users(request):
#     return R.ok("Hello World")


def users(request):
    print(user)
    if request.method == "POST":
        res = request.body
        user = UserModel()
        user.fromJson(res)
        return R.ok("Hello World")
    else:
        return R.methodNotAllowed("Method Not Allowed")
