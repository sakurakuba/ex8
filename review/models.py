from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Sum, F, Count

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = (
    (DEFAULT_CATEGORY, 'Other'),
    ('audio', 'Audio'),
    ('shoes', 'Shoes'),
    ('tv', 'TV'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Description')
    category = models.CharField(max_length=20, default=DEFAULT_CATEGORY, choices=CATEGORY_CHOICES,
                                verbose_name='Category')
    pr_img = models.ImageField(upload_to="pr_images", default="default.jpeg", null=True, blank=True, verbose_name="Product Image")

    def __str__(self):
        return f'{self.name} - {self.category}'

    def get_avg_score(self):
        avg_score = self.products.aggregate(avg_score=(Sum(F("score")) / Count(F("author__id"))))
        if avg_score['avg_score']:
            return avg_score['avg_score']
        return 0

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews', verbose_name='Author')
    product = models.ForeignKey("review.Product", on_delete=models.CASCADE, related_name="products",
                                verbose_name="Product")
    text = models.TextField(max_length=1000, verbose_name='Review')
    score = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Score')
    verified = models.BooleanField(default=False, verbose_name="Verified review")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    def __str__(self):
        return f'{self.author} - {self.score}, {self.text}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

