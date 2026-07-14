# PigeonHelper

`com.teamscreamrobotics.drivers.PigeonHelper`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java) · **7 callables** · **1 exposed fields/types**

## Public and protected callables

### `public PigeonHelper(Pigeon2 pigeon)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L20)*

Creates a helper wrapping the given Pigeon2 and caches its angular velocity signals.

**Parameter `pigeon`:** the Pigeon2 IMU to wrap

### `public double getVelocityX()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L30)*

Get the angular velocity around the X axis in degrees per second

### `public double getVelocityY()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L38)*

Get the angular velocity around the Y axis in degrees per second

### `public double getVelocityZ()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L46)*

Get the angular velocity around the Z axis (yaw rate) in degrees per second

### `public double[] getAllVelocities()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L55)*

Get all velocity values at once
Returns array: [velocityX, velocityY, velocityZ]

### `public double getYawRate()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L71)*

Get the yaw rate (most commonly used for drivetrain)

### `public double getYawRateRadians()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L78)*

Get yaw rate in radians per second (useful for some calculations)

## Exposed fields and types

### `public class PigeonHelper`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L9)*

Wraps a `Pigeon2` to provide convenient angular velocity accessors.
