import os
import random
import time

import numpy as np

import constants as c
import pyrosim.pyrosim as pyrosim


class SOLUTION:
    def __init__(self, id):
        self.myID = id

        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1

    def Evaluate(self, mode):
        pass

    def Start_Simulation(self, mode):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py {0} {1}".format(mode, self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness{0}.txt".format(self.myID)):
            time.sleep(.01)
        fitnessFile = open("fitness{0}.txt".format(self.myID), "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
        os.system("del fitness{0}.txt".format(self.myID))

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomCol = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow][randomCol] = random.random() * 2 - 1
        # self.weights[randomRow] = np.random.rand(1, c.numMotorNeurons) * 2 - 1

    def Set_ID(self, new):
        self.myID = new

    def Create_World(self):
        while not os.path.exists("world.sdf"):
            time.sleep(0.01)
            pyrosim.Start_SDF("world.sdf")
            pyrosim.Send_Cube(name="Box", pos=[5, 5, 0.5], size=[1, 1, 1])
            pyrosim.End()

    def Generate_Body(self):
        while not os.path.exists("body.urdf"):
            time.sleep(0.01)
            pyrosim.Start_URDF("body.urdf")
            pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 2.5, 1])

            # Points in positive diagonal direction opposite (-y)
            pyrosim.Send_Joint(
                name="Torso_BackLeg",
                parent="Torso",
                child="BackLeg",
                type="revolute",
                position=[-0.5, 0.2, 1],
                jointAxis="1 0 0"
            )
            pyrosim.Send_Cube(name="BackLeg", pos=[-0.1, 0.4, 0], size=[0.2, 0.8, 0.2])

            # Points in positive diagonal direction (+y)
            pyrosim.Send_Joint(
                name="Torso_FrontLeg",
                parent="Torso",
                child="FrontLeg",
                type="revolute",
                position=[-0.5, -0.2, 1],
                jointAxis="1 0 0"
            )
            pyrosim.Send_Cube(name="FrontLeg", pos=[-0.1, -0.4, 0], size=[0.2, 0.8, 0.2])

            # Points in negative diagonal direction (-x)
            pyrosim.Send_Joint(
                name="Torso_LeftLeg",
                parent="Torso",
                child="LeftLeg",
                type="revolute",
                position=[0.5, 0.2, 1],
                jointAxis="1 0 0"
            )
            pyrosim.Send_Cube(name="LeftLeg", pos=[0.1, 0.4, 0], size=[0.2, 0.8, 0.2])

            # Points in negative diagonal direction opposite (+x)
            pyrosim.Send_Joint(
                name="Torso_RightLeg",
                parent="Torso",
                child="RightLeg",
                type="revolute",
                position=[0.5, -0.2, 1],
                jointAxis="1 0 0"
            )
            pyrosim.Send_Cube(name="RightLeg", pos=[0.1, -0.4, 0], size=[0.2, 0.8, 0.2])

            pyrosim.Send_Joint(
                name="FrontLeg_FrontLowerLeg",
                parent="FrontLeg",
                child="FrontLowerLeg",
                type="revolute",
                position=[-0.1, -0.7, -0.1],
                jointAxis="1 0 0"
            )
            pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.4], size=[0.2, 0.2, 0.8])

            pyrosim.Send_Joint(
                name="BackLeg_BackLowerLeg",
                parent="BackLeg",
                child="BackLowerLeg",
                type="revolute",
                position=[-0.1, 0.7, -0.1],
                jointAxis="1 0 0"
            )
            pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.4], size=[0.2, 0.2, 0.8])

            pyrosim.Send_Joint(
                name="LeftLeg_LeftLowerLeg",
                parent="LeftLeg",
                child="LeftLowerLeg",
                type="revolute",
                position=[0.1, 0.7, -0.1],
                jointAxis="1 0 0"
            )
            pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.4], size=[0.2, 0.2, 0.8])
            #
            pyrosim.Send_Joint(
                name="RightLeg_RightLowerLeg",
                parent="RightLeg",
                child="RightLowerLeg",
                type="revolute",
                position=[0.1, -0.7, -0.1],
                jointAxis="1 0 0"
            )
            pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.4], size=[0.2, 0.2, 0.8])

            pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain{0}.nndf".format(self.myID))
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")

        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_RightLowerLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentCol in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentCol + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentCol])

        pyrosim.End()