from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustonUserModel
from validate_docbr import CPF
import sys
import re
from pessoas.models import Pessoas

# Create your views here.


def cad_user(request):
    """Cadastra usuario caso ele ainda não seja cadastrado. 
    Faz a verificação atraves do cpf """

    template_name = 'usuarios/signup.html'
    if request.method == 'GET':
        return render(request, template_name)
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')

        cpf_valida = CPF()
        if cpf_valida.validate(cpf) == False:
            messages.info(request, 'CPF iválido')
            return render(request, template_name)

        first_name = name.split(None, 1)[0]
        last_name = name.split(None, 1)[1]
        username = email.split('@')[0]

        # Em desuso, Validação de senha foi feita em javascipt
        flag = 0
        while True:
            if len(password) < 8:
                flag = -1
                break

            elif not ((re.search("[a-z]", password) or
                       re.search("[A-Z]", password)) and
                      re.search("[0-9]", password)):
                flag = -1
                break
            else:
                break
        if flag == -1:
            messages.add_message(
                request, messages.INFO, 'Senha iválida! A senha deve conter mínimo 8 caractere contendo letras e números')
            return redirect('signup')

        user = CustonUserModel.objects.filter(cpf=cpf).first()
        if user:
            messages.info(request, 'CPF já cadastrado')
            return redirect('signup')

        else:
            user = CustonUserModel.objects.create_user(
                username,
                email,
                password,
                cpf=cpf,
                first_name=first_name,
                last_name=last_name)
            user.save()

            # Cria o objeto pessoas - perfil para dados cadastrais
            pessoas = Pessoas.objects.create(
                usuario=user, nome=name, cpf=cpf, email=email)

            # Aqui faz o login automático, ao se cadastrar
            user2 = authenticate(cpf=cpf, password=password)
            # if user is not None:
            # login vem do django
            # login(request, user2)

            return redirect('login')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "GET":
            return render(request, 'usuarios/login.html')
        else:
            cpf = request.POST.get('username')
            password = request.POST.get('pswd')
            user = authenticate(cpf=cpf, password=password)
            if user is not None:
                # login vem do django
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Usuário ou senha incorretos")
                return redirect('login')


def logout_user(request):
    logout(request)
    return render(request, 'usuarios/login.html')


def lista_user(request):
    template_name = 'usuarios/lista_user.html'
    query = CustonUserModel.objects.all()

    context = {'query': query}
    return render(request, template_name, context)


