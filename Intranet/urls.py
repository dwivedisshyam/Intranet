"""Intranet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500

from Intranet import settings
from IntranetUser import views as intranetuser

urlpatterns = [
    path('', intranetuser.index),
    path('index/', intranetuser.index),
    path('carousel/', intranetuser.carousel),
    path('content/', intranetuser.getContent),
    path('menucontent/', intranetuser.menucontent),
    path('login/', intranetuser.login),
    path('editorhome/', intranetuser.editorhome),
    path('addCategory/', intranetuser.addCategory),
    path('addSubCategory/', intranetuser.addSubCategory),
    path('deleteCategory/', intranetuser.deleteCategory),
    path('logout/', intranetuser.logout),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = intranetuser.error_404
handler500 = intranetuser.error_500
