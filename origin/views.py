from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def location_autocomplete(req):
    query = req.GET.get('query')
    if not query:
        return JsonResponse([], safe=False)
    url = f"https://maps.gomaps.pro/maps/api/place/autocomplete/json?input=<f{query}>&key=AlzaSyccNxQvfcj06z_blIxi2VTBj9l7ViHMKGx"
    response = req.get(url)
    suggestions = response.json().get('features', [])
    print(suggestions)
    results = [{'place_name': place['place_name']} for place in suggestions]
    
    return JsonResponse(results, safe=False)