from django import forms
from django.forms.widgets import NumberInput
import datetime
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

class contactForm(forms.Form):
   name = forms.CharField(max_length = 10, help_text = "Enter your Name",error_messages={'required': 'Please enter your name.'}) # max length, initial (String) for CharField()
#    CharField() with Textarea widget
   comment = forms.CharField(widget=forms.Textarea, initial='Your comment')
#    CharField() with Textarea widget attribute
   cnt = forms.CharField(widget=forms.Textarea(attrs={'rows':2}), )
#    email
   email = forms.EmailField(required = False,label="Please enter your email address", disabled = True) #required (Boolean)
#    boolean
   agree = forms.BooleanField(initial=False)  
#    DateField()
   date = forms.DateField()
# DateField() with NumberInput widget attribute
   birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
# DateField() with SelectDateWidget widget
   birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
# DecimalField()
   value = forms.DecimalField()
# initial date not working
   day = forms.DateField(initial=datetime.date.today)
# Multiple choose
   FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
   favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
#    radio
   favoritColor = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
#    MultipleChoiceField()
   favorite_colors1 = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)

#    MultipleChoiceField() with CheckboxSelectMultiple widget
   favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

#    field_name = forms.Field(**options)
   DurationField = forms.DurationField( ) 

#    file=forms.FileField()

#    ImageField = forms.ImageField()

   GenericIPAddressField = forms.GenericIPAddressField( )
   RegexField = forms.RegexField(regex = "G.*s") 
   SlugField = forms.SlugField(max_length = 200) 
   URLField = forms.URLField( ) 
