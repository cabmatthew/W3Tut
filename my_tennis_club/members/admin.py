from django.contrib import admin
from .models import Member, ShoeBrand

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date", "phone")

class ShoeBrandAdmin(admin.ModelAdmin):
    list_display = ("modelname", "brand")

admin.site.register(ShoeBrand, ShoeBrandAdmin)
admin.site.register(Member, MemberAdmin)
