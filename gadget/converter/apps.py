from django.apps import AppConfig


class ConverterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'converter'


def convertMetricType(input_metric_type,output_metric_type,input):
    # meter input 
    input = float(input)
    if input_metric_type == 'meter':
        if output_metric_type == 'meter':
            return input
        elif output_metric_type == 'inches':
            return (input * 39.3701)
        elif output_metric_type == 'feet':
            return (input * 3.28084)
    
    #inches input
    elif input_metric_type =='inches':
        if output_metric_type =='inches':
            return input
        elif output_metric_type=='meter':
            return (input/39.3701)
        elif output_metric_type=='feet':
            return (input / 12)
    
    # feet input 
    elif input_metric_type =='feet':
        if output_metric_type =='feet':
            return input
        elif output_metric_type=='meter':
            return (input/3.28084)
        elif output_metric_type=='inches':
            return (input * 12)
            

def convertWeightType(input_weight_type,output_weight_type,input):
    input = float(input)
    
    # kilogram input
    if input_weight_type =='kg':
        if output_weight_type =='kg':
            return input
        elif output_weight_type =='lbs':
            return input * 2.20462
        elif output_weight_type == 'ounce':
            return input*35.274
    #pound input
    elif input_weight_type =='lbs':
        if output_weight_type =='kg':
            return input/2.20462
        elif output_weight_type =='lbs':
            return input
        elif output_weight_type == 'ounce':
            return input*16
    #ounce input
    elif input_weight_type =='ounce':
        if output_weight_type =='kg':
            return input/35.274
        elif output_weight_type =='lbs':
            return input/16
        elif output_weight_type == 'ounce':
            return input