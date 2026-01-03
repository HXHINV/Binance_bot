import pandas as pd
import numpy as np

def ema(series, period):
    return series.ewm(span=period, adjust=False).mean()

def fibonacci_levels(high, low):
    diff = high - low
    return {
        "0.382": high - diff * 0.382,
        "0.5": high - diff * 0.5,
        "0.618": high - diff * 0.618
    }

def detect_order_block(df):
    last = df.iloc[-10:]
    high = last["high"].max()
    low = last["low"].min()
    return low, high
