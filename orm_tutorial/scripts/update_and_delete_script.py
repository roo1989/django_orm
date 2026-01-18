from django.db import connection

from orm_tutorial.models import Restaurant


def run():
    last_restaurant = Restaurant.objects.last()
    update_restaurant_name_only_using_update_fields(restaurant=last_restaurant)
    print(connection.queries)
    print(last_restaurant.name)

def update_restaurant_name_using_save(restaurant: Restaurant) -> None:
    """
    This will update every single field instead of just the name.

    query:
        UPDATE orm_tutorial.restaurant SET name = 'New Restaurant name',
        website = '', 'date_opened': timezone.now(), latitude = '' ...;
    """
    print(restaurant.name)

    restaurant.name = 'New Restauant Name'
    restaurant.save()

def update_restaurant_name_only_using_update_fields(restaurant: Restaurant) -> None:
    """
    This will only update the name field in the restaurant table.
    UPDATE orm_tutorial.restaurant SET name = 'New Restaurant name';
    """
    restaurant.name = 'Another Restaurant Name'
    restaurant.save(update_fields=['name']) # Will only update the `name` field.
