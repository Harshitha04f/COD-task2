# COD-task2
Name: Bharthipudi Sri Harshitha  
ID: CT08PD419  
Domain: Data Science  
Duration: 4 weeks from 20th May 2024 to 20th June 2024  
Mentor: Sravani Gouni  

Description: The dataset appears to be related to car attributes and is likely used for predicting car prices or categories (e.g., good, acceptable, unacceptable). Each row represents a car, and the columns provide various attributes related to its features, specifications, and ratings. Below is a brief description of each column:

- Buying: The buying price of the car (e.g., low, medium, high, very high).
- Maint: The maintenance cost of the car (e.g., low, medium, high, very high).
- Doors: Number of doors in the car (e.g., 2, 3, 4, 5-more).
- Persons: The capacity of persons the car can carry (e.g., 2, 4, more).
- Lug_boot: The size of the luggage boot (e.g., small, medium, big).
- Safety: The safety rating of the car (e.g., low, medium, high).
- Class: The classification of the car (e.g., unacc, acc, good, vgood).

Data Loading and Cleaning:
1. Load the Car Dataset: Import the dataset into a pandas DataFrame.
2. Initial Data Cleaning: Handle missing values, ensure correct data types for each column, and preprocess categorical variables using encoding techniques.

Decision Tree Model:
1. Model Preparation:
   - Feature Selection: Select relevant features for predicting the car classification.
   - Data Splitting: Split the dataset into training and testing sets.
2. Model Training:
   - Training the Decision Tree: Use the training set to build a decision tree model using scikit-learn.
   - Hyperparameter Tuning: Optimize the decision tree parameters (e.g., max_depth, min_samples_split) to improve model performance.
3. Model Evaluation:
   - Performance Metrics: Evaluate the model using accuracy, precision, recall, and F1-score on the testing set.
   - Confusion Matrix: Visualize the confusion matrix to understand the model’s performance in classifying different car categories.

Visualization:
- Tree Visualization: Use tools like Graphviz to visualize the decision tree structure.
- Feature Importance: Plot the feature importance scores to understand the most influential features in the decision-making process.
- Performance Plots: Create plots to compare the performance of the decision tree model on training and testing sets.

Conclusion:
In this project, the decision tree model provides a comprehensive understanding of how different car attributes influence the car classification. The analysis highlights key factors such as buying price, maintenance cost, and safety rating that significantly impact the car's classification. By leveraging these insights, automotive companies and customers can make informed decisions regarding car purchases and categorization. Additionally, the decision tree model can serve as a predictive tool to assist in assessing car quality and value.
