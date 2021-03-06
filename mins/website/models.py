from django.db import models
from faker import  Factory
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    content = models.TextField(null=True, blank=True)
    url_image = models.URLField(null=True, blank=True)
    cover = models.FileField(upload_to='cover_image', null=True)
    editors_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile')
    profile_image = models.FileField(upload_to='profile_image')

class Ticket(models.Model):
    voter = models.ForeignKey(to=UserProfile, related_name='voted_tickets')
    video = models.ForeignKey(to=Video, related_name='tickets')
    VOTE_CHOICES = {
        ('like', 'like'),
        ('dislike', 'dislike'),
        ('normal', 'normal'),
    }
    choice = models.CharField(choices=VOTE_CHOICES, max_length=10)
    def __str__(self):
        return str(self.id)

# f = open('/Users/Hou/Desktop/web_url.txt','r')
# for url in f.readlines():
#     v = Video(
#         title=fake.text(max_nb_chars=90),
#         content=fake.text(max_nb_chars=3000),
#         url_image=url,
#         editors_choice=fake.pybool()
#     )
#     v.save()