from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    image = models.ImageField(verbose_name='Image', upload_to='Gallery/category_image/', null=True, blank=True)
    slug = models.SlugField(verbose_name='URL', default='Gallery-category-', unique=True, db_index=True)
    active = models.BooleanField(verbose_name="Active", default=True)
    created = models.DateField(verbose_name='Public date', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Category')
    name = models.CharField(max_length=100, verbose_name='Sub Category')
    image = models.ImageField(verbose_name='Image', upload_to='Gallery/subcategory_image/')
    active = models.BooleanField(verbose_name='Active', default=True)
    slug = models.SlugField(verbose_name='URL', default='Gallery-subcategory-', unique=True, db_index=True)
    created = models.DateField(verbose_name='Public date', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
        ordering = ['id']

    def __str__(self):
        return self.name


class Images(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    subcategory = ChainedForeignKey(SubCategory,
                                    chained_field='category',
                                    chained_model_field='category',
                                    show_all=False,
                                    auto_choose=True,
                                    sort=True,
                                    verbose_name='SubCategory',)
    name = models.CharField(max_length=100, verbose_name='name')
    slug = models.SlugField(verbose_name='URL', default='product-', unique=True, db_index=True)
    description = models.TextField(verbose_name='description')
    image = models.ImageField(verbose_name='Image', upload_to='Gallery/images/')
    article = models.IntegerField(verbose_name='Article', unique=True, blank=True, null=True)
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)
    updated = models.DateField(verbose_name='Date update', auto_now=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['id']

    def __str__(self):
        return '{name} {sub_category}'.format(name=self.name, sub_category=self.subcategory)


class ImagesInline(models.Model):
    inline_images = models.ImageField(verbose_name='Image', upload_to='Gallery/inline_images/')
    image = models.ForeignKey(Images, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
