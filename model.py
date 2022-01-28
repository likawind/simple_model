import pandas as pd
class Function:
    def predict(self, df, wine):
        # Inputs:
        # df: pd.DataFrame:
        #   A dataframe representing the inputs.
        #
        # Returns: pd.DataFrame:
        #   a new dataframe which will be captured in output table
        df['new'] = df['review'].str.upper()
        df['color'] = wine['color'].iloc[0]
        return df