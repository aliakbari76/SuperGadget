from django.apps import AppConfig
import requests
import json
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
        
        
def liveGoldPrice():
    url = "https://api.metalpriceapi.com/v1/latest?api_key=d1c2b08ce42ffb65e72069c37704d285&base=xau&currencies=usd"
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    json_content = json.loads(response.text)
    print(response.text)
    return json_content['rates']['USD']
    
    
def liveCryptoPrice():
    url = "https://api.livecoinwatch.com/coins/list"

    payload = json.dumps({
    "currency": "USD",
    "sort": "rank",
    "order": "ascending",
    "offset": 0,
    "limit": 50,
    "meta": True
    })
    headers = {
    'Content-Type': 'application/json',
    'x-api-key': '857977b0-789a-4b8b-a096-afee2108fc7a'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    json_content = json.loads(response.text)
    btc_price = json_content[0]['rate']
    print(btc_price)
    etherium_price = json_content[1]['rate']
    print(etherium_price)
    
    return btc_price , etherium_price