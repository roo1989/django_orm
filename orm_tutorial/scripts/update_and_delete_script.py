from orm_tutorial.models import Restaurant


def run():
    restaurant = Restaurant.objects.first()
    update_restaurant_name(restaurant)
    print(restaurant.name)

def update_restaurant_name(restaurant: Restaurant) -> None:
    print(restaurant.name)

    restaurant.name = 'New Restauant Name'
    restaurant.save()
