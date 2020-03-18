from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as lgin, logout as lgout
from django.contrib.auth.decorators import login_required
# Create your views here.
from IntranetUser.models import *


def index(request):
    response = {}
    response['menu'] = Menu.objects.all()
    response['submenu'] = SubMenu.objects.all().order_by("text")
    try:
        homeMenuId = Menu.objects.get(text='Home')
        response['category'] = Category.objects.filter(menuId=homeMenuId)
        response['subcategory'] = SubCategory.objects.all()
    except:
        pass
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
    response['category'] = Category.objects.filter(subMenuId=submenuid)
    response['subcategory'] = SubCategory.objects.all()
    response['contnt'] = SubMenu.objects.get(id=submenuid)
    return render(request, 'index.html', response)


def login(request):
    response = {}
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['pswd'])
        if user:
            lgin(request, user)
            return redirect('/editorhome')
        else:
            response['invalidlogin'] = "Invalid Username or Password."

    return render(request, 'login.html', response)


@login_required(login_url="/login")
def editorhome(request):
    response = {}
    user = request.user
    editor = Editor.objects.get(user=user)
    editorDept = Department.objects.get(id=editor.dept.id)
    response['username'] = user.username
    response['dept'] = editorDept.deptName
    subMenuId = SubMenu.objects.get(text=editorDept.deptName)
    categories = Category.objects.filter(subMenuId=subMenuId)
    response['catsNsubcats'] = {}
    for category in categories:
        response['catsNsubcats'][category] = []
        subcategories = SubCategory.objects.filter(categoryId=category)
        for subcategory in subcategories:
            response['catsNsubcats'][category].append(subcategory)
            # print(type(response['catsNsubcats'][category]))
    return render(request, 'editorhome.html', response)


@login_required(login_url="/login")
def addCategory(request):
    if request.method == 'POST':
        user = request.user
        editor = Editor.objects.get(user=user)
        # editorDept = Department.objects.get(id=editor.dept.id)
        subMenuId = SubMenu.objects.get(text=editor.dept.deptName)
        category = Category()
        category.text = request.POST['catName']
        category.subMenuId = subMenuId
        category.save()
    return redirect('/editorhome')


@login_required(login_url="/login")
def addSubCategory(request):
    if request.method == 'POST':
        categoryId = request.POST['category']
        category = Category.objects.get(id=categoryId)
        subcategory = SubCategory()
        subcategory.text = request.POST['subCatName']
        subcategory.categoryId = category
        subcategory.url = request.POST['url']
        subcategory.content = request.POST['content']
        subcategory.save()
        print("SubCategory Added")
    return redirect('/editorhome')


@login_required(login_url="/login")
def deleteCategory(request):
    if request.method == "POST":
        categoryId = request.POST['category']
        Category.objects.get(id=categoryId).delete()
    return redirect('/editorhome')


def logout(request):
    lgout(request)
    return redirect('/login')
