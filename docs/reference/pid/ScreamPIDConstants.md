# ScreamPIDConstants

`com.teamscreamrobotics.pid.ScreamPIDConstants`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java) · **49 callables** · **3 exposed fields/types**

## Competition usage

**2025:** [`ClimberConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/climber/ClimberConstants.java#L12), [`DrivetrainConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/drivetrain/DrivetrainConstants.java#L16), [`IntakeConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/intake/IntakeConstants.java#L13), [`ElevatorConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/elevator/ElevatorConstants.java#L15), [`WristConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/wrist/WristConstants.java#L19)

**2026:** [`DrivetrainConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/drivetrain/DrivetrainConstants.java#L6), [`IntakeConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/intake/IntakeConstants.java#L11), [`FlywheelConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/flywheel/FlywheelConstants.java#L9), [`HoodConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/hood/HoodConstants.java#L8)

## Public and protected callables

### `public FeedforwardConstants(double kV, double kS, double kG, double kA)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L21)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public FeedforwardConstants()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L25)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public ScreamPIDConstants()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L39)*

Creates a zeroed `ScreamPIDConstants` instance.

### `public ScreamPIDConstants(double p, double i, double d)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L48)*

Creates a `ScreamPIDConstants` with PID gains (F defaults to 0).

**Parameter `p`:** proportional gain
**Parameter `i`:** integral gain
**Parameter `d`:** derivative gain

### `public ScreamPIDConstants(double p, double i, double d, double f)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L62)*

Creates a `ScreamPIDConstants` with PIDF gains.

**Parameter `p`:** proportional gain
**Parameter `i`:** integral gain
**Parameter `d`:** derivative gain
**Parameter `f`:** feedforward gain

### `public void setPID(double p, double i, double d)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L70)*

Sets P, I, and D gains in place.

### `public void setPIDF(double p, double i, double d, double f)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L77)*

Sets P, I, D, and F gains in place.

### `public void setPeriod(double period)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L85)*

Sets the controller loop period in seconds (default `0.02`).

### `public void setP(double p)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L90)*

Sets the proportional gain.

### `public void setI(double i)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L95)*

Sets the integral gain.

### `public void setD(double d)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L100)*

Sets the derivative gain.

### `public void setF(double f)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L105)*

Sets the feedforward gain.

### `public void setIntegralZone(double Izone)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L110)*

Sets the integral zone — error must be within this bound for the integrator to accumulate.

### `public void setIntegralAccumulatorBounds(double max, double min)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L120)*

Sets the integrator accumulator clamp bounds.

**Parameter `max`:** upper bound on the accumulator
**Parameter `min`:** lower bound on the accumulator

### `public void setOutputBounds(double max, double min)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L131)*

Sets the controller output clamp bounds.

**Parameter `max`:** maximum output value
**Parameter `min`:** minimum output value

### `public ScreamPIDConstants withPID(double p, double i, double d)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L137)*

Sets P, I, D and returns `this` for chaining.

### `public ScreamPIDConstants withPIDF(double p, double i, double d, double f)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L145)*

Sets P, I, D, F and returns `this` for chaining.

### `public ScreamPIDConstants withPeriod(double period)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L154)*

Sets the loop period and returns `this` for chaining.

### `public ScreamPIDConstants withP(double p)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L160)*

Sets kP and returns `this` for chaining.

### `public ScreamPIDConstants withI(double i)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L166)*

Sets kI and returns `this` for chaining.

### `public ScreamPIDConstants withD(double d)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L172)*

Sets kD and returns `this` for chaining.

### `public ScreamPIDConstants withF(double f)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L178)*

Sets kF and returns `this` for chaining.

### `public ScreamPIDConstants withIntegralZone(double Izone)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L184)*

Sets the integral zone and returns `this` for chaining.

### `public ScreamPIDConstants withIntegralAccumulatorBounds(double max, double min)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L190)*

Sets the integral accumulator bounds and returns `this` for chaining.

### `public ScreamPIDConstants withOutputBounds(double max, double min)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L197)*

Sets the output bounds and returns `this` for chaining.

### `public double period()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L204)*

Returns the loop period in seconds.

### `public double kP()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L209)*

Returns the proportional gain.

### `public double kI()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L214)*

Returns the integral gain.

### `public double kD()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L219)*

Returns the derivative gain.

### `public double kF()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L224)*

Returns the feedforward gain.

### `public double integralZone()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L229)*

Returns the integral zone threshold.

### `public double maxIntegralAccumulator()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L234)*

Returns the upper bound on the integral accumulator.

### `public double minIntegralAccumulator()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L239)*

Returns the lower bound on the integral accumulator.

### `public double maxOutput()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L244)*

Returns the upper output clamp.

### `public double minOutput()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L249)*

Returns the lower output clamp.

### `public Slot0Configs getSlot0Configs(FeedforwardConstants ffConstants)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L258)*

Builds a `Slot0Configs` combining these PID gains with the given feedforward constants.

**Parameter `ffConstants`:** the feedforward gains and gravity type

### `public static ScreamPIDConstants fromSlot0Configs(Slot0Configs configs)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L276)*

Creates a `ScreamPIDConstants` from the PID portion of a `Slot0Configs`.

**Parameter `configs`:** the slot configs to extract P/I/D from

### `public Slot1Configs getSlot1Configs(FeedforwardConstants ffConstants)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L285)*

Builds a `Slot1Configs` combining these PID gains with the given feedforward constants.

**Parameter `ffConstants`:** the feedforward gains

### `public static ScreamPIDConstants fromSlot1Configs(Slot1Configs configs)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L302)*

Creates a `ScreamPIDConstants` from the PID portion of a `Slot1Configs`.

**Parameter `configs`:** the slot configs to extract P/I/D from

### `public Slot2Configs getSlot2Configs(FeedforwardConstants ffConstants)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L311)*

Builds a `Slot2Configs` combining these PID gains with the given feedforward constants.

**Parameter `ffConstants`:** the feedforward gains

### `public static ScreamPIDConstants fromSlot2Configs(Slot2Configs configs)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L328)*

Creates a `ScreamPIDConstants` from the PID portion of a `Slot2Configs`.

**Parameter `configs`:** the slot configs to extract P/I/D from

### `public PIDController getPIDController()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L333)*

Creates a WPILib `PIDController` from these constants.

### `public PIDController getPIDController(double minInput, double maxInput)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L343)*

Creates a WPILib `PIDController` with continuous input enabled over `[minInput, maxInput]`.

**Parameter `minInput`:** lower bound of the continuous input range
**Parameter `maxInput`:** upper bound of the continuous input range

### `public ProfiledPIDController getProfiledPIDController(Constraints constraints)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L354)*

Creates a WPILib `ProfiledPIDController` with the given motion constraints.

**Parameter `constraints`:** max velocity and acceleration for the motion profile

### `public ProfiledPIDController getProfiledPIDController( Constraints constraints, double minInput, double maxInput)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L365)*

Creates a WPILib `ProfiledPIDController` with constraints and continuous input.

**Parameter `constraints`:** max velocity and acceleration for the motion profile
**Parameter `minInput`:** lower bound of the continuous input range
**Parameter `maxInput`:** upper bound of the continuous input range

### `public PhoenixPIDController getPhoenixPIDController()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L373)*

Creates a CTRE `PhoenixPIDController` from these constants.

### `public PhoenixPIDController getPhoenixPIDController(double minInput, double maxInput)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L383)*

Creates a CTRE `PhoenixPIDController` with continuous input enabled.

**Parameter `minInput`:** lower bound of the continuous input range
**Parameter `maxInput`:** upper bound of the continuous input range

### `public boolean equals(ScreamPIDConstants other)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L390)*

Returns `true` if all gains and bounds in `other` are identical to this instance.

### `public ScreamPIDConstants clone()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L404)*

Returns a deep copy of these constants.

## Exposed fields and types

### `public class ScreamPIDConstants implements Cloneable`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L13)*

A container class for PID constants, along with additional methods.

### `public record MotionMagicConstants(double cruiseVelocity, double acceleration, int jerk)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L16)*

Motion Magic cruise velocity (rot/s), acceleration (rot/s²), and jerk (rot/s³) limits.

### `public record FeedforwardConstants( double kV, double kS, double kG, double kA, GravityTypeValue gravityType)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L19)*

Feedforward gains (kV, kS, kG, kA) plus the gravity model type for a TalonFX slot.
