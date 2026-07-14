# Conversions

`com.teamscreamrobotics.math.Conversions`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java) · **7 callables** · **1 exposed fields/types**

## Competition usage

**2025:** [`Elevator.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/elevator/Elevator.java#L13)

**2026:** [`Shooter.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/Shooter.java#L7)

## Public and protected callables

### `public static double rpsToRPM(double falconRPS, double gearRatio)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L14)*

**Parameter `falconRPS`:** Falcon rotations per second
**Parameter `gearRatio`:** gear ratio between Falcon and mechanism (set to 1 for Falcon RPM)
**Returns:** RPM of mechanism

### `public static double rpmToRPS(double rpm, double gearRatio)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L24)*

**Parameter `rpm`:** RPM of mechanism
**Parameter `gearRatio`:** Gear ratio between Falcon and mechanism (set to 1 for Falcon RPS)
**Returns:** Falcon rotations per second

### `public static double rpsToMPS(double falconRPS, double circumference, double gearRatio)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L35)*

**Parameter `falconRPS`:** Falcon rotations per second
**Parameter `circumference`:** circumference of wheel in meters
**Parameter `gearRatio`:** gear ratio between Falcon and mechanism
**Returns:** mechanism linear velocity in meters per second

### `public static double mpsToRPS(double velocity, double circumference, double gearRatio)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L46)*

**Parameter `velocity`:** velocity in meters per second
**Parameter `circumference`:** circumference of wheel in meters
**Parameter `gearRatio`:** gear ratio between Falcon and mechanism
**Returns:** Falcon rotations per second

### `public static double rpmToFTS(double rpm, double circumference)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L56)*

**Parameter `rpm`:** RPM of the mechanism
**Parameter `circumference`:** circumference of the wheel in feet
**Returns:** linear velocity in feet per second

### `public static double linearDistanceToRotations(Length distance, Length circumference)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L65)*

**Parameter `distance`:** linear distance traveled
**Parameter `circumference`:** circumference per rotation
**Returns:** number of rotations

### `public static Length rotationsToLinearDistance(double rotations, Length circumference)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L74)*

**Parameter `rotations`:** number of rotations
**Parameter `circumference`:** circumference per rotation
**Returns:** linear distance traveled

## Exposed fields and types

### `public class Conversions`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L8)*
