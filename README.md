# Analysis-on-advertisment-data
This model predicts whether the user will click on an advertisment or not based off the feature of that user.Using  unsupervised learning algorithms (machine learning) and some  visualization tools 

# Dataset overview

<img width="688" alt="image" src="https://user-images.githubusercontent.com/88205480/169388901-db519670-b155-4bbf-849b-831811a1978c.png">

# Solution
  analysing using
     - histogram of age.
     - create a joint plot showing area of income vs age.
     - create a joint plot showing the kde distribution of daily time spent on site vs age
     - create a joint plot of 'Daily Time Spent on Site' vs 'Daily Internet Usage'
     - create a pair plot with hue defined by the 'Clicked on Ad' column feature step2
     - train test split, and train the model using logistic regression
     - split the data into training and testing set
     - train and fit a logistic regression model and decision tree on training set
     - Predict and Evaluate some values step3
     - get a classification report check the accuracy also evaluate the accuracy of a classification using confusion matrix
     - Compare the two algorithms and find the best algo


# Logistic Regression

<img width="464" alt="image" src="https://user-images.githubusercontent.com/88205480/169388019-3876c513-710c-499c-bf86-1f1b0488ffdd.png">


# Decision Tree

<img width="296" alt="image" src="https://user-images.githubusercontent.com/88205480/169387542-7e02943f-9ddc-4e89-9fcf-f54a3de36ac1.png">

# Conclusion
The obtained results showed the use value of both machine learning models. The Decision Tree model showed slightly better performance than the Logistic Regression model, but definitely, both models have shown that they can be very successful in solving classification problems.

The prediction results can certainly be changed by a different approach to data analysis. We encourage you to do your analysis from the beginning, to find new dependencies between variables and graphically display them. After that, create a new training set and a new test set. Let the training set contain a larger amount of data than in the article. Fit and evaluate your model. In the end, praise yourself in a comment if you get improved performances.
