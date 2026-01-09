from orm_tutorial.models import Restaurant


def run():
    # Get all restaurants
    print(Restaurant.objects.all())

    # Get the first restaurant
    print(Restaurant.objects.first())

    # Get the first restaurant via indexing
    print(Restaurant.objects.all()[0])

    # Get the last restaurant
    print(Restaurant.objects.last())

    # Fetch the number of restaurants in the table.
    print(Restaurant.objects.count())