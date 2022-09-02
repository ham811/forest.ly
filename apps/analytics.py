import ee
import streamlit as st
import geemap.foliumap as geemap


def app():

    st.title("Change layer opacity")

    col1, _, col2, _ = st.columns([1, 0.3, 2, 2])

    with col1:
        layer = st.selectbox("Select a layer", ["SRTM DEM", "Landsat", "US Census"])

    with col2:
        opacity = st.slider(
            "Opacity", min_value=0.0, max_value=1.0, value=0.8, step=0.05
        )

    Map = geemap.Map()

    # Add Earth Engine dataset
    dem = ee.Image("USGS/SRTMGL1_003")
    landsat7 = ee.Image("MODIS/006/MOD13Q1").select(
        'NDVI'
    )
    states = region= ee.FeatureCollection('FAO/GAUL/2015/level1').filter(ee.Filter.eq('ADM0_NAME', 'Germany')) 

    # Set visualization parameters.
    dem_vis = {
        "min": 0,
        "max": 1.0,
        "palette": [
        'FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901',
        '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01',
        '012E01', '011D01', '011301'
        ],
    }

    landsat7_vis = {"bands": ["B4", "B3", "B2"], "min": 20, "max": 200, "gamma": 2.0}

    layer = layer.strip()
    if layer == "SRTM DEM":
        Map.addLayer(dem, dem_vis, "SRTM DEM", True, opacity)
    elif layer == "Modis NDVI":
        Map.addLayer(landsat7, landsat7_vis, "Modis NDVI", True, opacity)
    elif layer == "US Census":
        Map.addLayer(states, {}, "US Census", True, opacity)

    Map.to_streamlit()
