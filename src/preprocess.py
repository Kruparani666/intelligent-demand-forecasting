def prepare_prophet_data(data):
    df = data[['date', 'sales']].copy()
    df.columns = ['ds', 'y']
    return df
