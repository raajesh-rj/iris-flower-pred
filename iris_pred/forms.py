from django import forms

class FlowerForm(forms.Form):
    sepal_length = forms.FloatField(label='sepal_length', required=True)
    sepal_width = forms.FloatField(label='sepal_width', required=True)
    petal_length = forms.FloatField(label='petal_length', required=True)
    petal_width = forms.FloatField(label='petal_width', required=True)