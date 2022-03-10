import pandas as pd

def _predict(df: pd.DataFrame) -> pd.DataFrame:
    df['new'] = df['review']
    return df