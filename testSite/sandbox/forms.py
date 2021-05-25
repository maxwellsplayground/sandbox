from django import forms
from .models import *



class CoffeeShopForm(forms.Form):
    name = forms.CharField(max_length=20)

class BarristaInfo(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)

class CoffeeOptionForm(forms.Form):
    brand_name = forms.CharField(max_length=25)
    cafienated = forms.BooleanField()

class UploadForm(forms.ModelForm):
    
    class Meta:
        model = CSVFile
        fields = ('new_file',)
   

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        interests = ProfileInterest.objects.filter(
            profile=self.instance
        )
        for i in range(len(interests) + 1):
            field_name = 'interest_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False)
            try:
                self.initial[field_name] = interests[i].interest
            except IndexError:
                self.initial[field_name] = ""
        # create an extra blank field
        field_name = 'interest_%s' % (i + 1,)
        self.fields[field_name] = forms.CharField(required=False)

    def clean(self):
        interests = set()
        i = 0
        field_name = 'interest_%s' % (i,)
        while self.cleaned_data.get(field_name):
           interest = self.cleaned_data[field_name]
           if interest in interests:
               self.add_error(field_name, 'Duplicate')
           else:
               interests.add(interest)
           i += 1
           field_name = 'interest_%s' % (i,)
        self.cleaned_data['interests'] = interests
    def get_interest_fields(self):
        for field_name in self.fields:
            if field_name.startswith('interest_'):
                yield self[field_name]

    def save(self):
        profile = self.instance
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']

        profile.interest_set.all().delete()
        for interest in self.cleaned_data['interests']:
           ProfileInterest.objects.create(
               profile=profile,
               interest=interest,
           )
    
