import pandas as pd
from binance_client import get_klines, market_buy, market_sell
from config import SYMBOL, INTERVAL, TRADE_QUANTITY, MAX_TRADES_PER_DAY
from strategy import evaluate_strategy
from risk import can_trade, register_trade
from tensorflow.keras.models import load_model

print("HxH PAXG Bot iniciado — Implementado por DevYHB")

model = load_model("model.h5")

while True:
    klines = get_klines(SYMBOL, INTERVAL)
    df = pd.DataFrame(klines, columns=[
        "time","open","high","low","close","volume",
        "_","_","_","_","_","_"
    ])
    df[["open","high","low","close"]] = df[["open","high","low","close"]].astype(float)

    signal = evaluate_strategy(df, model)
    print("Señal:", signal)

    if signal == "BUY" and can_trade(MAX_TRADES_PER_DAY):
        market_buy(SYMBOL, TRADE_QUANTITY)
        register_trade()
        print("BUY ejecutado")

    elif signal == "SELL" and can_trade(MAX_TRADES_PER_DAY):
        market_sell(SYMBOL, TRADE_QUANTITY)
        register_trade()
        print("SELL ejecutado")

    import time
    time.sleep(60)
