from flask import Flask, request
import numpy
from catboost import CatBoostRegressor

MODEL_PATH = 'data/catboost_predictor'

app = Flask(__name__)
model = CatBoostRegressor().load_model(MODEL_PATH)


@app.route('/predict_price', methods=['GET'])
def predict():
    args = request.args

    features = []
    feature_names = [
        'floor', 'open_plan', 'rooms', 'studio', 'area', 'kitchen_area',
        'living_area', 'agent_fee', 'renovation', 'offer_type', 'category_type'
    ]

    for feature_name in feature_names:
        features.append(args.get(feature_name, default=0))

    x = numpy.array(features).reshape(1, -1)
    print(x)
    prediction = model.predict(x)[0]

    return {"predicted_price": prediction}


if __name__ == '__main__':
    app.run(debug=True, port=5444, host='0.0.0.0')
