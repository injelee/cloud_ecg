import pandas as pd


def csvtojson(data):
    df = pd.read_csv(data, header=None)
    # df = pd.read_csv(r'/Users/injelee/Desktop/pleasework2.csv', header=None)
    df.columns = ['averaging_period', 'time', 'voltage']
    df.avg_period = df.averaging_period.astype(float)
    df.time = df.time.astype(float)
    df.voltage = df.voltage.astype(float)
    averaging_period = df.avg_period.tolist()
    t = df.time.tolist()
    v = df.voltage.tolist()
    data = {'averaging_period': averaging_period[0], 'time': t, 'voltage': v}
    return data
