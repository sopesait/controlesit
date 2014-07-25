from django.contrib import admin
from tasks.models import Dominio, DominioValor, Empresa, Agencia, Sistema, Subsistema, Modulo, Recurso, RecursoSistema, ColorIssue, Issue, IssueReferencia, IssueActividad, IssueEmpresa
from tasks import forms

class DominioValorInLine(admin.TabularInline):
    model = DominioValor

class DominioAdmin(admin.ModelAdmin):
    list_display = ('dominio_id', 'descripcion', 'activo',)
    list_filter = ('dominio_id',)
    search_fields = ['dominio_id',]
    sortable_field_name = "dominio_id"
    inlines = [DominioValorInLine,]

class AgenciaInLine(admin.TabularInline):
    model = Agencia
    form = forms.AgenciaForm
    extra = 3

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('corporacion', 'empresa_id', 'pais', 'activo',)
    list_filter = ('empresa_id',)
    search_fields = ['empresa_id',]
    sortable_field_name = "empresa_id"
    inlines = [AgenciaInLine,]

class AgenciaAdmin(admin.ModelAdmin):
    fields = ('empresa', 'descripcion', 'activo')
    list_display = ('empresa', 'descripcion', 'activo',)
    list_filter = ('descripcion',)
    search_fields = ['descripcion',]
    sortable_field_name = ('empresa', 'descripcion',)

class AgenciaAdmin(admin.ModelAdmin):
    exclude = ('agencia_id',)

admin.site.register(Dominio, DominioAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Agencia, AgenciaAdmin)
admin.site.register(Sistema)
admin.site.register(Subsistema)
admin.site.register(Modulo)
admin.site.register(Recurso)
admin.site.register(RecursoSistema)
admin.site.register(ColorIssue)
admin.site.register(Issue)
admin.site.register(IssueReferencia)
admin.site.register(IssueActividad)
admin.site.register(IssueEmpresa)
