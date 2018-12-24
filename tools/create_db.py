import os
import sys
import random

BASE_DIR = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

import factory

from tags.models import Tag
from categories.models import Category
from posts.models import Post
from django.contrib.auth.models import User


class TagFactory(factory.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Sequence(lambda n: 'tag%s' % n)


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category
    
    name = factory.Faker('sentence')
    parent_category = factory.SubFactory("tools.create_db.CategoryFactory")
 

class PostFactory(factory.DjangoModelFactory):
    class Meta:
        model = Post
    
    title = factory.Faker('sentence')
    content = factory.Faker('text')

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for tag in extracted:
                self.tags.add(tag)


if __name__ == "__main__":
    user = User.objects.create_user(username='fish',
                                 email='mail@mail.com',
                                 password='admin123')
    print('users created...')

    TagFactory.create_batch(10)
    print('tags created...')

    c = CategoryFactory(parent_category__parent_category__parent_category__parent_category=None)
    # c.create_batch(3)
    print('category created...')

    user = list(User.objects.all())[0]

    tags = list(Tag.objects.all())
    categories = list(Category.objects.all())

    for i in range(20):
        tag_sample = random.sample(tags, 2)
        category = random.choice(categories)
        PostFactory(author=user, tags=tag_sample, category=category)

    print('post done...!')
