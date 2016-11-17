from django import forms
#from gen.core.operacao import soma

class Operacao(forms.Form):

	numero_um = forms.IntegerField(label='Primeiro',
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)
	numero_dois = forms.IntegerField(label= 'Segundo', 
		widget=forms.TextInput(
			attrs={"class":"form-control"
			}
			)
		)