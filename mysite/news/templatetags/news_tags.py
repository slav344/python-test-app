from django import template

from news.models import Category

# register = template.library


def get_categories():
    return Category.objects.all()
