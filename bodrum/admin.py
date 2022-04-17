from django.contrib import admin
from .models import WriteUS , SpecialArea , Comment ,Subscribe , Parthners , Galeri
# Register your models here.


class WriteUsAdmin(admin.ModelAdmin):
    list_display = ['author']



class SpecialAdmin(admin.ModelAdmin):
    list_display = ['author']




class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']



class SubAdmin(admin.ModelAdmin):
    list_display = ['email']



class ParthnersAdmin(admin.ModelAdmin):
    list_display = ['name']



class GaleryAdmin(admin.ModelAdmin):
    list_display = ['info']


admin.site.register(WriteUS,WriteUsAdmin)
admin.site.register(SpecialArea,SpecialAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Subscribe,SubAdmin)
admin.site.register(Parthners,ParthnersAdmin)
admin.site.register(Galeri,GaleryAdmin)