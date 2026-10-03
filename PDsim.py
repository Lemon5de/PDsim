# This is a bare bones simple PD simulator, which simulates the mathematical behavior of a system (specifically a line following robot)
# with given Kp, Kd, sim time.This should help to give a rough idea.
# Written By 4k1l.k451r, Github : https://github.com/Lemon5de

# consts

MAX_PWM = 255   
RAND_SCALING_FACT = 0.2

# vars
Kp, Kd = map(float, input("Enter Kp and Kd values separated by a space: ").split())
print(f"Using Kp = {Kp}, Kd = {Kd} for the PD controller.")

# base speed input validation
base_speed = 0
yes = False
while not yes:
    base_speed = int(input("Enter the base speed of your robot(PWM): "))
    if base_speed > 255:
        print("Invalid base speed given")
        yes = False
    else:
        yes = True
        
last_error = 0.0
center_position = 0.0

# pd main func
def PD(position: float, dt: float):
    global last_error
    e = center_position - position
    p = Kp * e
    d = Kd * (e - last_error) / dt 
    pd = p + d
    last_error = e
    return pd,e


#  sim params
offset = float(input("Enter the initial offset of the robot (cm): "))
print(f"Using initial robot offset = {offset} cm for the simulation.")
dt = 0.05 # the time interval in seconds
time = int(input("Enter the Duration of the Sim (seconds, x lines per second you input) "))
steps = int(time / dt)
print(f"{'Time (s)':<15} | {'Position':<15} | {'Error':<15} | {'PD Output':<15} | {'Lspeed':<15} | {'Rspeed':<15}")
print("-" * 100)

# main sim loop

for i in range(int(steps + 1)):
    sim_time = i * dt
    correction,e = PD(offset, dt) # calculating the correction, treated as force in Newtons (N) for the simulation, which is applioed to the robot as a correction

    # inverse kinematics
    left_pwm = max(0, min((base_speed - correction), MAX_PWM))
    right_pwm = max(0, min((base_speed + correction), MAX_PWM))

    # reduction of the offset based on an arbritrary scaling factor(WILL BE REPLACED BY PHYSICAL PROPERTIES)
    diff = left_pwm - right_pwm
    offset -= diff * RAND_SCALING_FACT * dt

    #printing every 1 sec 
    if i % int(1/dt) == 0:
        print(f"{sim_time:<15.2f} | {offset:<15.2f} | {e:<15.2f} | {correction:<15.2f} | {left_pwm:<15.2f} | {right_pwm:<15.2f}")




