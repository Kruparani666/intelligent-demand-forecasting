import pandas as pd

def load_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])
    data = data.sort_values('date')
    return data
