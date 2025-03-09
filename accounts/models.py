from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, OneToOneField, CASCADE, TextField
from django.forms import CharField


# Create your models here.
class Profile(Model):
    # OneToOneField inseamna o asociere stricta de 1:1 intre User si Profile
    # on_delete=CASCADE inseamna ca atunci cand se sterge un User
    # se va sterge automat si Profile-ul asociat lui
    user = OneToOneField(User, on_delete=CASCADE)

    biography = TextField()

    def __str__(self):
        return f'Profilul lui {self.user.username}'