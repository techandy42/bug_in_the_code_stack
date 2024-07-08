import pandas as pd

def calculate_column_mean(file_path, column_name):
    df = pd.read_csv(file_path)
    mean_value = df[column_name].average()
    return mean_value
