# PhoenixSwerveHelper

`com.teamscreamrobotics.drivers.PhoenixSwerveHelper`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java) · **20 callables** · **1 exposed fields/types**

## Competition usage

**2025:** [`Drivetrain.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/drivetrain/Drivetrain.java#L9)

**2026:** [`Drivetrain.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/drivetrain/Drivetrain.java#L10)

## Public and protected callables

### `public PhoenixSwerveHelper( Supplier&lt;Pose2d&gt; poseSup, double maxSpeed, ScreamPIDConstants snapConstants, ScreamPIDConstants headingCorrectionConstants)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L55)*

Creates a new helper with configured swerve requests.

**Parameter `poseSup`:** supplier of the robot's current field pose
**Parameter `maxSpeed`:** drivetrain maximum speed in m/s (used to set deadbands)
**Parameter `snapConstants`:** PID constants for the heading snap controller
**Parameter `headingCorrectionConstants`:** PID constants for the heading drift correction controller

### `public void setLastAngle(Rotation2d angle)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L93)*

Overrides the heading correction hold angle — call this when intentionally changing heading.

### `public FieldCentricFacingAngle getFacingAngle(Translation2d translation, Rotation2d targetAngle)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L103)*

Returns a `FieldCentricFacingAngle` request using the built-in snap controller.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `targetAngle`:** desired heading

### `public FieldCentric getFacingAngle( Translation2d translation, Rotation2d targetAngle, PIDController headingController)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L117)*

Returns a `FieldCentric` request with angular velocity computed from a custom PID controller.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `targetAngle`:** desired heading
**Parameter `headingController`:** PID constants for heading control (uses a fresh controller per call)

### `public FieldCentric getFacingAngleProfiled( Translation2d translation, Rotation2d targetAngle, ProfiledPIDController profile)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L132)*

Returns a `FieldCentric` request with angular velocity from a profiled PID controller.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `targetAngle`:** desired heading
**Parameter `profile`:** profiled PID controller for smooth heading control

### `public FieldCentricFacingAngle getFacingAngleCOR( Translation2d translation, Rotation2d targetAngle, Translation2d centerOfRotation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L146)*

Returns a `FieldCentricFacingAngle` request using the built-in snap controller and a custom center of rotation.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `targetAngle`:** desired heading
**Parameter `centerOfRotation`:** offset from robot center for rotation

### `public FieldCentric getFacingAngleProfiledCOR( Translation2d translation, Rotation2d targetAngle, ProfiledPIDController profile, Translation2d centerOfRotation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L159)*

Returns a `FieldCentric` request with profiled heading and a custom center of rotation.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `targetAngle`:** desired heading
**Parameter `profile`:** profiled PID controller
**Parameter `centerOfRotation`:** offset from robot center for rotation

### `public FieldCentricFacingAngle getPointingAt( Translation2d translation, Translation2d targetPoint)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L176)*

Returns a `FieldCentricFacingAngle` request that keeps the robot aimed at a field point.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `targetPoint`:** the field point to face

### `public FieldCentricFacingAngle getPointingAt( Translation2d translation, Translation2d targetPoint, Rotation2d offset)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L189)*

Returns a `FieldCentricFacingAngle` request that keeps the robot aimed at a field point
with an angular offset added to the computed heading.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `targetPoint`:** the field point to face
**Parameter `offset`:** additional rotation added to the target heading

### `public FieldCentric getPointingAtProfiled( Translation2d translation, Translation2d targetPoint, ProfiledPIDController profile)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L204)*

Returns a `FieldCentric` request that aims at a field point using a profiled controller.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `targetPoint`:** the field point to face
**Parameter `profile`:** profiled PID controller for smooth heading tracking

### `public FieldCentric getPointingAtProfiled( Translation2d translation, Translation2d targetPoint, Rotation2d offset, ProfiledPIDController profile)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L218)*

Returns a `FieldCentric` request that aims at a field point with an offset, using a
profiled controller.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `targetPoint`:** the field point to face
**Parameter `offset`:** additional rotation added to the target heading
**Parameter `profile`:** profiled PID controller

### `public FieldCentric getHeadingCorrectedFieldCentric( Translation2d translation, double angularVelocity)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L231)*

Returns a field-centric request with automatic heading drift correction.
While `angularVelocity` is near zero the correction controller holds the last known
heading; otherwise the driver input is passed through and the hold angle is updated.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `angularVelocity`:** driver-commanded rotation rate (rad/s)

### `public FieldCentric getFieldCentric(Translation2d translation, double angularVelocity)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L255)*

Returns a basic field-centric drive request.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `angularVelocity`:** rotation rate in rad/s

### `public FieldCentric getFieldCentricCOR( Translation2d translation, double angularVelocity, Translation2d centerOfRotation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L270)*

Returns a field-centric drive request with a custom center of rotation.

**Parameter `translation`:** field-relative XY velocity vector
**Parameter `angularVelocity`:** rotation rate in rad/s
**Parameter `centerOfRotation`:** offset from robot center for rotation

### `public RobotCentric getRobotCentric(Translation2d translation, double angularVelocity)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L285)*

Returns a robot-centric drive request.

**Parameter `translation`:** robot-relative XY velocity vector
**Parameter `angularVelocity`:** rotation rate in rad/s

### `public RobotCentric getRobotCentricCOR( Translation2d translation, double angularVelocity, Translation2d centerOfRotation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L300)*

Returns a robot-centric drive request with a custom center of rotation.

**Parameter `translation`:** robot-relative XY velocity vector
**Parameter `angularVelocity`:** rotation rate in rad/s
**Parameter `centerOfRotation`:** offset from robot center for rotation

### `public ApplyRobotSpeeds getApplyRobotSpeeds(ChassisSpeeds chassisSpeeds)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L310)*

Returns an `ApplyRobotSpeeds` request for closed-loop velocity control.

### `public ApplyRobotSpeeds getApplyRobotSpeedsCOR( ChassisSpeeds chassisSpeeds, Translation2d centerOfRotation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L320)*

Returns an `ApplyRobotSpeeds` request with a custom center of rotation.

**Parameter `chassisSpeeds`:** desired robot-relative speeds
**Parameter `centerOfRotation`:** offset from robot center for rotation

### `public ApplyFieldSpeeds getApplyFieldSpeeds(ChassisSpeeds chassisSpeeds)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L326)*

Returns an `ApplyFieldSpeeds` request for closed-loop field-relative velocity control.

### `public ApplyFieldSpeeds getApplyFieldSpeedsCOR(ChassisSpeeds chassisSpeeds, Translation2d centerOfRotation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L336)*

Returns an `ApplyFieldSpeeds` request with a custom center of rotation.

**Parameter `chassisSpeeds`:** desired field-relative speeds
**Parameter `centerOfRotation`:** offset from robot center for rotation

## Exposed fields and types

### `public class PhoenixSwerveHelper`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L30)*

Factory for CTRE Phoenix 6 swerve drive requests with built-in heading snap and correction.
Wraps `FieldCentric`, `FieldCentricFacingAngle`, `RobotCentric`, and
`ApplyRobotSpeeds`/`ApplyFieldSpeeds` requests with pre-configured deadbands and
drive/steer request types.
