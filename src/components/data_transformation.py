import pandas as pd
from sklearn.model_selection import train_test_split


class DataTransformation:
    def initiate_data_transformation(self, file_path):
        df = pd.read_csv(file_path)

        # Convert date
        df['saledate'] = pd.to_datetime(df['saledate'])

        # Create features
        df['YearSold'] = df['saledate'].dt.year
        df['MonthSold'] = df['saledate'].dt.month
        df['DaySold'] = df['saledate'].dt.day
        df['SaleElapsed'] = df['saledate'].map(pd.Timestamp.timestamp)

        # Select required columns
        df = df[['YearMade',
                 'MachineHoursCurrentMeter',
                 'YearSold',
                 'MonthSold',
                 'DaySold',
                 'SaleElapsed',
                 'SalePrice']]

        df = df.dropna()

        X = df.drop("SalePrice", axis=1)
        y = df["SalePrice"]

        # 🔥 THIS WAS MISSING
        return train_test_split(X, y, test_size=0.2, random_state=42)