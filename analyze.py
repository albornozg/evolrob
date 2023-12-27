import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/BackSensor_data.npy')
frontLegSensorValues = np.load('data/FrontaSensor_data.npy')
backleg_targetAngles = np.load('data/backleg_targetAngles.npy')
frontleg_targetAngles = np.load('data/frontleg_targetAngles.npy')

# print(backLegSensorValues)

# plt.plot(backLegSensorValues, label='Back Leg Sensor')
# plt.plot(frontLegSensorValues, label='Front Leg Sensor')
plt.plot(backleg_targetAngles, label='Back leg Target Angles')
plt.plot(frontleg_targetAngles, label='Front leg Target Angles')

plt.legend()
plt.show()
