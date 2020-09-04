from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #todo ha ido bien,eviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["francisco.regular@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #todo ha ido bien, redirect a ok
                return redirect(reverse('contact')+"?ok")

            except:
                #algo no ha ido bien, redirect a Fail
                return redirect(reverse('contact')+"?fail")



    return render(request,'contact/contact.html',{'form': contact_form})

