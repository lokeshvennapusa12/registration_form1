from django.shortcuts import render

# Create your views here.

from app.models import *
from app.forms import *
from django.http import HttpResponse

def Register_form(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={ 'UFO':UFO, 'PFO':PFO }

    if request.method=='POST' and request.FILES:

        UFD=UserForm(request.POST) 
        PFD=ProfileForm(request.POST,request.FILES)

        if UFD.is_valid() and PFD.is_valid():

            NSUD=UFD.save(commit=False)
            NSUD.set_password(UFD.cleaned_data['password']) #Hashing operation( Encrypting the password)89
            NSUD.save()

            NPUD=PFD.save(commit=False)
            NPUD.user_name=NSUD
            NPUD.save()

            UD=User.objects.all()
            PD=Register.objects.all()
            d={'UD':UD , 'PD':PD}
            
            return render (request,'display_register.html',d)

            #return HttpResponse('Data Submitted Successfully ')
            
        else:
            return HttpResponse('Data Is not Valid')



    return render(request,'Register_form.html',d)


def display_details(request):
    UD=User.objects.all()
    PD=Register.objects.all()
    d={'UD':UD , 'PD':PD}
    
    return render (request,'display_register.html',d)
