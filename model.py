import pandas as pd
class Function:
    def predict(self, df):
        # Inputs:
        # df: pd.DataFrame:
        #   A dataframe representing the inputs.
        #
        # Returns: pd.DataFrame:
        #   a new dataframe which will be captured in output table
        df['new'] = df['review'].str.upper()
        return df