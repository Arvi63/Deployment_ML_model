# End to End Project with Deployment ML model
## This is House Rent Prediction Project

# Steps 
1. Acquring the data
    Dataset: https://drive.google.com/file/d/1oMeyn00HwinB1YrGvYIrwHAVheVcZYS5/view

2. Data cleaning and preprocessing
    In this repo there are 2 notebooks: preprocess.ipynb and eda_and_model.ipynb
    
    **Preprocess.ipynb** : In this notebook all the missing values are imputed for various features using various techniques. The unwanted features are also removed from   the dataset. And the categorical features are also converted into numerical features as number of features was very high.
    
    **eda_and_model.ipynb** : In this notebook, we analyze and data and remove the various outliers from the many features and modeling is also done. Here we have used Linear Regression , KNN and Random Forest as Machine Learning models. Here more other robust model can be used, since those model size can be very high and it will cause meomory issue while deploying I stayed these models.
    
    Evaluation : The evaluation metric used is R^2 . R^2 value ranges to maximum of 1, so it is easy to interpret. If R^2 value is 0, then the model is as simple average model(model which gives only mean value for every input), less than 0 is worst than mean model and 1 represents the best model.
    
    There are comments in all portion of code so following the code wont be difficult.
    
    **Note**: For deploying I have used the Linear Regression model though other performed better as this model has lowest model size.
    
3. Deployment
      Deployment is done using Fastapi in Heroku
      Heroku gives limited free cloud space ,so it one of the best platform to start for begineers. And it is very simple to use as well.

  You can access the deployed application from this link: https://house-rent-pred.herokuapp.com/


# External Resources
For Fastapi  :   https://amitness.com/2020/06/fastapi-vs-flask/

For Regression EDA : https://blog.exploratory.io/a-practical-guide-of-exploratory-data-analysis-with-linear-regression-part-1-9f3a182d7a92

For deployment :  https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99
