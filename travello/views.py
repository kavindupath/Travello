from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name="Colombo"
    dest1.img='destination_1.jpg'
    dest1.desc="Capital of sri lanka"
    dest1.price=600

    dest2=Destination()
    dest2.name="Kandy"
    dest2.img='destination_2.jpg'
    dest2.desc="Cnetral of sri lanka"
    dest2.price=400

    dest3=Destination()
    dest3.name="Galle"
    dest3.img='destination_3.jpg'
    dest3.desc="Downsouth  sri lanka"
    dest3.price=700

    dests=[dest1,dest2,dest3]

    return render(request, "index.html",{'dests':dests})
