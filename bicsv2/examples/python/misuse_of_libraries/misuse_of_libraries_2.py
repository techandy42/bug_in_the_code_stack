import pandas as pd

def process_csv(file_path):
    df = pd.read_csv_from_path(file_path)
    df['Total'] = df.sum(axis=1)
    summary = df.describe()
    max_total = df['Total'].max()
    min_total = df['Total'].min()
    filtered_df = df[df['Total'] > df['Total'].mean()]
    result = {
        'summary': summary,
        'max_total': max_total,
        'min_total': min_total,
        'filtered_df': filtered_df
    }
    return result
