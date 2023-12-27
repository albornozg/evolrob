import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load('data/BackSensor_data.npy')
frontLegSensorValues = np.load('data/FrontaSensor_data.npy')

# print(backLegSensorValues)

plt.plot(backLegSensorValues, label='Back Leg Sensor')
plt.plot(frontLegSensorValues, label='Front Leg Sensor')

plt.legend()
plt.show()
