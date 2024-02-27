from django.urls.converters import SlugConverter

class My_slug(SlugConverter):
    regex="[-a-zA-Z0-9_А-Яа-яЁё_]+"
