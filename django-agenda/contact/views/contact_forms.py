from typing import Any
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from contact.models import Contact


#forms
from contact.forms import ContactForm


# Create your views here.

def create(request):
    form_action = reverse('contact:create')


    if request.POST:
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action
        }
        if form.is_valid():
            print("Form Valido")
            contact = form.save()
            print(contact)
            print(contact.pk)
            return redirect("contact:update",contact_id = contact.pk)



        return render(request,'contact/create.html',context)
    context = {
        'form': ContactForm(),
        'form_action' : form_action
    }
    return render(request,'contact/create.html',context)




def update(request,contact_id):
    form_action = reverse('contact:update', args=(contact_id,))
    print("_---------------")
    contact = get_object_or_404(Contact,pk=contact_id,)


    if request.POST:
        form = ContactForm(request.POST,request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action
        }
        if form.is_valid():
            print("Form Valido")
            contact = form.save()
            return redirect("contact:update",contact_id = contact.pk)



        return render(request,'contact/create.html',context)
    context = {
        'form': ContactForm(instance=contact),
        'form_action' : form_action
    }
    return render(request,'contact/create.html',context)

def delete(request, contact_id):
    contact = get_object_or_404(Contact,pk = contact_id)
    contact.delete()
    return redirect("contact:index")

  
    
