from pprint import pprint

from django.contrib.auth.models import User
from django.db import connection

from orm_tutorial.models import Restaurant, Rating


def run():
    print(Rating.objects.all())

    # Filter queryset based off ratings.
    print(Rating.objects.filter(rating=3))

    # Use double underscore helper to get all ratings greater than or equal 3.
    print(Rating.objects.filter(rating__gte=3))

    # Same as above, less than or equal.
    print(Rating.objects.filter(rating__lte=3))

    # Filter by NOT value.
    print(Rating.objects.exclude(rating__lte=3))

    pprint(connection.queries)