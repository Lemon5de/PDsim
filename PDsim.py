# This is a bare bones simple PD simulator, which simulates the mathematical behavior of a system (specifically a line following robot)
# with given Kp, Kd, steering values, sim time, and the mass. This should help to give a rough idea.
# Written By 4k1l.k451r, Github : https://github.com/Lemon5de

# vars
Kp, Kd = map(float, input("Enter Kp and Kd values separated by a space: ").split())
print(f"Using Kp = {Kp}, Kd = {Kd} for the PD controller.")

min_steering, max_steering = map(float, input("Enter min and max steering values separated by a space: ").split())
print(f"Using min_steering = {min_steering}, max_steering = {max_steering} for the PD controller.")
last_error = 0.0
center_position = 0.0

# pd main func
def PD(position: float, dt: int):
    global last_error
    e = center_position - position
    p = Kp * e
    d = Kd * (e - last_error) / dt 
    pd = p + d
    last_error = e
    if max_steering != None and pd > max_steering: pd = max_steering
    if min_steering != None and pd < min_steering: pd = min_steering
    return pd


#  sim params

r_mass = float(input("Enter the mass of the robot (kg): "))
print(f"Using robot mass = {r_mass} kg for the simulation.")
r_position = float(input("Enter the initial position of the robot (cm): "))
print(f"Using initial robot position = {r_position} cm for the simulation.")
correction_velocity = 0.0 # in cm/s
dt = 0.05 # the tine interval iN seconds
time = int(input("Enter the Duration of the Sim (seconds, x lines per second you input) "))
steps = time / dt
print(f"{'Time (s)':<15} | {'Position':<15} | {'Error':<15} | {'PD Output':<15}")
print("-" * 70)

# main sim loop

for i in range(int(steps + 1)):
    sim_time = i * dt
    offset = r_position
    correction_force = PD(offset, dt) # calculating the correction

    # apply physics
    correction_acceleration = correction_force / r_mass # a = F/m
    correction_velocity += correction_acceleration * dt # v = a*t every second
    r_position += correction_velocity * dt # s = v*t every sencond

    #printing every 5 sec 
    if i % 20 == 0:
        error = center_position - offset
        print(f"{sim_time:<15.2f} | {offset:<15.2f} | {error:<15.2f} | {correction_force:<15.2f}")




