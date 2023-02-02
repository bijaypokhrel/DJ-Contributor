from django.db import models


class Menu(models.Model):
    menu_text = models.CharField(max_length=255)
    menu_link = models.CharField(max_length=255)
