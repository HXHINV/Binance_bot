from datetime import date

trades_today = {"date": date.today(), "count": 0}

def can_trade(max_trades):
    global trades_today
    if trades_today["date"] != date.today():
        trades_today = {"date": date.today(), "count": 0}
    return trades_today["count"] < max_trades

def register_trade():
    trades_today["count"] += 1
