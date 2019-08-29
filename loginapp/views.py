from django.shortcuts import redirect,render
from . models import User

def index(request):
	return render(request,"loginapp/index.html")
def login(request):
	uname = request.POST["txtuser"]
	pass1 = request.POST["txtpass"]
	raj = User.objects.filter(user=uname,password=pass1)
	if len(raj)>0:
		rj = raj.values('id')[0]
		request.session["sid"]=rj['id']
		request.session["uid"]=uname
		return redirect('/stuapp')
	else:
	    return render(request,"loginapp/index.html",{'key':'invalid userid and password'}) 


def registor(request):
	return render(request,"loginapp/registor.html")

def registration(request):
	uname = request.POST["txtuser"]
	pass1 = request.POST["txtpass"]
	raj = User(user=uname,password=pass1)
	raj.save()
	return render(request,"loginapp/registor.html",{'key':'registrations done'})