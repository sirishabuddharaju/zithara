from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
from .models import Recipient
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User



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

        Recipient.objects.create(
            user_location=Uloc,
            user_age=int(Uage),
            user_gender=Ugen,
            recipient_relationship=Rrel,
            recipient_age=int(Rage),
            recipient_gender=Rgen,
            recipient_interests=Rint,
            special_occasion=socc,
            budget_preference=Bud,
            gift_name=Gnam,
            category=Gcat,
            brand=Bran,
            price=float(Pric),  # Convert to float
            description=Desc,
            gift_rating=float(Grat)  # Convert to float
        )

        return redirect('recipient_list')
    return render(request,'admin.html')


 # Read (list) view
def recipient_list(request):
    recipients = Recipient.objects.all()  # Ensure this retrieves objects
    return render(request, 'recipient_list.html', {'recipients': recipients})

def recipient_update(request):
    recipients = Recipient.objects.all()  # Ensure this retrieves objects
    return render(request, 'recipient_update.html', {'recipients': recipients})

def recipient_delete(request):
    recipients = Recipient.objects.all()  # Ensure this retrieves objects
    return render(request, 'recipient_delete.html', {'recipients': recipients})



def edit_recipient(request, pk):
    recipient = get_object_or_404(Recipient, pk=pk)  # Fetch recipient by primary key

    if request.method == "POST":
        # Retrieve and update recipient fields
        recipient.user_location = request.POST.get('U', recipient.user_location)
        recipient.user_age = request.POST.get('UA', recipient.user_age)
        recipient.user_gender = request.POST.get('UG', recipient.user_gender)
        recipient.recipient_relationship = request.POST.get('RR', recipient.recipient_relationship)
        recipient.recipient_age = request.POST.get('RA', recipient.recipient_age)
        recipient.recipient_gender = request.POST.get('RG', recipient.recipient_gender)
        recipient.recipient_interests = request.POST.get('RI', recipient.recipient_interests)
        recipient.special_occasion = request.POST.get('SO', recipient.special_occasion)
        recipient.budget_preference = request.POST.get('B', recipient.budget_preference)
        recipient.gift_name = request.POST.get('GN', recipient.gift_name)
        recipient.category = request.POST.get('C', recipient.category)
        recipient.brand = request.POST.get('BR', recipient.brand)
        recipient.price = request.POST.get('P', recipient.price)
        recipient.description = request.POST.get('GD', recipient.description)
        recipient.gift_rating = request.POST.get('GR', recipient.gift_rating)

        recipient.save()  # Save the updated recipient
        return redirect('recipient_list')  # Redirect to list after saving

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

            return redirect("contact_view")  # Redirect to the same page after submission

    return render(request, "contact.html")




def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect("adddata")  # Redirect to Django Admin
        else:
            messages.error(request, "Invalid credentials or not an admin.")

    return render(request, "adminlogin.html")

def admin_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "Registration successful! Please log in.")
                return render(request, "loginpage.html") # Redirect to login page
        else:
            messages.error(request, "Passwords do not match!")

    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to user dashboard
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, "loginpage.html")

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("user_login")
