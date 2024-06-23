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
                print(x, y)
                x, y = np.meshgrid(x, y)

                # Create 3D surface plot
                fig = go.Figure(data=[go.Surface(z=dem, x=x, y=y, colorscale='earth')])

                fig.update_layout(
                    scene=dict(
                        xaxis_title='Longitude',
                        yaxis_title='Latitude',
                        zaxis_title='Elevation (m)'
                    ),
                    updatemenus=[
                        dict(
                            buttons = [
                                {"args": ["colorscale", "aggrnyl"], "label": "Aggrnyl", "method": "restyle"},
                                {"args": ["colorscale", "agsunset"], "label": "Agsunset", "method": "restyle"},
                                {"args": ["colorscale", "blackbody"], "label": "Blackbody", "method": "restyle"},
                                {"args": ["colorscale", "bluered"], "label": "Bluered", "method": "restyle"},
                                {"args": ["colorscale", "blues"], "label": "Blues", "method": "restyle"},
                                {"args": ["colorscale", "blugrn"], "label": "Blugrn", "method": "restyle"},
                                {"args": ["colorscale", "bluyl"], "label": "Bluyl", "method": "restyle"},
                                {"args": ["colorscale", "brwnyl"], "label": "Brwnyl", "method": "restyle"},
                                {"args": ["colorscale", "bugn"], "label": "Bugn", "method": "restyle"},
                                {"args": ["colorscale", "bupu"], "label": "Bupu", "method": "restyle"},
                                {"args": ["colorscale", "burg"], "label": "Burg", "method": "restyle"},
                                {"args": ["colorscale", "burgyl"], "label": "Burgyl", "method": "restyle"},
                                {"args": ["colorscale", "cividis"], "label": "Cividis", "method": "restyle"},
                                {"args": ["colorscale", "darkmint"], "label": "Darkmint", "method": "restyle"},
                                {"args": ["colorscale", "electric"], "label": "Electric", "method": "restyle"},
                                {"args": ["colorscale", "emrld"], "label": "Emrld", "method": "restyle"},
                                {"args": ["colorscale", "gnbu"], "label": "Gnbu", "method": "restyle"},
                                {"args": ["colorscale", "greens"], "label": "Greens", "method": "restyle"},
                                {"args": ["colorscale", "greys"], "label": "Greys", "method": "restyle"},
                                {"args": ["colorscale", "hot"], "label": "Hot", "method": "restyle"},
                                {"args": ["colorscale", "inferno"], "label": "Inferno", "method": "restyle"},
                                {"args": ["colorscale", "jet"], "label": "Jet", "method": "restyle"},
                                {"args": ["colorscale", "magenta"], "label": "Magenta", "method": "restyle"},
                                {"args": ["colorscale", "magma"], "label": "Magma", "method": "restyle"},
                                {"args": ["colorscale", "mint"], "label": "Mint", "method": "restyle"},
                                {"args": ["colorscale", "orrd"], "label": "Orrd", "method": "restyle"},
                                {"args": ["colorscale", "oranges"], "label": "Oranges", "method": "restyle"},
                                {"args": ["colorscale", "oryel"], "label": "Oryel", "method": "restyle"},
                                {"args": ["colorscale", "peach"], "label": "Peach", "method": "restyle"},
                                {"args": ["colorscale", "pinkyl"], "label": "Pinkyl", "method": "restyle"},
                                {"args": ["colorscale", "plasma"], "label": "Plasma", "method": "restyle"},
                                {"args": ["colorscale", "plotly3"], "label": "Plotly3", "method": "restyle"},
                                {"args": ["colorscale", "pubu"], "label": "Pubu", "method": "restyle"},
                                {"args": ["colorscale", "pubugn"], "label": "Pubugn", "method": "restyle"},
                                {"args": ["colorscale", "purd"], "label": "Purd", "method": "restyle"},
                                {"args": ["colorscale", "purp"], "label": "Purp", "method": "restyle"},
                                {"args": ["colorscale", "purples"], "label": "Purples", "method": "restyle"},
                                {"args": ["colorscale", "purpor"], "label": "Purpor", "method": "restyle"},
                                {"args": ["colorscale", "rainbow"], "label": "Rainbow", "method": "restyle"},
                                {"args": ["colorscale", "rdbu"], "label": "Rdbu", "method": "restyle"},
                                {"args": ["colorscale", "rdpu"], "label": "Rdpu", "method": "restyle"},
                                {"args": ["colorscale", "redor"], "label": "Redor", "method": "restyle"},
                                {"args": ["colorscale", "reds"], "label": "Reds", "method": "restyle"},
                                {"args": ["colorscale", "sunset"], "label": "Sunset", "method": "restyle"},
                                {"args": ["colorscale", "sunsetdark"], "label": "Sunsetdark", "method": "restyle"},
                                {"args": ["colorscale", "teal"], "label": "Teal", "method": "restyle"},
                                {"args": ["colorscale", "tealgrn"], "label": "Tealgrn", "method": "restyle"},
                                {"args": ["colorscale", "turbo"], "label": "Turbo", "method": "restyle"},
                                {"args": ["colorscale", "viridis"], "label": "Viridis", "method": "restyle"},
                                {"args": ["colorscale", "ylgn"], "label": "Ylgn", "method": "restyle"},
                                {"args": ["colorscale", "ylgnbu"], "label": "Ylgnbu", "method": "restyle"},
                                {"args": ["colorscale", "ylorbr"], "label": "Ylorbr", "method": "restyle"},
                                {"args": ["colorscale", "ylorrd"], "label": "Ylorrd", "method": "restyle"},
                                {"args": ["colorscale", "algae"], "label": "Algae", "method": "restyle"},
                                {"args": ["colorscale", "amp"], "label": "Amp", "method": "restyle"},
                                {"args": ["colorscale", "deep"], "label": "Deep", "method": "restyle"},
                                {"args": ["colorscale", "dense"], "label": "Dense", "method": "restyle"},
                                {"args": ["colorscale", "gray"], "label": "Gray", "method": "restyle"},
                                {"args": ["colorscale", "haline"], "label": "Haline", "method": "restyle"},
                                {"args": ["colorscale", "ice"], "label": "Ice", "method": "restyle"},
                                {"args": ["colorscale", "matter"], "label": "Matter", "method": "restyle"},
                                {"args": ["colorscale", "solar"], "label": "Solar", "method": "restyle"},
                                {"args": ["colorscale", "speed"], "label": "Speed", "method": "restyle"},
                                {"args": ["colorscale", "tempo"], "label": "Tempo", "method": "restyle"},
                                {"args": ["colorscale", "thermal"], "label": "Thermal", "method": "restyle"},
                                {"args": ["colorscale", "turbid"], "label": "Turbid", "method": "restyle"},
                                {"args": ["colorscale", "armyrose"], "label": "Armyrose", "method": "restyle"},
                                {"args": ["colorscale", "brbg"], "label": "Brbg", "method": "restyle"},
                                {"args": ["colorscale", "earth"], "label": "Earth", "method": "restyle"},
                                {"args": ["colorscale", "fall"], "label": "Fall", "method": "restyle"},
                                {"args": ["colorscale", "geyser"], "label": "Geyser", "method": "restyle"},
                                {"args": ["colorscale", "prgn"], "label": "Prgn", "method": "restyle"},
                                {"args": ["colorscale", "piyg"], "label": "Piyg", "method": "restyle"},
                                {"args": ["colorscale", "picnic"], "label": "Picnic", "method": "restyle"},
                                {"args": ["colorscale", "portland"], "label": "Portland", "method": "restyle"},
                                {"args": ["colorscale", "puor"], "label": "Puor", "method": "restyle"},
                                {"args": ["colorscale", "rdgy"], "label": "Rdgy", "method": "restyle"},
                                {"args": ["colorscale", "rdylbu"], "label": "Rdylbu", "method": "restyle"},
                                {"args": ["colorscale", "rdylgn"], "label": "Rdylgn", "method": "restyle"},
                                {"args": ["colorscale", "spectral"], "label": "Spectral", "method": "restyle"},
                                {"args": ["colorscale", "tealrose"], "label": "Tealrose", "method": "restyle"},
                                {"args": ["colorscale", "temps"], "label": "Temps", "method": "restyle"},
                                {"args": ["colorscale", "tropic"], "label": "Tropic", "method": "restyle"},
                                {"args": ["colorscale", "balance"], "label": "Balance", "method": "restyle"},
                                {"args": ["colorscale", "curl"], "label": "Curl", "method": "restyle"},
                                {"args": ["colorscale", "delta"], "label": "Delta", "method": "restyle"},
                                {"args": ["colorscale", "oxy"], "label": "Oxy", "method": "restyle"},
                                {"args": ["colorscale", "edge"], "label": "Edge", "method": "restyle"},
                                {"args": ["colorscale", "hsv"], "label": "Hsv", "method": "restyle"},
                                {"args": ["colorscale", "icefire"], "label": "Icefire", "method": "restyle"},
                                {"args": ["colorscale", "phase"], "label": "Phase", "method": "restyle"},
                                {"args": ["colorscale", "twilight"], "label": "Twilight", "method": "restyle"},
                                {"args": ["colorscale", "mrybm"], "label": "Mrybm", "method": "restyle"},
                                {"args": ["colorscale", "mygbm"], "label": "Mygbm", "method": "restyle"},
                            ],
                            direction="down",
                            pad={"r": 10, "t": 10},
                            showactive=True,
                        )
                    ]
                )

                # Convert plotly figure to JSON
                plot_div = pio.to_html(fig, full_html=False)

                return render(request, 'dem_data.html', {'plot_div': plot_div, "url": url})
        else:
            return render(request, "messsage.html", {"message": "Invalid API Key or Request Error"})
    else:
        return render(request, "index.html")