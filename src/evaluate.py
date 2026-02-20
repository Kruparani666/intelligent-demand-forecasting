from sklearn.metrics import mean_absolute_error

def calculate_mae(actual, predicted):
    return mean_absolute_error(actual, predicted)
