# A360-example-repo

![Hex.pm](https://img.shields.io/hexpm/l/apa)

![image](a360_logo.png)

## [NEW- Oct 2022]
A360 AI community edition is now available. You can get free compute to train, test, and deploy your machine learning (ML) models. You can try out A360 AI's fast ML deployment and power model experiment tracking. Sign up [here](https://andromeda360.ai/community-edition/).

## Introduction

This is the template repository to get started with A360 AI Platform. A360 AI is the next generation ML platform, aiming to help data scientists/ analysts focus on model development and create business values by abstracting infrastructure complexities from them. A360 AI's key technologies are `MDK` (Model Development Kit) and `Starpack` (single-touch model deployment in 5-10 mins with only a few clicks). More information can be found in [A360 AI website](https://andromeda360.ai/).

## Getting Started

Here we provide the examples of common data science business use cases for data scientists/ analysts, such as churn prediction and product demand forecasting. Since the main development environment in A360 AI is Jupyter Lab, the examples provided are notebooks. A360 AI Users can simply follow the notebook examples for data exploratory analysis (EDA), data preprocessing, and ML model development. After the model is developed and ready for deployment, users will then utilize `Starpack` from A360 UI to package and publish the ML model as a cloud endpoint API (Starpack also supports edge deployment, examples will be released soon). `Starpack` requires a Python based deployment script to define how the endpoint payload takes the input data and how ML model make new predictions. The deployment script examples are also provided here, as well as the example notebooks showing users how to utilize the endpoint for inference with new data. 

## Directory Structure

The directory structure is below:

```

|-- business use case 			
	|-- model flavor			<- sklearn, tensorflow, pytorch etc.
		|-- local_env			<- model development in user's local environment
		|-- a360_env_e2e		<- end-to-end model development in A360 environment
		|-- a360_env_import		<- users bring the pre-built model for deployment in A360
		|-- deployment			<- deployment script example for Starpack

```

## Development Environment

#### Local or non-A360 environment

We provide generic notebook examples for each business use cases and assume users develop ML models in their local or non-A360 environment, such as Amazon SageMaker. The example notebooks are located in `local_env` directory. 

#### A360 Environment

We provide notebook starter examples for data scientist users to develop their ML models in A360 environment. `MDK` (Model Development Kit) is pre-built in all A360 environments. The starter notebooks provide practical examples on how data scientist can use `MDK` to easily interact with A360 Data Repo (with managing cloud credentials) as well as ML experiment tracking by only adding a few line of code. We also have `MDK` examples on how to register model for `Starpack` deployment in A360 environment. Since `MDK` is a powerful tool to help data scientists develop models effectively, we encourage users to do their end-to-end data science work in A360 environment. The full end-to-end example notebooks are located in `a360_env_e2e` directory.

However, in some cases, data scientists might use other ML tooling and environment they are familar with to build their ML models, such as MLflow or SageMaker. A360 AI Platform provide options for A360 users to import the model artifacts and register the model in `Starpack` so you can utilize the single-touch ML deployment in A360 AI. The model import example notebooks are located in `a360_env_import`.

## Deployment

`Starpack` is the key technology in A360 AI; it simplifies the deployment process for data scientists. With only a few click, A360 users will be able to deploy their ML model as endpoint API within 5-10 mins. In the model packaging process, users are required to provide a Python deployment script, which defines how data is loaded in endpoint payload. Users can simply follow the deployment script example for their customized ML models. The deployment script examples are located in `deployment` directory.

## Model Flavor

We currently support most of the commonly used ML frameworks, such as sklearn, tensorflow, and pytorch. Our `MDK` requires A360 users to tell the system which model flavor they used to build their ML models, so `Starpack` can take care of the backend process to prepare the model to be serialized in the correct format. 

## Contributing

A360 AI Platform users are encourage to share their ML workflow examples with the community. If you are interested in contributing to add more business use case examples, please check out the Contributor Guide (coming soon) and follow the template to create new business use cases.

## Non-A360 users
Here we provid general business use case notebook examples for data scienists, if you are not A360 AI Platform users, you are still welcomed to take advantage of these examples (in '`local_env` directory) for your own purpose. In Andromeda 360, we aim to build an open community where data scientists can educate each other and share best practices for the community, so we can grow and improve together.

