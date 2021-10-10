from django.contrib import admin
from .models import PSAttribute, PSConfig

class PSConfigAdmin(admin.ModelAdmin):
    pass
class PSAttributeAdmin(admin.ModelAdmin):
    pass
admin.site.register(PSConfig, PSConfigAdmin)
admin.site.register(PSAttribute, PSAttributeAdmin)