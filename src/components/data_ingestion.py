import os
import pandas as pd

class DataIngestion:
    def initiate_data_ingestion(self):
        file_path = os.path.join(os.getcwd(), "data", "train.csv")

        df = pd.read_csv(file_path)

        os.makedirs("artifacts", exist_ok=True)
        df.to_csv("artifacts/train.csv", index=False)

        return "artifacts/train.csv"