# ScreamUtil

`com.teamscreamrobotics.util.ScreamUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java) · **13 callables** · **2 exposed fields/types**

## Competition usage

**2025:** [`Controlboard.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/controlboard/Controlboard.java#L18), [`Drivetrain.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/drivetrain/Drivetrain.java#L35)

**2026:** [`Controlboard.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/controlboard/Controlboard.java#L4), [`Drivetrain.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/drivetrain/Drivetrain.java#L15)

## Public and protected callables

### `public static Rotation2d boundRotation(Rotation2d rotation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L15)*

Wraps `rotation` to the range `(-π, π]`.

### `public static Rotation2d boundRotation0_360(Rotation2d rotation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L20)*

Wraps `rotation` to the range `[0°, 360°)`.

### `public static Rotation2d getTangent(Translation2d start, Translation2d end)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L32)*

Returns the tangent (heading) angle of the vector from `start` to `end`.

**Parameter `start`:** the starting point
**Parameter `end`:** the ending point

### `public static boolean epsilonEquals(double a, double b, final double epsilon)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L44)*

Returns `true` if `|a - b| <= epsilon`.

**Parameter `a`:** first value
**Parameter `b`:** second value
**Parameter `epsilon`:** tolerance

### `public static boolean epsilonEquals(double a, double b)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L49)*

Returns `true` if `|a - b| <= EPSILON`.

### `public static boolean epsilonEquals(int a, int b, int epsilon)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L54)*

Returns `true` if `|a - b| <= epsilon` (integer overload).

### `public double getStallTorque(double stallTorque, double freeSpeed, double speed)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L65)*

Estimates output torque at the given speed using a linear motor model.

**Parameter `stallTorque`:** maximum torque at zero speed (N·m)
**Parameter `freeSpeed`:** no-load speed (rad/s or RPM — must match units of `speed`)
**Parameter `speed`:** current speed

### `public static Twist2d chassisSpeedsToTwist2d(ChassisSpeeds chassisSpeeds)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L74)*

Converts a `ChassisSpeeds` to a `Twist2d` with the same vx, vy, and omega.

**Parameter `chassisSpeeds`:** the speeds to convert

### `public static boolean epsilonEquals(final Twist2d twist, final Twist2d other, double epsilon)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L88)*

Returns `true` if all components of two twists are within `epsilon` of each other.

**Parameter `twist`:** first twist
**Parameter `other`:** second twist
**Parameter `epsilon`:** per-component tolerance

### `public static boolean epsilonEquals(final Twist2d twist, final Twist2d other)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L95)*

Returns `true` if all twist components are within `#EPSILON` of each other.

### `public static boolean valueBetween(double value, double upper, double lower)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L106)*

Returns `true` if `lower < value < upper` (exclusive).

**Parameter `value`:** the value to test
**Parameter `upper`:** the exclusive upper bound
**Parameter `lower`:** the exclusive lower bound

### `public static boolean withinAngleThreshold( Rotation2d targetAngle, Rotation2d currentAngle, Rotation2d threshold)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L118)*

Returns `true` if `currentAngle` is within `threshold` of `targetAngle`,
accounting for wrap-around.

**Parameter `targetAngle`:** the desired angle
**Parameter `currentAngle`:** the measured angle
**Parameter `threshold`:** the maximum allowable error

### `public static double random(double lower, double upper)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L130)*

Returns a random double in `[lower, upper]`, swapping bounds if `lower >= upper`.

**Parameter `lower`:** lower bound
**Parameter `upper`:** upper bound

## Exposed fields and types

### `public class ScreamUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L10)*

Various utility methods

### `public static final double EPSILON = 1e-3`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L12)*

Default epsilon used by the no-argument `#epsilonEquals` overloads.
