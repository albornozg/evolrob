import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)                # Set gravity
planeId = p.loadURDF("plane.urdf")      # Set floor
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")                    # Load wolrd

for t in range(500):

    time.sleep(1/60)
    print("Iteration number: ", t)
    p.stepSimulation()

p.disconnect()