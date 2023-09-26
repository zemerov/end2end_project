from flask import Flask, request
import numpy
from catboost import CatBoostRegressor
from loguru import logger
from argparse import ArgumentParser

FEATURE_NAMES = [
    'floor', 'open_plan', 'rooms', 'studio', 'area', 'kitchen_area',
    'living_area', 'agent_fee', 'renovation', 'offer_type', 'category_type'
]

parser = ArgumentParser()
parser.add_argument("--port", type=int, default=8080, help="Port for serving requests")
parser.add_argument("--model-path", type=str, default='data/catboost_predictor')

args = parser.parse_args()

app = Flask(__name__)
model = CatBoostRegressor().load_model(args.model_path)


@app.route('/predict_price', methods=['GET'])
def predict():
    args = request.args
    logger.info(f"Got predict_price request with args: {args}")

    features = []

    for feature_name in FEATURE_NAMES:
        features.append(args.get(feature_name, default=0))

    x = numpy.array(features).reshape(1, -1)
    prediction = model.predict(x)[0]

    logger.info(f"Model predicted: {prediction}")

    return {"predicted_price": prediction}


if __name__ == '__main__':
    app.run(debug=True, port=args.port, host='0.0.0.0')
