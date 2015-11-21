import random

from django.test import TestCase
from django.utils import timezone

from . import factories
from . import models


class ProductTestCase(TestCase):


    def setUp(self):
        roles = []
        for i in xrange(1, 10):
            role = factories.RoleFactory()
            print "Role: {}".format(
                role
            )
            role.save()
            roles.append(role)

        for i in xrange(1, 10):
            product = factories.ProductFactory()
            print "Product: {} - Sprint: {} {}".format(
                product,
                product.sprint_repeats_every,
                product.sprint_repeat_duration
            )
            product.save()
            sprints = []

            for i in xrange(1, random.randint(1, 10)):
                sprint = factories.SprintFactory(
                    product = product,
                    number = i
                )
                sprint.save()
                sprints.append(sprint)

                print "    Sprint: {}".format(
                    sprint.number
                )

            stories = []

            for i in xrange(1, 40):

                story = factories.StoryFactory(
                    role = roles[random.randint(0, len(roles) - 1)],
                    product = product
                )
                story.save()
                stories.append(story)

                print "Story: {}\n Size: {}\n Product: {}\n Sprint start: {}\n Sprint end: - {}".format(
                    story,
                    story.size,
                    story.product,
                    story.started_at_sprint,
                    story.completed_at_sprint,
                )

            for sprint in sprints:
                
                for i in xrange(1, random.randint(0, len(stories) - 1)):
                    
                    try:
                        story = stories[i]

                        if story.started_at_sprint is None:
                            # start the story
                            story.started_at_sprint = sprint
                        
                        if random.randint(1,2) == 1:
                            # story is potentially completed
                            story.completed_at_sprint = sprint
                            # popped off the list.
                            stories.pop(stories.index(story))

                        story.save()

                        print "Story ID: {}\n Size: {}\n Sprint start: {}\n Sprint end: {}".format(
                            story.id,
                            story.size,
                            story.started_at_sprint,
                            story.completed_at_sprint
                        )
                    except IndexError:
                        print i

                print "=== Sprint {} Velocity {} ===".format(
                    sprint.number,
                    sprint.velocity()
                ) 






    def test_say_yo(self):

        pass


    def tearDown(self):
        models.Story.objects.all().delete()
        models.Sprint.objects.all().delete()
        models.Product.objects.all().delete()
        models.Role.objects.all().delete()


