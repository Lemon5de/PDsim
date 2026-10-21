# 🤖 PDSim - Line Follower Robot PD Controller Simulator ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**PDSim** is a lightweight Python simulator that models the closed-loop mathematical behavior of a differential-drive line-following robot using Proportional-Derivative (PD) control logic.

---

## ✨ Features

- **Interactive CLI Input:** Configurable proportional gain ($K_p$), derivative gain ($K_d$), base PWM motor speed, initial track offset, and simulation run time.
- **Differential Drive Mechanics:** Calculates real-time left and right wheel PWM adjustments bounded between `0` and `255`.
- **Live Output Table:** Prints structured interval snapshots of simulation time, error values, PD output, and individual motor power levels.

---

## 🛠️ How It Works

1. **Error Calculation:** Evaluates offset distance from track center ($e = \text{center} - \text{position}$).
2. **PD Control Loop:**
   $$\text{Correction} = K_p \cdot e + K_d \cdot \frac{\Delta e}{dt}$$
3. **Inverse Kinematics & Motor Mapping:**
   ```text
   PWM_left  = clamp(base_speed - correction, 0, 255)
   PWM_right = clamp(base_speed + correction, 0, 255)
   ```
---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed (uses standard library modules only).

### Running the Simulator

1. Clone the repository:
   ```bash
   git clone [https://github.com/Lemon5de/PDsim.git](https://github.com/Lemon5de/PDsim.git)
   cd PDsim
   ```

2. Run the script:
   ```bash
   python PDsim.py
   ```

3. Follow the terminal prompts:
   ```text
   Enter Kp and Kd values separated by a space: 0.8 0.15
   Enter the base speed of your robot(PWM): 180
   Enter the initial offset of the robot (cm): 2.5
   Enter the Duration of the Sim (seconds): 5
   ```

---

## 📄 License 

This project is open-source and available under the [MIT License](LICENSE).


---

## 📜 Version History

See [CHANGELOG.md](CHANGELOG.md) for full details on releases and updates.
