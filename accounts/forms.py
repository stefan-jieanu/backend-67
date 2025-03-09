from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # field-ul password este inclus automat
        fields = ['username', 'first_name']

    biography = CharField(
        label='Tell us about yourself',
        min_length=10,
        widget=Textarea
    )

    # Ne asigura ca toate obiectele sunt salvate corect
    # Daca salvam un User si apar probleme la Profile,
    # it will 'roll-back changes', 'va da timpul inapoi' la starea initiala,
    # adica nu o sa se salveze nimic
    @atomic
    def save(self, commit=True):
        result = super().save(commit)

        biography = self.cleaned_data['biography']

        profile = Profile(user=result, biography=biography)

        if commit:
            profile.save()

        return result