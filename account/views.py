from django.shortcuts import render, redirect, get_object_or_404 
from .models import College,School,Department,Level,Category,Student_category,Lecturer_category
from .models import Department_council,School_council,College_council,Academic_council,MyUser
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'home.html')

def load_departments(request):
    skl= request.GET.get('school')
    school = School.objects.get(name=skl)
    departments = Department.objects.filter(school=school)
    context={'departments':departments}
    return render(request, 'dep_options.html', context)

def load_levels(request):
    depart=request.GET.get('department')
    department =Department.objects.get(name=depart)
    levels=Level.objects.filter(department=department)
    context={'levels':levels}
    return render(request, 'lv_options.html', context)

def load_category(request):
    cat=request.GET.get('category')
    student_cats=Student_category.objects.all()
    lecturer_cats=Lecturer_category.objects.all()
    col_council_cats=College_council.objects.all()
    skl_council_cats=School_council.objects.all()
    dep_council_cats=Department_council.objects.all()
    acad_council_cats=Academic_council.objects.all()
    schools=School.objects.all()
    levels=Level.objects.all()
    context={ 'cat':cat,'student_cats':student_cats,'lecturer_cats':lecturer_cats,
            'col_council_cats':col_council_cats,'dep_council_cats':dep_council_cats,
            'schools':schools,'levels':levels,'skl_council_cats':skl_council_cats,
            'acad_council_cats':acad_council_cats }
    return render(request, 'cat_selected.html', context)

def register(request):
    categories=Category.objects.all()
    if request.method == 'POST':
        data=request.POST.copy()
        fname=str(data.get('Fname'))
        lname=str(data.get('Lname'))
        mail=str(data.get('Email'))
        pne=str(data.get('Phone'))
        pass1=str(data.get('Pwd1'))
        pass2=str(data.get('Pwd2'))
        cat=str(data.get('Catgy'))
        std=str(data.get('Std_cat'))
        if std == 'None':
            std ='.x.'
        regN=str(data.get('Reg'))
        if regN == 'None':
            regN ='.x.'
        lect=str(data.get('Lect'))
        if lect == 'None':
            lect ='.x.'
        stfId=str(data.get('Staff'))
        if stfId == 'None':
            stfId ='.x.'
        col_cnl=str(data.get('Col_council_cat'))
        if col_cnl == 'None':
            col_cnl ='.x.'
        acad_cnl=str(data.get('Acad_council_cat'))
        if acad_cnl == 'None':
            acad_cnl ='.x.'
        skl_cnl=str(data.get('Skl_council_cat'))
        if skl_cnl == 'None':
            skl_cnl ='.x.'
        dep_cnl=str(data.get('Dep_council_cat'))
        if dep_cnl == 'None':
            dep_cnl ='.x.'
        skl=str(data.get('Skl'))
        if skl == 'None':
            skl ='.x.'
        dep=str(data.get('Depart'))
        if dep == 'None':
            dep ='.x.'
        lev=str(data.get('Lv'))
        if lev == 'None':
            lev ='.x.'
        if pass1 == pass2:
            if MyUser.objects.filter(first_name=fname).exists():
                messages.info(request,'Name taken')
                return redirect('register')
            else:
                user=MyUser.objects.create_user(first_name=fname,last_name=lname,email=mail,password=pass1,username=fname,
                     phone=pne,category=cat,student=std,regNo=regN,lecturer=lect,staffId=stfId,college_council=col_cnl,
                     academic_council=acad_cnl,school_council=skl_cnl,department_council=dep_cnl,school=skl,department=dep,
                     level=lev)
                login(request, user) 
                return redirect('homeP',name=user.username)
                   
        else:
            messages.info(request,'password not matching')
            return redirect('register')
    context={'categories':categories}
    return render(request, 'register.html', context)

def loginfx(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request,"You are logged in as ")
                context={'form':form,'user':user}
                return redirect('homeP',name=user.username)
            else:
                messages.error(request,"Invalid username or password")    
        else:
            messages.error(request,"Form not valid")
    form=AuthenticationForm()
    context={'form':form}
    return render(request,'login.html',context)

def logoutfx(request):
    logout(request)
    messages.info(request,'Logged out successfully!')
    return redirect('/')