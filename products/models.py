from django.db import models

DURATION_CHOICES = (
    # ('day', 'Days'),
    # ('business-day', 'Business Days'),
    ('week', 'Weeks'),
    ('month', 'Months'),
)

class Product(models.Model):
    """
    The Product your building.
    """

    name = models.CharField(
        max_length=255)

    first_sprint_starts_at = models.DateField()

    sprint_repeats_every = models.IntegerField(
        default=2)

    sprint_repeat_duration = models.CharField(
        choices=DURATION_CHOICES,
        default='week',
        max_length=64
    )

    def __unicode__(self):
        return self.name


class Sprint(models.Model):
    """
    A Product Sprint
    """

    product = models.ForeignKey('Product')

    number = models.IntegerField()

    class Meta:
        unique_together = (
            'product',
            'number'
        )

    def __unicode__(self):
        return "{}".format(self.number)

    def velocity(self):
        # import ipdb; ipdb.set_trace()
        return sum(
            self.stories_completed_at_sprint.all().values_list('size', flat=True)
        )

class Role(models.Model):
    """
    The (reuseable) Role
    """

    name = models.CharField(
        max_length=255)

    def __unicode__(self):
        return self.name


class Story(models.Model):
    """
    As a <role>
    I want <action>
    So that <benefit>

    TODO support other formats: https://en.wikipedia.org/wiki/User_story#Format
    """

    product = models.ForeignKey('Product')

    role = models.ForeignKey('Role')

    action = models.TextField()

    benefit = models.TextField()

    size = models.IntegerField()

    started_at_sprint = models.ForeignKey(
        'Sprint',
        related_name='started_at_sprint',
        null=True)

    completed_at_sprint = models.ForeignKey(
        'Sprint',
        related_name='stories_completed_at_sprint',
        null=True)

    def __unicode__(self):
        return 'AS A {} I WANT {} SO THAT {}'.format(
            self.role,
            self.action,
            self.benefit
        )

    # TODO validate sprint numbers are sequential or same.

