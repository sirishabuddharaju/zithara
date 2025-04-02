from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
from .models import Recipient
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings

@csrf_exempt
def filter(request):
    if request.method=="POST":
        occ = request.POST.get('occasion')
        b = request.POST.get('b')
        g = request.POST.get('g')
        r = request.POST.get('r')


        prediction={}
        if occ:
            prediction["special_occasion"]=occ
        if b:
            prediction["budget_preference"] = b
        if g:
            prediction["recipient_gender"] = g
        if r:
            prediction["recipient_relationship"] = r

        data = Recipient.objects.filter(**prediction)
        return render(request,'result.html',{"data":data})
    return render(request,"filters.html")



def adddata(request):
    if request.method=="POST":

        Uloc= request.POST.get('U')
        Uage = request.POST.get('UA')
        Ugen = request.POST.get('UG')
        Rrel = request.POST.get('RR')
        Rage = request.POST.get('RA')
        Rgen = request.POST.get('RG')
        Rint = request.POST.get('RI')
        socc = request.POST.get('SO')
        Bud = request.POST.get('B')
        Gnam = request.POST.get('GN')
        Gcat = request.POST.get('C')
        Bran = request.POST.get('BR')
        Pric = request.POST.get('P')
        Desc = request.POST.get('GD')
        Grat = request.POST.get('GR')

        Recipient.objects.create(user_location=Uloc,user_age=Uage,user_gender=Ugen,recipient_relationship=Rrel,recipient_age=Rage,recipient_gender=Rgen,
                                recipient_interests=Rint,special_occasion=socc,budget_preference=Bud,gift_name=Gnam,category=Gcat,brand=Bran,price=Pric,
                                description=Desc,gift_rating=Grat)
        return HttpResponse("the data added")


    return render(request,'admin.html')


 # Read (list) view
def recipient_list(request):
    recipients = Recipient.objects.all()
    return render(request, 'recipient_list.html', {'recipients': recipients})


def edit_recipient(request, pk):
    recipient = Recipient.objects.get(pk=pk)  # Fetch recipient by pk

    if request.method == "POST":
        # Update fields manually
        Uloc = request.POST.get('U')
        Uage = request.POST.get('UA')
        Ugen = request.POST.get('UG')
        Rrel = request.POST.get('RR')
        Rage = request.POST.get('RA')
        Rgen = request.POST.get('RG')
        Rint = request.POST.get('RI')
        socc = request.POST.get('SO')
        Bud = request.POST.get('B')
        Gnam = request.POST.get('GN')
        Gcat = request.POST.get('C')
        Bran = request.POST.get('BR')
        Pric = request.POST.get('P')
        Desc = request.POST.get('GD')
        Grat = request.POST.get('GR')

        recipient.save()  # Save the updated recipient

        return redirect('recipient_list')  # Redirect after saving

    return render(request, 'edit_recipient.html', {'recipient': recipient})

def delete_recipient(request, pk):
    recipient = Recipient.objects.get(pk=pk)  # Fetch recipient by pk

    if request.method == "POST":
        recipient.delete()  # Delete the recipient from the database
        return redirect('recipient_list')  # Redirect to the list after deletion

    return render(request, 'delete_recipient.html', {'recipient': recipient})


def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"Aboutus.html")




def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and phone and email and message:
            subject = f"New Contact Us Message from {name}"
            email_message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\n\nMessage:\n{message}"

            try:
                send_mail(subject, email_message, settings.EMAIL_HOST_USER, ["sirishabuddharaju520@gmail.com"])
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"Error sending message: {str(e)}")

            return redirect("contact")  # Redirect to the same page after submission

    return render(request, "contact.html")


