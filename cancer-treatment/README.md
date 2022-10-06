# Use Case: Cancer treatment prediction

## Introduction

Personalized medicine is a common use case in healthcare. Once sequenced, a cancer tumor can have thousands of genetic mutations. But the challenge is distinguishing the mutations that contribute to tumor growth (drivers) from the neutral mutations (passengers). Currently this interpretation of genetic mutations is being done manually. This is a very time-consuming task where a clinical pathologist has to manually review and classify every single genetic mutation based on evidence from text-based clinical literature.

## Goal

The general goal for this use case is to accurately classifiy the genetic variations, which automates the current time-consuming manual reiew process that performed by human specialists (i.e. clinical pathologists).

## Dataset

The dataset used here is from [2017 Kaggle competition](https://www.kaggle.com/competitions/msk-redefining-cancer-treatment/overview). The data were provided by Memorial Sloan Kettering Cancer Center (MSKCC). 

Both, training and test, data sets are provided via two different files. One (training/test_variants) provides the information about the genetic mutations, whereas the other (training/test_text) provides the clinical evidence (text) that our human experts used to classify the genetic mutations. Both are linked via the ID field. Therefore the genetic mutation (row) with ID=15 in the file training_variants, was classified using the clinical evidence (text) from the row with ID=15 in the file training_text

Details of each file descriptions can be found [here](https://www.kaggle.com/competitions/msk-redefining-cancer-treatment/data).

## Model type

Classification.

## Model flavor built for this use case

Sklearn (Random Forest).

## [NEW]
A360 AI community edition is now available. You can get free compute to train, test, and deploy your machine learning (ML) models. You can try out A360 AI's fast ML deployment and power model experiment tracking. Sign up [here](https://andromeda360.ai/community-edition/).
