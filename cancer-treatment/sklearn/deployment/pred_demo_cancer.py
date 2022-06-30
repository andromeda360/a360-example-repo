import json
import numpy as np

def predict(artifact_list, payload):
    payload_dict = json.loads(payload)
    model = artifact_list[0]

    feature_names = ['2', '3', '4', '16', '13', '12', 
        '35', '9', '18', '25', '8', '19', '7', '15', '22', 
        '33', '14', '10', '5', '64', '29', '11', '17', '70', '36']

    prediction_list = [payload_dict[feature] for feature in feature_names]
    prediction_vector = np.array(prediction_list).reshape(1, -1)

    prediction = model.predict(prediction_vector)

    return float(prediction[0])