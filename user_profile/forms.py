from django import forms
from accounts.models import Coustomer

class EditForm(forms.ModelForm):

    class Meta: 
        model = Coustomer
        fields = ['username','email','first_name','last_name','mobile_num', 'location','photo']
    def __init__(self,*args,**kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['email'].disabled = True