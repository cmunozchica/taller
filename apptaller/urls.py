from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.index), name='index'),    
    path('accounts/login/', LoginView.as_view(template_name='apptaller/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),
    path('cliente-list/', login_required(views.clienteList), name='cliente-list'),
    path('add-cliente', login_required(views.addCliente), name='add-cliente'),
    path('edit-cliente', login_required(views.editCliente), name='edit-cliente'),
    path('update-cliente/<str:id>', login_required(views.updateCliente), name='update-cliente'),
    path('delete-cliente/<str:id>', login_required(views.deleteCliente), name='delete-cliente'),
    path('pdf-clientes/', login_required(views.ListClientesPdf.as_view()), name='pdf-clientes'),
    path('reporte_excel_clientes/', login_required(views.reporteClienteExcel.as_view()) , name='reporte_excel_clientes'),
    path('tecnico-list/', login_required(views.tecnicoList), name='tecnico-list'),
    path('add-tecnico', login_required(views.addTecnico), name='add-tecnico'),
    path('edit-tecnico', login_required(views.editTecnico), name='edit-tecnico'),
    path('update-tecnico/<str:id>', login_required(views.updateTecnico), name='update-tecnico'),
    path('delete-tecnico/<str:id>', login_required(views.deleteTecnico), name='delete-tecnico'),
    path('pdf-tecnico/', login_required(views.ListTecnicosPdf.as_view()), name='pdf-tecnico'),
    path('reporte_excel_tecnicos/', login_required(views.reporteTecnicoExcel.as_view() ), name='reporte_excel_tecnicos'),
    path('add-marca', login_required(views.addMarca), name='add-marca'),
    path('add-modelo', login_required(views.addModelo), name='add-modelo'),
    path('equipo-list/', login_required(views.equipoList), name='equipo-list'),
    path('add-equipo/', login_required(views.addEquipo), name='add-equipo'),    
    path('equipo-list/update-equipo/<str:id>', login_required(views.updateEquipo), name='update-equipo'),
    path('delete-equipo/<str:id>', login_required(views.deleteEquipo), name='delete-equipo'),
    path('manualServicio-list/', login_required(views.manualServicio_list_view), name='manualServicio-list'),
    path("uploadFileServ/", login_required(views.uploadFileServ), name = "uploadFileServ"),
    path('delete-manual/<str:id>', login_required(views.deleteManualServ), name='delete-manual'),
    path('manualParte-list/', login_required(views.manualParte_list_view), name='manualParte-list'),
    path("uploadFilePart/", login_required(views.uploadFilePart), name = "uploadFilePart"),
    path('numParte-list/', login_required(views.numParteList), name='numParte-list'),
    path('add-numparte', login_required(views.addNumParte), name='add-numparte'),
    path('edit-numparte', login_required(views.editNumParte), name='edit-numparte'),
    path('update-numparte/<str:id>', login_required(views.updateNumParte), name='update-numparte'),
    path('delete-numparte/<str:id>', login_required(views.deleteNumParte), name='delete-numparte'),
    path('alistamiento-list/', login_required(views.alistamientoList), name='alistamiento-list'),
    path('add-alistamiento/', login_required(views.addAlistamiento), name='add-alistamiento'),    
    path('alistamiento-list/update-alistamiento/<str:id>', login_required(views.updateAlistamiento), name='update-alistamiento'),
    path('diagnostico-list/', login_required(views.diagnosticoList), name='diagnostico-list'),
    path('add-diagnostico/', login_required(views.addDiagnostico), name='add-diagnostico'), 
    path('insumo-list/', login_required(views.insumoTecnicoList), name='insumo-list'),
    path('add-insumo/', login_required(views.addInsumo), name='add-insumo'),
    path('herramienta-list/', login_required(views.herramientaList), name='herramienta-list'),
    path('add-herramienta/', login_required(views.addHerramienta), name='add-herramienta'),
    path('equipo-list/qr_gen/', views.qr_gen, name="qr_gen"),
]
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )