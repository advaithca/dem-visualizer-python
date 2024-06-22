from django.shortcuts import render
import requests

def index(request):
    return render(request, "index.html")

def process(request):
    if request.method == "POST":
        # get the data from the form
        data = request.POST.dict()
        data['url'] = f"https://portal.opentopography.org/API/globaldem?demtype={data["demtype"]}&south={data['south']}&north={data['north']}&west={data['west']}&east={data['east']}&outputFormat={data['outputFormat']}&API_Key={data['API_Key']}"
        return render(request, "process.html", {"data": data})
    else:
        return render(request, "index.html")