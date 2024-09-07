from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=255,verbose_name='Category:')
    category_slug = models.CharField(unique=True,max_length=255,verbose_name='Slug:')
    
    class Meta:
        verbose_name = 'Kategoryasi'
        verbose_name_plural = 'Kategoryalar'

    def __str__(self):
        return self.category_name 

class Janr(models.Model):
    Janr_name = models.CharField(max_length=255,verbose_name='Janr:')
    Janr_slug = models.CharField(unique=True,max_length=255,verbose_name='Janr Slug:')

    class Meta:
        verbose_name = 'Janri'
        verbose_name_plural = 'Janrlar'

    def __str__(self):
        return self.Janr_name 

class Movies(models.Model):
    title = models.CharField(max_length=255,verbose_name='Kinonin ati:')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    janr = models.ForeignKey(Janr,on_delete=models.CASCADE)
    published_date = models.DateField(verbose_name='Kinonin shiqqan waqti')
    image = models.ImageField(upload_to='media/posters',verbose_name='Poster:')
    description = models.TextField(verbose_name='Kino haqqinda:')
    actors = models.TextField(verbose_name='Kino oynagan aktyorlar:')
    country = models.CharField(max_length=255,verbose_name='Kino tusirilgen mamleket:')
    movies = models.FileField(upload_to='media/movies',verbose_name='Kinonin ozi:')

    class Meta:
        verbose_name = 'Kinosi'
        verbose_name_plural = 'Kinolar'

    def __str__(self):
        return self.title

class Comments(models.Model):
    text = models.TextField(verbose_name='Komment text:')
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True,verbose_name='Komment shiqqan waqti')

    class Meta:
        verbose_name = 'Komment'
        verbose_name_plural = 'Kommentlar'

    def __str__(self):
        return self.text
