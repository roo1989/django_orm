from django.contrib import admin
from orm_tutorial.models import Restaurant, Sale, Rating

admin.site.register(Restaurant)
admin.site.register(Sale)
admin.site.register(Rating)