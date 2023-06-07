from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('listarEquipo/', login_required(views.equipo_list_view), name='listarEquipo'),
    path('equipo-create/', login_required(views.equipoCreate), name='equipo-create'),
    path('equipo-update/<int:id>', login_required(views.equipoUpdate), name='equipo-update'),
    path('listarCliente/', login_required(views.cliente_list_view), name='listarCliente'),
    path('cliente-create/', login_required(views.clienteCreate), name='cliente-create'),
    path('cliente-update/<int:id>', login_required(views.clienteUpdate), name='cliente-update'),
    path('tecnico-list/', login_required(views.tecnicoList), name='tecnico-list'),
    path('tecnico-create/', login_required(views.tecnicoCreate), name='tecnico-create'),
    path('tecnico-update/<int:id>', login_required(views.tecnicoUpdate), name='tecnico-update'),
    path('numparte-list/', login_required(views.numparte_list_view), name='numparte-list'),
    path('parte-create/', login_required(views.parteCreate), name='parte-create'),
    path('parte-update/<int:id>', login_required(views.parteUpdate), name='parte-update'),
    path('alistamiento-create/', login_required(views.alistamientoCreate), name='alistamiento-create'),
    path('alistamiento-list/', login_required(views.alistamiento_list_view), name='alistamiento-list'),
    path('alistamiento-update/<int:id>', login_required(views.alistamientoUpdate), name='alistamiento-update'),
    path('modelo-create/', login_required(views.modeloCreate), name='modelo-create'),
    path('marca-create/', login_required(views.marcaCreate), name='marca-create'),
    path('register/', views.register, name='register'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("uploadFile/", views.uploadFile, name = "uploadFile"),
    path("uploadFileServ/", views.uploadFileServ, name = "uploadFileServ"),
    path('manualPartes-list/', login_required(views.manualPartes_list_view), name='manualPartes-list'),
    path('manualServicio-list/', login_required(views.manualServicio_list_view), name='manualServicio-list'),
    path('repuestotaller-create/', login_required(views.repuestoTallerCreate), name='repuestotaller-create'),
    path('repuestotaller-list/', login_required(views.repuestotaller_list_view), name='repuestotaller-list'),
    path('ejemplo-modal/', login_required(views.ejemploModal), name='ejemplo-modal'),
    path('add-modal', login_required(views.addModal), name='add-modal'),
    path('edit-modal', login_required(views.editModal), name='edit-modal'),
    path('update-modal/<str:id>', login_required(views.updateModal), name='update-modal'),
    path('delete-modal/<str:id>', login_required(views.deleteModal), name='delete-modal'),
]
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )