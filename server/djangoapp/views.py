from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
#from restapis import get_dealers_from_cf

# Get an instance of a logger
logger = logging.getLogger(__name__)


def about(request):
    return render(request, 'djangoapp/about.html', {})


def contact(request):
    return render(request, 'djangoapp/contact.html', {})


def login_request(request):
    return render(request, )


def logout_request(request):
    return render(request, 'djangoapp/logout.html', {})


def registration_request(request):
    return render(request, 'djangoapp/registration.html', {})


def get_dealerships(request):
    if request.method == "GET":
        url = "your-cloud-function-domain/dealerships/dealer-get"
        # Get dealers from the URL
        dealerships = get_dealer_details(url)
        # Contact all dealer's short name
        dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return HttpResponse(dealer_names)


def home_page(request):
    return render(request, 'djangoapp/index.html', {})


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request):
    return render(request, 'djangoapp/dealer_details.html', {})
# ...


def add_review(request):
    return render(request, 'djangoapp/add_review.html', {})


def submit(request):
    return render(request, 'djangoapp/submission.html', {})
