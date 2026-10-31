from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *


def index(request):
    return render(request,'index.html')

def login(request):
    error=""
    if request.method == "POST":
        ur = request.POST['uname']
        pd = request.POST['pwd']
        user = auth.authenticate(username=ur,password=pd)
        try:
            if user.is_staff:
                auth.login(request,user)
                error = "no"
            elif user is not None:
                auth.login(request,user)
                error = "not"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error,'error':error}
    return render(request,'login.html',d)

def admin_home(request):
    return render(request,'admin_home.html')

def user_home(request):
    return render(request,'user_home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    error = ""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        p = request.POST['pwd']
        gen = request.POST['gender']
        i=request.FILES['image']
        addr=request.POST['address']
        d=request.POST['dob']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Signup.objects.create(user=user,mobile=con,image=i,gender=gen,address=addr,dob=d)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'signup.html',d)

def users(request):
    data = Signup.objects.all()
    d = {'data':data}
    return render(request,'users.html',d)

def delete_user(request,id):
    student = User.objects.get(id=id)
    student.delete()
    return redirect('users')

def apply(request):
    return render(request,'apply.html')

import datetime
def apply(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    time = datetime.datetime.today()
    error=""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        c=request.POST['contact']
        pt=request.POST['ptype']
        rd=request.POST['rdate']
        gi=request.POST['gid']
        coun=request.POST['country']
        gn=request.POST['gidn']
        w=request.POST['weight']
        add=request.POST['address']
        try:
            VisaRequest.objects.create(first_name=f,last_name=l,email=e,mobile=c,parcel_type=pt,request_date=rd,country=coun,gov_id=gi,gov_no=gn,weight=w,address=add,status="Pending")
            error="no"
        except:
            error="yes"
    d={'time':time,'user':user,'error':error}
    return render(request,'apply.html',d)


def my_visa(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = VisaRequest.objects.all()
    d={'data':data}
    return render(request,'my_visa.html',d)

def all_visa(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = VisaRequest.objects.all()
    data = data[::-1]
    d={'data':data}
    return render(request,'all_visa.html',d)

def change_status(request,id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    booking=VisaRequest.objects.get(id=id)
    error=""
    if request.method == "POST":
        rs = request.POST['rstatus']
        booking.status = rs
        try:
            booking.save()
            error = "no"
        except:
            error = "yes"
    d = {'booking': booking,'error':error}
    return render(request,'change_status.html',d)

def delete_visa(request,id):
    data=VisaRequest.objects.get(id=id)
    data.delete()
    return redirect('all_visa')

def delete_my_visa(request,id):
    data=VisaRequest.objects.get(id=id)
    data.delete()
    return redirect('my_visa')

def pay_now(request,id):
    data = VisaRequest.objects.get(id=id)
    error = ""
    if request.method == "POST":
        data.status = "Paid"
        try:
            data.save()
            error = "no"
        except:
            error = "yes"
    d = {'data': data, 'error': error}
    return render(request,'pay_now.html',d)

def feedback(request):
    if not request.user.is_authenticated:
        return redirect('feedback')
    error=""
    if request.method=='POST':
        n = request.POST['fname']
        p = request.POST['fphone']
        e = request.POST['femail']
        c = request.POST['fcomment']
        try:
            Feedback.objects.create(feedback_name=n,feedback_contact=p,feedback_email=e,feedback_comment=c)
            error = "no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'feedback.html',d)

def view_feedback(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Feedback.objects.all()
    d = {'data':data}
    return render(request,'view_feedback.html',d)

def delete_feedback(request,id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    feedback = Feedback.objects.get(id=id)
    feedback.delete()
    return redirect('view_feedback')

def edit_profile(request):
    error=""
    data=User.objects.get(id=request.user.id)
    data2=Signup.objects.get(user=data)
    if request.method=='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        g = request.POST['gender']
        do = request.POST['dob']
        data.first_name=f
        data.last_name=l
        data2.mobile=c
        data2.gender=g
        data2.dob=do
        try:
            data.save()
            data2.save()
            error="no"
        except:
            error="yes"
        try:
            i=request.FILES['image']
            data2.image=i
            data2.save()
            error="no"
        except:
            pass
    d={'data':data,'data2':data2,'error':error}
    return render(request,'edit_profile.html',d)


