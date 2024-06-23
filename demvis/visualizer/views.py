from django.shortcuts import render
import requests
from io import BytesIO
import rasterio
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

def index(request):
    return render(request, "index.html")

def process(request):
    if request.method == "POST":
        data = request.POST.dict()
        data['url'] = f"https://portal.opentopography.org/API/globaldem?demtype={data['demtype']}&south={data['south']}&north={data['north']}&west={data['west']}&east={data['east']}&outputFormat={data['outputFormat']}&API_Key={data['API_Key']}"
        
        demtype = request.POST.get("demtype")
        south = request.POST.get("south")
        north = request.POST.get("north")
        west = request.POST.get("west")
        east = request.POST.get("east")
        outputFormat = request.POST.get("outputFormat", "GTiff")
        api_key = request.POST.get("API_Key")
        
        url = f"https://portal.opentopography.org/API/globaldem?demtype={demtype}&south={south}&north={north}&west={west}&east={east}&outputFormat={outputFormat}&API_Key={api_key}"
        
        response = requests.get(url)
        if response.status_code == 200:
            buffer = BytesIO(response.content)
            with rasterio.open(buffer) as src:
                dem = src.read(1)
                x = np.linspace(src.bounds.left, src.bounds.right, dem.shape[1])
                y = np.linspace(src.bounds.bottom, src.bounds.top, dem.shape[0])
                x, y = np.meshgrid(x, y)

                # Create 3D surface plot
                fig = go.Figure(data=[go.Surface(z=dem, x=x, y=y, colorscale='earth')])
                fig.update_layout(
                    scene=dict(
                        xaxis_title='Longitude',
                        yaxis_title='Latitude',
                        zaxis_title='Elevation (m)'
                    ),
                    autosize=True,
                    width=None,
                    height=None
                )

                # Convert plotly figure to JSON
                plot_div = pio.to_html(fig, full_html=False)

                return render(request, 'dem_data.html', {'plot_div': plot_div, "url": url})
        else:
            return render(request, "messsage.html", {"message": "Invalid API Key or Request Error"})
    else:
        return render(request, "index.html")