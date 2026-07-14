# SimWrapper

`com.teamscreamrobotics.sim.SimWrapper`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java) · **10 callables** · **1 exposed fields/types**

## Competition usage

**2025:** [`IntakeConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/intake/IntakeConstants.java#L15), [`ElevatorConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/elevator/ElevatorConstants.java#L17), [`WristConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/wrist/WristConstants.java#L21)

**2026:** [`IntakeConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/intake/IntakeConstants.java#L14)

## Public and protected callables

### `public SimWrapper(DCMotorSim sim)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L36)*

Wraps a `DCMotorSim`. Position and velocity are scaled by the model's internal gearing
to produce rotor rotations/RPS. Use the explicit-gearing overload if `sim` was built
with `gearing = 1.0` and gearing is tracked separately.

**Parameter `sim`:** the DC motor simulation model

### `public SimWrapper(DCMotorSim sim, double gearing)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L50)*

Wraps a `DCMotorSim` with an explicit gear ratio. Use this when the sim model was
constructed with `gearing = 1.0` and the ratio is tracked in `TalonFXSubsystemSimConstants`.

**Parameter `sim`:** the DC motor simulation model
**Parameter `gearing`:** gear ratio from mechanism to motor (motor rotations per mechanism rotation)

### `public SimWrapper(ElevatorSim sim, Length spoolCircumference, double gearing)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L65)*

Wraps an `ElevatorSim`. Position and velocity are converted from meters to rotations/RPS
using the spool circumference and gear ratio.

**Parameter `sim`:** the elevator simulation model
**Parameter `spoolCircumference`:** circumference of the elevator spool
**Parameter `gearing`:** gear ratio between motor and spool

### `public SimWrapper(SingleJointedArmSim sim, double gearing)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L79)*

Wraps a `SingleJointedArmSim`. Position and velocity are converted from radians to
rotations/RPS using the gear ratio.

**Parameter `sim`:** the arm simulation model
**Parameter `gearing`:** gear ratio between motor and arm joint

### `public SimWrapper(FlywheelSim sim)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L92)*

Wraps a `FlywheelSim`. Position always returns `0.0`; velocity is in RPS scaled
by the model's internal gearing. Use the explicit-gearing overload if the model gearing is 1.0.

**Parameter `sim`:** the flywheel simulation model

### `public SimWrapper(FlywheelSim sim, double gearing)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L106)*

Wraps a `FlywheelSim` with an explicit gear ratio. Use this when the sim model was
constructed with `gearing = 1.0` and the ratio is tracked in `TalonFXSubsystemSimConstants`.

**Parameter `sim`:** the flywheel simulation model
**Parameter `gearing`:** gear ratio from mechanism to motor

### `public void update(double deltaTime)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L114)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public void setInputVoltage(double inputVoltage)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L119)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public double getPosition()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L124)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public double getVelocity()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L129)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

## Exposed fields and types

### `public class SimWrapper implements SimInterface`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L17)*

Adapts WPILib simulation models (`DCMotorSim`, `ElevatorSim`, etc.) to the
`SimInterface` contract, normalizing position and velocity to rotations / rotations-per-second.
