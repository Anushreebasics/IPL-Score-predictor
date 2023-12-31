# Importing essential Libraries
import pandas as pd
import pickle


# Loading the dataset
df=pd.read_csv("C:\\Users\\kamal\\Downloads\\ipl.csv")

#------Data Cleaning --------
# removing unwanted columns
columns_to_remove=['mid','venue','batsman','striker','non-striker']
df.drop(labels=columns_to_remove, axis=1, inplace=True)

print(df['bat_team'].unique())

# keeping only the teams which are still available
current_teams = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
       'Mumbai Indians', 'Kings XI Punjab',
       'Royal Challengers Bangalore', 'Delhi Daredevils', 'Sunrisers Hyderabad']

# filtering out from batting and bowling teams
df = df[(df['bat_team'].isin(current_teams)) & (df['bowl_team'].isin(current_teams))]

# Removing the first 5 overs data in every match
df = df[df['overs']>=5.0]

# converting the column 'date' from string to datatime object
from datetime import datetime
df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

# Data preprocessing
# converting categorical features using OneHotEncoding method
encoded_df = pd.get_dummies(data=df, columns=['bat_team','bowl_team'])

# Rearranging the columns
encoded_df = encoded_df[['date', 'bat_team_Chennai Super Kings', 'bat_team_Delhi Daredevils', 'bat_team_Kings XI Punjab',
              'bat_team_Kolkata Knight Riders', 'bat_team_Mumbai Indians', 'bat_team_Rajasthan Royals',
              'bat_team_Royal Challengers Bangalore', 'bat_team_Sunrisers Hyderabad',
              'bowl_team_Chennai Super Kings', 'bowl_team_Delhi Daredevils', 'bowl_team_Kings XI Punjab',
              'bowl_team_Kolkata Knight Riders', 'bowl_team_Mumbai Indians', 'bowl_team_Rajasthan Royals',
              'bowl_team_Royal Challengers Bangalore', 'bowl_team_Sunrisers Hyderabad',
              'overs', 'runs', 'wickets', 'runs_last_5', 'wickets_last_5', 'total']]

# splitting the data into train and test set
X_train = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year <= 2016]
X_test = encoded_df.drop(labels='total', axis=1)[encoded_df['date'].dt.year >= 2017]

y_train = encoded_df[encoded_df['date'].dt.year <= 2016]['total'].values
y_test = encoded_df[encoded_df['date'].dt.year >= 2017]['total'].values

# removing the date column
X_train.drop(labels='date', axis=True, inplace=True)
X_test.drop(labels='date', axis=True, inplace=True)

#-----MOdel Building-------
# Linear Regression Model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# Creating a pickle file for classifier
filename = 'first-innings-score-lr-model-pk1'
pickle.dump(regressor, open(filename, 'wb'))

import joblib

# Save the model
filename = 'first-innings-score-lr-model.joblib'
joblib.dump(regressor, filename)
