from django.db import models
from django.contrib.sites.models import Site
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    category model
    """
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_friendly_name(self):
        """
        friendly name instead of id
        """
        return self.friendly_name
    
    def __str__(self):
        return self.friendly_name


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    first_name1 = models.CharField(max_length=40, blank=True, default=" ")
    last_name1 = models.CharField(max_length=40, blank=True, default=" ")

    def __str__(self):
        return f"{self.first_name} {self.last_name} , {self.first_name1} {self.last_name1}"


class Book(models.Model):

    QUARTER = (
        ("Earrach 2023", "Spring 2023"),
        ("Samhradh 2023", "Summer 2023"),
        ("Fómhar 2023", "Autumn 2023"),
        ("Geimhreadh 2023", "Winter 2023"),
    )

    AUDIENCE = (
        ("adult", "adult"),
        ("children", "children"),
    )

    LANGUAGE = (
        ("Irish", "Gaelige"),
        ("English", "English"),
    )

    GENRE = (
        ("poetry", "poetry"),
        ("fiction", "fiction"),
        ("non-fiction", "non-fiction"),
    )

    FORMAT = (
        ("hardback", "hardback"),
        ("paperback", "paperback"),
        ("chapbook", "chapbook"),
    )

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.CharField(
        choices=GENRE, default="fiction", max_length=20)
    quarter = models.CharField(choices=QUARTER, max_length=100)
    audience = models.CharField(
        choices=AUDIENCE, default="adult", max_length=10)
    language = models.CharField(
        choices=LANGUAGE, default="English", max_length=10)
    format = models.CharField(choices=FORMAT, default=None, max_length=20)
    sku = models.CharField(max_length=250, null=True, blank=True, unique=True)
    title = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    publication_year = models.PositiveSmallIntegerField(
        null=True, blank=False, default=2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    distributor = models.CharField(max_length=100, default="Unknown")
    in_stock = models.BooleanField(default=True)
    blurb = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        ordering = ['quarter']


class Featured_Product(models.Model):

    QUARTER = (
        ("Earrach 2023", "Spring 2023"),
        ("Samhradh 2023", "Summer 2023"),
        ("Fómhar 2023", "Autumn 2023"),
        ("Geimhreadh 2023", "Winter 2023"),
    )

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)    
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    quarter = models.CharField(choices=QUARTER, max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    manufacturer = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)
    featured_image = CloudinaryField('image', default='placeholder')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    advert_image1 = CloudinaryField('image', default='placeholder')
    image1_url = models.URLField(max_length=1024, null=True, blank=True)
    advert_image2 = CloudinaryField('image', default='placeholder')
    image2_url = models.URLField(max_length=1024, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True,
                              db_index=True)

    def __str__(self):
        return f"{self.name} by {self.manufacturer}"

    class Meta:
        verbose_name_plural = 'Featured Products'
        ordering = ['quarter']
