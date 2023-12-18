import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length, width, height = 1, 1, 1     # starting dimensions of the 1st cube/box
x, y, z = 0, 0, height/2            # position of the centroid of the 1st cube/box
number_cubes = 10

prev_length, prev_width, prev_height = length, width, height
new_z = 0
sum_heights = 0

for i in range(number_cubes):

    new_z = ((2 * sum_heights) + prev_height) / 2
    name = "Box{box_number}".format(box_number=(i + 1))
    pyrosim.Send_Cube(name=name, pos=[x, y, new_z], size=[prev_length, prev_width, prev_height])
    sum_heights = sum_heights + prev_height
    prev_length, prev_width, prev_height = prev_length*0.9, prev_width*0.9, prev_height*0.9


pyrosim.End()
