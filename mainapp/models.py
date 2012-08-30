from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)



class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.name


class syslog_AH_505_ICP_WJ_SEV3(models.Model):
    type = models.CharField(max_length=10)
    item1 = models.CharField(max_length=20)
    item2 = models.CharField(max_length=20)
    message = models.CharField(max_length=200)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)

    def __unicode__(self):
         return u'%s %s' % (self.type,self.item1)
