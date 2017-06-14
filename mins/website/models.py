from django.db import models
from faker import  Factory

# Create your models here.
class Video(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    content = models.TextField(null=True, blank=True)
    url_image = models.URLField(null=True, blank=True)
    cover = models.FileField(upload_to='cover_image', null=True)
    editors_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# f = open('/Users/Hou/Desktop/web_url.txt','r')
# for url in f.readlines():
#     v = Video(
#         title=fake.text(max_nb_chars=90),
#         content=fake.text(max_nb_chars=3000),
#         url_image=url,
#         editors_choice=fake.pybool()
#     )
#     v.save()