import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, heatmap, upload, app, split # import your app modules here

st.set_page_config(page_title="GeoIT App", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": heatmap.app, "title": "Heatmap", "icon": "map"},
    {"func": upload.app, "title": "Upload", "icon": "cloud-upload"},
    {"func": split.app, "title": "ESA WorldCover", "icon": "forest"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web is made to Monitor the Geospatial and environmental factors Worldwide.

        This analysis will complement CLASP’s ongoing efforts on
        region/county selection and inform a robust, data driven
        prioritization process.

        More menu infos? please visit!: [forest.ly](https://ham811.github.io/forest.ly/)
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
