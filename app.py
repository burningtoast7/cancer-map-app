import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a nice Seaborn theme
sns.set_theme(style="white")

st.set_page_config(layout="wide", page_title="Global Cancer Rate Map")

st.title("🌍 Global Cancer Rate per Capita by Country (ASR, 2022)")
st.markdown(
    """
    **ASR = Age-Standardized Rate per 100,000 people**  
    Data visualized for select countries.
    """
)

# 1. Load base world map from GeoPandas
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# 2. Cancer incidence data (ASR per 100,000 people)
cancer_data = {
    'Australia': 452.4,
    'New Zealand': 422.5,
    'Ireland': 375.6,
    'Hungary': 368.1,
    'United States': 362.2,
    'Belgium': 356.7,
    'France': 352.1,
    'Netherlands': 350.2,
    'Norway': 345.9,
    'Canada': 342.3,
    'Denmark': 341.5,
    'South Korea': 340.1,
    'Germany': 335.5,
    'Italy': 324.6,
    'Sweden': 317.8,
    'Japan': 298.7,
    'Poland': 294.2,
    'United Kingdom': 290.0,
    'Spain': 282.5,
    'China': 210.1,
    'Brazil': 205.4,
    'South Africa': 186.3,
    'Mexico': 171.5,
    'Russia': 246.0,
    'India': 104.4,
    'Nigeria': 95.8,
    'Egypt': 112.3,
    'Kenya': 133.9
}

# 3. Convert cancer data to DataFrame
df_cancer = pd.DataFrame({
    'name': list(cancer_data.keys()),
    'cancer_asr': list(cancer_data.values())
})

# 4. Merge world GeoDataFrame with cancer data
world = world.merge(df_cancer, on='name', how='left')

# 5. Plotting the map
fig, ax = plt.subplots(1, 1, figsize=(18, 10))

# Plot choropleth
world.plot(
    column='cancer_asr',
    ax=ax,
    cmap='OrRd',
    linewidth=0.8,
    edgecolor='0.8',
    legend=True,
    missing_kwds={
        'color': 'lightgrey',
        'label': 'No data'
    },
    legend_kwds={
        'label': "Cancer Incidence Rate per 100,000 People (ASR)",
        'shrink': 0.5,
        'orientation': 'horizontal'
    }
)

# Final map styling
ax.set_axis_off()
plt.tight_layout()
st.pyplot(fig)