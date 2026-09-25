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
def PD(position: float, dt: float):
    global last_error
    e = center_position - position
    p = Kp * e
    d = Kd * (e - last_error) / dt 
    pd = p + d
    last_error = e
    if max_steering != 0 and pd > max_steering: pd = max_steering
    if min_steering != 0 and pd < min_steering: pd = min_steering
    return pd


#  sim params
mass_grams = float(input("Enter the mass of the robot (grams): "))
r_mass = mass_grams / 1000.0  # to take into SI units (kg)
print(f"Using robot mass = {r_mass} kg for the simulation.")
pos_cm = float(input("Enter the initial position of the robot (cm): "))
r_position = pos_cm / 100.0  # to take into SI units (m)
print(f"Using initial robot position = {r_position} m for the simulation.")
correction_velocity = 0.0 # in m/s
dt = 0.05 # the time interval in seconds
time = int(input("Enter the Duration of the Sim (seconds, x lines per second you input) "))
steps = time / dt
print(f"{'Time (s)':<15} | {'Position':<15} | {'Error':<15} | {'PD Output':<15}")
print("-" * 70)

# main sim loop

for i in range(int(steps + 1)):
    sim_time = i * dt
    offset = r_position
    correction_force = PD(offset, dt) # calculating the correction, treated as force in Newtons (N) for the simulation, which is applioed to the robot as a correction

    # Applying Physics
    correction_acceleration = correction_force / r_mass # (F = ma -> a = F/m) m/s^2
    correction_velocity += correction_acceleration * dt # (v = a*t) m/s
    r_position += correction_velocity * dt # (s = v*t)m

    #printing every 1 sec 
    if i % 1 == 0:
        error = center_position - offset
        print(f"{sim_time:<15.2f} | {offset:<15.2f} | {error:<15.2f} | {correction_force:<15.2f}")




