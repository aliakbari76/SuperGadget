from django.shortcuts import render
from .forms import MeterConversionForm , WeightConversationForm
from .apps import convertMetricType, convertWeightType
# Create your views here.
def index(request):
    return render(request , 'index.html')

def metrics(request):
    if request.method =='POST':
        form =  MeterConversionForm(request.POST)
        if form.is_valid():
            print("HERE!")
            input_metric_type = form.cleaned_data['input_metric']
            metric_value = form.cleaned_data['text_input']
            output_metric_type = form.cleaned_data['output_metric']
            result_of_metric = convertMetricType(input_metric_type , output_metric_type , metric_value)
            
            return render(request , 'metricConversation.html', {
                'form':MeterConversionForm,
                'result_of_metric':result_of_metric})
    return render(request , 'metricConversation.html', {'form':MeterConversionForm})


def weightConversion(request):
    if request.method =='POST':
        print("here")
        form = WeightConversationForm(request.POST)
        if form.is_valid():
            print("here2")
            input_weight_type = form.cleaned_data['input_weight_type']
            weight_value = form.cleaned_data['text_input']
            output_weight_type = form.cleaned_data['output_weight_type']
            result_of_weight = convertWeightType(input_weight_type,output_weight_type,weight_value)
            print(result_of_weight)
            return render(request , 'weightConversation.html', {
                'form':WeightConversationForm,
                'result_of_Weight':result_of_weight})
            
    return render(request , 'weightConversation.html', {'form':WeightConversationForm})