from django.db import models

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


class Book(models.Model):
    quarter = models.CharField(choices=QUARTER, max_length=100)
    audience = models.CharField(
        choices=AUDIENCE, default="adult", max_length=10)
    language = models.CharField(
        choices=LANGUAGE, default="English", max_length=10)
    genre = models.CharField(
        choices=GENRE, default="fiction", max_length=20)
    format = models.CharField(choices=FORMAT, default=None, max_length=20)
    sku = models.CharField(max_length=250, null=True, blank=True)
    isbn = models.IntegerField(unique=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    distributor = models.CharField(max_length=100, default="Unknown")
    blurb = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ['quarter']
