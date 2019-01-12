from django import forms


class Users(forms.Form):
    user_name = forms.CharField(max_length=100)
    user_email = forms.EmailField(max_length=255)
    # user_phone = forms.CharField(max_length=11)
    user_password = forms.CharField(max_length=16)
    user_password1 = forms.CharField(max_length=16)


class loginform(forms.Form):
    user_email = forms.CharField(max_length=255)
    user_password = forms.CharField(max_length=16)


# class caseform(forms.Form):
#     type = forms.CharField(max_length=100)
#     max_len = forms.IntegerField(max_length=50)
#     min_len = forms.IntegerField(max_length=50)



