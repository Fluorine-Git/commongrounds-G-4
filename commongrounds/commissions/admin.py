from django.contrib import admin
from .models import Commission, CommissionType


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    readonly_fields = ("created_on", "updated_on")


class CommissionTypeAdmin(admin.ModelAdmin):
    model = CommissionType


admin.site.register(Commission, CommissionAdmin)
admin.site.register(CommissionType, CommissionTypeAdmin)
