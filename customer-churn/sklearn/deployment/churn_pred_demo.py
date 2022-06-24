import json
import numpy as np


def predict(artifact_list, payload):
    payload_dict = json.loads(payload)
    model = artifact_list[0]

    feature_names = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       'MobileOnRecord', 'AddressOnRecord', 'TwoFactorAuth', 'OnlineBackup',
       'DeviceProtection', 'TechSupport', 'NewsletterSubscribe',
       'PaperlessBilling', 'LastLogInOneMonth', 'MonthlyCharges',
       'TotalCharges', 'LinkedAccount_Amazon', 'LinkedAccount_Starbucks',
       'LinkedAccount_Target', 'Contract_Month-to-month', 'Contract_One year',
       'Contract_Two year', 'Generation_Boomers', 'Generation_Gen X',
       'Generation_Gen Z', 'Generation_Millennials']

    prediction_list = [payload_dict[feature] for feature in feature_names]
    prediction_vector = np.array(prediction_list).reshape(1, -1)

    prediction = model.predict(prediction_vector)

    return float(prediction[0])