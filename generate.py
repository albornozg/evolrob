import pyrosim.pyrosim as pyrosim


def Create_World():

    pyrosim.Start_SDF("world.sdf")

    length, width, height = 1, 1, 1
    x, y, z = 10, 10, height / 2
    pyrosim.Send_Cube(name='box', pos=[x, y, z], size=[length, width, height])

    pyrosim.End()


Create_World()


def Create_Robot():

    pyrosim.Start_URDF("body.urdf")

    length, width, height = 1, 1, 1
    x, y, z = 1.5, 0, 1.5

    pyrosim.Send_Cube(name='Torso', pos=[x, y, z], size=[length, width, height])                                # torso

    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])    # joint

    pyrosim.Send_Cube(name='BackLeg', pos=[-0.5, 0, -0.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])

    pyrosim.Send_Cube(name='FrontLeg', pos=[0.5, 0, -0.5], size=[length, width, height])

    pyrosim.End()


Create_Robot()

