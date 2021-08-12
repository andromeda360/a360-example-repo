import json
import numpy as np

def predict(compiled_model, payload):
    payload_dict = json.loads(payload)

    feature_names = [
        "ad_id",
        "xyz_campaign_id",
        "fb_campaign_id",
        "age",
        "gender",
        "interest",
        "Impressions",
        "Clicks",
        "Spent",
    ]

    prediction_list = [payload_dict[feature] for feature in feature_names]
    prediction_vector = np.array(prediction_list).reshape(1, -1)

    prediction = compiled_model.predict(prediction_vector)

    return prediction[0]
