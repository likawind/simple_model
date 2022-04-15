import pandas as pd
from utils.helper import _predict

class Model:
    def run(self, df):
        return _predict(df)