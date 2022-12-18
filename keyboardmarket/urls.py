"""keyboardmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from keyboardmarket import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

# keyboardmarket\urls.py
urlpatterns = [
    # 路徑 url， if 下面path 'admin/' 搜尋django後臺資料庫 路徑'admin/'
    path('admin', admin.site.urls),
    url('user', include('users.urls')),
    url('login', include('login.urls')),
    url('product', include('product.urls')),
    url('usercart', include('usercart.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
