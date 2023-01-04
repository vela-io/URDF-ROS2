from controller import Robot, Motor, DistanceSensor


robot = Robot()


timestep = int(robot.getBasicTimeStep())

#initialize motor
left_wheel = robot.getDevice("left_wheel")
right_wheel = robot.getDevice("right_wheel")

left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))

left_wheel.setVelocity(0.0)
right_wheel.setVelocity(0.0)

#initialize sensors

distance_sensor = robot.getDevice("distance_sensor")
print(distance_sensor)
# sensor.enable(TIME_STEP)


while robot.step(timestep) != -1:
    pass
    # print("Hello World")
    left_wheel.setVelocity(1)
    right_wheel.setVelocity(1)

