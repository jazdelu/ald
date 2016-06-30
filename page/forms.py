from django.forms import ModelForm
from suit.widgets import AutosizedTextarea, NumberInput

class PageForm(ModelForm):
    class Meta:
        widgets = {
            'content': AutosizedTextarea,

            # You can also specify html attributes
            'content': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
        }

class HomepageLinkForm(ModelForm):
    class Meta:
        widgets = {
            'order': NumberInput,

            # Optionally you specify attrs too
            'order': NumberInput(attrs={'class': 'input-mini'})

        }