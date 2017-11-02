import pandas as pd

df = pd.read_csv(r'C:\Users\Niranjana\Documents\Python Scripts\test_data\test_data9.csv', header = None)
df.columns = ['time', 'voltage']
df.time = df.time.astype(float)
df.voltage = df.voltage.astype(float)
t = df.time.tolist()
v = df.voltage.tolist()
data = {'time' : t, 'voltage' : v}