from django.db import models

quarter = (
    ("Spring", "Earrach"),
    ("Summer", "Samhradh"),
    ("Autumn", "Fómhar"),
    ("Winter", "Geimhreadh"),
)


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Book(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    length_pgs = models.IntegerField()
    publisher = models.CharField(max_length=250)
    year = models.IntegerField
    isbn = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    blurb = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name