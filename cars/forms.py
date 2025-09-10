from django import forms
from cars.models import Car
  
class CarModelForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = '__all__'

  def clean_price(self):
    price = self.cleaned_data.get('price')
    if price < 20000:
      raise forms.ValidationError('Não é permitido o cadastro de carros menores de R$20.000')
    return price
  
  def clean_factory_year(self):
    factory_year = self.cleaned_data.get('factory_year')
    if factory_year < 1975:
      raise forms.ValidationError('Não é permitido o cadastro de carros abaixo de 1975')
    return factory_year
  
  def clean_model_year(self):
    model_year = self.cleaned_data.get('model_year')
    if model_year < 1975:
      raise forms.ValidationError('Não é permitido o cadastro de carros abaixo de 1975')
    return model_year