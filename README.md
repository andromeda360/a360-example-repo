# A360-example-repo

![Hex.pm](https://img.shields.io/hexpm/l/apa)

![image](a360_logo.png)

This is the template repository for data scientists to get started with A360 AI Platform. A360 AI is the next generation ML platform, aiming to help data scientists focus on model development and create business values by abstracting infrastructure complexities. A360 AI's key technologies are MDK (Model Development Kit) and Starpack (zero-touch model deployment in 5-10 mins with only a few clicks). More information can be found in [A360 AI website](https://andromeda360.ai/).

## Getting Started

Here we provide the examples of common data science business use cases for data scientists, such as churn prediction and product demand forecasting. Since the main development environment in A360 AI is Jupyter Lab, the examples provided are notebooks. Users can simply follow the notebook examples for data exploratory analysis (EDA), data preprocessing, and ML model development. After the model is developed and ready for deployment, users will then use `Starpack` to package and publish the ML model as a cloud endpoint API. `Starpack` requires a Python based deployment script to define how the endpoint payload takes the input data and use the ML model to make new predictions. The deployment script example is provided here. We also have example notebooks to show the users how they can utilize the endpoint for inference with new data. 

## Directory Structure

The directory structure is below:

```

|-- business use case 			
	|-- model flavor			<- sklearn, tensorflow, pytorch
		|-- local_env			<- model development in user's local environment
		|-- a360_env_e2e		<- end-to-end model development in A360 environment
		|-- a360_env_import		<- users bring the pre-built model for deployment 
		|-- deployment			<- deployment script example

```

## Development Environment

### Local or non-A360 environment

We provide generic notebook examples for each business use cases and assume users develop the models in their local or non-A360 environment, such as Amazon SageMaker. The example notebooks are located in `local_env` directory. 

### A360 Environment

Here we provide notebook starter examples for data scientist users to develop their ML models in A360 environment. In A360 environment, our `MDK` (Model Development Kit) is pre-built. Therefore, we provide practical examples on how data scientist can use `MDK` to easily interact with A360 Data Repo as well as ML experiment tracking with adding only a few line of code. We also have `MDK` example on how to register model for `Starpack` deployment. Since the `MDK` is a powerful tool to help data scientists develop models effectively, we encourage users to do their end-to-end data science work in A360 environment. The full end-to-end example notebooks are located in `a360_env_e2e` directory.

However, in some cases, data scientists might use other ML tooling and environment they are familar with to build their ML models, such as MLflow or SageMaker. A360 AI Platform also has options for the users to import the model artifacts and register the model in `Starpack` so the users can utilize the zero-touch ML deployment in A360 AI. The model import example notebooks are located in `a360_env_import`.

## Deployment

`Starpack` is the key technology in A360 AI, which simplifies the deployment process for data scientists. With only a few click, the users will be able to deploy their ML model as endpoint API within 5-10 mins. In the model packaging process, users are required to provide a Python deployment script, which defines how data is loaded in endpoint payload. Users can simply follow the deployment script example for their customized ML models. The deployment script examples are located in `deployment` directory.

## Model Flavor

In A360 AI, we currently support most of the commonly used ML frameworks, such as sklearn, tensorflow, and pytorch. Our `MDK` also requires the users to tell the system which model flavor they used to build their ML models, so `Starpack` can take care of the backend process to prepare the model to be serialized in the correct format. 

## Contributing

A360 AI Platform users are encourage to share their ML workflow examples with the community. If you are interested in contributing to add more business use case examples, please check out the Contributor Guide and follow the template to create new business use cases.



