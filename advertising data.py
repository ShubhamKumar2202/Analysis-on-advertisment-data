import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
To check whether the user will click on the ad or not

step1 - analysing using:-

    1) histogram of age
    2) create a joint plot  showing area of income vs age
    3) create a joint plot  showing the kde distribution of daily time spent on site  vs age
    4) create a joint plot of 'Daily Time Spent on Site'  vs 'Daily Internet Usage'
    5) create a pair plot with hue defined by the 'Clicked on Ad' column feature

step2- train test split,  and train the model using logistic regression
    1)split the data into training and testing set
    2)train and fit a logistic regression model on training set
    3)Predict and Evaluate some values

step3- get a classification report check the accuracy
        also evaluate the accuracy of a classification using confusion matrix 
"""
ad_data = pd.read_csv('advertising.csv')
# dataset from (https://www.kaggle.com/)
print(ad_data.head)
ad_data.info()
print(ad_data.describe)
# analysing data
sns.set_style('darkgrid')
ad_data['Age'].plot.hist(bins=30)
sns.jointplot(x='Age', y='Area Income', data=ad_data)
sns.jointplot(x='Age', y='Daily Time Spent on Site', data=ad_data, kind='kde', color='red')
sns.jointplot(x='Daily Time Spent on Site', y='Daily Internet Usage', data=ad_data, color='green')
sns.pairplot(data=ad_data, hue='Clicked on Ad')
plt.show()

# logistic regression
from sklearn.model_selection import train_test_split

X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']]
y = ad_data['Clicked on Ad']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# train the data
from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

# predict values for testing model
predictions = logmodel.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print("this is the classification report\n", classification_report(y_test, predictions))
print("this is the confusion matrix\n", confusion_matrix(y_test, predictions))
