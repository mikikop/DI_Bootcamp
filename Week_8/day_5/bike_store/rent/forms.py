from django import forms

# def check_old(age):
#     if age > 65:
#         raise forms.ValidationError(f'You are too old to be an astronaut')
        
# def check_young(age):
#     if age < 30:
#         raise forms.ValidationError(f'You are not old enough to be an astronaut')

class CustomerForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    phone_number = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()

    # age = forms.IntegerField(
    #     validators=[check_old, check_young]
    # )
    # rank = forms.CharField(
    #     required=True,
    #     label="Type your Rank", 
    #     help_text='You better be in the military.', 
    #     error_messages={'required': 'Please enter a valid Rank'}
    # )
    

class VehicleForm(forms.Form):
    vehicle_type = forms.CharField(required=True)
    size = forms.CharField(required=True)

