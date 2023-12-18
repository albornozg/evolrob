import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)                # Set gravity
planeId = p.loadURDF("plane.urdf")      # Set floor

p.loadSDF("boxes.sdf")                    # Load box

for t in range(500):

    time.sleep(1/60)
    print("Iteration number: ", t)
    p.stepSimulation()

p.disconnect()