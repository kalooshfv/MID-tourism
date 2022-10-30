from django import forms
from resto.models import *

DAYS = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'resto_name', 
            'resto_address',
            'resto_email', 
            'resto_phone',
            'resto_description',
            'resto_photo',
            'resto_delivery',
        ]

    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        self.fields['resto_photo'].required = True
        self.fields['resto_delivery'].required = True

        

class OpeningHoursForm(forms.ModelForm):
    class Meta:
        model = OpeningHours
        fields = [
            'hours_weekday',
            'hours_from_hour',
            'hours_to_hour',
        ]

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            'food_name', 
            'food_price',
            'food_stock', 
            'food_description',
            'food_photo', 
        ]

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.fields['food_photo'].required = True

        
    
