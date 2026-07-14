# LimelightVision

`com.teamscreamrobotics.vision.LimelightVision`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java) · **20 callables** · **3 exposed fields/types** · **1 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2026: Declare named Limelights and their robot-relative poses

[`src/main/java/frc2026/tars/subsystems/vision/VisionManager.java` lines 35–64](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/vision/VisionManager.java#L35-L64)

```java
public class VisionManager {

  public static class Limelights {
    public static final Limelight shooter =
        new Limelight(
            "limelight-shooter",
            new Pose3d(
                Units.inchesToMeters(-13.066),
                Units.inchesToMeters(0.0),
                Units.inchesToMeters(13.925),
                new Rotation3d(180.0, Units.degreesToRadians(-25.0), 0.0)));

    public static final Limelight right =
        new Limelight(
            "limelight-right",
            new Pose3d(
                Units.inchesToMeters(0.220),
                Units.inchesToMeters(12.670),
                Units.inchesToMeters(18.984),
                new Rotation3d(0.0, Units.degreesToRadians(0.0), Units.degreesToRadians(90.0))));

    public static final Limelight left =
        new Limelight(
            "limelight-left",
            new Pose3d(
                Units.inchesToMeters(0.220),
                Units.inchesToMeters(-12.670),
                Units.inchesToMeters(18.285),
                new Rotation3d(180.0, Units.degreesToRadians(0.0), Units.degreesToRadians(-90.0))));
  }
```

## Public and protected callables

### `public static double getTX(Limelight limelight)`

[Source lines 25–27](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L25)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `LimelightHelpers.getTX(limelight.name)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 25–27)"

    ```java
    public static double getTX(Limelight limelight) {
      return LimelightHelpers.getTX(limelight.name);
    }
    ```

??? note "Author note from JavaDoc"

    Returns the horizontal offset angle (TX) to the primary target in degrees.

### `public static double getTY(Limelight limelight)`

[Source lines 30–32](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L30)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `LimelightHelpers.getTY(limelight.name)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 30–32)"

    ```java
    public static double getTY(Limelight limelight) {
      return LimelightHelpers.getTY(limelight.name);
    }
    ```

??? note "Author note from JavaDoc"

    Returns the vertical offset angle (TY) to the primary target in degrees.

### `public static double getTA(Limelight limelight)`

[Source lines 35–37](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L35)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `LimelightHelpers.getTA(limelight.name)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 35–37)"

    ```java
    public static double getTA(Limelight limelight) {
      return LimelightHelpers.getTA(limelight.name);
    }
    ```

??? note "Author note from JavaDoc"

    Returns the target area (TA) as a percentage of the image (0–100).

### `public static boolean getTV(Limelight limelight)`

[Source lines 40–42](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L40)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `LimelightHelpers.getTV(limelight.name)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 40–42)"

    ```java
    public static boolean getTV(Limelight limelight) {
      return LimelightHelpers.getTV(limelight.name);
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if the camera has a valid target.

### `public static double getLatency_Pipeline(Limelight limelight)`

[Source lines 45–47](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L45)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `LimelightHelpers.getLatency_Pipeline(limelight.name)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 45–47)"

    ```java
    public static double getLatency_Pipeline(Limelight limelight) {
      return LimelightHelpers.getLatency_Pipeline(limelight.name);
    }
    ```

??? note "Author note from JavaDoc"

    Returns pipeline processing latency in milliseconds.

### `public static double getLatency_Capture(Limelight limelight)`

[Source lines 50–52](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L50)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `LimelightHelpers.getLatency_Capture(limelight.name)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 50–52)"

    ```java
    public static double getLatency_Capture(Limelight limelight) {
      return LimelightHelpers.getLatency_Capture(limelight.name);
    }
    ```

??? note "Author note from JavaDoc"

    Returns image capture latency in milliseconds.

### `public static double getLatency(Limelight limelight)`

[Source lines 55–57](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L55)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLatency_Pipeline(limelight) + getLatency_Capture(limelight)`.
- Key collaborators/calls: `getLatency_Pipeline()`, `getLatency_Capture()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 55–57)"

    ```java
    public static double getLatency(Limelight limelight){
      return getLatency_Pipeline(limelight) + getLatency_Capture(limelight);
    }
    ```

??? note "Author note from JavaDoc"

    Returns total latency (pipeline + capture) in milliseconds.

### `public static PoseEstimate getPoseEstimate_MT2( Limelight limelight, double robotHeadingDegrees, double yawRateDps)`

[Source lines 65–70](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L65)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `LimelightHelpers.getBotPoseEstimate_wpiBlue(limelight.name)`.
- Key collaborators/calls: `LimelightHelpers.SetRobotOrientation()`, `LimelightHelpers.getBotPoseEstimate_wpiBlue()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |
| `robotHeadingDegrees` | `double` | current robot yaw in degrees **Parameter `yawRateDps`:** current yaw rate in degrees per second |
| `yawRateDps` | `double` | current yaw rate in degrees per second |

