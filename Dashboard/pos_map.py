#import required libraries.
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

cov_cases = pd.read_csv("data/cov_cases.csv")
fig = go.Figure()
fig = px.choropleth(cov_cases,
                   locations='abbrev',
                   color='positive',
                   hover_name = 'state',
                   locationmode = 'USA-states',
                   animation_frame = 'date')

layout = (
fig.update_layout(
title_text = 'Spread of Covid-19 in the United States',
title_x = 0.5,
geo_scope = 'usa',
geo=dict(
showframe = False,
showcoastlines = False))
)

pio.write_html(fig,
               file='pos_cases.html',
               config={'displayModeBar': False},
               auto_open=True,
               include_plotlyjs='cdn',
               full_html=False)


