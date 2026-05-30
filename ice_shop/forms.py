from django import forms

from .models import IceCream


class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = '__all__'
    # title = forms.CharField()
    # description = forms.CharField(widget=forms.Textarea)
    # price = forms.IntegerField()
    # image = forms.ImageField()
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Название должно быть больше 3 символов.")
        return title