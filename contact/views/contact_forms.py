from django.shortcuts import render,redirect, get_object_or_404
from contact.models import Contact
from django.db.models import Q
from django import forms
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.urls import reverse
from contact.forms import ContactForm 
         

# Create your views here.
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
            'forms': form,
            'form_action': form_action
        }
        if form.is_valid():
            contato = form.save(commit=False)
            contato.save()
            return redirect('contact:update', contact_id=contato.pk)

        return render(request, 'contact/create.html', context)
    
    context = {
        'forms': ContactForm(),
        'form_action': form_action
    }
    return render(request, 'contact/create.html', context)

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES, instance=contact)
        context = {
            'forms': form,
            'form_action': form_action
        }
        if form.is_valid():
            contato = form.save(commit=False)
            contato.save()
            return redirect('contact:update', contact_id=contato.pk)

        return render(request, 'contact/create.html', context)
    
    context = {
        'forms': ContactForm(instance=contact),
        'form_action': form_action
    }
    return render(request, 'contact/create.html', context)

def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    confirma = request.POST.get('confirma', 'não')
    if confirma == 'sim':
        contact.delete()
        return redirect('contact:index')
    
    return render(
        request, 
        'contact/contact.html',
        {
            'contato': contact,
            'confirma': confirma
        }
    )