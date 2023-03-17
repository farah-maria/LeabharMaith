from django.db import models

QUARTER = (
    ("Earrach", "spring"),
    ("Samhradh", "summer"),
    ("Fómhar", "autumn"),
    ("Geimhreadh", "winter"),
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


class Book(models.Model):
    quarter = models.CharField(choices=QUARTER, max_length=10)
    audience = models.CharField(
        choices=AUDIENCE, default="adult", max_length=10)
    language = models.CharField(
        choices=LANGUAGE, default="English", max_length=10)
    genre = models.CharField(
        choices=GENRE, default="fiction", max_length=20)
    sku = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    length = models.IntegerField()
    publisher = models.CharField(max_length=100)
    year = models.IntegerField
    isbn = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    distributor = models.CharField(max_length=100)
    blurb = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ['quarter']
