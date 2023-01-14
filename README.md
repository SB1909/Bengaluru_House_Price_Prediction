# Link for application: https://bhp-predictions.el.r.appspot.com

# Bengaluru_House_Price_Prediction End to End Project.

The real estate markets in Bangalore / Bengaluru, present an interesting opportunity for data analysts to analyze and predict where property prices are moving towards. Prediction of property prices is becoming increasingly important and beneficial. Property prices are a good indicator of both the overall market condition and the economic health of a country. Considering the data provided, we are wrangling a large set of property sales records stored in an unknown format and with unknown data quality issues.

Buying a home, especially in a city like Bengaluru, is a tricky choice. While the major factors are usually the same for all metros, there are others to be considered for the Silicon Valley of India. With its help millennial crowd, vibrant culture, great climate and a slew of job opportunities, it is difficult to ascertain the price of a house in Bengaluru.


# Stpes:
## 1. Collection of data:
We will use dataset provided on kaggle.

Link for dataset: https://www.kaggle.com/datasets/abhinaykumarsingh/bengaluru-house-price-data

## 2. Creating Virtual Environment in VS Code for programming:
Install all libraries required for training.

## 3. Data cleaning, Analysis, Preprocessing:
We will deep dive through data and then clean all the data, remove unnecessory variables (punctuations, spaces, words), unnecessory columns from data and will make it ready for further analysis.

Then handle missing data and outliers using various techniques. Plot various graphs, charts to make further analysis and draw some intutions from them and take necessory actions.

Handle categorical data split it into training and testing sets, use scaling and make it ready to feed it into ML model.

## 4. ML Model Development:
Use Random Forest Regressor, Ridge, Linear Regression, XGB Regressor model and find out accuracy for each model.

## 5. Optimising model:
Select best performing model and tune it by optimising its hyperparameter.

In this we select XGB Regressor as our final model.

Save final model with pipeline using pickle to use it for prediction anywhere.

Also save other necessory files.

## 6. Creating application for end use of model (server and UI file):
We will use Flask server to create application and html file for front end.

First we will test our model in local host.

## 7. Deploy model in production using cloud:

Now we will deploy our model into production.

Here I choose Google Cloud Platform to deploy this model. (Standard Environment)

Create necesorry files and rename it as per GCP's requirement (yaml, requirements files)
