from django.shortcuts import render,HttpResponseRedirect
from .models import User
from .forms import UserRegistration
# Create your views here.
def addShowStudent(request):
    if request.method =='POST': 
      fm=UserRegistration(request.POST)
      if fm.is_valid():
         nm=fm.cleaned_data['name']
         # print(nm)
         em=fm.cleaned_data['email']
         # print(em)
         pw=fm.cleaned_data['password']
         # print(pw)

         reg=User(name=nm,email=em,password=pw)
         reg.save()
         # fm.save()
         fm= UserRegistration()

    else:
      fm= UserRegistration()
    stud = User.objects.all()  #get all data
    return render(request,'CRUD/addShow.html',{'form':fm,'stu':stud})

# //deleting data
def delete_data(request,id):
   if request.method=='POST':
      pi=User.objects.get(pk=id)
      pi.delete()
   return HttpResponseRedirect('/')

def update_data(request,id):
   if request.method !='POST':
      pi =User.objects.get(pk=id)
      fm=UserRegistration(request.POST, instance=pi)
      if fm.is_valid():
         fm.save()

   else:
      pi =User.objects.get(pk=id)
      fm=UserRegistration(instance=pi)
   return render(request,"CRUD/updateData.html",
   {'form':fm})