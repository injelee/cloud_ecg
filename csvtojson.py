import pandas as pd


def csvtojson(data):
    df = pd.read_csv(data, header=None)
    df.columns = ['time', 'voltage']
    df.time = df.time.astype(float)
    df.voltage = df.voltage.astype(float)
    t = df.time.tolist()
    v = df.voltage.tolist()
    data = {'time': t, 'voltage': v}
    return data
