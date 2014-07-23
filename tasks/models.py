#encoding:utf-8
from django.db import models

class Dominio(models.Model):
    dominio_id = models.CharField(primary_key=True, max_length=40)
    dominio_desc = models.CharField(max_length=80)
    dominio_activo = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'task_dominios'
        verbose_name = u'Dominio'
        verbose_name_plural = u'Dominios'
        ordering = ('dominio_id',)
    def __unicode__(self):
        return self.dominio_id

class DominioValor(models.Model):
    dominio = models.ForeignKey(Dominio)
    dominio_valor = models.CharField(primary_key=True, max_length=40)
    dominio_activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_dominios_valores'
        unique_together = ('dominio', 'dominio_valor')
        verbose_name = u'Dominio Valor'
        verbose_name_plural = u'Dominio Valores'
        ordering = ('dominio', 'dominio_valor',)
    def __unicode__(self):
        return self.dominio_id

class Empresa(models.Model):
    empresa_id = models.CharField(primary_key=True, max_length=40)
    corporacion = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_empresas'

class Agencia(models.Model):
    empresa = models.ForeignKey(Empresa)
    agencia_id = models.CharField(max_length=40)
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_agencias'

class Sistema(models.Model):
    sistema_id = models.CharField(primary_key=True, max_length=40)
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_sistemas'

class Subsistema(models.Model):
    sistema = models.ForeignKey(Sistema)
    subsistema_id = models.CharField(max_length=40)
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_subsistemas'

class Modulo(models.Model):
    sistema = models.ForeignKey(Subsistema, related_name='Modulo_sistemas')
    subsistema = models.ForeignKey(Subsistema, related_name='Modulo_subsistemas')
    modulo_id = models.CharField(max_length=40)
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_modulos'

class Recurso(models.Model):
    recurso_id = models.CharField(primary_key=True, max_length=40)
    nombre_completo = models.CharField(max_length=40)
    cod_empleado = models.IntegerField()
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_recursos'

class RecursoSistema(models.Model):
    recurso = models.ForeignKey(Recurso)
    sistema = models.ForeignKey(Sistema)
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_recursos_sistemas'

class ColorIssue(models.Model):
    color_id = models.CharField(primary_key=True, max_length=20)
    hexadecimal = models.CharField(max_length=6)
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_colores_issue'

class Issue(models.Model):
    issue_id = models.IntegerField(primary_key=True)
    recurso = models.ForeignKey(Recurso)
    segmento = models.CharField(max_length=40)
    empresa = models.ForeignKey(Agencia, related_name='Issue_empresas')
    agencia = models.ForeignKey(Agencia, related_name='Issue_agencias')
    sistema = models.ForeignKey(Modulo, related_name='Issue_sistemas')
    subsistema = models.ForeignKey(Modulo, related_name='Issue_subsistemas')
    modulo = models.ForeignKey(Modulo, related_name='Issue_modulos')
    descripcion = models.CharField(max_length=4000)
    tipo_issue = models.CharField(max_length=40)
    origen_issue = models.CharField(max_length=40)
    referencia = models.CharField(max_length=1000, blank=True)
    clase_issue = models.CharField(max_length=40)
    complejidad = models.CharField(max_length=40)
    estimacion_hrs = models.IntegerField()
    fecha_entrega = models.DateField(blank=True, null=True)
    prioridad = models.IntegerField()
    estado_issue = models.CharField(max_length=40)
    pct_avance = models.IntegerField()
    fase_issue = models.CharField(max_length=40)
    color = models.ForeignKey(ColorIssue)
    observaciones = models.CharField(max_length=2000, blank=True)
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_issues'

class IssueReferencia(models.Model):
    referencia_id = models.IntegerField(primary_key=True)
    issue = models.ForeignKey(Issue)
    solicitante = models.CharField(max_length=60)
    patrocinador = models.CharField(max_length=60)
    fecha_solicitud = models.DateField()
    tipo_ref = models.CharField(max_length=40)
    dato_ref = models.CharField(max_length=40, blank=True)
    link_ref = models.CharField(max_length=512, blank=True)
    file_ref = models.CharField(max_length=64, blank=True)
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_issues_referencias'

class IssueActividad(models.Model):
    actividad_id = models.IntegerField(primary_key=True)
    issue = models.ForeignKey(Issue)
    recurso = models.ForeignKey(Recurso)
    descripcion = models.CharField(max_length=4000)
    fecha_actividad = models.DateField()
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_issues_actividades'
        verbose_name=u'Issue Actividad'
        verbose_name_plural = u'Issues Actividades'
        ordering = ('actividad_id',)
    def __unicode__(self):
        return self.actividad_id

class IssueEmpresa(models.Model):
    issue = models.ForeignKey(Issue)
    empresa = models.ForeignKey(Empresa)
    referencia = models.CharField(max_length=512, blank=True)
    fecha_ref = models.DateField(blank=True, null=True)
    activo = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'task_issues_empresas'
