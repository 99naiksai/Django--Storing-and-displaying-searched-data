from django.shortcuts import render
from items.models import ItemA , ItemB , ItemC
# Create your views here.
def laptop(request):
    lap = ItemA.objects.all() 
    return render(request , 'laptop.html' , {'lap':lap})

def mobile(request):    
    mob = ItemB.objects.all() 
    return render(request , 'mobile.html' , {'mob':mob})

def mobile_accessories(request):    
    moba = ItemC.objects.all() 
    return render(request , 'mobilea.html' , {'moba':moba})

def search(request):
    return render (request , 'search.html')

def info(request):
    query = request.GET.get('search')

    lap = ItemA.objects.filter(model_name__contains=query)
    mob = ItemB.objects.filter(model_name__contains=query)
    moba = ItemC.objects.filter(model_name__contains=query)

    return render(request , 'info.html' , {'lap':lap, 'mob':mob, 'moba':moba })
