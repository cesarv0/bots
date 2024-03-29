import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from simulation import SIMULATION

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
#
# p.setGravity(0, 0, -9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
#
# pyrosim.Prepare_To_Simulate(robotId)
#
# backLegSensorValues = np.zeros(1000)
# frontLegSensorValue = np.zeros(1000)
# targetAngles = np.linspace(0, 2 * np.pi, 1000)
# FrontLegMotorValues = c.FrontAmplitude * np.sin(c.FrontFrequency * targetAngles + c.FrontPhaseOffset)
#
# BackLegMotorValues = c.BackAmplitude * np.sin(c.BackFrequency * targetAngles + c.BackPhaseOffset)
#
# # np.save("data/BackLegMotorValues", BackLegMotorValues)
# # np.save("data/FrontLegMotorValues", FrontLegMotorValues)
# # exit()
#
# for _ in range(1_000):
#     p.stepSimulation()
#     backLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValue[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_BackLeg', controlMode=p.POSITION_CONTROL,
#                                 targetPosition=BackLegMotorValues[_], maxForce=50)
#     pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_FrontLeg', controlMode=p.POSITION_CONTROL,
#                                 targetPosition=FrontLegMotorValues[_], maxForce=50)
#     if _ % 100 == 0:
#         print(_)
#     time.sleep(1 / 60)
# np.save("backLegSensorValues", backLegSensorValues)
# np.save("data/FrontLegSensorValues", frontLegSensorValue)
# print("hello")
# p.disconnect()
simulation = SIMULATION()
simulation.RUN()

