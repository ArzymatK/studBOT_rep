from django.db import models

class Category(models.Model):
    title_ru = models.CharField(max_length=120)
    title_kg = models.CharField(max_length=120)
    title_tu = models.CharField(max_length=120)
    title_en = models.CharField(max_length=120)
    image = models.ImageField(upload_to='categories/')
    link = models.CharField(max_length=120)

    is_about = models.BooleanField(default=False)
    is_constructr = models.BooleanField(default=False)
    is_collagen = models.BooleanField(default=False)
    is_coffe = models.BooleanField(default=False)
    is_tea = models.BooleanField(default=False)
    is_drink = models.BooleanField(default=False)
    is_bar = models.BooleanField(default=False)
    is_smuzi = models.BooleanField(default=False)
    is_wine = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    number = models.IntegerField(default=0, null=True, blank=True)

    def str(self) -> str:
        return self.title_ru

    class Meta:
        db_table = 'categories'


class SubCategory(models.Model):
    title_ru = models.CharField(max_length=120)
    title_kg = models.CharField(max_length=120)
    title_tu = models.CharField(max_length=120)
    title_en = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    custom_orange_ru = models.CharField(max_length=120, blank=True, null=True)
    custom_orange_kg = models.CharField(max_length=120, blank=True, null=True)
    custom_orange_tu = models.CharField(max_length=120, blank=True, null=True)
    custom_orange_en = models.CharField(max_length=120, blank=True, null=True)
    custom_black_ru = models.CharField(max_length=120, blank=True, null=True)
    custom_black_kg = models.CharField(max_length=120, blank=True, null=True)
    custom_black_tu = models.CharField(max_length=120, blank=True, null=True)
    custom_black_en = models.CharField(max_length=120, blank=True, null=True)
    main_title_ru = models.CharField(max_length=120, blank=True, null=True)
    main_title_kg = models.CharField(max_length=120, blank=True, null=True)
    main_title_tu = models.CharField(max_length=120, blank=True, null=True)
    main_title_en = models.CharField(max_length=120, blank=True, null=True)

    def str(self) -> str:
        return f"{self.title_ru} -> {self.category.title_ru}"

    class Meta:
        db_table = 'subcategories'


class SVG(models.Model):
    svg = models.FileField(upload_to='svgs/')

    def str(self) -> str:
        return str(self.svg)

    class Meta:
        db_table = 'svgs'


class Dish(models.Model):
    title_ru = models.CharField(max_length=120)
    title_kg = models.CharField(max_length=120)
    title_tu = models.CharField(max_length=120)
    title_en = models.CharField(max_length=120)
    image = models.ImageField(upload_to='dishes/')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    svgs = models.ManyToManyField(SVG, blank=True)
    text_ru = models.TextField(null=True, blank=True)
    text_kg = models.TextField(null=True, blank=True)
    text_tu = models.TextField(null=True, blank=True)
    text_en = models.TextField(null=True, blank=True)

    advice_ru = models.TextField(null=True, blank=True)
    advice_kg = models.TextField(null=True, blank=True)
    advice_tu = models.TextField(null=True, blank=True)
    advice_en = models.TextField(null=True, blank=True)

    price = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    weight = models.IntegerField(default=0, null=True, blank=True)

    def str(self) -> str:
        return self.title_ru

    class Meta:
        db_table = 'dishes'