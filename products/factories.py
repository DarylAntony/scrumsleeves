import datetime

import factory
import random

from . import fakers
from . import models


class ProductFactory(factory.Factory):
    
    class Meta:
        model = models.Product
    

    name = factory.LazyAttribute(
        lambda o: fakers.words(2, common=False).title())

    first_sprint_starts_at = factory.LazyAttribute(
        lambda o: datetime.date.fromordinal(datetime.date.today().toordinal() - random.randint(0, 100))
    )

    sprint_repeats_every = factory.LazyAttribute(
        lambda o: random.randint(1, 3)
    )

    sprint_repeat_duration = factory.LazyAttribute(
        lambda o: models.DURATION_CHOICES[
            random.randint(
                0, len(models.DURATION_CHOICES) - 1
            )
        ]
    )


class SprintFactory(factory.Factory):

    class Meta:
        model = models.Sprint

    product = factory.SubFactory(ProductFactory)

    number = factory.LazyAttribute(
        lambda o: random.randint(1, 10)
    )


class RoleFactory(factory.Factory):

    class Meta:
        model = models.Role

    name = factory.LazyAttribute(
        lambda o: fakers.noun().title())


SIZES = (1, 2, 3, 5, 8, 13, 21, 34)

class StoryFactory(factory.Factory):

    class Meta:
        model = models.Story

    product = factory.SubFactory(ProductFactory)

    size = factory.LazyAttribute(
        lambda o: SIZES[
            random.randint(
                0, len(SIZES) - 1
            )
        ]
    )

    action = factory.LazyAttribute(
        lambda o: fakers.words(5, common=False))

    benefit = factory.LazyAttribute(
        lambda o: fakers.words(5, common=False))





