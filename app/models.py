from django.db import models

# Create your models here.
class Tecnico(models.Model):
    cedula = models.CharField(max_length=15, unique=True ,null=True)
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    cargo = models.CharField(max_length=10, null=False)
    celular = models.CharField(max_length=15, null=True)
    correo = models.EmailField(null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{} - {} - {} - {}'.format(
            self.cedula,
            self.nombre,
            self.apellido,
            self.cargo,
            self.celular,
            self.correo
        )

EQUIPO_CHOICES = (
    ('RICOH', 'RICOH'),
    ('KYOCERA', 'KYOCERA'),
    ('KONICA-MINOLTA', 'KONICA-MINOLTA'),
    ('BROTHER', 'BROTHER'),
    ('HP', 'HP'),
    
)
class Equipo1(models.Model):
    serie = models.CharField(max_length=20 ,unique=True)
    marca = models.CharField(max_length=20, choices=EQUIPO_CHOICES)
    modelo = models.CharField(max_length=10)
    accesorio = models.TextField(max_length=100)
    contador = models.CharField(max_length=8, null=True)

    def __str__(self):
        return self.serie

class Cliente(models.Model):
    nit = models.CharField(max_length=20, unique=True)
    razon_social = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    contacto = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(
            self.nit,
            self.razon_social,
            self.direccion,
            self.telefono,
            self.ciudad,
            self.contacto
        )

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

class Marca(models.Model):
    marca = models.CharField(primary_key=True, max_length=15)

    def __str__(self):
        return self.marca
    
    class Meta:
        db_table = "marca"

class Modelo(models.Model):
    modelo = models.CharField(primary_key=True, max_length=15)

    def __str__(self):
        return self.modelo

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
    serie = models.CharField(max_length=30)
    marca = models.CharField(max_length=20, choices=EQUIPO_CHOICES )
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE )
    accesorio = models.CharField(max_length=50)
    contador = models.CharField(max_length=30)
    estado = models.CharField(max_length=25, choices=ALISTAR_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'alistamiento'
        verbose_name_plural = 'alistamientos'




    def __str__(self):
        return '{} - {} - {} - {}'.format(
            self.serie,
            self.marca,
            self.modelo,
            self.accesorio,
            self.contador,
            self.estado,
            self.created,
            self.update
            )

class RepuestoTaller(models.Model):    
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    numero_parte = models.ForeignKey(NumParte, on_delete=models.CASCADE)
    serie = models.ForeignKey(Equipo1, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now=True)

class ManualParte(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'manualParte'
        verbose_name_plural = 'manualPartes'

class ManualServicio(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Uploaded Files/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'manualServicio'
        verbose_name_plural = 'manualServicios'

class Employees(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name


