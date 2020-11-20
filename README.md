# UCI Data Analytics Final Project
### Vishal Patel, Stephen Chu, Saburo Nakano, Steve Thorne

## NBA Prediction Project
The aim of the project is to see if given data of players in the NBA and their stats, could we determine the type of success a player will have in the NBA based on PER, or player efficiency  rating. To do this, we took the data, found here: https://www.kaggle.com/drgilermo/nba-players-stats and filtered and transformed it. To view that, look at Data-Cleanup.ipynb. The resulting csv was then stored in Amazon S3, not included locally in the Github repo. Then using 3 machine learning models, Random Forest Classification, Support Vector Machine, and Deep Learning, we were able to create 3 models to choose from that predicts player efficiency based on inputted stats. We used Random Forest from sklearn, SVM from sklearn, and finall Deep Learning from Tensorflow. All included in the predict page of the application.


## Notebooks and Prep Work:

Data-Cleanup.ipynb. includes how ETL was done from the dataset, and that resulting csv was uploaded to s3.SVM_Model.ipynb, Random_Forest_Model.ipynb, and Deep_Learning_Model.ipynb are all where the training and saving of models are done, named accordingly. These notebooks also show how the s3 data is received.
Finally the models are saved as Random_Forest_Model.sav, SVM_Model.sav, and Deep_Learning_Model.h5. 



## Flask Routes
#### All routes found in app python file. Follows standard format used in flask
 (/) is the home page using index.html 

(/predict) leads to the predict.html predict page. Just so that the user can input data and submit a button

(/predictinput) is where the inputted forms are taken and ran through the models. Then depending on the selected model, a prediction is given. Most of the work here is in the python route. This leads back to the predict.html page with the new parameters. To get new parameters we were helped by this page
found: https://www.kdnuggets.com/2020/05/build-deploy-machine-learning-web-app.html

(/overview) leads to the project overview page in overview.html. Just a general overview of what the project is about and the steps we took.

(/data) leads to the data page in data.html, first talking about what the data looks like in terms of each category, then going more in depth of trends found in the data. This is done in Tableau.

(/model) leads to the modelOverview.html model overview page. This page explains all 3 of the models in detail, and compares each one.

(/NBAData) is a route that reads the data from S3. Then it jsonifies it, and returns the json. Used in the data page.
