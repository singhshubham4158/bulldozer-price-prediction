import pandas as pd
from src.utils import load_object

class PredictPipeline:
    def predict(self, df):
        model = load_object("artifacts/model.pkl")

        # 🔥 enforce column order
        expected_cols = ['YearMade',
                         'MachineHoursCurrentMeter',
                         'YearSold',
                         'MonthSold',
                         'DaySold',
                         'SaleElapsed']

        df = df[expected_cols]

        return model.predict(df)