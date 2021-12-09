
import json
import numpy as np

def predict(artifact_list, payload):

    payload_dict = json.loads(payload)
    model = artifact_list[0]

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

    prediction = model.predict(prediction_vector)

    return float(prediction[0])