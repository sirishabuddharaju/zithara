from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipient
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def filter(request):
    data=Recipient.objects.filter( special_occasion=request.POST.get('occasion'))
    print(data)

    return render(request,'filters.html',{"data":data})



