from django.shortcuts import  render
from django.shortcuts import  redirect
from .models import UserRegister, booking_table
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def homepage(request):
    return render(request,'home.html')




def user_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        image = request.FILES.get('user_image')

        # Save user details
        user = UserRegister(name=name, address=address, email=email, phone=phone, dob=dob, image=image)
        user.save()
        

        # Save user ID in session
        request.session['user_id'] = user.id
        

        # Redirect to the user homepage
        return redirect('user_homepage')

    return render(request, 'registration.html')


    
    


def user_homepage(request):
    user_id = request.session.get('user_id')

    if user_id:
        user_data = UserRegister.objects.filter(id=user_id).first()
        
    else:
        user_data = None
        
    user_email = user_data.email if user_data else None

    # If user email is None or empty, redirect to another page or show an error message
    if not user_email:
        return redirect('user_homepage')  # Or a page that makes sense for your app

    return render(request, 'user_home.html', {
        'user_data': user_data, 
        'user_email': user_email
    })

def booking_page(request):
    return render(request,'booking.html')


def event_booking(request):
    if request.method=='POST':
        name=request.POST['name']
        mail=request.POST['email']
        event=request.POST['event-type']
        event_date=request.POST['event-date']
        guest=request.POST['guests']
        venue=request.POST['venue']
        note=request.POST['notes']
        bookings=booking_table(name=name,email=mail,event=event,event_date=event_date,guests=guest,venue=venue,message=note)
        bookings.save()
        subject = f"Booking Confirmation: {event.capitalize()} on {event_date}"
        message = (
        f"Dear {name},\n\n"
        f"Thank you for booking with us!\n\n"
        f"Here are your booking details:\n"
        f"Event: {event.capitalize()}\n"
        f"Date: {event_date}\n"
        f"Guests: {guest}\n"
        f"Venue: {venue}\n\n"
        f"We have successfully received your booking, and our team will reach out to you shortly for further details.\n"
        f"Feel free to reply to this email if you have any questions or need to make adjustments.\n\n"
        f"Best regards,\n"
        f"The Event Planning Team"
        )
        
        send_mail(subject,message,settings.EMAIL_HOST_USER,[mail])  
        return redirect('success_page')
    
def my_event(request, email):
    bookings = booking_table.objects.filter(email=email)
    return render(request, 'myevents.html', {'bookings': bookings})

def delete_page(request,pk):
    delete_data=booking_table.objects.get(id=pk)
    return render(request,'delete.html',{'delete_value':delete_data})

def delete_event(request,pk):
    delete_event_data=booking_table.objects.get(id=pk)
    delete_event_data.delete()
    return redirect('user_homepage')


def edit_event(request,pk):
    edit_data=booking_table.objects.get(id=pk)
    return render(request,'event_edit.html',{'edit_value':edit_data})


def edititem(request,pk):
    if request.method=='POST':
        edit_item=booking_table.objects.get(id=pk)
        edit_item.name=request.POST['name']
        edit_item.email=request.POST['email']
        edit_item.event=request.POST['event-type']
        edit_item.event_date=request.POST['event-date']
        edit_item.guests=request.POST['guests']
        edit_item.venue=request.POST['venue']
        edit_item.message=request.POST['notes']
        edit_item.save()
        return redirect('user_homepage')
    

def success_page(request):
    return render(request,'success.html')

def user_edit(request,pk):
    user_data=UserRegister.objects.get(id=pk)
    return render(request,'user_edit.html',{'user_value':user_data})

def useritem(request,pk):
    if request.method=='POST':
        edit_item=UserRegister.objects.get(id=pk)
        old=edit_item.image
        new=request.FILES.get('user_image')
        if old != None and new == None:
            edit_item.image=old
        else:
            edit_item.image=new
        edit_item.name=request.POST['name']
        edit_item.address=request.POST['address']
        edit_item.email=request.POST['email']
        edit_item.phone=request.POST['phone']
        edit_item.dob=request.POST['dob']
        edit_item.save()
        return redirect('user_homepage')

    
    