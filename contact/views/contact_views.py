from django.http import Http404
from django.shortcuts import render, get_object_or_404,redirect
from contact.models import Contact
from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    contatos = Contact.objects.all() \
        .filter(show=True) \
        .order_by('-id')
    
    paginator = Paginator(contatos , 10 )
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }
    return render(request, 'contact/index.html', context)

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')
    
    contatos = Contact.objects.all() \
        .filter(show=True) \
        .filter(
                Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value)
                )\
        .order_by('-id')
    
    paginator = Paginator(contatos , 10 )
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Pesquisa - '
    }
    return render(request, 'contact/index.html', context)

def contact(request, contact_id):
    # contatos = Contact.objects.filter(pk=contact_id).first()
    contatos = get_object_or_404(Contact, pk=contact_id, show=True)
    site_title = f'{contatos.first_name} {contatos.last_name} - '
    if contatos is None:
        raise Http404()
    context = {
        'contato': contatos,
        'site_title': site_title

    }
    return render(request, 'contact/contact.html', context)