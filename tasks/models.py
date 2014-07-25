#encoding:utf-8
from django.db import models

class Dominio(models.Model):
    dominio_id = models.CharField(primary_key=True, max_length=40)
    descripcion = models.CharField(max_length=80)
    activo = models.BooleanField(default=True)
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
    valor = models.CharField(primary_key=True, max_length=40)
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_dominios_valores'
        unique_together = ('dominio', 'valor')
        verbose_name = u'Dominio Valor'
        verbose_name_plural = u'Dominio Valores'
        ordering = ('dominio', 'valor',)
    def __unicode__(self):
        return u"%s - %s" % (self.dominio, self.valor)

class Corporacion(models.Model):
    corporacion_id = models.CharField(primary_key=True, max_length=40)
    class Meta:
        managed = False
        db_table = 'vtask_corporaciones'
        verbose_name = u'Corporacion'
        verbose_name_plural = u'Corporaciones'
        ordering = ('corporacion_id',)
    def __unicode__(self):
        return self.corporacion_id

class Pais(models.Model):
    pais_id = models.CharField(primary_key=True, max_length=40)
    class Meta:
        managed = False
        db_table = 'vtask_paises'
        verbose_name = u'Pais'
        verbose_name_plural = u'Paises'
        ordering = ('pais_id',)
    def __unicode__(self):
        return self.pais_id

class Empresa(models.Model):
    empresa_id = models.CharField(primary_key=True, max_length=40)
    corporacion = models.ForeignKey(Corporacion)
    pais = models.ForeignKey(Pais)
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_empresas'
        verbose_name = u'Empresa'
        verbose_name_plural = u'Empresas'
        ordering = ('corporacion', 'empresa_id',)
    def __unicode__(self):
        return u"%s - %s" % (self.corporacion, self.empresa_id)

class Agencia(models.Model):
    empresa = models.ForeignKey(Empresa)
    agencia_id = models.IntegerField(primary_key=True, blank=True, null=True)
    descripcion = models.CharField(max_length=40)
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_agencias'
        unique_together = (('empresa', 'agencia_id'),)
        verbose_name = u'Agencia'
        verbose_name_plural = u'Agencias'
        ordering = ('empresa', 'agencia_id',)
    def __unicode__(self):
        return u"%s - %s" % (self.empresa, self.descripcion)

class Sistema(models.Model):
    sistema_id = models.CharField(primary_key=True, max_length=40)
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_sistemas'
        verbose_name = u'Sistema'
        verbose_name_plural = u'Sistemas'
        ordering = ('sistema_id',)
    def __unicode__(self):
        return self.sistema_id

class Subsistema(models.Model):
    sistema = models.ForeignKey(Sistema)
    subsistema_id = models.CharField(primary_key=True, max_length=40)
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_subsistemas'
        unique_together = ('sistema', 'subsistema_id')
        verbose_name = u'SubSistema'
        verbose_name_plural = u'SubSistemas'
        ordering = ('sistema', 'subsistema_id',)
    def __unicode__(self):
        return u"%s - %s" % (self.sistema, self.subsistema_id)

class Modulo(models.Model):
    sistema = models.ForeignKey(Subsistema, related_name='Modulo_sistemas')
    subsistema = models.ForeignKey(Subsistema, related_name='Modulo_subsistemas')
    modulo_id = models.CharField(primary_key=True, max_length=40)
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_modulos'
        unique_together = ('sistema', 'subsistema', 'modulo_id')
        verbose_name = u'Modulo'
        verbose_name_plural = u'Modulos'
        ordering = ('sistema', 'subsistema', 'modulo_id',)
    def __unicode__(self):
        return u"%s - %s - %s" % (self.sistema, self.subsistema, self.modulo_id)

class Recurso(models.Model):
    recurso_id = models.CharField(primary_key=True, max_length=40)
    nombre_completo = models.CharField(max_length=40)
    cod_empleado = models.IntegerField()
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_recursos'
        verbose_name = u'Recurso'
        verbose_name_plural = u'Recursos'
        ordering = ('recurso_id',)
    def __unicode__(self):
        return u"%s - %s" % (self.recurso_id, self.nombre_completo)

