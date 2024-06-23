from django.shortcuts import render
import requests

def index(request):
    return render(request, "index.html")

def process(request):
    if request.method == "POST":
        data = request.POST.dict()
        data['url'] = f"https://portal.opentopography.org/API/globaldem?demtype={data['demtype']}&south={data['south']}&north={data['north']}&west={data['west']}&east={data['east']}&outputFormat={data['outputFormat']}&API_Key={data['API_Key']}"
        return render(request, "process.html", {"data": data})
    elif request.method == "GET":
        demtype = request.GET.get("demtype")
        south = request.GET.get("south")
        north = request.GET.get("north")
        west = request.GET.get("west")
        east = request.GET.get("east")
        outputFormat = request.GET.get("outputFormat", "GTiff")
        api_key = request.GET.get("API_Key")
        
        url = f"https://portal.opentopography.org/API/globaldem?demtype={demtype}&south={south}&north={north}&west={west}&east={east}&outputFormat={outputFormat}&API_Key={api_key}"
        response = requests.get(url)
        dem_data = response.json() if response.status_code == 200 else {}
        return render(request, "dem_data.html", {"dem_data": dem_data})
    else:
        return render(request, "index.html")