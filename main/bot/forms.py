from django import forms
from .models import User
from .models import Condition
from .models import Projects
from .models import Organisation


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'project', 'role', 'approved', 'develop', 'agile', 'organisation')
        widgets = {
            'telegram_id': forms.TextInput,
            'first_name': forms.TextInput,
            'last_name': forms.TextInput,
            'email': forms.TextInput,
        }


class ConditionForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ('user', 'registration', 'on_validate')


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('project_name', 'project_id')
        widgets = {'project_name': forms.TextInput,
                   'project_id': forms.TextInput
                   }


class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ('organisation_name',)
        widgets = {'organisation_name': forms.TextInput
                   }
