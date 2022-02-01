import pandas as pd
class Function:
    def predict(self, df):
        # Inputs:
        # df: pd.DataFrame:
        #   A dataframe representing the inputs.
        #
        # Returns: pd.DataFrame:
        #   a new dataframe which will be captured in output table
        print(df)
        return pd.Series([df.shape[0] == 2])
        #return pd.DataFrame.from_dict({'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']})