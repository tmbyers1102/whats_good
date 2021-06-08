from django.contrib import admin
from . models import Tag, Checkin, Author

admin.site.register(Tag)
admin.site.register(Checkin)
admin.site.register(Author)