**Result:** Returns `PoseEstimate`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 65–70)"

    ```java
    public static PoseEstimate getPoseEstimate_MT2(
        Limelight limelight, double robotHeadingDegrees, double yawRateDps) {
      LimelightHelpers.SetRobotOrientation(
          limelight.name, robotHeadingDegrees, yawRateDps, 0, 0, 0, 0);
      return LimelightHelpers.getBotPoseEstimate_wpiBlue(limelight.name);
    }
    ```

??? note "Author note from JavaDoc"

    Sets robot orientation and returns a MegaTag2 pose estimate in WPILib blue-origin coordinates.
    
    **Parameter `robotHeadingDegrees`:** current robot yaw in degrees
    **Parameter `yawRateDps`:** current yaw rate in degrees per second

### `public static Length getDistanceToTargetTYBased(Length targetHeight, Limelight limelight)`

[Source lines 78–84](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L78)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Return path: `Length.fromMeters(height_diff / Math.tan(goal_theta))`.
- Key collaborators/calls: `limelight.relativePosition.getRotation()`, `getY()`, `Math.toRadians()`, `getTY()`, `targetHeight.getMeters()`, `limelight.relativePosition.getZ()`, `Length.fromMeters()`, `Math.tan()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `targetHeight` | `Length` | the known height of the target **Parameter `limelight`:** the camera to use |
| `limelight` | `Limelight` | the camera to use |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 78–84)"

    ```java
    public static Length getDistanceToTargetTYBased(Length targetHeight, Limelight limelight) {
      double goal_theta =
          limelight.relativePosition.getRotation().getY() + Math.toRadians(getTY(limelight));
      double height_diff = targetHeight.getMeters() - limelight.relativePosition.getZ();
    
      return Length.fromMeters(height_diff / Math.tan(goal_theta));
    }
    ```

??? note "Author note from JavaDoc"

    Estimates horizontal ground distance to a target using the TY angle and known heights.
    
    **Parameter `targetHeight`:** the known height of the target
    **Parameter `limelight`:** the camera to use

### `public static Length get3D_DistanceToTarget(Limelight limelight)`

[Source lines 87–89](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L87)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Return path: `Length.fromMeters(LimelightHelpers.getTargetPose3d_CameraSpace(limelight.name).getTranslation().getNorm())`.
- Key collaborators/calls: `Length.fromMeters()`, `LimelightHelpers.getTargetPose3d_CameraSpace()`, `getTranslation()`, `getNorm()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 87–89)"

    ```java
    public static Length get3D_DistanceToTarget(Limelight limelight){
      return Length.fromMeters(LimelightHelpers.getTargetPose3d_CameraSpace(limelight.name).getTranslation().getNorm());
    }
    ```

??? note "Author note from JavaDoc"

    Returns the 3D Euclidean distance to the primary target in camera space.

### `public static Rotation2d getAngleToTargetTXBased(Limelight limelight)`

[Source lines 92–95](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L92)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `Rotation2d.fromDegrees( -getTX(limelight) - Math.toDegrees(limelight.relativePosition.getRotation().getZ()))`.
- Key collaborators/calls: `Rotation2d.fromDegrees()`, `getTX()`, `Math.toDegrees()`, `limelight.relativePosition.getRotation()`, `getZ()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** Returns `Rotation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 92–95)"

    ```java
    public static Rotation2d getAngleToTargetTXBased(Limelight limelight) {
      return Rotation2d.fromDegrees(
          -getTX(limelight) - Math.toDegrees(limelight.relativePosition.getRotation().getZ()));
    }
    ```

??? note "Author note from JavaDoc"

    Returns the robot-relative horizontal angle to the target, accounting for camera offset.

### `public static int getCurrentPipeline(Limelight limelight)`

[Source lines 98–100](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L98)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `(int) LimelightHelpers.getCurrentPipelineIndex(limelight.name)`.
- Key collaborators/calls: `LimelightHelpers.getCurrentPipelineIndex()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** Returns `int`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 98–100)"

    ```java
    public static int getCurrentPipeline(Limelight limelight) {
      return (int) LimelightHelpers.getCurrentPipelineIndex(limelight.name);
    }
    ```

??? note "Author note from JavaDoc"

    Returns the currently active pipeline index.

### `public static void setLEDMode(LEDMode ledMode, Limelight limelight)`

[Source lines 103–115](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L103)

**Detailed behavior**

- The implementation executes 11 non-blank source lines.
- Key collaborators/calls: `LimelightHelpers.setLEDMode_ForceOff()`, `LimelightHelpers.setLEDMode_ForceOn()`, `LimelightHelpers.setLEDMode_ForceBlink()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `ledMode` | `LEDMode` | `LEDMode` input consumed by the implementation shown below. |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 103–115)"

    ```java
    public static void setLEDMode(LEDMode ledMode, Limelight limelight) {
      switch (ledMode) {
        case OFF:
          LimelightHelpers.setLEDMode_ForceOff(limelight.name);
          break;
        case ON:
          LimelightHelpers.setLEDMode_ForceOn(limelight.name);
          break;
        case BLINK:
          LimelightHelpers.setLEDMode_ForceBlink(limelight.name);
          break;
      }
    }
    ```

