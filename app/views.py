from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy
from .models import  Cliente, Equipo1, Tecnico, NumParte, Alistamiento, Marca, Modelo, RepuestoTaller, ManualParte, ManualServicio, Employees
from django.template import RequestContext
from .forms import TecnicoForm, EquipoForm, ClienteForm, NumParteForm, AlistamientoForm, modeloForm, MarcaForm, UserRegisterForm, ManualPartesForm, RepuestoTallerForm
from django.http import Http404
from .serializers import RepuestoSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
    else:
        form = UserRegisterForm()
    context = { 'form' : form }
    return render(request, 'register.html', context)        




def equipo_list_view(request):
    busqueda = request.GET.get("buscar")
    equipo_queryset = Equipo1.objects.all().order_by('id')
    page = request.GET.get('page', 1)

    if busqueda:
            equipo_queryset = Equipo1.objects.filter(
                Q(id__icontains = busqueda) |
                Q(serie__icontains = busqueda) |
                Q(modelo__icontains = busqueda) 
            ).distinct()
    try:        
        paginator = Paginator(equipo_queryset,8)    
        equipo_queryset = paginator.page(page)
    except:
        raise Http404    

    context = {'equipo_context':equipo_queryset, 'paginator': paginator}
    return render(request, "listarEquipo.html", context)

def equipoCreate(request):  
    if request.method == "POST":  
        form = EquipoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('equipo-list')  
            except:  
                pass  
    else:  
        form = EquipoForm()  
    return render(request,'equipo-create.html',{'form':form}) 

def equipoUpdate(request, id):  
    equipo = Equipo1.objects.get(id=id)
    form = EquipoForm(initial={'serie': equipo.serie, 'marca': equipo.marca, 'modelo': equipo.modelo, 'accesorios': equipo.accesorio, 'contador': equipo.contador})
    if request.method == "POST":  
        form = EquipoForm(request.POST, instance=equipo)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/listarEquipo')  
            except Exception as e: 
                pass    
    return render(request,'equipo-update.html',{'form':form})              

def tecnicoList(request):
    busqueda = request.GET.get("buscar")
    tecnico_queryset = Tecnico.objects.all().order_by('id')


    if busqueda:
            tecnico_queryset = Tecnico.objects.filter(
                Q(id__icontains = busqueda) |
                Q(cedula__icontains = busqueda) |
                Q(nombre__icontains = busqueda) 
            ).distinct()
    paginator = Paginator(tecnico_queryset,10)
    page = request.GET.get('page')
    tecnico_queryset = paginator.get_page(page)
    

    context = {'tecnico_context':tecnico_queryset}
    return render(request, "tecnico-list.html", context)

def tecnicoCreate(request):  
    if request.method == "POST":  
        form = TecnicoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('tecnico-list')  
            except:  
                pass  
    else:  
        form = TecnicoForm()  
    return render(request,'tecnico-create.html',{'form':form})

def tecnicoUpdate(request, id):  
    tecnico = Tecnico.objects.get(id=id)
    form = TecnicoForm(initial={'cedula': tecnico.cedula, 'nombre': tecnico.nombre, 'apellido': tecnico.apellido, 'cargo': tecnico.cargo, 'celular': tecnico.celular, 'correo': tecnico.correo})
    if request.method == "POST":  
        form = TecnicoForm(request.POST, instance=tecnico)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/tecnico-list')  
            except Exception as e: 
                pass    
    return render(request,'tecnico-update.html',{'form':form})       



def cliente_list_view(request):
    busqueda = request.GET.get("buscar")
    cliente_queryset = Cliente.objects.all().order_by('id')


    if busqueda:
            equipo_queryset = Cliente.objects.filter(
                Q(id__icontains = busqueda) |
                Q(nit__icontains = busqueda) |
                Q(razon_social__icontains = busqueda) 
            ).distinct()
    paginator = Paginator(cliente_queryset,10)
    page = request.GET.get('page')
    cliente_queryset = paginator.get_page(page)
    

    context = {'cliente_context':cliente_queryset}
    return render(request, "listarClientes.html", context)

