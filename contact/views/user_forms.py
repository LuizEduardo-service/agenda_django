from  django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'forms': form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            print(user)
            messages.success(request, 'Logado com Sucesso!')
            return redirect('contact:index')
        messages.error(request, 'Login Invalido')

    return render(
        request,
        'contact/login.html',
        {
            'forms': form
        }
    )   

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request) 
    return redirect('contact:login')

@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'forms': form
            }
        )
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/login.html',
            {
                'forms': form
            }
        )
    form.save()
    return redirect('user:user_update')