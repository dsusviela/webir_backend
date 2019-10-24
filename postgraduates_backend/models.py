# uncomment this code if you prefer a db approach for storing the data.
# the spiders code should be changed to actually put data in the db

#from django.db import models

# class Career(models.Model):
#     INDUSTRIAL = 'IN'
#     INVESTIGACION = 'IV'
#     COMPUTACION = 'CN'
#     CAREER_AREAS = ((INDUSTRIAL, 'Industrial'), (INVESTIGACION, 'Investigación'), (COMPUTACION, 'Computación'))
#     name = models.CharField('Career Name', max_length=120)
#     description = models.TextField(blank=True)
#     url = models.CharField('Career Site', max_length=200)
#     image_url = models.CharField('Career Image url', max_length=200)
#     university = models.CharField('Career university', max_length=50)
#     area = models.CharField('Event Date', choices=CAREER_AREAS, default=COMPUTACION, max_length=2)