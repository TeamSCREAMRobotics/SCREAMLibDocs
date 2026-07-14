# ScreamMath

`com.teamscreamrobotics.math.ScreamMath`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java) · **9 callables** · **2 exposed fields/types**

## Competition usage

**2025:** [`DriveToPose.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/commands/DriveToPose.java#L21), [`Controlboard.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/controlboard/Controlboard.java#L16), [`LED.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/leds/LED.java#L17), [`Elevator.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/elevator/Elevator.java#L14)

**2026:** [`LED.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/leds/LED.java#L7), [`Shooter.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/Shooter.java#L8)

## Public and protected callables

### `public static double average(double... nums)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L24)*

Returns the arithmetic mean of the given values, or `0.0` if the array is empty.

**Parameter `nums`:** the values to average

### `public static double mapRange( double value, double fromLow, double fromHigh, double toLow, double toHigh)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L44)*

Linearly maps `value` from one range to another.

**Parameter `value`:** the input value in the source range
**Parameter `fromLow`:** lower bound of the source range
**Parameter `fromHigh`:** upper bound of the source range
**Parameter `toLow`:** lower bound of the target range
**Parameter `toHigh`:** upper bound of the target range
**Throws `IllegalArgumentException`:** if the source range has zero width

### `public static double getLinearVelocity(ChassisSpeeds speeds)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L58)*

Returns the translational speed magnitude (vx² + vy²)^½ from a `ChassisSpeeds`.

**Parameter `speeds`:** the chassis speed

### `public static Translation3d rotatePoint(Translation3d point, Rotation2d yaw)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L68)*

Rotates a 3D point around the Z-axis by `yaw`, preserving Z.

**Parameter `point`:** the point to rotate
**Parameter `yaw`:** the rotation angle around the Z-axis

### `public static Translation2d rotatePoint(Translation2d point, Rotation2d yaw)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L85)*

Rotates a 2D point by `yaw`.

**Parameter `point`:** the point to rotate
**Parameter `yaw`:** the rotation angle

### `public static Rotation2d calculateAngleToPoint(Translation2d current, Translation2d target)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L96)*

Returns the bearing angle from `current` to `target`.

**Parameter `current`:** the observer position
**Parameter `target`:** the target position

### `public static Rotation2d clamp(Rotation2d rotation, Rotation2d high, Rotation2d low)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L109)*

Clamps `rotation` to the range `[low, high]` in radians.

**Parameter `rotation`:** the rotation to clamp
**Parameter `high`:** the upper bound
**Parameter `low`:** the lower bound

### `public static double square(double n)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L115)*

Returns `n²`.

### `public static MomentOfInertia parallelAxisTheorem(MomentOfInertia moi, Mass mass, Length distance)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L127)*

Applies the parallel axis theorem: `I = I_cm + m * d²`.

**Parameter `moi`:** moment of inertia about the center of mass
**Parameter `mass`:** mass of the object
**Parameter `distance`:** distance from the center of mass to the new axis
**Returns:** the moment of inertia about the new parallel axis

## Exposed fields and types

### `public class ScreamMath`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L14)*

General-purpose math utilities for FRC calculations.

### `public static final double METERS_PER_INCH = 0.0254`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L17)*

Conversion factor: meters per inch ({@value} m/in).