class RecursoSistema(models.Model):
    recurso = models.ForeignKey(Recurso)
    sistema = models.ForeignKey(Sistema)
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_recursos_sistemas'
        unique_together = ('recurso', 'sistema')
        verbose_name = u'Recurso Sistema'
        verbose_name_plural = u'Recursos Sistema'
        ordering = ('recurso', 'sistema',)
    def __unicode__(self):
        return u"%s - %s" % (self.sistema, self.recurso)

class ColorIssue(models.Model):
    color_id = models.CharField(primary_key=True, max_length=20)
    hexadecimal = models.CharField(max_length=6)
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_colores_issue'
        verbose_name = u'Color Issue'
        verbose_name_plural = u'Colores Issue'
        ordering = ('color_id',)
    def __unicode__(self):
        return u"%s - %s" % (self.color_id, self.hexadecimal)

class Issue(models.Model):
    issue_id = models.IntegerField(primary_key=True)
    recurso = models.ForeignKey(Recurso, related_name='Issue_recursos')
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
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    prioridad = models.IntegerField()
    estado_issue = models.CharField(max_length=40)
    pct_avance = models.IntegerField()
    fase_issue = models.CharField(max_length=40)
    color = models.ForeignKey(ColorIssue, related_name='Issue_coloresissue')
    observaciones = models.CharField(max_length=2000, blank=True)
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_issues'
        verbose_name = u'Issue'
        verbose_name_plural = u'Issues'
        ordering = ('issue_id',)
    def __unicode__(self):
        return u"%s - %s - %s - %s - %s - %s - %s" % (self.issue_id, self.recurso, self.segmento, self.empresa, self.sistema, self.subsistema, self.tipo_issue)

class IssueReferencia(models.Model):
    issue = models.ForeignKey(Issue)
    referencia_id = models.IntegerField(primary_key=True)
    solicitante = models.CharField(max_length=60)
    patrocinador = models.CharField(max_length=60)
    fecha_solicitud = models.DateTimeField()
    tipo_ref = models.CharField(max_length=40)
    dato_ref = models.CharField(max_length=40, blank=True)
    link_ref = models.CharField(max_length=512, blank=True)
    file_ref = models.FileField(upload_to='documents/%Y/%m/%d')
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_issues_referencias'
        unique_together = ('issue', 'referencia_id')
        verbose_name = u'Issue Referencia'
        verbose_name_plural = u'Issue Referencias'
        ordering = ('issue', 'referencia_id',)
    def __unicode__(self):
        return u"%s - %s - %s" % (self.issue, self.referencia_id, self.solicitante)

class IssueActividad(models.Model):
    issue = models.ForeignKey(Issue)
    actividad_id = models.IntegerField(primary_key=True)
    recurso = models.ForeignKey(Recurso)
    descripcion = models.CharField(max_length=4000)
    fecha_actividad = models.DateTimeField()
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_issues_actividades'
        unique_together = ('issue', 'actividad_id')
        verbose_name=u'Issue Actividad'
        verbose_name_plural = u'Issues Actividades'
        ordering = ('issue', 'actividad_id',)
    def __unicode__(self):
        return u"%s - %s - %s" % (self.issue, self.actividad_id, self.recurso)

class IssueEmpresa(models.Model):
    issue = models.ForeignKey(Issue)
    empresa = models.ForeignKey(Empresa)
    referencia = models.CharField(max_length=512, blank=True)
    fecha_ref = models.DateTimeField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    class Meta:
        managed = False
        db_table = 'task_issues_empresas'
        unique_together = ('issue', 'empresa')
        verbose_name = u'Issue Empresa'
        verbose_name_plural = u'Issue Empresas'
        ordering = ('issue', 'empresa',)
    def __unicode__(self):
        return u"%s - %s" % (self.issue, self.Empresa)
