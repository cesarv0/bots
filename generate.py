import pyrosim.pyrosim as pyrosim


# pos = [x, y, z(height)]
def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(
        name='Torso_BackLeg',
        parent="Torso",
        child="BackLeg",
        type="revolute",
        position=[1, 0, 1],
    )
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(
        name='Torso_FrontLeg',
        parent="Torso",
        child="FrontLeg",
        type="revolute",
        position=[2, 0, 1],
    )
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.End()


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[5, 5, 0], size=[1, 1, 1])
    pyrosim.End()


if __name__ == "__main__":
    Create_World()
    Create_Robot()
