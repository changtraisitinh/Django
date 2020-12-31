from django.shortcuts import render

# Create your views here.
def home(request):

    import json
    import requests

    if request.method == 'POST':
        zipcode = request.POST['zipcode']
        print(zipcode)
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=AE746482-3655-4881-9A75-3A149FD4E7F5")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = e

        return render(request, 'home.html', {'api' : api})
    else:
        api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=AE746482-3655-4881-9A75-3A149FD4E7F5')

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = e

        return render(request, 'home.html', {'api' : api})


def about(request):
    return render(request, 'about.html', {})