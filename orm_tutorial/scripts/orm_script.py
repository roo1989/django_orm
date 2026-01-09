from django.db import connection
from django.utils import timezone

from orm_tutorial.models import Restaurant


def run():
    # restaurant = Restaurant()
    # restaurant.name = 'My Italian Restaurant'
    # restaurant.latitude = 50.2
    # restaurant.longitude = 50.2
    # restaurant.date_opened = timezone.now()
    # restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    #
    # restaurant.save()

    restaurants = Restaurant.objects.all()
    print(restaurants)

    print(connection.queries)



