# LimelightVision

`com.teamscreamrobotics.vision.LimelightVision`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java) · **17 callables** · **3 exposed fields/types**

## Competition usage

**2025:** [`VisionManager.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/vision/VisionManager.java#L36)

**2026:** [`VisionManager.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/vision/VisionManager.java#L8)

## Public and protected callables

### `public static double getTX(Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L25)*

Returns the horizontal offset angle (TX) to the primary target in degrees.

### `public static double getTY(Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L30)*

Returns the vertical offset angle (TY) to the primary target in degrees.

### `public static double getTA(Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L35)*

Returns the target area (TA) as a percentage of the image (0–100).

### `public static boolean getTV(Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L40)*

Returns `true` if the camera has a valid target.

### `public static double getLatency_Pipeline(Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L45)*

Returns pipeline processing latency in milliseconds.

### `public static double getLatency_Capture(Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L50)*

Returns image capture latency in milliseconds.

### `public static double getLatency(Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L55)*

Returns total latency (pipeline + capture) in milliseconds.

### `public static PoseEstimate getPoseEstimate_MT2( Limelight limelight, double robotHeadingDegrees, double yawRateDps)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L65)*

Sets robot orientation and returns a MegaTag2 pose estimate in WPILib blue-origin coordinates.

**Parameter `robotHeadingDegrees`:** current robot yaw in degrees
**Parameter `yawRateDps`:** current yaw rate in degrees per second

### `public static Length getDistanceToTargetTYBased(Length targetHeight, Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L78)*

Estimates horizontal ground distance to a target using the TY angle and known heights.

**Parameter `targetHeight`:** the known height of the target
**Parameter `limelight`:** the camera to use

### `public static Length get3D_DistanceToTarget(Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L87)*

Returns the 3D Euclidean distance to the primary target in camera space.

### `public static Rotation2d getAngleToTargetTXBased(Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L92)*

Returns the robot-relative horizontal angle to the target, accounting for camera offset.

### `public static int getCurrentPipeline(Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L98)*

Returns the currently active pipeline index.

### `public static void setLEDMode(LEDMode ledMode, Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L103)*

Sets the camera LED to the given `LEDMode`.

### `public static void setPriorityTagID(int id, Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L118)*

Sets the AprilTag ID that the camera should prioritize when multiple tags are visible.

### `public static void setPipeline(int index, Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L123)*

Switches the camera to the pipeline at the given zero-based index.

### `public static void setCropWindow( double cropXMin, double cropXMax, double cropYMin, double cropYMax, Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L135)*

Restricts the active image region to reduce processing load.

**Parameter `cropXMin`:** left edge (−1 to 1)
**Parameter `cropXMax`:** right edge (−1 to 1)
**Parameter `cropYMin`:** bottom edge (−1 to 1)
**Parameter `cropYMax`:** top edge (−1 to 1)

### `public static void setThrottle(int skipFrames, Limelight limelight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L145)*

Sets the camera frame throttle — higher values skip more frames to reduce CPU load.

**Parameter `skipFrames`:** number of frames to skip between processed frames (0 = no throttle)

## Exposed fields and types

### `public class LimelightVision`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L12)*

Typed wrapper around `LimelightHelpers` providing vision measurements and camera control.

### `public record Limelight(String name, Pose3d relativePosition)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L15)*

Identifies a Limelight camera by NetworkTables name and its pose relative to the robot.

### `public enum LEDMode`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L18)*

LED control modes supported by Limelight cameras.
