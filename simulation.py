import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)                    # Set gravity
planeId = p.loadURDF("plane.urdf")          # Set floor
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")                      # Load wolrd

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(500)
frontLegSensorValues = np.zeros(500)

for t in range(500):                        # iteration for world simulation

    time.sleep(1/60)
    # print("Iteration number: ", t)
    p.stepSimulation()
    backLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link('BackLeg')     # set up back sensor
    frontLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link('FrontLeg')   # set up front  sensor
    # print(backLegTouch)  # printing the sensor values

np.save('data/BackSensor_data.npy', backLegSensorValues)
np.save('data/FrontaSensor_data.npy', frontLegSensorValues)

p.disconnect()
