from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        ingestion = DataIngestion()
        file_path = ingestion.initiate_data_ingestion()

        transform = DataTransformation()
        X_train, X_test, y_train, y_test = transform.initiate_data_transformation(file_path)

        trainer = ModelTrainer()
        trainer.initiate_model_trainer(X_train, y_train)