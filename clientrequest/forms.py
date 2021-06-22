from django import forms
from .models import ClientRequest, ModelAuto, BrandAuto


class ClientRequestForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        fields = '__all__'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['modelauto'].queryset = ModelAuto.objects.none()

    def save(self, commit=True):
        super().save(self,commit)
        brand = int(self.fields['brandauto'].value)
        brand = BrandAuto.objects.get (id= brand)
        model = int(self.fields['modelauto'].value)
        model = ModelAuto.objects.get (id= model)
        brand_models = brand.modelauto_set.all()
        if model not in brand_models:
            return TypeError