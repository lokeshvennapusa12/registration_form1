from django.shortcuts import render

# Create your views here.

from app.models import *
from app.forms import *
from django.http import HttpResponse

from django.core.mail import send_mail

def Register_form(request):   #azimwookvyjnvkag
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

             # to send the mail after the registration is successfully . it will send the mail to the 
            send_mail('tq for registering ',
                      'your registration is successfully submitted for any quires contact through mail',
                      'lokeshvennapusa22@gmail.com',
                      [NSUD.email],
                      fail_silently=True
                      )

            UD=User.objects.all()
            PD=Register.objects.all()
            d={'UD':UD , 'PD':PD}
            
            return render (request,'display_register.html',d)

            #return HttpResponse('Data Submitted Successfully ')
            
        else:
            return HttpResponse('Data Is not Valid')



    return render(request,'Register_form.html',d)


# def display_details(request):
#     UD=User.objects.all()
#     PD=Register.objects.all()
#     d={'UD':UD , 'PD':PD}
    
#     return render (request,'display_register.html',d)
