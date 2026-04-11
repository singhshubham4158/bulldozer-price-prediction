from src.pipeline.train_pipeline import TrainPipeline


def main():
    print("🚀 Training Pipeline Started...")

    pipeline = TrainPipeline()
    pipeline.run_pipeline()

    print("✅ Training Completed Successfully!")


if __name__ == "__main__":
    main()