??? note "Author note from JavaDoc"

    Sets the camera LED to the given `LEDMode`.

### `public static void setPriorityTagID(int id, Limelight limelight)`

[Source lines 118–120](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L118)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | `int` | `int` input consumed by the implementation shown below. |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 118–120)"

    ```java
    public static void setPriorityTagID(int id, Limelight limelight) {
      LimelightHelpers.setPriorityTagID(limelight.name, id);
    }
    ```

??? note "Author note from JavaDoc"

    Sets the AprilTag ID that the camera should prioritize when multiple tags are visible.

### `public static void setPipeline(int index, Limelight limelight)`

[Source lines 123–125](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L123)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `LimelightHelpers.setPipelineIndex()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `index` | `int` | `int` input consumed by the implementation shown below. |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 123–125)"

    ```java
    public static void setPipeline(int index, Limelight limelight) {
      LimelightHelpers.setPipelineIndex(limelight.name, index);
    }
    ```

??? note "Author note from JavaDoc"

    Switches the camera to the pipeline at the given zero-based index.

### `public static void setCropWindow( double cropXMin, double cropXMax, double cropYMin, double cropYMax, Limelight limelight)`

[Source lines 135–138](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L135)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `cropXMin` | `double` | left edge (−1 to 1) **Parameter `cropXMax`:** right edge (−1 to 1) **Parameter `cropYMin`:** bottom edge (−1 to 1) **Parameter `cropYMax`:** top edge (−1 to 1) |
| `cropXMax` | `double` | right edge (−1 to 1) **Parameter `cropYMin`:** bottom edge (−1 to 1) **Parameter `cropYMax`:** top edge (−1 to 1) |
| `cropYMin` | `double` | bottom edge (−1 to 1) **Parameter `cropYMax`:** top edge (−1 to 1) |
| `cropYMax` | `double` | top edge (−1 to 1) |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 135–138)"

    ```java
    public static void setCropWindow(
        double cropXMin, double cropXMax, double cropYMin, double cropYMax, Limelight limelight) {
      LimelightHelpers.setCropWindow(limelight.name, cropXMin, cropXMax, cropYMin, cropYMax);
    }
    ```

??? note "Author note from JavaDoc"

    Restricts the active image region to reduce processing load.
    
    **Parameter `cropXMin`:** left edge (−1 to 1)
    **Parameter `cropXMax`:** right edge (−1 to 1)
    **Parameter `cropYMin`:** bottom edge (−1 to 1)
    **Parameter `cropYMax`:** top edge (−1 to 1)

### `public static void setThrottle(int skipFrames, Limelight limelight)`

[Source lines 145–148](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L145)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It reads or writes NetworkTables data, so the result depends on live robot/network state.
- Key collaborators/calls: `NetworkTableInstance.getDefault()`, `getTable()`, `llt.getEntry()`, `setNumber()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `skipFrames` | `int` | number of frames to skip between processed frames (0 = no throttle) |
| `limelight` | `Limelight` | `Limelight` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 145–148)"

    ```java
    public static void setThrottle(int skipFrames, Limelight limelight){
      NetworkTable llt = NetworkTableInstance.getDefault().getTable(limelight.name);
      llt.getEntry("throttle_set").setNumber(skipFrames);
    }
    ```

??? note "Author note from JavaDoc"

    Sets the camera frame throttle — higher values skip more frames to reduce CPU load.
    
    **Parameter `skipFrames`:** number of frames to skip between processed frames (0 = no throttle)

### `public Limelight(String name, Pose3d relativePosition)`

[Source lines 15–15](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L15)

**Detailed behavior**

- Java generates this record canonical constructor. It stores each argument in the corresponding final record component; Java also supplies component accessors, value-based `equals`, `hashCode`, and `toString`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | `String` | `String` input consumed by the implementation shown below. |
| `relativePosition` | `Pose3d` | Position in the units required by this API and configuration. |

**Result:** Constructs and initializes a `Limelight` instance.

??? example "Record declaration that generates this callable"

    ```java
    public record Limelight(String name, Pose3d relativePosition)
    ```

??? note "Author note from JavaDoc"

    Java generates this canonical constructor from the record header.

### `public String name()`

[Source lines 15–15](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L15)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record Limelight(String name, Pose3d relativePosition)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `name` record component.

### `public Pose3d relativePosition()`

[Source lines 15–15](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L15)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record Limelight(String name, Pose3d relativePosition)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `relativePosition` record component.

## Exposed fields and types

### `public class LimelightVision`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L12)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Typed wrapper around `LimelightHelpers` providing vision measurements and camera control.

### `public record Limelight(String name, Pose3d relativePosition)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L15)*

This exposed `record` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Identifies a Limelight camera by NetworkTables name and its pose relative to the robot.

### `public enum LEDMode`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightVision.java#L18)*

This exposed `enum` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    LED control modes supported by Limelight cameras.
