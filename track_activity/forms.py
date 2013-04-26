from django.forms import ModelForm
from track_activity.models import Activity
from django import forms

class ActivityForm(ModelForm):
    class Meta:
        model = Activity


    def save(self,request):

        activity = Activity()
        activity.name = self.cleaned_data['name'].strip()
        activity.has_end_time = self.cleaned_data['has_end_time']
        activity.user = request.user
        activity.save()
        
    def clean(self):
        if 'name' in self.cleaned_data and len(self.cleaned_data['name'].strip()) == 0:
            raise forms.ValidationError("Sorry, name cannot be empty.")

        return self.cleaned_data

  
    
