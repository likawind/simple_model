import pandas as pd
from .utils.helper import _predict
class Function:
    def predict(self, df):
        return _predict(df)