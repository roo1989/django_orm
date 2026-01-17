from django.contrib.auth.models import User

from orm_tutorial.models import Restaurant, Rating


def run():
    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    rating = Rating.objects.create(user=user, restaurant=restaurant, rating=9)

    rating.full_clean()
    rating.save()
