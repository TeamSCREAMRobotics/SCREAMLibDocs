# SimUtil

`com.teamscreamrobotics.util.SimUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java) · **4 callables** · **1 exposed fields/types**

## Public and protected callables

### `public static DCMotorSim createDCMotorSim( DCMotor gearbox, double gearing, double JKgMetersSquaredMOI)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java#L18)*

Creates a `DCMotorSim` for the given gearbox and moment of inertia.

**Parameter `gearbox`:** the motor gearbox model
**Parameter `gearing`:** gear ratio (input/output)
**Parameter `JKgMetersSquaredMOI`:** moment of inertia at the mechanism in kg·m²

### `public static DCMotorSim createDCMotorSim( DCMotor gearbox, double gearing, double JKgMetersSquaredMOI, double positionStdDev, double velocityStdDev)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java#L33)*

Creates a `DCMotorSim` with measurement noise.

**Parameter `gearbox`:** the motor gearbox model
**Parameter `gearing`:** gear ratio (input/output)
**Parameter `JKgMetersSquaredMOI`:** moment of inertia at the mechanism in kg·m²
**Parameter `positionStdDev`:** standard deviation of position measurement noise (rotations)
**Parameter `velocityStdDev`:** standard deviation of velocity measurement noise (RPS)

### `public static FlywheelSim createFlywheelSim( DCMotor gearbox, double gearing, double JKgMetersSquaredMOI)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java#L53)*

Creates a `FlywheelSim` for the given gearbox and moment of inertia.

**Parameter `gearbox`:** the motor gearbox model
**Parameter `gearing`:** gear ratio (input/output)
**Parameter `JKgMetersSquaredMOI`:** moment of inertia at the flywheel in kg·m²

### `public static FlywheelSim createFlywheelSim( DCMotor gearbox, double gearing, double JKgMetersSquaredMOI, double positionStdDev, double velocityStdDev)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java#L68)*

Creates a `FlywheelSim` with measurement noise.

**Parameter `gearbox`:** the motor gearbox model
**Parameter `gearing`:** gear ratio (input/output)
**Parameter `JKgMetersSquaredMOI`:** moment of inertia at the flywheel in kg·m²
**Parameter `positionStdDev`:** standard deviation of position measurement noise (rotations)
**Parameter `velocityStdDev`:** standard deviation of velocity measurement noise (RPS)

## Exposed fields and types

### `public class SimUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java#L9)*

Convenience factory methods for creating WPILib simulation objects.
