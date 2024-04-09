import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, RepeatVector, TimeDistributed
from sklearn.metrics import mean_absolute_error, mean_squared_error

os.environ['TF_ENABLE_ONEDNN_OPTS'] = "0"
os.environ['CUDA_VISIBLE_DEVICES'] = "0"

# Завантаження та попередня обробка даних
df = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df[['Temp']])

# Функція для створення датасету
def create_dataset(data, n_past, n_future):
    X, y = [], []
    for i in range(n_past, len(data) - n_future +1):
        X.append(data[i-n_past:i, 0])
        y.append(data[i:i+n_future, 0])
    return np.array(X), np.array(y)

n_past = 14
n_future = 7
n_features = 1

X, y = create_dataset(scaled_data, n_past, n_future)
X = X.reshape((X.shape[0], X.shape[1], n_features))
y = y.reshape((y.shape[0], y.shape[1], n_features))

# Розділення даних
train_size = int(len(X) * 0.8)
val_size = int(len(X) * 0.1)
test_size = len(X) - train_size - val_size

X_train, y_train = X[:train_size], y[:train_size]
X_val, y_val = X[train_size:train_size+val_size], y[train_size:train_size+val_size]
X_test, y_test = X[train_size+val_size:], y[train_size+val_size:]

# Побудова моделі без використання Sequential API
inputs = Input(shape=(n_past, n_features))
lstm1 = LSTM(100, activation='relu', return_sequences=True)(inputs)
lstm2 = LSTM(100, activation='relu', return_sequences=False)(lstm1)
repeat_vector = RepeatVector(n_future)(lstm2)
lstm3 = LSTM(100, activation='relu', return_sequences=True)(repeat_vector)
output = TimeDistributed(Dense(1))(lstm3)
model = Model(inputs=inputs, outputs=output)

model.compile(optimizer='adam', loss='mse')
model.summary()

# Тренування моделі
model.fit(X_train, y_train, epochs=1000, validation_data=(X_val, y_val), verbose=2)

# Прогнозування
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions.reshape(-1, 1)).reshape(-1, n_future)
true_y_test = scaler.inverse_transform(y_test.reshape(-1, 1)).reshape(-1, n_future)

# Визначення та друк метрик
mape = np.mean(np.abs((true_y_test[:, 0] - predictions[:, 0]) / true_y_test[:, 0])) * 100
rmse = np.sqrt(mean_squared_error(true_y_test[:, 0], predictions[:, 0]))
ame = mean_absolute_error(true_y_test[:, 0], predictions[:, 0])

print(f"MAPE: {mape}, RMSE: {rmse}, AME: {ame}")

# Візуалізація результатів
plt.figure(figsize=(10, 6))
plt.plot(true_y_test[:, 0], label='True')
plt.plot(predictions[:, 0], label='Predicted')
plt.legend()
plt.show()
