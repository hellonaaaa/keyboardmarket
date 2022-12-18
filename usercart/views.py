from tools.R import R
from tools.login_check import logincheck
from .models import Cart
from tools.models.cartModel import CartModel
from product.models import Product
from users.models import User
from tools.db import CartStatus


@logincheck('GET', 'POST', 'PUT', 'DELETE')
def usercart(request):
    return R.ok("API reachable")
# if request.method == "POST":
# 	req = request.body
# 	ucart = CartModel()
# 	ucart.fromJson(req)
# 	if ucart.amount == 0:
# 		return R.badRequest("Add cart amount can not be 0")
# 	product = Product.objects.filter(id = ucart.product_id)
# 	if not product:
# 		return R.badRequest("Product does not exist")
# 	product = product[0]
# 	if ucart.amount > product.stored_amount:
# 		return R.badRequest("Add cart amount reach maximum stored amount")
# 	user = User.objects.filter(name = ucart.username)
# 	if not user:
# 		return R.badRequest("User does not exist")
# 	user = user[0]
# 	dbcart = Cart.objects.filter(user = user).filter(product = product)
# 	if dbcart:
# 		dbcart[0].amount += ucart.amount
# 		dbcart[0].save()
# 	else:
# 		cart = Cart.objects.create(
# 			product = product,
# 			user = user,
# 			amount = ucart.amount,
# 			status = CartStatus.activate.value
# 		)
# 		cart.save()
