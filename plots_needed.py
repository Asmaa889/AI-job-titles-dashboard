from dash import html, dcc, Dash
from jupyter_dash import JupyterDash #instead of app = Dash()
import plotly.express as px
import numpy as np
import dash_bootstrap_components as dbc
import pandas as pd
import dash_daq as daq
from dash.dependencies import Input, Output, State
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# pl_cl = "#323232"
# bg_cl = "#323232"
# pltte = ['deepskyblue', 'powderblue','darkcyan', 'blue', 'grey','royalblue']

def plot_hist(data, x = None, y = None, color = None, n_bins = None, range_x = None, barmode = 'group', template=None, fontcolor = 'white', color_discrete_sequence = None, pl_cl = None, bg_cl = None, order = 'trace', xaxis_title = None, yaxis_title = None, text = None):
    fig = px.histogram(data, x = x, y = y, color=color, barmode=barmode, template=template, range_x = range_x, nbins = n_bins,
                 color_discrete_sequence=color_discrete_sequence).update_xaxes(categoryorder=order)

    fig.update_layout(font_color=fontcolor, plot_bgcolor=pl_cl, paper_bgcolor= bg_cl,
                                    xaxis_title=xaxis_title,
                                    yaxis_title=yaxis_title,
                                    title={
                                        'text': text,
                                        'font': {
                                            'size': 24,
                                            'color': fontcolor
            }
        }
    )

    return fig

def plot_line(data, x = None, y = None, color = None, fontcolor = 'white', template=None, color_discrete_sequence = None, pl_cl = None, bg_cl = None, xaxis_title = None, yaxis_title = None, text = None):
    fig = px.line(data, x = x, y = y, color=color, template=template,
                 color_discrete_sequence=color_discrete_sequence)

    fig.update_layout(font_color=fontcolor, plot_bgcolor=pl_cl, paper_bgcolor= bg_cl,
                                    xaxis_title=xaxis_title,
                                    yaxis_title=yaxis_title,
                                    title={
                                        'text': text,
                                        'font': {
                                            'size': 24,
                                            'color': fontcolor
            }
        }
    )

    return fig

def plot_pie(data, names = None, values = None, color = None, fontcolor = 'white', template=None, color_discrete_sequence = None, pl_cl = None, bg_cl = None, text = None, hole = None):
    fig = px.pie(data, names=names, color=color, template=template,
                           color_discrete_sequence=color_discrete_sequence, hole=hole)
    fig.update_layout(plot_bgcolor=pl_cl, paper_bgcolor=bg_cl,
                                font_color=fontcolor,  # set the font color
                                title={
                                    'text': text,
                                    'font': {'size': 24,
                                            'color': fontcolor}
                                    }
                        )

    return fig