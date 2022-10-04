# Use Case: Customer Churn Prediction

## Introduction

Churn prediction is a common business use case, which aims to detect which customers are likely to leave a service or to cancel a subscription to a service. It is a critical prediction for many businesses because acquiring new clients often costs more than retaining existing ones.

## Goal

The general goal for this use case is to predict possible churn in the next 3 month, with the accuracy of 80%, so the business can focus on forming strategy to retain them before they actually cancel the service.

## Dataset

The dataset used here is the customer database of a reward subscription program, which contain each customer's information, including subscription time (tenure), gender, generation (Gen Z, Gen X, Millennials	etc.), and monthly charges. The prediction target is the `churn` data column, which is a binary classification (Yes, No).

All the sensitive information about the customer were removed beforehand. 

## Model type

Classification.

## Model flavor built for this use case

Sklearn (Random Forest), TensorFlow, Xgboost.

## [NEW]
A360 AI community edition is now available. You can get free compute to train, test, and deploy your machine learning (ML) models. You can try out A360 AI's fast ML deployment and power model experiment tracking. Sign up [here](https://andromeda360.ai/community-edition/).
