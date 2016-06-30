from django.forms import *
from suit.widgets import *
class ColorAdminForm(ModelForm):
	class Media:
		css ={
			"all": ('/static/color/css/pick-a-color-1.2.2.min.css',)
		}
		