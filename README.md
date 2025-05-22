# Typhoon Track Viewer

A Streamlit-based web application for visualizing historical typhoon tracks and their impacts on coastal municipalities in Region 3, Philippines. The app leverages geospatial data and interactive maps to provide insights into storm frequency, landfall locations, and affected areas from 1980 to 2024.

## Features

- Interactive selection of city/municipality and province
- Visualization of coastal barangays and typhoon tracks on a folium map
- Filtering and reporting of storms that affected selected areas
- Tabular view of filtered storm data
- Customizable map layers and popups

## Project Structure

```
.
├── main.py
├── constants.py
├── requirements.txt
├── data/
│   ├── typ_1980_2024_r3.csv
│   └── shp/
│       ├── coastal_brgy/
│       │   └── coastal_brgy.* (shapefile components)
│       └── typhoon_tracks/
│           └── typhoon_traversing_r3.* (shapefile components)
```

## Requirements

- Python 3.11+
- See [requirements.txt](requirements.txt) for dependencies

## Installation

1. Clone the repository:
    ```sh
    git clone <repo-url>
    cd storm_chaser
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure the data files are present in the `data/` directory as shown above.

## Usage

Run the Streamlit app:

```sh
streamlit run main.py
```

Open the provided local URL in your browser to interact with the app.

## Data Sources

- Typhoon tracks: IBTrACS dataset (NOAA)
- Coastal barangays: Local shapefiles

## Customization

- Update `constants.py` to modify the list of places or other constants.
- Add or update shapefiles in the `data/shp/` directory as needed.

## License

MIT License

---

*Developed by [junealexissantos].*