from django.forms import *

from viewer.models import Genre


class DateInput(DateInput):
    input_type = 'date'


# Clasa pentru a crea un formular generic
# Poate fi folosit in orice scop
class MovieForm(Form):
    # max_length va fi validat in mod automat
    title = CharField(max_length=128)

    # Va afisa un ChoiceField unde optiunile sunt definite prin parametrul
    # queryset
    genre = ModelChoiceField(queryset=Genre.objects)

    # min_value si max_value vor fi validate in mod automat
    rating = IntegerField(min_value=1, max_value=10)

    released = DateField(widget=DateInput)

    # Parametrul widget indica elementul de HTML care vrem sa fie
    # afisat pe pagina
    description = CharField(widget=Textarea)