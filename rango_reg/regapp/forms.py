from django import forms
from regapp.models import User, UserProfile, GitHub

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=8, help_text="Please use your GUID, e.g., 2029999z")
    #email = forms.CharField(widget=forms.HiddenInput(), initial="")
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

#class UserProfileForm(forms.ModelForm):
#    website=forms.URLField(max_length=200, help_text="Please enter your Github repository here.")
#    class Meta:
#        model = UserProfile
#        fields = ('website',)

class GithubForm(forms.ModelForm):
    url = forms.URLField(max_length=200, help_text="Please enter the URL of your GitHub rango repository.")

    class Meta:
        model = GitHub
        fields = ('url',)
        # exclude = ('userid',)

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     url = cleaned_data.get('url')
    #     if url and not url.startswith('https://'):
    #         url = 'http://' + url
    #         cleaned_data['url'] = url
    #         return cleaned_data