def clienteUpdate(request, id):  
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(initial={'nit': cliente.nit,'razon_social': cliente.razon_social, 'direccion': cliente.direccion, 'telefono': cliente.telefono, 'ciudad': cliente.ciudad,  'contacto': cliente.contacto})
    if request.method == "POST":  
        form = ClienteForm(request.POST, instance=cliente)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/cliente-list')  
            except Exception as e: 
                pass    
    return render(request,'cliente-update.html',{'form':form})   

def clienteCreate(request):  
    if request.method == "POST":  
        form = ClienteForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('listarCliente')  
            except:  
                pass  
    else:  
        form = TecnicoForm()  
    return render(request,'cliente-create.html',{'form':form}) 

def numparte_list_view(request):
    busqueda = request.GET.get("buscar")
    numparte_queryset = NumParte.objects.all().order_by('id')
    page = request.GET.get('page', 1)


    if busqueda:
            numparte_queryset = NumParte.objects.filter(
                Q(id__icontains = busqueda) |
                Q(numero_parte__icontains = busqueda) |
                Q(modelo__icontains = busqueda) |
                Q(descripcion__icontains = busqueda) 
            ).distinct()

    try:        
        paginator = Paginator(numparte_queryset,8)    
        numparte_queryset = paginator.page(page)
    except:
        raise Http404



    context = {'numparte_context':numparte_queryset, 'paginator': paginator}
    return render(request, "numparte-list.html", context)

def parteCreate(request):  
    if request.method == "POST":  
        form = NumParteForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('numparte-list')  
            except:  
                pass  
    else:  
        form = NumParteForm()  
    return render(request,'parte-create.html',{'form':form})

def parteUpdate(request, id):  
    parte = NumParte.objects.get(id=id)
    form = NumParteForm(initial={'marca': parte.marca,'modelo': parte.modelo,'numero_parte': parte.numero_parte, 'descripcion': parte.descripcion})
    if request.method == "POST":  
        form = NumParteForm(request.POST, instance=parte)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/numparte-list')  
            except Exception as e: 
                pass    
    return render(request,'parte-update.html',{'form':form})   

def alistamiento_list_view(request):
    busqueda = request.GET.get("buscar")
    alistamiento_queryset = Alistamiento.objects.all().order_by('id')
    page = request.GET.get('page', 1)

    if busqueda:
            alistamiento_queryset = Alistamiento.objects.filter(
                Q(id__icontains = busqueda) |
                Q(serie__icontains = busqueda) | 
                Q(estado__icontains = busqueda) |                
                Q(create__icontains = busqueda) |
                Q(update__icontains = busqueda) 
            ).distinct()
    try:        
        paginator = Paginator(alistamiento_queryset,8)    
        alistamiento_queryset = paginator.page(page)
    except:
        raise Http404    

    context = {'alistamiento_context':alistamiento_queryset,'paginator': paginator}
    return render(request, "alistamiento-list.html", context)

 
def alistamientoCreate(request):  
    if request.method == "POST":  
        form = AlistamientoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('alistamiento-list')  
            except:  
                pass  
    else:  
        form = AlistamientoForm()  
    return render(request,'alistamiento-create.html',{'form':form})

def listar_list_view(request):
    busqueda = request.GET.get("buscar")
    alistamiento_queryset = Alistamiento.objects.all().order_by('id')


    if busqueda:
            equipo_queryset = Alistamiento.objects.filter(
                Q(id__icontains = busqueda) |
                Q(serie__icontains = busqueda) |
                Q(modelo__icontains = busqueda) 
            ).distinct()
    paginator = Paginator(equipo_queryset,10)
    page = request.GET.get('page')
    alistamiento_queryset = paginator.get_page(page)

    context = {'alistamiento_context':alistamiento_queryset}
    return render(request, "listarAlistamiento.html", context)

def alistamientoDelete(request, id):
    book = Alistamiento.objects.get(id=id)
    try:
        alistamientoDelete.delete()
    except:
        pass
    return redirect('alistamiento-list')

def alistamientoUpdate(request, id):  
    alistamiento = Alistamiento.objects.get(id=id)
    form = AlistamientoForm(initial={'serie': alistamiento.serie ,'marca': alistamiento.marca, 'modelo': alistamiento.modelo, 'accesorio': alistamiento.accesorio, 'contador': alistamiento.contador})
    if request.method == "POST":  
        form = AlistamientoForm(request.POST, instance=alistamiento)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('/alistamiento-list')  
            except Exception as e: 
                pass    
    return render(request,'alistamiento-update.html',{'form':form})   
 
