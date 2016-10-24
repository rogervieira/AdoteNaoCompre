from django.shortcuts import render, redirect
from AdoteNaoCompreSITE.forms import UserForm, ExtraInfoForm
from django.contrib.auth.decorators import login_required
from AdoteNaoCompreSITE.models.dog import Dog
from AdoteNaoCompreSITE.models.user_extras import User_extras
from AdoteNaoCompreSITE.controllers import user_controller
from django.contrib.auth.models import User
from django.contrib import messages


def create(request):
    # se for POST, o usuario esta sendo criado
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                    username=request.POST['username'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    password=request.POST['password'],
                    email=request.POST['email']
                )

            user = User.objects.get(username=request.POST['username'])

            User_extras.objects.create(
                IdPai=user
            )

            messages.success(request, 'Usuário criado com sucesso.', extra_tags='alert-success')
            return render(request, 'home.html', {})
        else:
            print(form.errors)
                        
    # se for GET, devolve a pagina de criação do usuario
    else:
        form = UserForm()
        
    return render(request, 'user/create.html', {'UserForm': form})


@login_required
def show_profile(request):
    user = request.user
    if user.is_authenticated():
        caes = Dog.objects.filter(IdProtetor=request.user)
        dto = {
                'Nome': user.first_name + ' ' + user.last_name
            }
        return render(request, 'user/profile.html', {'dto': dto.items(), 'caes': caes})

@login_required
def edit_extras(request):
    user = request.user
    extra = User_extras.objects.get(IdPai=user)

    if request.method == "POST":
        form = ExtraInfoForm(request.POST, instance=extra)

        if form.is_valid():
            extra = form.save(commit=False)
            extra.Telefone = request.POST['Telefone']
            extra.Celular = request.POST['Celular']
            extra.Estado = request.POST['Estado']
            extra.Cidade = request.POST['Cidade']
            extra.CEP = request.POST['CEP']
            extra.save()
            return redirect(user_controller.show_profile)
    else:
        form = ExtraInfoForm(instance=extra)
        return render(request, 'user/extra_info.html', {'form': form})


def show(request, id):
    user = User.objects.filter(id=id)
    return render(request, 'user/show.html', {'user': user})
