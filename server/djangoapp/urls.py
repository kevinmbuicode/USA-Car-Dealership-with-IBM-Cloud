from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp/'
urlpatterns = [

    path('djangoapp/', views.home_page, name='djangoapp'),
    path('djangoapp/registration', views.registration_request, name='registration'),

    path('add_review/', views.add_review, name='add_review'),
    path('add_review/submission', views.submit, name='submission'),
    path('djangoapp/add_review', views.add_review, name='add_review'),

    path('dealer_details/', views.get_dealer_details, name='dealer_details'),
    path('dealer_details/add_review', views.add_review, name='add_review'),
    path('djangoapp/dealer_details/',
         views.get_dealer_details, name='dealer_details'),
    path('djangoapp/dealer_details/add_review',
         views.add_review, name='add_review'),

    path('registration/', views.registration_request, name='registration'),
    path('registration/index.html', views.home_page, name='index'),
    path('djangoapp/registration/',
         views.registration_request, name='registration'),
    path('djangoapp/registration/index.html',
         views.home_page, name='index'),

    path('about/', views.about, name='about'),
    path('djangoapp/about', views.about, name='about'),

    path('contact/', views.contact, name='contact'),
    path('djangoapp/contact/', views.contact, name='contact'),

    path('logout/', views.logout_request, name='logout'),
    path('logout/logout', views.logout_request, name='logout'),
    path('djangoapp/logout/', views.logout_request, name='logout'),

    path(route='', view=views.home_page, name='index'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''paths appear twice I understand, but the first ones are the ones I configured in knowledge of the user may..
     input the website url and add a path directly rather than getting inside the website/homedirectory to..
     access an inner/already known path eg 'domain_name/contact.'''
