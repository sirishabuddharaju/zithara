from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipient
from django.views.decorators.csrf import csrf_exempt

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

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"Aboutus.html")

