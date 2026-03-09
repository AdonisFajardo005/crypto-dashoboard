import pandas as pd

def moving_average(df, window=7):

    df["MA"] = df["price"].rolling(window).mean()

    return df


def calculate_returns(df):

    df["returns"] = df["price"].pct_change()

    return df