# LogS Prediction Model

This project provides a machine learning model for predicting logS (aqueous solubility) values. The model utilizes a Random Forest Regressor trained on the Delaney solubility dataset.

## <span style="color: #007bff;">Purpose</span>

The model's sole function is to predict logS values based on input molecular descriptors. LogS, the logarithm of solubility, is a critical parameter in fields such as pharmaceutical research and environmental science.

## <span style="color: #28a745;">Functionality</span>

The model accepts the following molecular descriptors as input:

* <span style="color: #dc3545;">`MolLogP`</span> (lipophilicity)
* <span style="color: #ffc107;">`MolWt`</span> (molecular weight)
* <span style="color: #17a2b8;">`NumRotatableBonds`</span> (molecular flexibility)
* <span style="color: #6c757d;">`AromaticProportion`</span> (aromaticity)

It produces an estimated logS value as output.

## <span style="color: #007bff;">Methodology</span>

A Random Forest Regressor is trained on the Delaney dataset to establish a predictive relationship between the input descriptors and the target logS values. The trained model is then used to generate predictions for new descriptor sets.

## <span style="color: #28a745;">Output</span>

The project provides:

* <span style="color: #dc3545;">Model performance metrics</span> (MSE and R2).
* <span style="color: #ffc107;">A visualization</span> of predicted versus actual logS values.
* <span style="color: #17a2b8;">The predicted logS values</span> for given input data.

## <span style="color: #6c757d;">Limitations</span>

This model is specifically designed for logS prediction. Its applicability is limited to scenarios where logS estimation is required.

DATA CREDITS: dataprofessor, https://github.com/dataprofessor
