from django.shortcuts import render,get_object_or_404,HttpResponse, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail
from mainApp.models import Products
from .forms import ProductsForm
from django.core.mail import EmailMessage


def emailSend(request):


    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        topic = str(name)+"/"+"/"+str(subject)

        message = str(message)+"-----from---- "+str(email)

        recipient_list = ['info@nordiclaboratories.net',]
        send_mail(topic, message, email, recipient_list)

        text = "Thank you for your message. We will respond as soon as possible"

        return render(request, 'mainApp/English/homeEn.html', {'text': text})
    else:
        return render(request, 'mainApp/English/homeEn.html', {})


def emailSendTr(request):


    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        topic = str(name) + "/" + "/" + str(subject)

        message = str(message) + "-----from---- " + str(email)

        recipient_list = ['info@nordiclaboratories.net', ]
        send_mail(topic, message, email, recipient_list)

        text = "Mesajınız için teşekkürler. En kısa sürede geri dönüş sağlayacağız"

        return render(request, 'mainApp/Turkish/homeTr.html', {'text': text})
    else:
        return render(request, 'mainApp/Turkish/homeTr.html', {})



def insertCodes(request):
    if request.method != 'POST':
        with open('codes.txt') as f:
            lines = f.readlines()

        for data in lines:
            print(data)
            newPrd = Products()
            newPrd.prdId = data
            newPrd.used = 0
            newPrd.save()
        return render(request, 'mainApp/English/homeEn.html', {})
    else:
        return render(request, 'mainApp/English/homeEn.html', {})



def verifyCode(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid():

        products = Products.objects.all()
        prdId = form.cleaned_data['prdId']

        text = str(prdId)
        pid = 0
        i=0
        print(len(products))
        while i<len(products) and str(products[i].prdId.strip()) != str(prdId):
            i = i+1
            pid = products[i].id

        if i>=len(products):
            text = text + " Product's code is wrong"
            return render(request, 'mainApp/English/homeEn.html', {'text': text})

        else:
            prd = get_object_or_404(Products, id=pid)
            prd.used = prd.used +1
            prd.save()
            if prd.used <= 2:
                # found and not used
                text = text + " Product's code is approved"
                return render(request, 'mainApp/English/homeEn.html', {'text': text})
            else:
                # found and used
                text = text + " Product's code was used"
                return render(request, 'mainApp/English/homeEn.html', {'text': text})

    else:
        return render(request, 'mainApp/English/homeEn.html', {})



def verifyCodeTr(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid():

        products = Products.objects.all()
        prdId = form.cleaned_data['prdId']

        text = str(prdId)
        pid = 0
        i=0
        print(len(products))
        while i<len(products) and str(products[i].prdId.strip()) != str(prdId):
            i = i+1
            pid = products[i].id

        if i>=len(products):
            text = text + " Ürün Kodu yanlış!!"
            return render(request, 'mainApp/Turkish/homeTr.html', {'text': text})

        else:
            prd = get_object_or_404(Products, id=pid)
            prd.used = prd.used +1
            prd.save()
            if prd.used <= 2:
                # found and not used
                text = text + " Ürün kodu onaylıdır"
                return render(request, 'mainApp/Turkish/homeTr.html', {'text': text})
            else:
                # found and used
                text = text + " Ürün kodu kullanılmıştır"
                return render(request, 'mainApp/Turkish/homeTr.html', {'text': text})

    else:
        return render(request, 'mainApp/Turkish/homeTr.html', {})





## English
class HomePageEnView(TemplateView):
    template_name = 'mainApp/English/homeEn.html'

class ContactPageEnView(TemplateView):
    template_name = 'mainApp/English/contactEn.html'

class InjectionsPageEnView(TemplateView):
    template_name = 'mainApp/English/injectionsEn.html'

class TabletsPageEnView(TemplateView):
    template_name = 'mainApp/English/tabletsEn.html'





###############################################################


# Turkish
class HomePageTrView(TemplateView):
    template_name = 'mainApp/Turkish/homeTr.html'




