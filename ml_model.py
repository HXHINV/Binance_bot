import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        LSTM(50),
        Dense(1, activation="sigmoid")
    ])
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
    return model

def predict_signal(model, X):
    prob = model.predict(X, verbose=0)[0][0]
    if prob > 0.6:
        return "BUY"
    elif prob < 0.4:
        return "SELL"
    return "HOLD"
