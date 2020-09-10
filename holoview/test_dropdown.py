import numpy as np
import holoviews as hv
import pandas as pd
from holoviews import opts
import bokeh.sampledata

bokeh.sampledata.download()
from bokeh.sampledata import stocks
from holoviews.operation.timeseries import rolling, rolling_outlier_std
from holoviews import opts

hv.extension('bokeh')


def load_symbol(symbol, variable='adj_close', **kwargs):
    df = pd.DataFrame(getattr(stocks, symbol))
    df['date'] = df.date.astype('datetime64[ns]')
    return hv.Curve(df, ('date', 'Date'), variable).opts(framewise=True)

stock_symbols = ['AAPL', 'IBM', 'FB', 'GOOG', 'MSFT']
dmap = hv.DynamicMap(load_symbol, kdims='Symbol').redim.values(Symbol=stock_symbols)
dmap.opts(framewise=True)