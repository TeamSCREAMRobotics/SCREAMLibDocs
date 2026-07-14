# Trajectory

`com.teamscreamrobotics.physics.Trajectory`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java) · **19 callables** · **14 exposed fields/types**

## Public and protected callables

### `public double getArea()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L57)*

Returns the cross-sectional area of the game piece in m² (used for drag calculation).

### `public TrajectoryConfig setShotVelocity(double velocity)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L81)*

Sets the muzzle velocity of the shot in m/s.

### `public TrajectoryConfig setShotAngle(double angle)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L87)*

Sets the launch angle in degrees (above horizontal).

### `public TrajectoryConfig setRobotVelocity(double velocity)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L93)*

Sets the robot's forward velocity in m/s (added to shot velocity for moving shots).

### `public TrajectoryConfig setRobotAngle(double angle)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L99)*

Sets the robot's travel direction in degrees relative to the shot direction.

### `public TrajectoryConfig setTargetDistance(double distance)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L105)*

Sets the horizontal distance to the target in meters.

### `public TrajectoryConfig setTargetHeight(double height)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L111)*

Sets the height of the target opening in meters.

### `public TrajectoryConfig setInitialHeight(double height)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L117)*

Sets the launch height above the ground in meters.

### `public TrajectoryConfig setGamePiece(GamePiece piece)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L123)*

Sets the game piece type to use for physics calculations.

### `public TrajectoryConfig setCustomGamePiece(double massKg, double diameterMeters, double dragCoefficient)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L134)*

Set custom game piece properties
**Parameter `massKg`:** Mass in kilograms
**Parameter `diameterMeters`:** Diameter in meters
**Parameter `dragCoefficient`:** Drag coefficient (sphere ≈ 0.47)

### `public TrajectoryConfig setCustomGamePieceImperial(double massLbs, double diameterInches, double dragCoefficient)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L148)*

Convenience method to set custom game piece from imperial units
**Parameter `massLbs`:** Mass in pounds
**Parameter `diameterInches`:** Diameter in inches
**Parameter `dragCoefficient`:** Drag coefficient

### `public TrajectoryPoint(double time, double x, double y, double vx, double vy)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L198)*

Creates a trajectory sample point.

**Parameter `time`:** time since launch (s)
**Parameter `x`:** horizontal position (m)
**Parameter `y`:** vertical position (m)
**Parameter `vx`:** horizontal velocity (m/s)
**Parameter `vy`:** vertical velocity (m/s)

### `public String toString()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L207)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public static TrajectoryConfig configure()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L216)*

Get the configuration builder

### `public static TrajectoryConfig getConfig()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L223)*

Get the current configuration (read-only access)

### `public static List&lt;TrajectoryPoint&gt; getDesiredTrajectory()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L231)*

Main method to get the desired trajectory based on current configuration
**Returns:** List of trajectory points

### `public static double getOptimalAngle()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L249)*

Get the optimal angle to hit the configured target
**Returns:** Optimal angle in degrees, or -1 if no solution found

### `public static double getRequiredVelocity()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L267)*

Get the required velocity to hit the configured target at the configured angle
**Returns:** Required velocity in m/s, or -1 if no solution found

### `public static double getTimeOfFlight()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L285)*

Get the time of flight for the configured shot
**Returns:** Time in seconds

## Exposed fields and types

### `public class Trajectory`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L22)*

Trajectory calculator for projectile motion with air resistance
Designed for scoring with a ball

Usage:
Trajectory.configure()
.setShotVelocity(12.0)
.setShotAngle(45.0)
.setTargetDistance(4.0)
.setGamePiece(GamePiece.FUEL);

List path = Trajectory.getDesiredTrajectory();
double angle = Trajectory.getOptimalAngle();

### `public static final double HUB_HEIGHT = Units.inchesToMeters(72.0)`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L30)*

### `public static final double HUB_DISTANCE_FROM_ALLIANCE_WALL = Units.inchesToMeters(158.6)`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L31)*

### `public enum GamePiece`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L39)*

Game piece types with their physical properties

### `public final double mass`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L44)*

Mass of the game piece in kilograms.

### `public final double diameter`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L46)*

Diameter of the game piece in meters.

### `public final double dragCoefficient`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L48)*

Aerodynamic drag coefficient (sphere ≈ 0.47).

### `public static class TrajectoryConfig`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L65)*

Configuration builder for trajectory calculations

### `public static class TrajectoryPoint`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L177)*

Represents a point in the trajectory

### `public final double time`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L179)*

Time since launch in seconds.

### `public final double x`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L181)*

Horizontal distance traveled in meters.

### `public final double y`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L183)*

Height above ground in meters.

### `public final double vx`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L185)*

Horizontal velocity component in m/s.

### `public final double vy`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L187)*

Vertical velocity component in m/s.
