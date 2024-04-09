import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = "0"
os.environ['CUDA_VISIBLE_DEVICES'] = "0"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, RepeatVector,TimeDistributed, Dense

df = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")
print(df.head())
df.plot()

max_value = max(df['Temp'])
min_value = min(df['Temp'])

def normalize_data(data):
    return (data - min_value) / (max_value - min_value)

def denormalize_data(data):
    return data * (max_value - min_value) + min_value

normalized_df = normalize_data(df['Temp'])

n_features = 1
n_future = 7
n_past = 14

x = []
for i in range(len(normalized_df) - n_past - 1):
    window = normalized_df.iloc[i:i+n_past].to_numpy().reshape(-1, 1)
    x.append(window)
x = np.array(x)

y = []
for i in range(n_past, len(normalized_df)-n_future+1):
    window = normalized_df.iloc[i:i+n_future].to_numpy().reshape(-1, 1)
    y.append(window)
y = np.array(y)

train_size = 0.8
validation_size = 0.1
test_size = 0.1

indices = np.arange(min(len(x),len(y)))
np.random.shuffle(indices)
train_index = int(train_size * len(indices))
val_index = int((train_size + validation_size) * len(indices))

train_indices = indices[:train_index]
val_indices = indices[train_index:val_index]
test_indices = indices[val_index:]

x_train, y_train = x[train_indices], y[train_indices]
x_val, y_val = x[val_indices], y[val_indices]
x_test, y_test = x[test_indices], y[test_indices]

print("Number of samples in training set:", len(x_train))
print("Number of samples in validation set:", len(x_val))
print("Number of samples in test set:", len(x_test))

print(x_train.shape)
print(x_test.shape)
print(x_val.shape)

print(y_train.shape)
print(y_test.shape)
print(y_val.shape)


batch_size = x_train.shape[0]
epochs = 1000
hidden_layer = 100

model = Sequential()
model.add(LSTM(100, activation='relu', input_shape=(n_past, n_features), return_sequences=True))
model.add(LSTM(100, activation='relu', return_sequences=False))
model.add(RepeatVector(n_future))
model.add(LSTM(100, activation='relu', return_sequences=True))
model.add(LSTM(100, activation='relu', return_sequences=True))
model.add(TimeDistributed(Dense(1)))
model.compile(optimizer='adam', loss='mse')
model.summary()

history = model.fit(x_train, y_train, epochs=epochs, validation_data=(x_test, y_test))

plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss over Time')
plt.legend()
plt.show()

predictions = []
for i, x in enumerate(x_val):
    x = x.reshape(1, n_past, 1)
    predicted = denormalize_data(model.predict(x)).flatten()
    predictions.append(predicted)
    real = denormalize_data(y_val[i].flatten())

    print(f"MAPE: {np.mean(np.abs((real - predicted) / real)) * 100}")
    print(f"RMSE: {np.sqrt(np.mean((real - predicted) ** 2))}")
    print(f"AME: {np.mean(np.abs(real - predicted))}")

    plt.plot(predicted, label='Predicted Data')
    plt.plot(real, label='Real Data')
    plt.xlabel('Time Step')
    plt.ylabel('Number of Temp')
    plt.legend()
    plt.show()

sales_values = denormalize_data(normalize_data(df['Temp'].values))
predicted_values = []

for i, p in enumerate(predictions):
    index = val_indices[i] + n_past
    x_values = [j for j in range(index,index+n_future)]
    plt.figure(figsize=(10, 6))
    plt.plot(sales_values)
    plt.plot(x_values,p, label=f"Prediction {i}")
    plt.plot(x_values,denormalize_data(y_val[i].flatten()), label=f"Actual data {i}")
    plt.xlabel('Time Step')
    plt.ylabel('Number of Temp')
    plt.title('All Data and Predictions')
    plt.legend()
    plt.show()

plt.figure(figsize=(10, 6))
plt.plot(sales_values)
for i, p in enumerate(predictions):
    index = val_indices[i] + n_past
    x_values = [j for j in range(index,index+n_future)]
    plt.plot(x_values,p, label=f"Prediction {i}", color="red")
    plt.plot(x_values,denormalize_data(y_val[i].flatten()), label=f"Actual data {i}", color="green")

plt.xlabel('Time Step')
plt.ylabel('Number of Temp')
plt.title('All Data and Predictions')
plt.legend()
plt.show()
plt.figure(figsize=(10, 6))
plt.plot(sales_values)

input = normalize_data(np.array(sales_values[-15:]).reshape(1,-1,1))
y_prediction = denormalize_data(model.predict(input)).flatten()
x_prediction = [len(sales_values) + i for i in range(7)]
plt.plot(x_prediction,y_prediction)

input = normalize_data(np.array([*sales_values[-8:], *y_prediction]).reshape(1,-1,1))
y_prediction = denormalize_data(model.predict(input)).flatten()
x_prediction = [len(sales_values) + i for i in range(7,14)]
plt.plot(x_prediction,y_prediction)

plt.xlabel('Time Step')
plt.ylabel('Number of Temp')
plt.title('Predictions')
plt.show()
