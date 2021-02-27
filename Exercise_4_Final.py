# Import the neccesary modules

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from scipy import stats

# Create the function to calculate MSE
def caluclate_mse(x, y):
    summation = 0  #variable to store the summation of differences
    n = len(y) #finding total number of items in list
    for i in range (0,n):  #looping through each element of the list
      difference = x[i] - y[i]  #calculating the difference between observed and predicted value
      squared_difference = difference**2  #taking square of the differene
      summation = summation + squared_difference  #taking a sum of all the differences
    MSE = summation/n  #dividing summation by total values to obtain average
    print ("The Mean Squared Error is: " , MSE)


# Read in the data

portland_data = pd.read_csv('portland_clean.csv')

# Normalize the data

portland_data['prices'] = portland_data['prices'] /1000
portland_data['sqft'] = portland_data['sqft']/1000

# Build the model
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[3])])

model.compile(optimizer='sgd', loss='mean_squared_error')

# Process the data

xhp1 = portland_data['no_beds'].to_numpy(dtype=float) # Bedrooms
xhp2 = portland_data['sqft'].to_numpy(dtype=float)# Square feet
xhp3 = portland_data['baths'].to_numpy(dtype=float) # bathrooms
xhp = np.stack([xhp1,xhp2, xhp3], axis=1) # Stack the data
yhp = portland_data['prices'].to_numpy(dtype=float) #prices

# Fit the model
model.fit(xhp, yhp, epochs=500)

# Create the model predictions
prediction = model.predict(xhp)
prediction_df = pd.DataFrame(prediction)
portland_data[['prediction']]= prediction_df

# Create a column to determine over or under prediction
portland_data[['Difference']] =portland_data['prices']-portland_data['prediction']

# Top 10 over predictions
over_pred = portland_data.sort_values(by = 'Difference').head(10)

# Top 10 under predictions
under_pred = portland_data.sort_values(by = 'Difference', ascending=False).head(10)

#Top 10 most accurate predictions
abs_portland_data = portland_data.copy()
abs_portland_data['Difference'] = abs_portland_data['Difference'].abs()
acc_resul = abs_portland_data.sort_values(by ='Difference').head(10)

# Calculate over prediction
caluclate_mse(over_pred['prices'].to_numpy(dtype=float), over_pred['prediction'].to_numpy(dtype=float))

# Calculate under prediction
caluclate_mse(under_pred['prices'].to_numpy(dtype=float), under_pred['prediction'].to_numpy(dtype=float))

# Calculate the most accurate
caluclate_mse(acc_resul['prices'].to_numpy(dtype=float), acc_resul['prediction'].to_numpy(dtype=float))

# Calculate the percentiles for the most accurate prediction
#Lower bound
print(stats.percentileofscore(portland_data['prices'].to_numpy(dtype=float), acc_resul['prices'].min()))
#Upper bound
print(stats.percentileofscore(portland_data['prices'].to_numpy(dtype=float), acc_resul['prices'].max()))

