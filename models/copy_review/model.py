import pandas as pd
class Function:
    def predict(self, df):
        df['new'] = df['review']
        return df