from django.db import models

# Create your models here.
class Cliente(models.Model):
    nit = models.CharField(max_length=20, unique=True)
    razon_social = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    contacto = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(
            self.nit,
            self.razon_social,
            self.direccion,
            self.telefono,
            self.email,
            self.ciudad,
            self.contacto
        )

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'


ESTADO_CHOICES = (
    ('ACTIVO', 'ACTIVO'),
    ('INACTIVO', 'INACTIVO')

)

class Tecnico(models.Model):
    cedula = models.CharField(max_length=15, unique=True ,null=True)
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    cargo = models.CharField(max_length=10, null=False)
    celular = models.CharField(max_length=15, null=False)
    correo = models.EmailField(null=True)
    estado = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}  {}'.format(
            
            self.nombre,
            self.apellido,

        )
    
class Marca(models.Model):
    marca = models.CharField(max_length=15)

    def __str__(self):

       return self.marca
    
class Modelo(models.Model):
    modelo = models.CharField(max_length=15)

    def __str__(self):

       return self.modelo
    
class Equipo(models.Model):
    serie = models.CharField(max_length=20 ,unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    accesorio = models.TextField(max_length=100, blank=True )
    contador = models.CharField(max_length=8, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(blank=True)



    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(
            self.serie,
            self.marca,
            self.modelo,
            self.accesorio,
            self.contador,
            self.created,
            self.update
        )

    class Meta:
        verbose_name = 'equipo'
        verbose_name_plural = 'equipos'


class ManualServicio(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'manualServicio'
        verbose_name_plural = 'manualServicios'

class ManualParte(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'manualParte'
        verbose_name_plural = 'manualPartes'


class NumParte(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    numero_parte = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return '{} - {} - {} - {}'.format(
            self.marca,
            self.modelo,
            self.numero_parte,
            self.descripcion
        )

ALISTAR_CHOICES = (
    ('Para alistar', 'Para alistar'),
    ('En alistamiento', 'En alistamiento'),
    ('Equipo listo', 'Equipo listo'),
    ('Equipo entregado', 'Equipo entregado'),
    ('Equipo para partes', 'Equipo para partes'),
    
)

class Alistamiento(models.Model):    
    serie = models.CharField(max_length=30 )
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE )
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    accesorio = models.CharField(max_length=50, blank=True, null=True)
    contador = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=25, choices=ALISTAR_CHOICES)
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    update = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'alistamiento'
        verbose_name_plural = 'alistamientos'

    def __str__(self):
        return '{} - {} - {} - {}'.format(
            self.serie,
            self.marca,
            self.modelo,
            self.accesorio,
            self.tecnico,
            self.accesorio,
            self.contador,
            self.estado,
            self.created,

            )

class EquipoPartes(models.Model):
    serie = models.CharField(max_length=20 ,unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    detalle = models.TextField(max_length=500, blank=True, null=True)
    ubicacion = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(blank=True, null=True)



    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(
            self.serie,
            self.marca,
            self.modelo,
            self.detalle,
            self.ubicacion,
            self.created,
            self.update
        )

TIPO_CHOICES = (
    ('Multifuncional', 'Multifuncional'),
    ('Impresora', 'Impresora'),    
)
DISPONIBLE_CHOICES = (
    ('SI', 'SI'),
    ('NO', 'NO')
)

class DiagnosticoEquipos(models.Model):
    serie = models.CharField(max_length=20)
    created = models.DateField(auto_now_add=True)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    bodega = models.CharField(max_length=20)
    localizacion = models.CharField(max_length=20)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo,on_delete=models.CASCADE )
    contador = models.CharField(max_length=7)
    accesorio = models.TextField(max_length=100)
    update = models.DateField()
    diagnostico = models.TextField(max_length=100)
    disponible = models.CharField(max_length=2, choices=DISPONIBLE_CHOICES)

    class Meta:
        verbose_name = 'diagnostico'
        verbose_name_plural = 'diagnosticos'

    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(
            self.serie,
            
            self.tecnico,
            self.bodega,
            self.localizacion,
            self.marca,
            self.modelo,
            self.contador,
            self.accesorio,
            self.update,
            self.diagnostico
        )
    
class InsumosTecnicos(models.Model):
    insumo = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'insumo'
        verbose_name_plural = 'insumos'

    def __str__(self):
        return '{} - {} - {} - {} '.format(
            self.insumo,
            self.cantidad,
            self.tecnico,
            self.fecha,

        )
    
class HerramientaTecnicos(models.Model):
    herramienta = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    prestamo = models.CharField(max_length=2, choices=DISPONIBLE_CHOICES)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'herramienta'
        verbose_name_plural = 'herramientas'

    def __str__(self):
        return '{} - {} - {} - {} '.format(
            self.herramienta,
            self.cantidad,
            self.prestamo,
            self.tecnico,
            self.fecha,

        )


