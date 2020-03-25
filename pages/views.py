from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

	dest1 = Destination()
	dest1.name = 'Tokyo'
	dest1.desc = 'This is a great place to be'
	dest1.img = 'destination_1.jpg'
	dest1.price = 600
	dest1.offer = True

	dest2 = Destination()
	dest2.name = 'Paris'
	dest2.desc = 'This is a great place to be'
	dest2.img = 'destination_2.jpg'
	dest2.price = 900


	dest3 = Destination()
	dest3.name = 'Bali'
	dest3.desc = 'This is a great place to be'
	dest3.img = 'destination_3.jpg'
	dest3.price = 600


	dests = [dest1, dest2, dest3]

	return render(request, 'index.html', {'dests': dests})