import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)                    # Set gravity
planeId = p.loadURDF("plane.urdf")          # Set floor
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")                      # Load wolrd

pyrosim.Prepare_To_Simulate(robotId)        # preparation to simulate robot

# stating the sensors

backLegSensorValues = np.zeros(500)
frontLegSensorValues = np.zeros(500)

backleg_amplitude = math.pi/4
backleg_frequency = 10
backleg_phaseOffset = 0


frontleg_amplitude = math.pi/4
frontleg_frequency = 10
frontleg_phaseOffset = math.pi/4

backleg_targetAngles = backleg_amplitude*np.sin(np.linspace(0, 2*backleg_frequency*np.pi, 500)+backleg_phaseOffset)
frontleg_targetAngles = frontleg_amplitude*np.sin(np.linspace(0, 2*frontleg_frequency*np.pi, 500)+frontleg_phaseOffset)

np.save('data/backleg_targetAngles.npy', backleg_targetAngles)
np.save('data/frontleg_targetAngles.npy', frontleg_targetAngles)

# exit()
for t in range(500):                        # iteration for world simulation

    "Setting up..."

    time.sleep(1/60)
    print("Iteration number: ", t)
    p.stepSimulation()

    "Sensors"

    backLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link('BackLeg')     # set up back sensor
    frontLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link('FrontLeg')   # set up front  sensor
    # print(backLegTouch)  # printing the sensor values

    "Motors"

    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName="Torso_BackLeg",

        controlMode=p.POSITION_CONTROL,

        targetPosition=backleg_targetAngles[t],

        maxForce=50)

    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName="Torso_FrontLeg",

        controlMode=p.POSITION_CONTROL,

        targetPosition=frontleg_targetAngles[t],

        maxForce=50)

np.save('data/BackSensor_data.npy', backLegSensorValues)
np.save('data/FrontaSensor_data.npy', frontLegSensorValues)

p.disconnect()
