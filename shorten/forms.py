from django import forms


class URLForm(forms.Form):
    MainURL = forms.URLField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Example: https://github.com/kistolbov'})
    )
    CustomURL = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Example: cutiepie'}), required=False
    )