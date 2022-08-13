from tabnanny import verbose
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Categoriy(models.Model):
    categoriy = models.CharField(max_length=20, verbose_name= 'Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.categoriy

class Name_testing(models.Model):
    categoriy = models.ForeignKey(Categoriy, on_delete= models.CASCADE)
    name_test = models.CharField(max_length=50, verbose_name= 'Название теста')
    
    class Meta:
        verbose_name = 'Название теста'
        verbose_name_plural = 'название тестов'
    def __str__(self):
        return self.name_test


