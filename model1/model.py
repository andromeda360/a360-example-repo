import json
import numpy as np

def predict(compiled_model, payload):
    payload_dict = json.loads(payload)

    feature_names = [
        "avg(BMI)",
        "avg(active_heartrate)",
        "avg(resting_heartrate)",
        "avg(VO2_max)",
    ]

    prediction_list = [payload_dict[feature] for feature in feature_names]
    prediction_vector = np.array(prediction_list).reshape(1, -1)

    prediction = compiled_model.predict(prediction_vector)

    return prediction[0]
