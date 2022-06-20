import json
import numpy as np


def predict(artifact_list, payload):
    payload_dict = json.loads(payload)
    model = artifact_list[0]

    feature_names = ['trend-index', 'day_of_month', 'day_of_year', 'week_of_year', 'year',
       'is_wknd', 'is_month_start', 'is_month_end', 'month_1', 'month_2',
       'month_3', 'month_4', 'month_5', 'month_6', 'month_7', 'month_8',
       'month_9', 'month_10', 'month_11', 'month_12']

    prediction_list = [payload_dict[feature] for feature in feature_names]
    prediction_vector = np.array(prediction_list).reshape(1, -1)

    prediction = model.predict(prediction_vector)

    return float(prediction[0])