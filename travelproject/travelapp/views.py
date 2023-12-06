from django.shortcuts import render

from travelapp.models import Place, Actor


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    name=Actor.objects.all()

    return render(request,'index.html',{'result':obj,'result1':name})

