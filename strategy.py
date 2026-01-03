import pandas as pd
from indicators import ema, fibonacci_levels, detect_order_block
from config import EMA_SHORT, EMA_LONG
from ml_model import predict_signal

def evaluate_strategy(df, ml_model):
    df["ema_short"] = ema(df["close"], EMA_SHORT)
    df["ema_long"] = ema(df["close"], EMA_LONG)

    last = df.iloc[-1]
    prev = df.iloc[-2]

    # EMA crossover
    if prev.ema_short < prev.ema_long and last.ema_short > last.ema_long:
        ema_signal = "BUY"
    elif prev.ema_short > prev.ema_long and last.ema_short < last.ema_long:
        ema_signal = "SELL"
    else:
        ema_signal = "HOLD"

    # Order Block
    ob_low, ob_high = detect_order_block(df)
    in_ob = ob_low <= last.close <= ob_high

    # Fibonacci
    fib = fibonacci_levels(df.high.max(), df.low.min())
    in_fib = fib["0.618"] <= last.close <= fib["0.382"]

    # ML
    X = df[["close"]].values[-50:].reshape(1, 50, 1)
    ml_signal = predict_signal(ml_model, X)

    if ema_signal == ml_signal and in_ob and in_fib:
        return ema_signal

    return "HOLD"
