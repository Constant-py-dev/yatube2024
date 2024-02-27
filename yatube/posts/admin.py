from django.contrib import admin
from .models import Post, Group

admin.site.site_header = 'Админ панель'
admin.site.index_title = 'Администрирование Yatube'

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    list_editable = ('group',)
    empty_value_display = "-пусто-"

admin.site.register(Post, PostAdmin)
admin.site.register(Group)
