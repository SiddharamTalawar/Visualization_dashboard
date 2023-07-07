import requests
import json
#url/endpoint of our APIview.
URL = "http://localhost:8000/api/data/"
#creating a callable function.
def get_data(country = None):
    data = {}
    if country is not None:
        data = {'country':country}
    #converting python data to json data.    
    json_data = json.dumps(data)
    #sending request.
    response = requests.get(url= URL, data = json_data) 
    #storing response.
    data = response.json()
    print(data)

# To get all the data.
get_data()    

# To get data of a specific country.
#get_data(country name)  