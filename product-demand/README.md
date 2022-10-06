# Use Case: Product Demand Forecasting

## Introduction

Demand forecasting is a common business use case, which aims to estimate what customer demand will look like in the future, and how it will affect a business' supply chain.

## Goal

The general goal for this use case is to predict the sales in the next 3 month, with the accuracy of 80%, so the business can better manage their supply chain, inventory and procurement.

## Dataset

The dataset used here is the historical sales for a specific item in all US stores. The data columns are: 

- (1) `trend-index`: this is the company's internal demand indicator calculated from Google Analytics.
- (2) `sales`: actual sales for the item in all US stores combined.

Data range from `2015-01-01` to `2020-04-29`. One interesting factor about this dataset is the sales data covered pre-COVID and COVID periods, which is a good use case to explore data drift and concept drift.  

## Model type

Regression.

## Model flavor built for this use case

Sklearn (Random Forest), TensorFlow, PyTorch.

## [NEW]
A360 AI community edition is now available. You can get free compute to train, test, and deploy your machine learning (ML) models. You can try out A360 AI's fast ML deployment and power model experiment tracking. Sign up [here](https://andromeda360.ai/community-edition/).
