from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from COMPRA_VENTA.forms import FormularioProductos
from COMPRA_VENTA.models import Producto
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest

# VISTA INICIAL 
def index(request):
    productos = Producto.objects.all()
    return render(request, 'COMPRA_VENTA/index.html',
                    {"productos": productos,
                    "titulo": "mis produtos son:"})

def all_productos(request):
    if request.method == 'GET':
        # Obtener un formulario vacio 
        formulario_vacio = FormularioProductos()
        return render(request, 'COMPRA_VENTA/agregar.html', {'formulario':formulario_vacio})
    elif request.method == 'POST':
        # Crear un formulario con los datos recibidos 
        formulario = FormularioProductos(request.POST, request.FILES)


        if formulario.is_valid():
            # Guardar en la BD
            formulario.save()
            return render(request, 'COMPRA_VENTA/agregar.html', {
                'formulario': formulario,
                'message': 'Ariticulo Creado con exito'})
        else:
            # Regresar al formulario con los errores 
            return render(request, 'COMPRA_VENTA/agregar.html', {'formulario': formulario})

def signupAdmin(request): 
    if request.method == 'GET':
        return render(request, 'COMPRA_VENTA/signup.html',{
        'form': UserCreationForm
    }) 
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.
                POST['password1'])
                user.save()
                login(request, user)
                return redirect('homeuser')
            except IntegrityError:
                return render(request, 'COMPRA_VENTA/signupAdmin.html',{
                    'form': UserCreationForm,
                    'error': 'Username Already Exist'
                }) 
        return render(request, 'COMPRA_VENTA/signupAdmin.html',{
                    'form': UserCreationForm,
                    'error': 'Password Do not match'
                })

def signupUser(request): 
    if request.method == 'GET':
        return render(request, 'COMPRA_VENTA/signupUser.html',{
        'form': UserCreationForm
    }) 
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.
                POST['password1'])
                user.save()
                login(request, user)
                return redirect('homeuserU')
            except IntegrityError:
                return render(request, 'COMPRA_VENTA/signupUser.html',{
                    'form': UserCreationForm,
                    'error': 'Username Already Exist'
                }) 
        return render(request, 'COMPRA_VENTA/signupUser.html',{
                    'form': UserCreationForm,
                    'error': 'Password Do not match'
                })  
            
def homeuser(request):
    if request.method == 'GET':
        view = request.GET.get('view')
        fabricante = request.GET.get('fabricante')
        
        if view == 'index':
            if fabricante:
                productos = Producto.objects.filter(fabricante__icontains=fabricante)
            else:
                productos = Producto.objects.all()
            return render(request, 'COMPRA_VENTA/homeuser.html', {
                "productos": productos,
                "view": "index",
                "fabricante": fabricante
            })
        elif view == 'all_productos':
            formulario_vacio = FormularioProductos()
            return render(request, 'COMPRA_VENTA/homeuser.html', {
                'formulario': formulario_vacio,
                'view': 'all_productos'
            })
        else:
            return render(request, 'COMPRA_VENTA/homeuser.html', {
                'view': 'default'
            })
    elif request.method == 'POST' and 'all_productos' in request.POST:
        formulario = FormularioProductos(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('homeuser?view=index')
        else:
            return render(request, 'COMPRA_VENTA/homeuser.html', {
                'formulario': formulario,
                'view': 'all_productos'
            })
    else:
        return render(request, 'COMPRA_VENTA/homeuser.html', {
            'view': 'default'
        })

def homeuserU(request):
    if request.method == 'GET' or request.method=='POST':
        view = request.GET.get('view')
        fabricante = request.GET.get('fabricante')

        if request.method == 'POST':
            producto_id = request.POST.get('producto_id')
            if not producto_id:
                return  HttpResponseBadRequest("Missing product ID")
            producto = get_object_or_404(Producto, id=producto_id)
            producto.favorito= True
            producto.save()

        
        if view == 'index':
            if fabricante:
                productos = Producto.objects.filter(fabricante__icontains=fabricante)
            else:
                productos = Producto.objects.all()
            return render(request, 'COMPRA_VENTA/homeuserU.html', {
                "productos": productos,
                "view": "index",
                "fabricante": fabricante
            })
        elif view == 'all_productos':
            formulario_vacio = FormularioProductos()
            return render(request, 'COMPRA_VENTA/homeuserU.html', {
                'formulario': formulario_vacio,
                'view': 'all_productos'
            })
        else:
            return render(request, 'COMPRA_VENTA/homeuserU.html', {
                'view': 'default'
            })
    else:
        return render(request, 'COMPRA_VENTA/homeuserU.html', {
            'view': 'default'
        })

def signout(request):
    logout(request)
    return redirect('index')

def signinAdmin(request):
    if request.method == 'GET':
        return render(request, 'COMPRA_VENTA/signinAdmin.html',{
            'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'COMPRA_VENTA/signinAdmin.html',{
                'form': AuthenticationForm,
                'error': 'Username or Password is incorrect'
            })
        else:
            login(request, user)
            return redirect('homeuser')
        
def signinUser(request):
    if request.method == 'GET':
        return render(request, 'COMPRA_VENTA/signinUser.html',{
            'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'COMPRA_VENTA/signinUser.html',{
                'form': AuthenticationForm,
                'error': 'Username or Password is incorrect'
            })
        else:
            login(request, user)
            return redirect('homeuserU')
        
def favoritos(request):
    if request.method == 'GET' or request.method == 'POST':
        if request.method == 'POST':
            producto_id = request.POST.get('producto_id')
            if not producto_id:
                return HttpResponseBadRequest("Missing product ID")
            producto = get_object_or_404(Producto, id=producto_id)
            producto.favorito = False
            producto.save()

        # Filtrar solo productos favoritos
        productos = Producto.objects.filter(favorito=True)

        return render(request, 'COMPRA_VENTA/favoritos.html', {
            "productos": productos
        })
    else:
        return render(request, 'COMPRA_VENTA/favoritos.html')

