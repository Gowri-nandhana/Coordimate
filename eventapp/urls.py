
from django.urls import  path

from eventapp import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('register/', views.user_registration, name='user_registration'),
    path('user_homepage/', views.user_homepage, name='user_homepage'),
    path('booking_page',views.booking_page,name='booking_page'),
    path('event_booking',views.event_booking,name='event_booking'),
    path('my_event/<str:email>/', views.my_event, name='my_event'),
    path('delete_page/<int:pk>',views.delete_page,name='delete_page'),
    path('delete_event/<int:pk>',views.delete_event,name='delete_event'),
    path('edit_event/<int:pk>',views.edit_event,name='edit_event'),
    path('edititem/<int:pk>',views.edititem,name='edititem'),
    path('success_page',views.success_page,name='success_page'),
    path('user_edit/<int:pk>',views.user_edit,name='user_edit'),
    path('useritem/<int:pk>',views.useritem,name='useritem'),
]
