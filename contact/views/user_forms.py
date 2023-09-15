from  django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages

def register(request):
    form = RegisterForm()
    # messages.info(request, 'Menssagem teste')
    # messages.error(request, 'Menssagem teste')
    # messages.warning(request, 'Menssagem teste')
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Usuario criado com sucesso')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'forms': form
        }
    )