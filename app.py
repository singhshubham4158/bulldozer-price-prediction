from flask import Flask, request, render_template
import pandas as pd
from sklearn import pipeline
from xgboost import data
from src.pipeline.predict_pipeline import PredictPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.to_dict()

# convert all to float
    data = {k: float(v) for k, v in data.items()}

    import pandas as pd
    df = pd.DataFrame([data])

    pipeline = PredictPipeline()
    pred = pipeline.predict(df)

    return render_template("home.html", prediction=round(pred[0], 2))

if __name__ == "__main__":
    app.run(debug=True)