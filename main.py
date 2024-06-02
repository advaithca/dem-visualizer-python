import streamlit as st

st.write('''
         # DEM Visualizer
            This is a simple DEM Visualizer web app to view DEM data.
            **Credit:** This web app is based on the [Streamlit](https://streamlit.io/) framework.
''')

api_key = st.text_input('Enter your API key')

if st.button('Submit'):
    if api_key:
        st.write(f'API key: {api_key}')
    else:
        api_key = "231a69cc3930e8ba0ffcab5322b94570"
    
    # Options for the API
    demTypes = {
        "SRTMGL3 (SRTM GL3 90m)" : "SRTMGL3",
        "SRTMGL1 (SRTM GL1 30m)" : "SRTMGL1",
        "SRTMGL1_E (SRTM GL1 Ellipsoidal 30m)" : "SRTMGL1_E",
        "AW3D30 (ALOS World 3D 30m)" : "AW3D30",
        "AW3D30_E (ALOS World 3D Ellipsoidal, 30m)" : "AW3D30_E",
        "SRTM15Plus (Global Bathymetry SRTM15+ V2.1 500m)" : "SRTM15Plus",
        "NASADEM (NASADEM Global DEM)" : "NASADEM",
        "COP30 (Copernicus Global DSM 30m)" : "COP30",
        "COP90 (Copernicus Global DSM 90m)" : "COP90",
        "EU_DTM (DTM 30m)" : "EU_DTM",
        "GEDI_L3 (DTM 1000m)" : "GEDI_L3",
        "GEBCOIceTopo (Global Bathymetry 500m)" : "GEBCOIceTopo",
       " GEBCOSubIceTopo (Global Bathymetry 500m)" : "GEBCOSubIceTopo",
    }
    label = '\n  '.join([key for key, value in demTypes.items()])
    st.write(f'''Select the type of DEM data, available types are''')
    st.write(label)
    dem_type = st.selectbox(f'DEM Type', list(demTypes.values()))

    south = st.number_input('South Latitude, WGS 84', -90, 90, 0)
    north = st.number_input('North Latitude, WGS 84', -90, 90, 0)
    west = st.number_input('West Longitude, WGS 84', -180, 180, 0)
    east = st.number_input('East Longitude, WGS 84', -180, 180, 0)
    
    output_format = st.selectbox('Output Format (optional) - GTiff for GeoTiff, AAIGrid for Arc ASCII Grid, HFA for Erdas Imagine (.IMG). Defaults to GTiff if parameter is not provided',
                                 ['GTiff', 'AAIGrid', 'HFA'])
    
    st.write(f'''The selected parameters are:
                - DEM Type: {dem_type}
                - South Latitude: {south}
                - North Latitude: {north}
                - West Longitude: {west}
                - East Longitude: {east}
                - Output Format: {output_format}
            ''')
    if st.button('Get DEM Data'):
        st.write('Fetching DEM data...')