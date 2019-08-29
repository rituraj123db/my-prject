from django.shortcuts import redirect,render
from .models import Student
from django.http import HttpResponse
from loginapp.models import User
def index(request):
  if request.session.has_key('uid'):
    sr=request.session["sid"]
    stu=User.objects.get(pk=sr)
    return render(request,"stuapp/index.html",{'k':stu})
  else:
    return redirect('/loginapp')
def checkrno(request):
    n = request.GET.get("q")
    s = Student.objects.filter(rno=n)
    if len(s)>0:
       return HttpResponse("Rno is already exist")
    else:
       return HttpResponse("Valid")         

def insertstudent(request):
  r = request.POST["txtrno"] 
  n = request.POST["txtname"]
  b = request.POST["txtbranch"] 
  f = request.POST["txtfees"]
  s = Student(rno=r,name=n,branch=b,fees=f)
  s.save()
  res="data inserted successfully"

  return render(request,"stuapp/index.html",{'key':res})
def viewsall(request):
  s = Student.objects.all()
  return render(request,"stuapp/viewsall.html",{'s':s})
def viewsall1(request):
  n = request.GET.get("q")
  s=Student.objects.filter(name__startswith=n)
  return render(request,"stuapp/viewsall1.html",{'s':s})
def editdata(request):
  rid=request.GET["q"]
  t=Student.objects.get(pk=rid)
  return render(request,"stuapp/editdata.html",{'key':t})
def updatedata(request):
  i=request.POST["hid"]
  r=request.POST["txtrno"]
  n = request.POST["txtname"]
  b = request.POST["txtbranch"] 
  f = request.POST["txtfees"]
  data=Student.objects.get(pk=i)
  data.rno=r
  data.name=n
  data.branch=b
  data.fees=f
  data.save()
  return redirect(viewsall)
def deletedata(request):
  cid=request.GET["q"]
  Student.objects.get(pk=cid).delete()
  return redirect(viewsall)
def logout(request):
  del request.session["uid"]
  return redirect('/loginapp')     