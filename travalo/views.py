from django.http import HttpResponse
from django.shortcuts import render
from .models import Destinations

# Create your views here.
def index(requast):
    """
    dest1 = Destinations()
    dest1.name='Mumbai'
    dest1.price=700
    dest1.img='destination_2.jpg'
    dest1.discr="the city that naver sleep"
    dest1.offer=False

    dest2 = Destinations()
    dest2.name='Aurangabad'
    dest2.price=780
    dest2.img='destination_1.jpg'
    dest2.discr="the city of gate's :) "
    dest2.offer=True

    dest3 = Destinations()
    dest3.name='Banlor'
    dest3.price=500
    dest3.img='destination_3.jpg'
    dest3.discr="the famous for biryani"
    dest3.offer=False

    dests =[dest1,dest2,dest3]     """
 ## this is faticching from database data
    dests = Destinations.objects.all()

    return render(requast,'index.html',{'dests':dests})