def modeloCreate(request):  
    if request.method == "POST":  
        form = modeloForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('alistamiento-create')  
            except:  
                pass  
    else:  
        form = modeloForm()  
    return render(request,'modelo-create.html',{'form':form})

def marcaCreate(request):  
    if request.method == "POST":  
        form = MarcaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('alistamiento-create')  
            except:  
                pass  
    else:  
        form = MarcaForm()  
    return render(request,'marca-create.html',{'form':form})


class repuesto_list(viewsets.ModelViewSet):
    queryset = RepuestoTaller.objects.all()
    serializer_class = RepuestoSerializer

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.ManualParte(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()
        return redirect('manualPartes-list') 

    documents = models.ManualParte.objects.all()

    return render(request, "upload-file.html", context = {
        "files": documents
    })

def uploadFileServ(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.ManualServicio(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()
        return redirect('manualServicio-list') 

    documents = models.ManualServicio.objects.all()

    return render(request, "upload-file-serv.html", context = {
        "files": documents
    })

def manualPartes_list_view(request):
    busqueda = request.GET.get("buscar")
    manualPartes_queryset = ManualParte.objects.all().order_by('id')


    if busqueda:
            manualPartes_queryset = ManualParte.objects.filter(
                Q(id__icontains = busqueda) |                
                Q(title__icontains = busqueda) 
            ).distinct()
    paginator = Paginator(manualPartes_queryset,10)
    page = request.GET.get('page')
    manualPartes_queryset = paginator.get_page(page)

    context = {'manualPartes_context':manualPartes_queryset}
    return render(request, "listarManualPartes.html", context)

def manualServicio_list_view(request):
    busqueda = request.GET.get("buscar")
    manualServicio_queryset = ManualServicio.objects.all().order_by('id')


    if busqueda:
            manualServicio_queryset = ManualServicio.objects.filter(
                Q(id__icontains = busqueda) |                
                Q(title__icontains = busqueda) 
            ).distinct()
    paginator = Paginator(manualServicio_queryset,10)
    page = request.GET.get('page')
    manualServicio_queryset = paginator.get_page(page)

    context = {'manualServicio_context':manualServicio_queryset}
    return render(request, "listarManualSer.html", context)

def repuestoTallerCreate(request):  
    if request.method == "POST":  
        form = RepuestoTallerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('repuestotaller-list')  
            except:  
                pass  
    else:  
        form = RepuestoTallerForm()  
    return render(request,'repuestotaller-create.html',{'form':form})


def repuestotaller_list_view(request):

    busqueda = request.GET.get("buscar")
    repuestotaller_queryset = RepuestoTaller.objects.all().order_by('id')
    page = request.GET.get('page', 1)

    if busqueda:
            repuestotaller_queryset = RepuestoTaller.objects.filter(
                Q(id__icontains = busqueda) |
                Q(numero_parte__icontains = busqueda) |
                Q(descripcion__icontains = busqueda) 
            ).distinct()
    try:        
        paginator = Paginator(repuestotaller_queryset,10)    
        repuestotaller_queryset = paginator.page(page)
    except:
        raise Http404    

    context = {'repuestotaller_context':repuestotaller_queryset, 'paginator': paginator}
    return render(request, "repuestotaller-list.html", context)


def ejemploModal(request):
    emp = Employees.objects.all()

    context = {'emp' : emp,}
    return render(request, 'ejemplo-modal.html', context)

def addModal(request):
   if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       address = request.POST.get('address')
       phone = request.POST.get('phone')

       emp = Employees(
           name = name,
           email = email,
           address = address,
           phone = phone
       )
       emp.save()
       return redirect('ejemplo-modal')

   return render(request, 'ejemplo-modal.html') 

def editModal(request):
        emp = Employees.objects.all()

        context = {'emp' : emp,}
        return render(request, 'ejemplo-modal.html') 

def updateModal(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone,
        )
        emp.save()
        return redirect('ejemplo-modal')

    return render(request, 'ejemplo-modal.html')

def deleteModal(request,id):
    emp = Employees.objects.filter(id = id).delete()
    context = {'emp' : emp,}
    return redirect('ejemplo-modal')
