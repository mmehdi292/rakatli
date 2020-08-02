from django.db import models

# Create your models here.
class Autor(models.Model):
    full_name =  models.CharField(max_length=200,null=False)
    profil_img = models.ImageField(default='logo.png',null=True, blank=True)
    username =  models.CharField(max_length=200,null=False)
    birthday = models.DateTimeField(null=True)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=32, null=False)

    def __str__ (self):
        return self.full_name
    


class Tag(models.Model):
    name = models.CharField(max_length=200,null=False)

    def __str__ (self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=200,null=False)
    url = models.CharField(max_length=50,null=False)
    image = models.ImageField(default='logo.png',null=True, blank=True)
    autor = models.ForeignKey(Autor, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    views = models.PositiveSmallIntegerField(default = 0)
    like = models.PositiveSmallIntegerField(default = 0)
    deslike = models.PositiveSmallIntegerField(default = 0)
    tags = models.ManyToManyField(Tag)


class Khatira(models.Model):
    title = models.CharField(max_length=200,null=False)
    image = models.ImageField(default='logo.png',null=True, blank=True)
    autor = models.ForeignKey(Autor, null=True, on_delete=models.SET_NULL)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    views = models.PositiveSmallIntegerField(default = 0)
    like = models.PositiveSmallIntegerField(default = 0)
    deslike = models.PositiveSmallIntegerField(default = 0)
    tags = models.ManyToManyField(Tag)

    def __str__ (self):
        return self.title

class Sound(models.Model):
    title = models.CharField(max_length=200,null=False)
    url = models.CharField(max_length=1000,null=False)
    image = models.ImageField(default='logo.png', null=True, blank=True)
    autor = models.ForeignKey(Autor, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    views = models.PositiveSmallIntegerField(default = 0)
    like = models.PositiveSmallIntegerField(default = 0)
    deslike = models.PositiveSmallIntegerField(default = 0)
    tags = models.ManyToManyField(Tag)

    def __str__ (self):
        return self.title


class Mail(models.Model):
    full_name = models.CharField(max_length=200,null=False)
    email_sender = models.EmailField(null=False)
    subject = models.CharField(max_length=200,null=False)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Sidebar(models.Model):
    title = models.CharField(max_length=200,null=True)
    HTML = models.TextField()
    
    def __str__(self):
        return self.title