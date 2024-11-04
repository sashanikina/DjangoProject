from django.forms import ModelForm

from .models import Lines

class LineForm(ModelForm):
    class Meta:
        model = Lines
        fields=('name', )