import re
from datetime import date

from django.forms import *

from viewer.models import Genre, Movie


class DateInput(DateInput):
    input_type = 'date'


# Clasa pentru a crea un formular generic
# Poate fi folosit in orice scop
# class MovieForm(Form):
#     # max_length va fi validat in mod automat
#     title = CharField(max_length=128)
#
#     # Va afisa un ChoiceField unde optiunile sunt definite prin parametrul
#     # queryset
#     genre = ModelChoiceField(queryset=Genre.objects)
#
#     # min_value si max_value vor fi validate in mod automat
#     rating = IntegerField(min_value=1, max_value=10)
#
#     released = DateField(widget=DateInput)
#
#     # Parametrul widget indica elementul de HTML care vrem sa fie
#     # afisat pe pagina
#     description = CharField(widget=Textarea)

# Validation/Cleanup forms
# Validarea unui field poate fi OK, sau NU ok
# in cazul in care un field nu este validat, vom returna o eroare
# daca toate field-urile sunt validate, mergem mai departe la curatarea de date

# A) cream o functie de validare pe care o dam parametru in field
# B) sa declaram o clasa noua pornind de la o clasa Field, si suprascriem functiile clean() si validate()
# C) sa cream in interirul clasei de formular functii de clean(), clean_numefield()

def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Trebuie litera mare!')


class PastMonthField(DateField):
    # Functia validate va fi apelata automat la procesarea acestui field
    def validate(self, value):
        # Apelam functia de baza din clasa DateField
        super().validate(value)

        # Conditiile noastre de validare
        if value >= date.today():
            raise ValidationError('Data trebuie sa fie din trecut!')

    # Exemplu de functie clean() pentru a modifica datele din formular
    # inainte de a le salva
    def clean(self, value):
        # Luam datele dupa ce au fost procesate in functia de baza
        result = super().clean(value)

        # Returnam o valoare noua
        return date(year=result.year, month=result.month, day=1)


class MovieForm(ModelForm):
    class Meta:
        model = Movie

        # Includem toate field-urile din model
        fields = '__all__'

        # Daca vrem sa includem doar anumite fields din model
        # fields = ['title', 'genre']

    # Suprascriem functia __init__() pentru a modifica field-urile
    # atunci cand se genereaza formularul
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # visible_fields() va returna toate field-urile vizible din formular
        # visible.field este obiectul de Python pentru acel field
        # visible.field.widget este HTML generat pentru el
        # visible.field.widget.attrs sunt atributele de HTML din acel field (ex: id, class, type, name, href, ...)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    # Toate functiile din parametrul validators vor fi apelate cand se proceseaza formularul
    title = CharField(max_length=128, validators=[capitalized_validator])
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField(widget=DateInput)
    description = CharField(widget=Textarea)

    # In interirul clasei MovieForm sa genereaza automat o functie de clean_numefield
    # pentru fiecare field din formular
    def clean_description(self):
        # Capitalizam prima litera din fiecare propozitie
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    # Functia clean() este un loc bun pentru validari/clean ce tin de tot formularul
    def clean(self):
        # result este un dictionar cu toate datele din formular
        result = super().clean()

        # In cazul in care un field nu este validat el nu va mai fi pus in dictionarul result
        # Daca incercam sa-l accesam cu result['nume_field'] vom primi un KeyError
        # Recomandat sa folosim functia result.get('nume_field') care va return None
        # daca nu exista acea cheie

        if result.get('genre').name == 'Comedy' and result.get('rating') > 5:
            # Functia add_error('numefield', 'mesajeroare') va adauga o eroare
            # pe cate un field din formular
            self.add_error('genre', 'Filmul este comedie.')
            self.add_error('rating', 'Ratingul este prea mare.')

            raise ValidationError('Nu ne plac comediile.')

        return result