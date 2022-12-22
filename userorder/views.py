from django.shortcuts import render
from tools.R import R
from tools.login_check import logincheck
from usercart.models import Cart
from users.models import User
from .models import Order
import json
import uuid
import datetime
from tools.db import CartStatus, OrderStatus
# from paypalTools.createOrderClient import CreateOrder
# from paypalTools.captureOrderClient import CaptureOrder
# from tools.emailClient import EmailClients


# Create your views here.
@logincheck('POST')
def userorder(request):
    if request.method == "POST":
        req = request.body
        udata = json.loads(req)
    if "username" not in udata:
        return R.badRequest("username not found")
    username = udata["username"]
    user = User.objects.filter(name=username)
    if not user:
        return R.badRequest("user does not exist")
    user = user[0]
    usercart = Cart.objects.filter(user=user)
    if not usercart:
        return R.badRequest("cart is empty")

    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    uuid4String = str(uuid.uuid4()).split("-")[0]
    orderno = now + uuid4String
    for cart in usercart:
        cart.status = CartStatus.deactivate.value
        cart.save()
        userorder = Order.objects.create(
            orderno=orderno,
            product=cart.product,
            user=cart.user,
            amount=cart.amount,
            status=OrderStatus.notPaid.value
        )
        return R.ok("checkout success")
    else:
        return R.methodNotAllowed('method not allowed')
