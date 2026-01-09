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
    restaurant = Restaurant.objects.first()
    restaurant_first_index = Restaurant.objects.all()[0] # Will return query LIMIT 1.

    # Create a restaurant using Restaurant.objects.create()
    # Restaurant.objects.create(
    #     name='Pizza Shop',
    #     date_opened=timezone.now(),
    #     restaurant_type=Restaurant.TypeChoices.ITALIAN,
    #     latitude=50.2,
    #     longitude=50.5
    # )

    # print(restaurants)
    # print(restaurant)
    print(Restaurant.objects.count())
    print(connection.queries)




