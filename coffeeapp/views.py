from django.shortcuts import render,redirect
from .forms import ContactForm,BookTableForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method =='POST':
        table = BookTableForm(request.POST)
        if table.is_valid():
            table.save()
            messages.add_message(request, messages.SUCCESS,'Table Booked Successfully!!')
            return redirect('home') 
    else:
        table = BookTableForm()        
    return render(request, 'index.html',{'tb':table})


def about(request):
    name = 'aisha'
    return render(request,  'about.html',{'n':name})


def contact(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
           fm.save()
           messages.add_message(request, messages.SUCCESS,'Message sends successfully!!')
           return  redirect('contact')
          
    else:
        fm = ContactForm()       
    return render(request, 'contact.html',{'frm':fm})


def menu(request):
    return render(request, 'menu.html')

def service(request):
    return render(request, 'service.html')


def reservation(request):
    return render(request, 'reservation.html')


def testimonial(request):
    return render(request, 'testimonial.html')    