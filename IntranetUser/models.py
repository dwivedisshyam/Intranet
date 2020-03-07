from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class Menu(models.Model):
    text = models.CharField(max_length=20, blank=False)
    isDropdown = models.BooleanField(default=False)
    url = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.text


class SubMenu(models.Model):
    menuId = models.ForeignKey(Menu, on_delete=models.CASCADE)
    text = models.CharField(max_length=20, blank=False)
    url = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.text


class Category(models.Model):
    text = models.CharField(max_length=40, blank=False)
    menuId = models.ForeignKey(
        Menu, on_delete=models.CASCADE, blank=True, null=True)
    subMenuId = models.ForeignKey(
        SubMenu, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text


class SubCategory(models.Model):
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.CharField(max_length=40, blank=False)
    url = models.CharField(max_length=40, blank=True)
    content = RichTextUploadingField(blank=False)

    def __str__(self):
        return self.text
