from django.forms import ModelForm

from maustrep.models import Trap

class TrapForm(ModelForm):
    class Meta:
        model = Trap
        fields = ['descriptor','password']

    def save(self, commit=True):
        trap = super(TrapForm, self).save(commit=False)
        trap.set_password(self.cleaned_data["password"])
        if commit:
            trap.save()
        return trap