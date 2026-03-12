#!/usr/bin/env python

import matplotlib.pyplot as plt
from models import calc_error, modelo_geom, modelo_circ


def make_plot():
    """
    (Si no modificas esta cadena de texto lloro)
    Si repites mucho tu código para
    graficar puedes guardarlo en una función
    """
    ... # Esto significa implementación pendiente, lo puedes eliminar

def main():
    """
    (Si no modificas esta cadena de texto lloro)
    Aquí va el código, recuerda reutilizar el 
    código que ya escribiste en otros archivos
    """
    ... # Esto significa implementación pendiente, lo puedes eliminar

    !pip install yfinance

    import pandas as pd
    import numpy as np
    import yfinance as yf
    import matplotlib.pyplot as plt
    %matplotlib inline
    %config InlineBackend.figure_format='retina'
    import warnings
    warnings.filterwarnings("ignore")

    sp500 = yf.Ticker("^GSPC").history(period="5y")

    sp500 = sp500.drop(columns=['Dividends', 'Stock Splits'])

    sp500.tail()

    sp500.describe()

    sp500.info()

    sp500['50ma'] = sp500['Close'].rolling(window=50).mean()
    sp500['200ma'] = sp500['Close'].rolling(window=200).mean()

    sp500['return'] = sp500['Close'].pct_change()

    plt.figure(figsize=(15, 5))
    plt.title('S&P 500 Daily Return')
    plt.plot(sp500['return'])
    plt.show()

    plt.figure(figsize=(15, 3))
    plt.title('S&P 500 Daily Return')
    sp500['return'].hist(bins=200, grid=False)
    plt.show()


if __name__ == "__main__":
    main()
