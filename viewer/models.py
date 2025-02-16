from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, IntegerField, DateField, TextField, DateTimeField


# Create your models here.
class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(Model):
    # CharField este folosit pentru campuri text cu lugime limitata
    title = CharField(max_length=128)

    # ForeignKey face legatura cu alt model
    # on_delete -> ce sa intampla cand se sterge modelul de care ne legam
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)

    rating = IntegerField()

    # DateField folosit pentru a stoca o data
    released = DateField()

    description = TextField()

    # auto_now_add inseamna ca acest field sa va completa automat
    # cand este adaugat un obiect
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Filmul: {self.title} - {self.genre.name}'