from django.contrib import admin
from .models import Post,Post_colum

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','tag_list','author','create','update','status')
    list_filter = ('tags','create','status')
    ordering = ('-create',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u",".join(o.name for o in obj.tags.all())

@admin.register(Post_colum)
class Post_columAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','create')
    list_filter = ('create',)
    ordering = ('-create',)





# Register your models here.
