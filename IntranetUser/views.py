from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from IntranetUser.models import Menu, SubMenu, Category, SubCategory


def index(request):
    response = {}
    response['menu'] = Menu.objects.all()
    response['submenu'] = SubMenu.objects.all()
    homeMenuId = Menu.objects.get(text='Home')
    response['category'] = Category.objects.filter(menuId=homeMenuId)
    response['subcategory'] = SubCategory.objects.all()
    return render(request, 'index.html', response)


def carousel(request):
    response = {}
    return render(request, 'carousel.html', response)


def getContent(request):
    response = {}
    subcatid = request.GET.get('subcatid')
    print(f'ID: {subcatid}')
    response['contnt'] = SubCategory.objects.get(id=subcatid)
    return render(request, 'content.html', response)


def menucontent(request):
    response = {}
    response['menu'] = Menu.objects.all()
    response['submenu'] = SubMenu.objects.all()
    submenuid = request.GET.get('submenuid')
    print(f'ID: {submenuid}')
    response['category'] = Category.objects.filter(subMenuId=submenuid)
    response['subcategory'] = SubCategory.objects.all()
    response['contnt'] = SubMenu.objects.get(id=submenuid)
    return render(request, 'index.html', response)
