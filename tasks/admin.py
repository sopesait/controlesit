from django.contrib import admin
from tasks.models import Dominio, DominioValor, Empresa, Agencia, Sistema, Subsistema, Modulo, Recurso, RecursoSistema, ColorIssue, Issue, IssueReferencia, IssueActividad, IssueEmpresa

class DominioAdmin(admin.ModelAdmin):
    list_display = ['dominio_id', 'dominio_desc', 'dominio_activo']
    search_fields = ['dominio_id']

admin.site.register(Dominio, DominioAdmin)
admin.site.register(DominioValor)
admin.site.register(Empresa)
admin.site.register(Agencia)
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
