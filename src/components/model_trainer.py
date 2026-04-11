class ModelTrainer:
    def initiate_model_trainer(self, X_train, y_train):
        print("Training started...")

        from sklearn.ensemble import RandomForestRegressor
        model = RandomForestRegressor()
        model.fit(X_train, y_train)

        print("Saving model...")
        from src.utils import save_object
        save_object("artifacts/model.pkl", model)

        print("Model saved ✅")