from django.contrib import admin
from .models import  Comment ,Subscribe , Parthners , Galeri,Slider,About , Cheff ,Category , Product ,Images ,SubCategory , History
# Register your models here.

class Gallery(admin.TabularInline):
    model = Images

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}

class subCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','category','available']
    list_editable = ['available']
    prepopulated_fields = {'slug':('name',)}
    inlines = (Gallery,)


class SliderAdmin(admin.ModelAdmin):
    list_display = ['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']



class SubAdmin(admin.ModelAdmin):
    list_display = ['email']



class ParthnersAdmin(admin.ModelAdmin):
    list_display = ['name']



class GaleryAdmin(admin.ModelAdmin):
    list_display = ['info']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['about']



class ChefAdmin(admin.ModelAdmin):
    list_display = ['name']


class HistoryAdmin(admin.ModelAdmin):
    list_display = ['about']

admin.site.register(History,HistoryAdmin)

admin.site.register(Comment,CommentAdmin)
admin.site.register(Subscribe,SubAdmin)
admin.site.register(Parthners,ParthnersAdmin)
admin.site.register(Galeri,GaleryAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Cheff,ChefAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,subCategoryAdmin)
admin.site.register(Product,ProductAdmin)

admin.site.site_header = "Bodrum Mutfak"

admin.site.index_title = "Developer - İhsan Gürol Demirtaş"

admin.site.site_title = "İGD"