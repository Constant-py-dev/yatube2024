from django.contrib import admin

from .models import Post, Group, Comment

admin.site.site_header = 'Админ панель'
admin.site.index_title = 'Администрирование Yatube'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author', 'group')
    list_select_related = ['author', 'group']
    search_fields = ('text',)
    list_filter = ('pub_date',)
    # list_editable = ('group',)
    list_per_page = 20
    autocomplete_fields = ['author']
    empty_value_display = "-пусто-"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'text', 'created')
    search_fields = ('author',)
    list_filter = ('created',)
    readonly_fields = ('author', 'post', 'created')

    def has_add_permission(self, request):
        return False


admin.site.register(Group)
