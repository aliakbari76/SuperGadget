from django import forms



class MeterConversionForm(forms.Form):
    METRICS_CHOICES = [
        ('meter', 'Meter'),
        ('inches', 'Inches'),
        ('feet', 'Feet'),
        ('foot', 'Foot'),
    ]

    input_metric = forms.ChoiceField(choices=METRICS_CHOICES,label='convert from', widget=forms.Select(attrs={'class': 'form-control ' }))
    text_input = forms.CharField(label='data',widget=forms.TextInput(attrs={'class': 'form-control mx-4'}))
    output_metric = forms.ChoiceField(choices=METRICS_CHOICES,label='convert to:', widget=forms.Select(attrs={'class': 'form-control ' }))
    

class WeightConversationForm(forms.Form):
    WEIGHT_CHOICES =[
        ('kg' , 'KG'),
        ('lbs' , 'LBS'),
        ('ounce','Ounce')
    ]

    input_weight_type = forms.ChoiceField(choices=WEIGHT_CHOICES,label='convert from', widget=forms.Select(attrs={'class': 'form-control ' }))
    text_input = forms.CharField(label='data',widget=forms.TextInput(attrs={'class': 'form-control mx-4'}))
    output_weight_type = forms.ChoiceField(choices=WEIGHT_CHOICES,label='convert to:', widget=forms.Select(attrs={'class': 'form-control ' }))    