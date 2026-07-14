# LimelightHelpers

`com.teamscreamrobotics.vision.LimelightHelpers`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java) · **118 callables** · **88 exposed fields/types** · **1 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## How to use this generated helper safely

`LimelightHelpers` is a broad NetworkTables adapter. Getter families read named Limelight entries and convert raw doubles/arrays/JSON into typed target, pose, and estimate objects. Setter families publish camera pose, crop, priority-tag, pipeline, orientation, and Python data back to NetworkTables. Pose-estimate methods also compensate timestamps with reported latency. The implementation details below show the exact NetworkTables key for every call; use those details when diagnosing an empty/default result.

!!! note "Default values are meaningful"
    Many getters return `0`, an empty array/string, or an empty result when an entry is missing. A default value is not proof that a valid target was observed; pair pose/target reads with the relevant validity and tag-count checks.


## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2026: Set robot orientation, select MegaTag mode, reject estimates, and add odometry data

[`src/main/java/frc2026/tars/subsystems/vision/VisionManager.java` lines 134–183](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/vision/VisionManager.java#L134-L183)

```java
private void addStaticEstimate(Limelight limelight) {
  LimelightHelpers.SetRobotOrientation(
      limelight.name(),
      drivetrain.getHeading().getDegrees(),
      drivetrain.getYawRate().getDegrees(),
      0,
      0,
      0,
      0);

  if (DriverStation.isDisabled()) {
    addPoseEstimate(
        LimelightHelpers.getBotPoseEstimate_wpiBlue(limelight.name()), limelight, true, false);
  } else {
    addPoseEstimate(
        LimelightHelpers.getBotPoseEstimate_wpiBlue_MegaTag2(limelight.name()),
        limelight,
        false,
        false);
  }
}

private void addPoseEstimate(
    PoseEstimate estimate, Limelight limelight, boolean mt1, boolean isTurret) {
  boolean shouldUseMt2 = !rejectEstimate(estimate, limelight);

  if (shouldUseMt2 && !Dashboard.disableAllVisionUpdates.get()) {
    double stdFactor = Math.pow(estimate.avgTagDist, 2.75) / (estimate.tagCount * 0.5);
    double xyStds =
        VisionConstants.xyStdBaseline
            * stdFactor
            * (mt1 ? 1.0 : VisionConstants.xyMt2StdFactor)
            * (isTurret ? VisionConstants.xyTurretFactor * estimate.avgTagDist : 1.0);
    double thetaStds =
        DriverStation.isDisabled() ? 0.5 : VisionConstants.thetaStdBaseline * stdFactor;
    drivetrain.addVisionMeasurement(
        estimate.pose,
        estimate.timestampSeconds,
        VecBuilder.fill(xyStds, xyStds, mt1 ? thetaStds : 999999999999.0),
        !mt1);

    Logger.log("Vision/" + limelight.name() + "/VisionType", VisionType.MT2);
    Logger.log("Vision/" + limelight.name() + "/PoseEstimate", estimate.pose);
    Logger.log("Vision/" + limelight.name() + "/XyStds", xyStds);
    Logger.log("Vision/" + limelight.name() + "/ThetaStds", thetaStds);
  } else {
    Logger.log("Vision/" + limelight.name() + "/PoseEstimate", Pose2d.kZero);
    Logger.log("Vision/" + limelight.name() + "/XyStds", 0.0);
    Logger.log("Vision/" + limelight.name() + "/ThetaStds", 0.0);
  }
```

## Public and protected callables

### `public Pose3d getCameraPose_TargetSpace()`

[Source lines 52–54](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L52)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(cameraPose_TargetSpace)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 52–54)"

    ```java
    public Pose3d getCameraPose_TargetSpace() {
      return toPose3D(cameraPose_TargetSpace);
    }
    ```

### `public Pose3d getRobotPose_FieldSpace()`

[Source lines 56–58](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L56)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(robotPose_FieldSpace)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 56–58)"

    ```java
    public Pose3d getRobotPose_FieldSpace() {
      return toPose3D(robotPose_FieldSpace);
    }
    ```

### `public Pose3d getRobotPose_TargetSpace()`

[Source lines 60–62](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L60)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(robotPose_TargetSpace)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 60–62)"

    ```java
    public Pose3d getRobotPose_TargetSpace() {
      return toPose3D(robotPose_TargetSpace);
    }
    ```

### `public Pose3d getTargetPose_CameraSpace()`

[Source lines 64–66](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L64)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(targetPose_CameraSpace)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 64–66)"

    ```java
    public Pose3d getTargetPose_CameraSpace() {
      return toPose3D(targetPose_CameraSpace);
    }
    ```

### `public Pose3d getTargetPose_RobotSpace()`

[Source lines 68–70](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L68)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(targetPose_RobotSpace)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 68–70)"

    ```java
    public Pose3d getTargetPose_RobotSpace() {
      return toPose3D(targetPose_RobotSpace);
    }
    ```

### `public Pose2d getCameraPose_TargetSpace2D()`

[Source lines 72–74](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L72)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(cameraPose_TargetSpace)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 72–74)"

    ```java
    public Pose2d getCameraPose_TargetSpace2D() {
      return toPose2D(cameraPose_TargetSpace);
    }
    ```

### `public Pose2d getRobotPose_FieldSpace2D()`

[Source lines 76–78](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L76)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(robotPose_FieldSpace)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 76–78)"

    ```java
    public Pose2d getRobotPose_FieldSpace2D() {
      return toPose2D(robotPose_FieldSpace);
    }
    ```

### `public Pose2d getRobotPose_TargetSpace2D()`

[Source lines 80–82](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L80)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(robotPose_TargetSpace)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 80–82)"

    ```java
    public Pose2d getRobotPose_TargetSpace2D() {
      return toPose2D(robotPose_TargetSpace);
    }
    ```

### `public Pose2d getTargetPose_CameraSpace2D()`

[Source lines 84–86](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L84)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(targetPose_CameraSpace)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 84–86)"

    ```java
    public Pose2d getTargetPose_CameraSpace2D() {
      return toPose2D(targetPose_CameraSpace);
    }
    ```

### `public Pose2d getTargetPose_RobotSpace2D()`

[Source lines 88–90](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L88)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(targetPose_RobotSpace)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 88–90)"

    ```java
    public Pose2d getTargetPose_RobotSpace2D() {
      return toPose2D(targetPose_RobotSpace);
    }
    ```

### `public LimelightTarget_Retro()`

[Source lines 110–116](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L110)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.

**Inputs:** None.

**Result:** Constructs and initializes a `LimelightTarget_Retro` instance.

??? example "Implementation (source lines 110–116)"

    ```java
    public LimelightTarget_Retro() {
      cameraPose_TargetSpace = new double[6];
      robotPose_FieldSpace = new double[6];
      robotPose_TargetSpace = new double[6];
      targetPose_CameraSpace = new double[6];
      targetPose_RobotSpace = new double[6];
    }
    ```

### `public Pose3d getCameraPose_TargetSpace()`

[Source lines 142–144](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L142)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(cameraPose_TargetSpace)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 142–144)"

    ```java
    public Pose3d getCameraPose_TargetSpace() {
      return toPose3D(cameraPose_TargetSpace);
    }
    ```

### `public Pose3d getRobotPose_FieldSpace()`

[Source lines 146–148](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L146)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(robotPose_FieldSpace)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 146–148)"

    ```java
    public Pose3d getRobotPose_FieldSpace() {
      return toPose3D(robotPose_FieldSpace);
    }
    ```

### `public Pose3d getRobotPose_TargetSpace()`

[Source lines 150–152](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L150)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(robotPose_TargetSpace)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 150–152)"

    ```java
    public Pose3d getRobotPose_TargetSpace() {
      return toPose3D(robotPose_TargetSpace);
    }
    ```

### `public Pose3d getTargetPose_CameraSpace()`

[Source lines 154–156](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L154)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(targetPose_CameraSpace)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 154–156)"

    ```java
    public Pose3d getTargetPose_CameraSpace() {
      return toPose3D(targetPose_CameraSpace);
    }
    ```

### `public Pose3d getTargetPose_RobotSpace()`

[Source lines 158–160](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L158)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(targetPose_RobotSpace)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 158–160)"

    ```java
    public Pose3d getTargetPose_RobotSpace() {
      return toPose3D(targetPose_RobotSpace);
    }
    ```

### `public Pose2d getCameraPose_TargetSpace2D()`

[Source lines 162–164](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L162)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(cameraPose_TargetSpace)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 162–164)"

    ```java
    public Pose2d getCameraPose_TargetSpace2D() {
      return toPose2D(cameraPose_TargetSpace);
    }
    ```

### `public Pose2d getRobotPose_FieldSpace2D()`

[Source lines 166–168](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L166)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(robotPose_FieldSpace)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 166–168)"

    ```java
    public Pose2d getRobotPose_FieldSpace2D() {
      return toPose2D(robotPose_FieldSpace);
    }
    ```

### `public Pose2d getRobotPose_TargetSpace2D()`

[Source lines 170–172](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L170)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(robotPose_TargetSpace)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 170–172)"

    ```java
    public Pose2d getRobotPose_TargetSpace2D() {
      return toPose2D(robotPose_TargetSpace);
    }
    ```

### `public Pose2d getTargetPose_CameraSpace2D()`

[Source lines 174–176](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L174)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(targetPose_CameraSpace)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 174–176)"

    ```java
    public Pose2d getTargetPose_CameraSpace2D() {
      return toPose2D(targetPose_CameraSpace);
    }
    ```

### `public Pose2d getTargetPose_RobotSpace2D()`

[Source lines 178–180](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L178)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(targetPose_RobotSpace)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 178–180)"

    ```java
    public Pose2d getTargetPose_RobotSpace2D() {
      return toPose2D(targetPose_RobotSpace);
    }
    ```

### `public LimelightTarget_Fiducial()`

[Source lines 200–206](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L200)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.

**Inputs:** None.

**Result:** Constructs and initializes a `LimelightTarget_Fiducial` instance.

??? example "Implementation (source lines 200–206)"

    ```java
    public LimelightTarget_Fiducial() {
      cameraPose_TargetSpace = new double[6];
      robotPose_FieldSpace = new double[6];
      robotPose_TargetSpace = new double[6];
      targetPose_CameraSpace = new double[6];
      targetPose_RobotSpace = new double[6];
    }
    ```

### `public LimelightTarget_Classifier()`

[Source lines 237–237](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L237)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs:** None.

**Result:** Constructs and initializes a `LimelightTarget_Classifier` instance.

??? example "Implementation (source lines 237)"

    ```java
    public LimelightTarget_Classifier() {}
    ```

### `public LimelightTarget_Detector()`

[Source lines 266–266](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L266)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs:** None.

**Result:** Constructs and initializes a `LimelightTarget_Detector` instance.

??? example "Implementation (source lines 266)"

    ```java
    public LimelightTarget_Detector() {}
    ```

### `public Pose3d getBotPose3d()`

[Source lines 318–320](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L318)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(botpose)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 318–320)"

    ```java
    public Pose3d getBotPose3d() {
      return toPose3D(botpose);
    }
    ```

### `public Pose3d getBotPose3d_wpiRed()`

[Source lines 322–324](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L322)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(botpose_wpired)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 322–324)"

    ```java
    public Pose3d getBotPose3d_wpiRed() {
      return toPose3D(botpose_wpired);
    }
    ```

### `public Pose3d getBotPose3d_wpiBlue()`

[Source lines 326–328](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L326)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose3D(botpose_wpiblue)`.
- Key collaborators/calls: `toPose3D()`.

**Inputs:** None.

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 326–328)"

    ```java
    public Pose3d getBotPose3d_wpiBlue() {
      return toPose3D(botpose_wpiblue);
    }
    ```

### `public Pose2d getBotPose2d()`

[Source lines 330–332](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L330)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(botpose)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 330–332)"

    ```java
    public Pose2d getBotPose2d() {
      return toPose2D(botpose);
    }
    ```

### `public Pose2d getBotPose2d_wpiRed()`

[Source lines 334–336](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L334)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(botpose_wpired)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 334–336)"

    ```java
    public Pose2d getBotPose2d_wpiRed() {
      return toPose2D(botpose_wpired);
    }
    ```

### `public Pose2d getBotPose2d_wpiBlue()`

[Source lines 338–340](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L338)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `toPose2D(botpose_wpiblue)`.
- Key collaborators/calls: `toPose2D()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 338–340)"

    ```java
    public Pose2d getBotPose2d_wpiBlue() {
      return toPose2D(botpose_wpiblue);
    }
    ```

### `public LimelightResults()`

[Source lines 357–367](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L357)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- It changes object/subclass state through `botpose`, `botpose_wpiblue`, `botpose_wpired`, `camerapose_robotspace`, `targets_Barcode`, `targets_Classifier`, `targets_Detector`, `targets_Fiducials`, `targets_Retro`.

**Inputs:** None.

**Result:** Constructs and initializes a `LimelightResults` instance.

??? example "Implementation (source lines 357–367)"

    ```java
    public LimelightResults() {
      botpose = new double[6];
      botpose_wpired = new double[6];
      botpose_wpiblue = new double[6];
      camerapose_robotspace = new double[6];
      targets_Retro = new LimelightTarget_Retro[0];
      targets_Fiducials = new LimelightTarget_Fiducial[0];
      targets_Classifier = new LimelightTarget_Classifier[0];
      targets_Detector = new LimelightTarget_Detector[0];
      targets_Barcode = new LimelightTarget_Barcode[0];
    }
    ```

### `public RawFiducial( int id, double txnc, double tync, double ta, double distToCamera, double distToRobot, double ambiguity)`

[Source lines 379–394](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L379)

**Detailed behavior**

- The implementation executes 7 non-blank source lines.
- It changes object/subclass state through `ambiguity`, `distToCamera`, `distToRobot`, `id`, `ta`, `txnc`, `tync`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | `int` | `int` input consumed by the implementation shown below. |
| `txnc` | `double` | `double` input consumed by the implementation shown below. |
| `tync` | `double` | `double` input consumed by the implementation shown below. |
| `ta` | `double` | `double` input consumed by the implementation shown below. |
| `distToCamera` | `double` | `double` input consumed by the implementation shown below. |
| `distToRobot` | `double` | `double` input consumed by the implementation shown below. |
| `ambiguity` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `RawFiducial` instance.

??? example "Implementation (source lines 379–394)"

    ```java
    public RawFiducial(
        int id,
        double txnc,
        double tync,
        double ta,
        double distToCamera,
        double distToRobot,
        double ambiguity) {
      this.id = id;
      this.txnc = txnc;
      this.tync = tync;
      this.ta = ta;
      this.distToCamera = distToCamera;
      this.distToRobot = distToRobot;
      this.ambiguity = ambiguity;
    }
    ```

### `public RawDetection( int classId, double txnc, double tync, double ta, double corner0_X, double corner0_Y, double corner1_X, double corner1_Y, double corner2_X, double corner2_Y, double corner3_X, double corner3_Y)`

[Source lines 411–436](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L411)

**Detailed behavior**

- The implementation executes 12 non-blank source lines.
- It changes object/subclass state through `classId`, `corner0_X`, `corner0_Y`, `corner1_X`, `corner1_Y`, `corner2_X`, `corner2_Y`, `corner3_X`, `corner3_Y`, `ta`, `txnc`, `tync`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `classId` | `int` | `int` input consumed by the implementation shown below. |
| `txnc` | `double` | `double` input consumed by the implementation shown below. |
| `tync` | `double` | `double` input consumed by the implementation shown below. |
| `ta` | `double` | `double` input consumed by the implementation shown below. |
| `corner0_X` | `double` | `double` input consumed by the implementation shown below. |
| `corner0_Y` | `double` | `double` input consumed by the implementation shown below. |
| `corner1_X` | `double` | `double` input consumed by the implementation shown below. |
| `corner1_Y` | `double` | `double` input consumed by the implementation shown below. |
| `corner2_X` | `double` | `double` input consumed by the implementation shown below. |
| `corner2_Y` | `double` | `double` input consumed by the implementation shown below. |
| `corner3_X` | `double` | `double` input consumed by the implementation shown below. |
| `corner3_Y` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `RawDetection` instance.

??? example "Implementation (source lines 411–436)"

    ```java
    public RawDetection(
        int classId,
        double txnc,
        double tync,
        double ta,
        double corner0_X,
        double corner0_Y,
        double corner1_X,
        double corner1_Y,
        double corner2_X,
        double corner2_Y,
        double corner3_X,
        double corner3_Y) {
      this.classId = classId;
      this.txnc = txnc;
      this.tync = tync;
      this.ta = ta;
      this.corner0_X = corner0_X;
      this.corner0_Y = corner0_Y;
      this.corner1_X = corner1_X;
      this.corner1_Y = corner1_Y;
      this.corner2_X = corner2_X;
      this.corner2_Y = corner2_Y;
      this.corner3_X = corner3_X;
      this.corner3_Y = corner3_Y;
    }
    ```

### `public PoseEstimate()`

[Source lines 450–459](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L450)

**Detailed behavior**

- The implementation executes 8 non-blank source lines.
- It changes object/subclass state through `avgTagArea`, `avgTagDist`, `latency`, `pose`, `rawFiducials`, `tagCount`, `tagSpan`, `timestampSeconds`.

**Inputs:** None.

**Result:** Constructs and initializes a `PoseEstimate` instance.

??? example "Implementation (source lines 450–459)"

    ```java
    public PoseEstimate() {
      this.pose = Pose2d.kZero;
      this.timestampSeconds = 0;
      this.latency = 0;
      this.tagCount = 0;
      this.tagSpan = 0;
      this.avgTagDist = 0;
      this.avgTagArea = 0;
      this.rawFiducials = new RawFiducial[] {};
    }
    ```

??? note "Author note from JavaDoc"

    Makes a PoseEstimate object with default values

### `public PoseEstimate( Pose2d pose, double timestampSeconds, double latency, int tagCount, double tagSpan, double avgTagDist, double avgTagArea, RawFiducial[] rawFiducials)`

[Source lines 461–479](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L461)

**Detailed behavior**

- The implementation executes 8 non-blank source lines.
- It changes object/subclass state through `avgTagArea`, `avgTagDist`, `latency`, `pose`, `rawFiducials`, `tagCount`, `tagSpan`, `timestampSeconds`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pose` | `Pose2d` | `Pose2d` input consumed by the implementation shown below. |
| `timestampSeconds` | `double` | Time value in seconds. |
| `latency` | `double` | `double` input consumed by the implementation shown below. |
| `tagCount` | `int` | `int` input consumed by the implementation shown below. |
| `tagSpan` | `double` | `double` input consumed by the implementation shown below. |
| `avgTagDist` | `double` | `double` input consumed by the implementation shown below. |
| `avgTagArea` | `double` | `double` input consumed by the implementation shown below. |
| `rawFiducials` | `RawFiducial[]` | `RawFiducial[]` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `PoseEstimate` instance.

??? example "Implementation (source lines 461–479)"

    ```java
    public PoseEstimate(
        Pose2d pose,
        double timestampSeconds,
        double latency,
        int tagCount,
        double tagSpan,
        double avgTagDist,
        double avgTagArea,
        RawFiducial[] rawFiducials) {
    
      this.pose = pose;
      this.timestampSeconds = timestampSeconds;
      this.latency = latency;
      this.tagCount = tagCount;
      this.tagSpan = tagSpan;
      this.avgTagDist = avgTagDist;
      this.avgTagArea = avgTagArea;
      this.rawFiducials = rawFiducials;
    }
    ```

### `public static Pose3d toPose3D(double[] inData)`

[Source lines 494–505](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L494)

**Detailed behavior**

- The implementation executes 10 non-blank source lines.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- It has 1 conditional path: `inData.length < 6`.
- Return paths: `Pose3d.kZero`; `new Pose3d( new Translation3d(inData[0], inData[1], inData[2]), new Rotation3d( Units.degreesToRadians(inData[3]), Units.degreesToRadians(inData[4]), Units.degreesToRadians(inData…`.
- Key collaborators/calls: `Pose3d()`, `Translation3d()`, `Rotation3d()`, `Units.degreesToRadians()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `inData` | `double[]` | `double[]` input consumed by the implementation shown below. |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 494–505)"

    ```java
    public static Pose3d toPose3D(double[] inData) {
      if (inData.length < 6) {
        // System.err.println("Bad LL 3D Pose Data!");
        return Pose3d.kZero;
      }
      return new Pose3d(
          new Translation3d(inData[0], inData[1], inData[2]),
          new Rotation3d(
              Units.degreesToRadians(inData[3]),
              Units.degreesToRadians(inData[4]),
              Units.degreesToRadians(inData[5])));
    }
    ```

### `public static Pose2d toPose2D(double[] inData)`

[Source lines 507–515](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L507)

**Detailed behavior**

- The implementation executes 7 non-blank source lines.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- It has 1 conditional path: `inData.length < 6`.
- Return paths: `Pose2d.kZero`; `new Pose2d(tran2d, r2d)`.
- Key collaborators/calls: `Translation2d()`, `Rotation2d()`, `Units.degreesToRadians()`, `Pose2d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `inData` | `double[]` | `double[]` input consumed by the implementation shown below. |

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 507–515)"

    ```java
    public static Pose2d toPose2D(double[] inData) {
      if (inData.length < 6) {
        // System.err.println("Bad LL 2D Pose Data!");
        return Pose2d.kZero;
      }
      Translation2d tran2d = new Translation2d(inData[0], inData[1]);
      Rotation2d r2d = new Rotation2d(Units.degreesToRadians(inData[5]));
      return new Pose2d(tran2d, r2d);
    }
    ```

### `public static double[] pose3dToArray(Pose3d pose)`

[Source lines 523–532](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L523)

**Detailed behavior**

- The implementation executes 8 non-blank source lines.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Return path: `result`.
- Key collaborators/calls: `pose.getTranslation()`, `getX()`, `getY()`, `getZ()`, `Units.radiansToDegrees()`, `pose.getRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pose` | `Pose3d` | The Pose3d object to convert. **Returns:** The array of doubles representing the pose. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 523–532)"

    ```java
    public static double[] pose3dToArray(Pose3d pose) {
      double[] result = new double[6];
      result[0] = pose.getTranslation().getX();
      result[1] = pose.getTranslation().getY();
      result[2] = pose.getTranslation().getZ();
      result[3] = Units.radiansToDegrees(pose.getRotation().getX());
      result[4] = Units.radiansToDegrees(pose.getRotation().getY());
      result[5] = Units.radiansToDegrees(pose.getRotation().getZ());
      return result;
    }
    ```

??? note "Author note from JavaDoc"

    Converts a Pose3d object to an array of doubles.
    
    **Parameter `pose`:** The Pose3d object to convert.
    **Returns:** The array of doubles representing the pose.

### `public static double[] pose2dToArray(Pose2d pose)`

[Source lines 540–549](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L540)

**Detailed behavior**

- The implementation executes 8 non-blank source lines.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Return path: `result`.
- Key collaborators/calls: `pose.getTranslation()`, `getX()`, `getY()`, `Units.radiansToDegrees()`, `pose.getRotation()`, `getRadians()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pose` | `Pose2d` | The Pose2d object to convert. **Returns:** The array of doubles representing the pose. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 540–549)"

    ```java
    public static double[] pose2dToArray(Pose2d pose) {
      double[] result = new double[6];
      result[0] = pose.getTranslation().getX();
      result[1] = pose.getTranslation().getY();
      result[2] = 0;
      result[3] = Units.radiansToDegrees(0);
      result[4] = Units.radiansToDegrees(0);
      result[5] = Units.radiansToDegrees(pose.getRotation().getRadians());
      return result;
    }
    ```

??? note "Author note from JavaDoc"

    Converts a Pose2d object to an array of doubles.
    
    **Parameter `pose`:** The Pose2d object to convert.
    **Returns:** The array of doubles representing the pose.

### `public static RawFiducial[] getRawFiducials(String limelightName)`

[Source lines 605–630](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L605)

**Detailed behavior**

- The implementation executes 20 non-blank source lines.
- It changes object/subclass state through `ambiguity`, `distToCamera`, `distToRobot`, `id`, `rawFiducials`, `ta`, `txnc`, `tync`.
- It has 1 conditional path: `rawFiducialArray.length % valsPerEntry != 0`.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return paths: `new RawFiducial[0]`; `rawFiducials`.
- Key collaborators/calls: `LimelightHelpers.getLimelightNTTableEntry()`, `entry.getDoubleArray()`, `extractArrayEntry()`, `RawFiducial()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `RawFiducial[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 605–630)"

    ```java
    public static RawFiducial[] getRawFiducials(String limelightName) {
      var entry = LimelightHelpers.getLimelightNTTableEntry(limelightName, "rawfiducials");
      var rawFiducialArray = entry.getDoubleArray(new double[0]);
      int valsPerEntry = 7;
      if (rawFiducialArray.length % valsPerEntry != 0) {
        return new RawFiducial[0];
      }
    
      int numFiducials = rawFiducialArray.length / valsPerEntry;
      RawFiducial[] rawFiducials = new RawFiducial[numFiducials];
    
      for (int i = 0; i < numFiducials; i++) {
        int baseIndex = i * valsPerEntry;
        int id = (int) extractArrayEntry(rawFiducialArray, baseIndex);
        double txnc = extractArrayEntry(rawFiducialArray, baseIndex + 1);
        double tync = extractArrayEntry(rawFiducialArray, baseIndex + 2);
        double ta = extractArrayEntry(rawFiducialArray, baseIndex + 3);
        double distToCamera = extractArrayEntry(rawFiducialArray, baseIndex + 4);
        double distToRobot = extractArrayEntry(rawFiducialArray, baseIndex + 5);
        double ambiguity = extractArrayEntry(rawFiducialArray, baseIndex + 6);
    
        rawFiducials[i] = new RawFiducial(id, txnc, tync, ta, distToCamera, distToRobot, ambiguity);
      }
    
      return rawFiducials;
    }
    ```

### `public static RawDetection[] getRawDetections(String limelightName)`

[Source lines 632–665](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L632)

**Detailed behavior**

- The implementation executes 28 non-blank source lines.
- It changes object/subclass state through `classId`, `corner0_X`, `corner0_Y`, `corner1_X`, `corner1_Y`, `corner2_X`, `corner2_Y`, `corner3_X`, `corner3_Y`, `ta`, `txnc`, `tync`.
- It has 1 conditional path: `rawDetectionArray.length % valsPerEntry != 0`.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return paths: `new RawDetection[0]`; `rawDetections`.
- Key collaborators/calls: `LimelightHelpers.getLimelightNTTableEntry()`, `entry.getDoubleArray()`, `extractArrayEntry()`, `RawDetection()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `RawDetection[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 632–665)"

    ```java
    public static RawDetection[] getRawDetections(String limelightName) {
      var entry = LimelightHelpers.getLimelightNTTableEntry(limelightName, "rawdetections");
      var rawDetectionArray = entry.getDoubleArray(new double[0]);
      int valsPerEntry = 11;
      if (rawDetectionArray.length % valsPerEntry != 0) {
        return new RawDetection[0];
      }
    
      int numDetections = rawDetectionArray.length / valsPerEntry;
      RawDetection[] rawDetections = new RawDetection[numDetections];
    
      for (int i = 0; i < numDetections; i++) {
        int baseIndex = i * valsPerEntry; // Starting index for this detection's data
        int classId = (int) extractArrayEntry(rawDetectionArray, baseIndex);
        double txnc = extractArrayEntry(rawDetectionArray, baseIndex + 1);
        double tync = extractArrayEntry(rawDetectionArray, baseIndex + 2);
        double ta = extractArrayEntry(rawDetectionArray, baseIndex + 3);
        double corner0_X = extractArrayEntry(rawDetectionArray, baseIndex + 4);
        double corner0_Y = extractArrayEntry(rawDetectionArray, baseIndex + 5);
        double corner1_X = extractArrayEntry(rawDetectionArray, baseIndex + 6);
        double corner1_Y = extractArrayEntry(rawDetectionArray, baseIndex + 7);
        double corner2_X = extractArrayEntry(rawDetectionArray, baseIndex + 8);
        double corner2_Y = extractArrayEntry(rawDetectionArray, baseIndex + 9);
        double corner3_X = extractArrayEntry(rawDetectionArray, baseIndex + 10);
        double corner3_Y = extractArrayEntry(rawDetectionArray, baseIndex + 11);
    
        rawDetections[i] =
            new RawDetection(
                classId, txnc, tync, ta, corner0_X, corner0_Y, corner1_X, corner1_Y, corner2_X,
                corner2_Y, corner3_X, corner3_Y);
      }
    
      return rawDetections;
    }
    ```

### `public static void printPoseEstimate(PoseEstimate pose)`

[Source lines 667–700](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L667)

**Detailed behavior**

- The implementation executes 29 non-blank source lines.
- It changes object/subclass state through `pose`.
- It has 2 conditional paths: `pose == null`; `pose.rawFiducials == null || pose.rawFiducials.length == 0`.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `System.out.println()`, `System.out.printf()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pose` | `PoseEstimate` | `PoseEstimate` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 667–700)"

    ```java
    public static void printPoseEstimate(PoseEstimate pose) {
      if (pose == null) {
        System.out.println("No PoseEstimate available.");
        return;
      }
    
      System.out.printf("Pose Estimate Information:%n");
      System.out.printf("Timestamp (Seconds): %.3f%n", pose.timestampSeconds);
      System.out.printf("Latency: %.3f ms%n", pose.latency);
      System.out.printf("Tag Count: %d%n", pose.tagCount);
      System.out.printf("Tag Span: %.2f meters%n", pose.tagSpan);
      System.out.printf("Average Tag Distance: %.2f meters%n", pose.avgTagDist);
      System.out.printf("Average Tag Area: %.2f%% of image%n", pose.avgTagArea);
      System.out.println();
    
      if (pose.rawFiducials == null || pose.rawFiducials.length == 0) {
        System.out.println("No RawFiducials data available.");
        return;
      }
    
      System.out.println("Raw Fiducials Details:");
      for (int i = 0; i < pose.rawFiducials.length; i++) {
        RawFiducial fiducial = pose.rawFiducials[i];
        System.out.printf(" Fiducial #%d:%n", i + 1);
        System.out.printf("  ID: %d%n", fiducial.id);
        System.out.printf("  TXNC: %.2f%n", fiducial.txnc);
        System.out.printf("  TYNC: %.2f%n", fiducial.tync);
        System.out.printf("  TA: %.2f%n", fiducial.ta);
        System.out.printf("  Distance to Camera: %.2f meters%n", fiducial.distToCamera);
        System.out.printf("  Distance to Robot: %.2f meters%n", fiducial.distToRobot);
        System.out.printf("  Ambiguity: %.2f%n", fiducial.ambiguity);
        System.out.println();
      }
    }
    ```

### `public static NetworkTable getLimelightNTTable(String tableName)`

[Source lines 702–704](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L702)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It reads or writes NetworkTables data, so the result depends on live robot/network state.
- Return path: `NetworkTableInstance.getDefault().getTable(sanitizeName(tableName))`.
- Key collaborators/calls: `NetworkTableInstance.getDefault()`, `getTable()`, `sanitizeName()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `NetworkTable`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 702–704)"

    ```java
    public static NetworkTable getLimelightNTTable(String tableName) {
      return NetworkTableInstance.getDefault().getTable(sanitizeName(tableName));
    }
    ```

### `public static void Flush()`

[Source lines 706–708](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L706)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It reads or writes NetworkTables data, so the result depends on live robot/network state.
- Key collaborators/calls: `NetworkTableInstance.getDefault()`, `flush()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 706–708)"

    ```java
    public static void Flush() {
      NetworkTableInstance.getDefault().flush();
    }
    ```

### `public static NetworkTableEntry getLimelightNTTableEntry(String tableName, String entryName)`

[Source lines 710–712](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L710)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It reads or writes NetworkTables data, so the result depends on live robot/network state.
- Return path: `getLimelightNTTable(tableName).getEntry(entryName)`.
- Key collaborators/calls: `getLimelightNTTable()`, `getEntry()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `entryName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `NetworkTableEntry`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 710–712)"

    ```java
    public static NetworkTableEntry getLimelightNTTableEntry(String tableName, String entryName) {
      return getLimelightNTTable(tableName).getEntry(entryName);
    }
    ```

### `public static DoubleArrayEntry getLimelightDoubleArrayEntry(String tableName, String entryName)`

[Source lines 714–722](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L714)

**Detailed behavior**

- The implementation executes 7 non-blank source lines.
- It reads or writes NetworkTables data, so the result depends on live robot/network state.
- Return paths: `doubleArrayEntries.computeIfAbsent( key, k -> { NetworkTable table = getLimelightNTTable(tableName)`; `table.getDoubleArrayTopic(entryName).getEntry(new double[0])`.
- Key collaborators/calls: `doubleArrayEntries.computeIfAbsent()`, `getLimelightNTTable()`, `table.getDoubleArrayTopic()`, `getEntry()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `entryName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `DoubleArrayEntry`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 714–722)"

    ```java
    public static DoubleArrayEntry getLimelightDoubleArrayEntry(String tableName, String entryName) {
      String key = tableName + "/" + entryName;
      return doubleArrayEntries.computeIfAbsent(
          key,
          k -> {
            NetworkTable table = getLimelightNTTable(tableName);
            return table.getDoubleArrayTopic(entryName).getEntry(new double[0]);
          });
    }
    ```

### `public static double getLimelightNTDouble(String tableName, String entryName)`

[Source lines 724–726](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L724)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTTableEntry(tableName, entryName).getDouble(0.0)`.
- Key collaborators/calls: `getLimelightNTTableEntry()`, `getDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `entryName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 724–726)"

    ```java
    public static double getLimelightNTDouble(String tableName, String entryName) {
      return getLimelightNTTableEntry(tableName, entryName).getDouble(0.0);
    }
    ```

### `public static void setLimelightNTDouble(String tableName, String entryName, double val)`

[Source lines 728–730](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L728)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It reads or writes NetworkTables data, so the result depends on live robot/network state.
- Key collaborators/calls: `getLimelightNTTableEntry()`, `setDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `entryName` | `String` | `String` input consumed by the implementation shown below. |
| `val` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 728–730)"

    ```java
    public static void setLimelightNTDouble(String tableName, String entryName, double val) {
      getLimelightNTTableEntry(tableName, entryName).setDouble(val);
    }
    ```

### `public static void setLimelightNTDoubleArray(String tableName, String entryName, double[] val)`

[Source lines 732–734](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L732)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It reads or writes NetworkTables data, so the result depends on live robot/network state.
- Key collaborators/calls: `getLimelightNTTableEntry()`, `setDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `entryName` | `String` | `String` input consumed by the implementation shown below. |
| `val` | `double[]` | `double[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 732–734)"

    ```java
    public static void setLimelightNTDoubleArray(String tableName, String entryName, double[] val) {
      getLimelightNTTableEntry(tableName, entryName).setDoubleArray(val);
    }
    ```

### `public static double[] getLimelightNTDoubleArray(String tableName, String entryName)`

[Source lines 736–738](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L736)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTTableEntry(tableName, entryName).getDoubleArray(new double[0])`.
- Key collaborators/calls: `getLimelightNTTableEntry()`, `getDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `entryName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 736–738)"

    ```java
    public static double[] getLimelightNTDoubleArray(String tableName, String entryName) {
      return getLimelightNTTableEntry(tableName, entryName).getDoubleArray(new double[0]);
    }
    ```

### `public static String getLimelightNTString(String tableName, String entryName)`

[Source lines 740–742](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L740)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTTableEntry(tableName, entryName).getString("")`.
- Key collaborators/calls: `getLimelightNTTableEntry()`, `getString()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `entryName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 740–742)"

    ```java
    public static String getLimelightNTString(String tableName, String entryName) {
      return getLimelightNTTableEntry(tableName, entryName).getString("");
    }
    ```

### `public static String[] getLimelightNTStringArray(String tableName, String entryName)`

[Source lines 744–746](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L744)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTTableEntry(tableName, entryName).getStringArray(new String[0])`.
- Key collaborators/calls: `getLimelightNTTableEntry()`, `getStringArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `entryName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `String[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 744–746)"

    ```java
    public static String[] getLimelightNTStringArray(String tableName, String entryName) {
      return getLimelightNTTableEntry(tableName, entryName).getStringArray(new String[0]);
    }
    ```

### `public static URL getLimelightURLString(String tableName, String request)`

[Source lines 748–758](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L748)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- Return paths: `url`; `null`.
- Key collaborators/calls: `sanitizeName()`, `URL()`, `System.err.println()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `request` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `URL`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 748–758)"

    ```java
    public static URL getLimelightURLString(String tableName, String request) {
      String urlString = "http://" + sanitizeName(tableName) + ".local:5807/" + request;
      URL url;
      try {
        url = new URL(urlString);
        return url;
      } catch (MalformedURLException e) {
        System.err.println("bad LL URL");
      }
      return null;
    }
    ```

### `public static double getTX(String limelightName)`

[Source lines 763–765](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L763)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDouble(limelightName, "tx")`.
- Key collaborators/calls: `getLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 763–765)"

    ```java
    public static double getTX(String limelightName) {
      return getLimelightNTDouble(limelightName, "tx");
    }
    ```

### `public static double getTY(String limelightName)`

[Source lines 767–769](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L767)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDouble(limelightName, "ty")`.
- Key collaborators/calls: `getLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 767–769)"

    ```java
    public static double getTY(String limelightName) {
      return getLimelightNTDouble(limelightName, "ty");
    }
    ```

### `public static double getTA(String limelightName)`

[Source lines 771–773](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L771)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDouble(limelightName, "ta")`.
- Key collaborators/calls: `getLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 771–773)"

    ```java
    public static double getTA(String limelightName) {
      return getLimelightNTDouble(limelightName, "ta");
    }
    ```

### `public static double[] getT2DArray(String limelightName)`

[Source lines 775–777](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L775)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "t2d")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 775–777)"

    ```java
    public static double[] getT2DArray(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "t2d");
    }
    ```

### `public static int getTargetCount(String limelightName)`

[Source lines 779–785](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L779)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It has 1 conditional path: `t2d.length == 17`.
- Return paths: `(int) t2d[1]`; `0`.
- Key collaborators/calls: `getT2DArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `int`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 779–785)"

    ```java
    public static int getTargetCount(String limelightName) {
      double[] t2d = getT2DArray(limelightName);
      if (t2d.length == 17) {
        return (int) t2d[1];
      }
      return 0;
    }
    ```

### `public static int getClassifierClassIndex(String limelightName)`

[Source lines 787–793](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L787)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It has 1 conditional path: `t2d.length == 17`.
- Return paths: `(int) t2d[10]`; `0`.
- Key collaborators/calls: `getT2DArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `int`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 787–793)"

    ```java
    public static int getClassifierClassIndex(String limelightName) {
      double[] t2d = getT2DArray(limelightName);
      if (t2d.length == 17) {
        return (int) t2d[10];
      }
      return 0;
    }
    ```

### `public static int getDetectorClassIndex(String limelightName)`

[Source lines 795–801](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L795)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It has 1 conditional path: `t2d.length == 17`.
- Return paths: `(int) t2d[11]`; `0`.
- Key collaborators/calls: `getT2DArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `int`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 795–801)"

    ```java
    public static int getDetectorClassIndex(String limelightName) {
      double[] t2d = getT2DArray(limelightName);
      if (t2d.length == 17) {
        return (int) t2d[11];
      }
      return 0;
    }
    ```

### `public static String getClassifierClass(String limelightName)`

[Source lines 803–805](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L803)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTString(limelightName, "tcclass")`.
- Key collaborators/calls: `getLimelightNTString()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 803–805)"

    ```java
    public static String getClassifierClass(String limelightName) {
      return getLimelightNTString(limelightName, "tcclass");
    }
    ```

### `public static String getDetectorClass(String limelightName)`

[Source lines 807–809](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L807)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTString(limelightName, "tdclass")`.
- Key collaborators/calls: `getLimelightNTString()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 807–809)"

    ```java
    public static String getDetectorClass(String limelightName) {
      return getLimelightNTString(limelightName, "tdclass");
    }
    ```

### `public static double getLatency_Pipeline(String limelightName)`

[Source lines 811–813](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L811)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDouble(limelightName, "tl")`.
- Key collaborators/calls: `getLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 811–813)"

    ```java
    public static double getLatency_Pipeline(String limelightName) {
      return getLimelightNTDouble(limelightName, "tl");
    }
    ```

### `public static double getLatency_Capture(String limelightName)`

[Source lines 815–817](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L815)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDouble(limelightName, "cl")`.
- Key collaborators/calls: `getLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 815–817)"

    ```java
    public static double getLatency_Capture(String limelightName) {
      return getLimelightNTDouble(limelightName, "cl");
    }
    ```

### `public static double getCurrentPipelineIndex(String limelightName)`

[Source lines 819–821](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L819)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDouble(limelightName, "getpipe")`.
- Key collaborators/calls: `getLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 819–821)"

    ```java
    public static double getCurrentPipelineIndex(String limelightName) {
      return getLimelightNTDouble(limelightName, "getpipe");
    }
    ```

### `public static String getCurrentPipelineType(String limelightName)`

[Source lines 823–825](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L823)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTString(limelightName, "getpipetype")`.
- Key collaborators/calls: `getLimelightNTString()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 823–825)"

    ```java
    public static String getCurrentPipelineType(String limelightName) {
      return getLimelightNTString(limelightName, "getpipetype");
    }
    ```

### `public static String getJSONDump(String limelightName)`

[Source lines 827–829](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L827)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTString(limelightName, "json")`.
- Key collaborators/calls: `getLimelightNTString()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 827–829)"

    ```java
    public static String getJSONDump(String limelightName) {
      return getLimelightNTString(limelightName, "json");
    }
    ```

### `public static double[] getBotpose(String limelightName)`

[Source lines 838–840](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L838)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "botpose")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | **return |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 838–840)"

    ```java
    public static double[] getBotpose(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "botpose");
    }
    ```

??? note "Author note from JavaDoc"

    Switch to getBotPose
    
    **Parameter `limelightName`:** 
    **return

### `public static double[] getBotpose_wpiRed(String limelightName)`

[Source lines 849–851](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L849)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "botpose_wpired")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | **return |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 849–851)"

    ```java
    public static double[] getBotpose_wpiRed(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "botpose_wpired");
    }
    ```

??? note "Author note from JavaDoc"

    Switch to getBotPose_wpiRed
    
    **Parameter `limelightName`:** 
    **return

### `public static double[] getBotpose_wpiBlue(String limelightName)`

[Source lines 860–862](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L860)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "botpose_wpiblue")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | **return |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 860–862)"

    ```java
    public static double[] getBotpose_wpiBlue(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "botpose_wpiblue");
    }
    ```

??? note "Author note from JavaDoc"

    Switch to getBotPose_wpiBlue
    
    **Parameter `limelightName`:** 
    **return

### `public static double[] getBotPose(String limelightName)`

[Source lines 864–866](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L864)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "botpose")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 864–866)"

    ```java
    public static double[] getBotPose(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "botpose");
    }
    ```

### `public static double[] getBotPose_wpiRed(String limelightName)`

[Source lines 868–870](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L868)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "botpose_wpired")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 868–870)"

    ```java
    public static double[] getBotPose_wpiRed(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "botpose_wpired");
    }
    ```

### `public static double[] getBotPose_wpiBlue(String limelightName)`

[Source lines 872–874](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L872)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "botpose_wpiblue")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 872–874)"

    ```java
    public static double[] getBotPose_wpiBlue(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "botpose_wpiblue");
    }
    ```

### `public static double[] getBotPose_TargetSpace(String limelightName)`

[Source lines 876–878](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L876)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "botpose_targetspace")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 876–878)"

    ```java
    public static double[] getBotPose_TargetSpace(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "botpose_targetspace");
    }
    ```

### `public static double[] getCameraPose_TargetSpace(String limelightName)`

[Source lines 880–882](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L880)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "camerapose_targetspace")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 880–882)"

    ```java
    public static double[] getCameraPose_TargetSpace(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "camerapose_targetspace");
    }
    ```

### `public static double[] getTargetPose_CameraSpace(String limelightName)`

[Source lines 884–886](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L884)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "targetpose_cameraspace")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 884–886)"

    ```java
    public static double[] getTargetPose_CameraSpace(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "targetpose_cameraspace");
    }
    ```

### `public static double[] getTargetPose_RobotSpace(String limelightName)`

[Source lines 888–890](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L888)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "targetpose_robotspace")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 888–890)"

    ```java
    public static double[] getTargetPose_RobotSpace(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "targetpose_robotspace");
    }
    ```

### `public static double[] getTargetColor(String limelightName)`

[Source lines 892–894](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L892)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "tc")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 892–894)"

    ```java
    public static double[] getTargetColor(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "tc");
    }
    ```

### `public static double getFiducialID(String limelightName)`

[Source lines 896–898](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L896)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDouble(limelightName, "tid")`.
- Key collaborators/calls: `getLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 896–898)"

    ```java
    public static double getFiducialID(String limelightName) {
      return getLimelightNTDouble(limelightName, "tid");
    }
    ```

### `public static String getNeuralClassID(String limelightName)`

[Source lines 900–902](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L900)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTString(limelightName, "tclass")`.
- Key collaborators/calls: `getLimelightNTString()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 900–902)"

    ```java
    public static String getNeuralClassID(String limelightName) {
      return getLimelightNTString(limelightName, "tclass");
    }
    ```

### `public static String[] getRawBarcodeData(String limelightName)`

[Source lines 904–906](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L904)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTStringArray(limelightName, "rawbarcodes")`.
- Key collaborators/calls: `getLimelightNTStringArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `String[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 904–906)"

    ```java
    public static String[] getRawBarcodeData(String limelightName) {
      return getLimelightNTStringArray(limelightName, "rawbarcodes");
    }
    ```

### `public static Pose3d getBotPose3d(String limelightName)`

[Source lines 911–914](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L911)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `toPose3D(poseArray)`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`, `toPose3D()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 911–914)"

    ```java
    public static Pose3d getBotPose3d(String limelightName) {
      double[] poseArray = getLimelightNTDoubleArray(limelightName, "botpose");
      return toPose3D(poseArray);
    }
    ```

### `public static Pose3d getBotPose3d_wpiRed(String limelightName)`

[Source lines 916–919](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L916)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `toPose3D(poseArray)`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`, `toPose3D()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 916–919)"

    ```java
    public static Pose3d getBotPose3d_wpiRed(String limelightName) {
      double[] poseArray = getLimelightNTDoubleArray(limelightName, "botpose_wpired");
      return toPose3D(poseArray);
    }
    ```

### `public static Pose3d getBotPose3d_wpiBlue(String limelightName)`

[Source lines 921–924](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L921)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `toPose3D(poseArray)`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`, `toPose3D()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 921–924)"

    ```java
    public static Pose3d getBotPose3d_wpiBlue(String limelightName) {
      double[] poseArray = getLimelightNTDoubleArray(limelightName, "botpose_wpiblue");
      return toPose3D(poseArray);
    }
    ```

### `public static Pose3d getBotPose3d_TargetSpace(String limelightName)`

[Source lines 926–929](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L926)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `toPose3D(poseArray)`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`, `toPose3D()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 926–929)"

    ```java
    public static Pose3d getBotPose3d_TargetSpace(String limelightName) {
      double[] poseArray = getLimelightNTDoubleArray(limelightName, "botpose_targetspace");
      return toPose3D(poseArray);
    }
    ```

### `public static Pose3d getCameraPose3d_TargetSpace(String limelightName)`

[Source lines 931–934](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L931)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `toPose3D(poseArray)`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`, `toPose3D()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 931–934)"

    ```java
    public static Pose3d getCameraPose3d_TargetSpace(String limelightName) {
      double[] poseArray = getLimelightNTDoubleArray(limelightName, "camerapose_targetspace");
      return toPose3D(poseArray);
    }
    ```

### `public static Pose3d getTargetPose3d_CameraSpace(String limelightName)`

[Source lines 936–939](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L936)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `toPose3D(poseArray)`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`, `toPose3D()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 936–939)"

    ```java
    public static Pose3d getTargetPose3d_CameraSpace(String limelightName) {
      double[] poseArray = getLimelightNTDoubleArray(limelightName, "targetpose_cameraspace");
      return toPose3D(poseArray);
    }
    ```

### `public static Pose3d getTargetPose3d_RobotSpace(String limelightName)`

[Source lines 941–944](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L941)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `toPose3D(poseArray)`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`, `toPose3D()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 941–944)"

    ```java
    public static Pose3d getTargetPose3d_RobotSpace(String limelightName) {
      double[] poseArray = getLimelightNTDoubleArray(limelightName, "targetpose_robotspace");
      return toPose3D(poseArray);
    }
    ```

### `public static Pose3d getCameraPose3d_RobotSpace(String limelightName)`

[Source lines 946–949](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L946)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `toPose3D(poseArray)`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`, `toPose3D()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 946–949)"

    ```java
    public static Pose3d getCameraPose3d_RobotSpace(String limelightName) {
      double[] poseArray = getLimelightNTDoubleArray(limelightName, "camerapose_robotspace");
      return toPose3D(poseArray);
    }
    ```

### `public static Pose2d getBotPose2d_wpiBlue(String limelightName)`

[Source lines 957–961](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L957)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `toPose2D(result)`.
- Key collaborators/calls: `getBotPose_wpiBlue()`, `toPose2D()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | **return |

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 957–961)"

    ```java
    public static Pose2d getBotPose2d_wpiBlue(String limelightName) {
    
      double[] result = getBotPose_wpiBlue(limelightName);
      return toPose2D(result);
    }
    ```

??? note "Author note from JavaDoc"

    Gets the Pose2d for easy use with Odometry vision pose estimator (addVisionMeasurement)
    
    **Parameter `limelightName`:** 
    **return

### `public static PoseEstimate getBotPoseEstimate_wpiBlue(String limelightName)`

[Source lines 970–972](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L970)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getBotPoseEstimate(limelightName, "botpose_wpiblue")`.
- Key collaborators/calls: `getBotPoseEstimate()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | **return |

**Result:** Returns `PoseEstimate`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 970–972)"

    ```java
    public static PoseEstimate getBotPoseEstimate_wpiBlue(String limelightName) {
      return getBotPoseEstimate(limelightName, "botpose_wpiblue");
    }
    ```

??? note "Author note from JavaDoc"

    Gets the Pose2d and timestamp for use with WPILib pose estimator (addVisionMeasurement) when
    you are on the BLUE alliance
    
    **Parameter `limelightName`:** 
    **return

### `public static PoseEstimate getBotPoseEstimate_wpiBlue_MegaTag2(String limelightName)`

[Source lines 981–983](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L981)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getBotPoseEstimate(limelightName, "botpose_orb_wpiblue")`.
- Key collaborators/calls: `getBotPoseEstimate()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | **return |

**Result:** Returns `PoseEstimate`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 981–983)"

    ```java
    public static PoseEstimate getBotPoseEstimate_wpiBlue_MegaTag2(String limelightName) {
      return getBotPoseEstimate(limelightName, "botpose_orb_wpiblue");
    }
    ```

??? note "Author note from JavaDoc"

    Gets the Pose2d and timestamp for use with WPILib pose estimator (addVisionMeasurement) when
    you are on the BLUE alliance
    
    **Parameter `limelightName`:** 
    **return

### `public static Pose2d getBotPose2d_wpiRed(String limelightName)`

[Source lines 991–995](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L991)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `toPose2D(result)`.
- Key collaborators/calls: `getBotPose_wpiRed()`, `toPose2D()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | **return |

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 991–995)"

    ```java
    public static Pose2d getBotPose2d_wpiRed(String limelightName) {
    
      double[] result = getBotPose_wpiRed(limelightName);
      return toPose2D(result);
    }
    ```

??? note "Author note from JavaDoc"

    Gets the Pose2d for easy use with Odometry vision pose estimator (addVisionMeasurement)
    
    **Parameter `limelightName`:** 
    **return

### `public static PoseEstimate getBotPoseEstimate_wpiRed(String limelightName)`

[Source lines 1004–1006](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1004)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getBotPoseEstimate(limelightName, "botpose_wpired")`.
- Key collaborators/calls: `getBotPoseEstimate()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | **return |

**Result:** Returns `PoseEstimate`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 1004–1006)"

    ```java
    public static PoseEstimate getBotPoseEstimate_wpiRed(String limelightName) {
      return getBotPoseEstimate(limelightName, "botpose_wpired");
    }
    ```

??? note "Author note from JavaDoc"

    Gets the Pose2d and timestamp for use with WPILib pose estimator (addVisionMeasurement) when
    you are on the RED alliance
    
    **Parameter `limelightName`:** 
    **return

### `public static PoseEstimate getBotPoseEstimate_wpiRed_MegaTag2(String limelightName)`

[Source lines 1015–1017](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1015)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getBotPoseEstimate(limelightName, "botpose_orb_wpired")`.
- Key collaborators/calls: `getBotPoseEstimate()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | **return |

**Result:** Returns `PoseEstimate`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 1015–1017)"

    ```java
    public static PoseEstimate getBotPoseEstimate_wpiRed_MegaTag2(String limelightName) {
      return getBotPoseEstimate(limelightName, "botpose_orb_wpired");
    }
    ```

??? note "Author note from JavaDoc"

    Gets the Pose2d and timestamp for use with WPILib pose estimator (addVisionMeasurement) when
    you are on the RED alliance
    
    **Parameter `limelightName`:** 
    **return

### `public static Pose2d getBotPose2d(String limelightName)`

[Source lines 1025–1029](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1025)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `toPose2D(result)`.
- Key collaborators/calls: `getBotPose()`, `toPose2D()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | **return |

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 1025–1029)"

    ```java
    public static Pose2d getBotPose2d(String limelightName) {
    
      double[] result = getBotPose(limelightName);
      return toPose2D(result);
    }
    ```

??? note "Author note from JavaDoc"

    Gets the Pose2d for easy use with Odometry vision pose estimator (addVisionMeasurement)
    
    **Parameter `limelightName`:** 
    **return

### `public static boolean getTV(String limelightName)`

[Source lines 1031–1033](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1031)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `1.0 == getLimelightNTDouble(limelightName, "tv")`.
- Key collaborators/calls: `getLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 1031–1033)"

    ```java
    public static boolean getTV(String limelightName) {
      return 1.0 == getLimelightNTDouble(limelightName, "tv");
    }
    ```

### `public static void setPipelineIndex(String limelightName, int pipelineIndex)`

[Source lines 1038–1040](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1038)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |
| `pipelineIndex` | `int` | `int` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1038–1040)"

    ```java
    public static void setPipelineIndex(String limelightName, int pipelineIndex) {
      setLimelightNTDouble(limelightName, "pipeline", pipelineIndex);
    }
    ```

### `public static void setPriorityTagID(String limelightName, int ID)`

[Source lines 1042–1044](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1042)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |
| `ID` | `int` | `int` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1042–1044)"

    ```java
    public static void setPriorityTagID(String limelightName, int ID) {
      setLimelightNTDouble(limelightName, "priorityid", ID);
    }
    ```

### `public static void setLEDMode_PipelineControl(String limelightName)`

[Source lines 1047–1049](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1047)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1047–1049)"

    ```java
    public static void setLEDMode_PipelineControl(String limelightName) {
      setLimelightNTDouble(limelightName, "ledMode", 0);
    }
    ```

??? note "Author note from JavaDoc"

    The LEDs will be controlled by Limelight pipeline settings, and not by robot code.

### `public static void setLEDMode_ForceOff(String limelightName)`

[Source lines 1051–1053](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1051)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1051–1053)"

    ```java
    public static void setLEDMode_ForceOff(String limelightName) {
      setLimelightNTDouble(limelightName, "ledMode", 1);
    }
    ```

### `public static void setLEDMode_ForceBlink(String limelightName)`

[Source lines 1055–1057](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1055)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1055–1057)"

    ```java
    public static void setLEDMode_ForceBlink(String limelightName) {
      setLimelightNTDouble(limelightName, "ledMode", 2);
    }
    ```

### `public static void setLEDMode_ForceOn(String limelightName)`

[Source lines 1059–1061](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1059)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1059–1061)"

    ```java
    public static void setLEDMode_ForceOn(String limelightName) {
      setLimelightNTDouble(limelightName, "ledMode", 3);
    }
    ```

### `public static void setStreamMode_Standard(String limelightName)`

[Source lines 1063–1065](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1063)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1063–1065)"

    ```java
    public static void setStreamMode_Standard(String limelightName) {
      setLimelightNTDouble(limelightName, "stream", 0);
    }
    ```

### `public static void setStreamMode_PiPMain(String limelightName)`

[Source lines 1067–1069](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1067)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1067–1069)"

    ```java
    public static void setStreamMode_PiPMain(String limelightName) {
      setLimelightNTDouble(limelightName, "stream", 1);
    }
    ```

### `public static void setStreamMode_PiPSecondary(String limelightName)`

[Source lines 1071–1073](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1071)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1071–1073)"

    ```java
    public static void setStreamMode_PiPSecondary(String limelightName) {
      setLimelightNTDouble(limelightName, "stream", 2);
    }
    ```

### `public static void setCropWindow( String limelightName, double cropXMin, double cropXMax, double cropYMin, double cropYMax)`

[Source lines 1079–1087](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1079)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- Key collaborators/calls: `setLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |
| `cropXMin` | `double` | `double` input consumed by the implementation shown below. |
| `cropXMax` | `double` | `double` input consumed by the implementation shown below. |
| `cropYMin` | `double` | `double` input consumed by the implementation shown below. |
| `cropYMax` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1079–1087)"

    ```java
    public static void setCropWindow(
        String limelightName, double cropXMin, double cropXMax, double cropYMin, double cropYMax) {
      double[] entries = new double[4];
      entries[0] = cropXMin;
      entries[1] = cropXMax;
      entries[2] = cropYMin;
      entries[3] = cropYMax;
      setLimelightNTDoubleArray(limelightName, "crop", entries);
    }
    ```

??? note "Author note from JavaDoc"

    Sets the crop window. The crop window in the UI must be completely open for dynamic cropping to
    work.

### `public static void setFiducial3DOffset( String limelightName, double offsetX, double offsetY, double offsetZ)`

[Source lines 1090–1097](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1090)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Key collaborators/calls: `setLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |
| `offsetX` | `double` | `double` input consumed by the implementation shown below. |
| `offsetY` | `double` | `double` input consumed by the implementation shown below. |
| `offsetZ` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1090–1097)"

    ```java
    public static void setFiducial3DOffset(
        String limelightName, double offsetX, double offsetY, double offsetZ) {
      double[] entries = new double[3];
      entries[0] = offsetX;
      entries[1] = offsetY;
      entries[2] = offsetZ;
      setLimelightNTDoubleArray(limelightName, "fiducial_offset_set", entries);
    }
    ```

??? note "Author note from JavaDoc"

    Sets 3D offset point for easy 3D targeting.

### `public static void SetRobotOrientation( String limelightName, double yaw, double yawRate, double pitch, double pitchRate, double roll, double rollRate)`

[Source lines 1099–1109](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1099)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Key collaborators/calls: `SetRobotOrientation_INTERNAL()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |
| `yaw` | `double` | `double` input consumed by the implementation shown below. |
| `yawRate` | `double` | `double` input consumed by the implementation shown below. |
| `pitch` | `double` | `double` input consumed by the implementation shown below. |
| `pitchRate` | `double` | `double` input consumed by the implementation shown below. |
| `roll` | `double` | `double` input consumed by the implementation shown below. |
| `rollRate` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1099–1109)"

    ```java
    public static void SetRobotOrientation(
        String limelightName,
        double yaw,
        double yawRate,
        double pitch,
        double pitchRate,
        double roll,
        double rollRate) {
      SetRobotOrientation_INTERNAL(
          limelightName, yaw, yawRate, pitch, pitchRate, roll, rollRate, true);
    }
    ```

### `public static void SetRobotOrientation_NoFlush( String limelightName, double yaw, double yawRate, double pitch, double pitchRate, double roll, double rollRate)`

[Source lines 1111–1121](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1111)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Key collaborators/calls: `SetRobotOrientation_INTERNAL()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |
| `yaw` | `double` | `double` input consumed by the implementation shown below. |
| `yawRate` | `double` | `double` input consumed by the implementation shown below. |
| `pitch` | `double` | `double` input consumed by the implementation shown below. |
| `pitchRate` | `double` | `double` input consumed by the implementation shown below. |
| `roll` | `double` | `double` input consumed by the implementation shown below. |
| `rollRate` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1111–1121)"

    ```java
    public static void SetRobotOrientation_NoFlush(
        String limelightName,
        double yaw,
        double yawRate,
        double pitch,
        double pitchRate,
        double roll,
        double rollRate) {
      SetRobotOrientation_INTERNAL(
          limelightName, yaw, yawRate, pitch, pitchRate, roll, rollRate, false);
    }
    ```

### `public static void SetFidcuial3DOffset(String limelightName, double x, double y, double z)`

[Source lines 1146–1153](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1146)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Key collaborators/calls: `setLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |
| `x` | `double` | `double` input consumed by the implementation shown below. |
| `y` | `double` | `double` input consumed by the implementation shown below. |
| `z` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1146–1153)"

    ```java
    public static void SetFidcuial3DOffset(String limelightName, double x, double y, double z) {
    
      double[] entries = new double[3];
      entries[0] = x;
      entries[1] = y;
      entries[2] = z;
      setLimelightNTDoubleArray(limelightName, "fiducial_offset_set", entries);
    }
    ```

### `public static void SetFiducialIDFiltersOverride(String limelightName, int[] validIDs)`

[Source lines 1155–1161](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1155)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `setLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |
| `validIDs` | `int[]` | `int[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1155–1161)"

    ```java
    public static void SetFiducialIDFiltersOverride(String limelightName, int[] validIDs) {
      double[] validIDsDouble = new double[validIDs.length];
      for (int i = 0; i < validIDs.length; i++) {
        validIDsDouble[i] = validIDs[i];
      }
      setLimelightNTDoubleArray(limelightName, "fiducial_id_filters_set", validIDsDouble);
    }
    ```

### `public static void SetFiducialDownscalingOverride(String limelightName, float downscale)`

[Source lines 1163–1181](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1163)

**Detailed behavior**

- The implementation executes 17 non-blank source lines.
- It has 5 conditional paths: `downscale == 1.0`; `downscale == 1.5`; `downscale == 2` plus 2 more.
- Key collaborators/calls: `setLimelightNTDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |
| `downscale` | `float` | `float` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1163–1181)"

    ```java
    public static void SetFiducialDownscalingOverride(String limelightName, float downscale) {
      int d = 0; // pipeline
      if (downscale == 1.0) {
        d = 1;
      }
      if (downscale == 1.5) {
        d = 2;
      }
      if (downscale == 2) {
        d = 3;
      }
      if (downscale == 3) {
        d = 4;
      }
      if (downscale == 4) {
        d = 5;
      }
      setLimelightNTDouble(limelightName, "fiducial_downscale_set", d);
    }
    ```

### `public static void setCameraPose_RobotSpace( String limelightName, double forward, double side, double up, double roll, double pitch, double yaw)`

[Source lines 1183–1199](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1183)

**Detailed behavior**

- The implementation executes 8 non-blank source lines.
- Key collaborators/calls: `setLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |
| `forward` | `double` | `double` input consumed by the implementation shown below. |
| `side` | `double` | `double` input consumed by the implementation shown below. |
| `up` | `double` | `double` input consumed by the implementation shown below. |
| `roll` | `double` | `double` input consumed by the implementation shown below. |
| `pitch` | `double` | `double` input consumed by the implementation shown below. |
| `yaw` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1183–1199)"

    ```java
    public static void setCameraPose_RobotSpace(
        String limelightName,
        double forward,
        double side,
        double up,
        double roll,
        double pitch,
        double yaw) {
      double[] entries = new double[6];
      entries[0] = forward;
      entries[1] = side;
      entries[2] = up;
      entries[3] = roll;
      entries[4] = pitch;
      entries[5] = yaw;
      setLimelightNTDoubleArray(limelightName, "camerapose_robotspace_set", entries);
    }
    ```

### `public static void setPythonScriptData(String limelightName, double[] outgoingPythonData)`

[Source lines 1204–1206](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1204)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |
| `outgoingPythonData` | `double[]` | `double[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 1204–1206)"

    ```java
    public static void setPythonScriptData(String limelightName, double[] outgoingPythonData) {
      setLimelightNTDoubleArray(limelightName, "llrobot", outgoingPythonData);
    }
    ```

### `public static double[] getPythonScriptData(String limelightName)`

[Source lines 1208–1210](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1208)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getLimelightNTDoubleArray(limelightName, "llpython")`.
- Key collaborators/calls: `getLimelightNTDoubleArray()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 1208–1210)"

    ```java
    public static double[] getPythonScriptData(String limelightName) {
      return getLimelightNTDoubleArray(limelightName, "llpython");
    }
    ```

### `public static CompletableFuture&lt;Boolean&gt; takeSnapshot(String tableName, String snapshotName)`

[Source lines 1216–1221](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1216)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `CompletableFuture.supplyAsync( () -> { return SYNCH_TAKESNAPSHOT(tableName, snapshotName)`.
- Key collaborators/calls: `CompletableFuture.supplyAsync()`, `SYNCH_TAKESNAPSHOT()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `snapshotName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `CompletableFuture&lt;Boolean&gt;`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 1216–1221)"

    ```java
    public static CompletableFuture<Boolean> takeSnapshot(String tableName, String snapshotName) {
      return CompletableFuture.supplyAsync(
          () -> {
            return SYNCH_TAKESNAPSHOT(tableName, snapshotName);
          });
    }
    ```

??? note "Author note from JavaDoc"

    Asynchronously take snapshot.

### `public static LimelightResults getLatestResults(String limelightName)`

[Source lines 1245–1268](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L1245)

**Detailed behavior**

- The implementation executes 18 non-blank source lines.
- It has 2 conditional paths: `mapper == null`; `profileJSON`.
- Return path: `results`.
- Key collaborators/calls: `System.nanoTime()`, `LimelightHelpers.LimelightResults()`, `ObjectMapper()`, `configure()`, `mapper.readValue()`, `getJSONDump()`, `e.getMessage()`, `System.out.printf()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `limelightName` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `LimelightResults`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 1245–1268)"

    ```java
    public static LimelightResults getLatestResults(String limelightName) {
    
      long start = System.nanoTime();
      LimelightHelpers.LimelightResults results = new LimelightHelpers.LimelightResults();
      if (mapper == null) {
        mapper =
            new ObjectMapper().configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
      }
    
      try {
        results = mapper.readValue(getJSONDump(limelightName), LimelightResults.class);
      } catch (JsonProcessingException e) {
        results.error = "lljson error: " + e.getMessage();
      }
    
      long end = System.nanoTime();
      double millis = (end - start) * .000001;
      results.latency_jsonParse = millis;
      if (profileJSON) {
        System.out.printf("lljson: %.2f\r\n", millis);
      }
    
      return results;
    }
    ```

??? note "Author note from JavaDoc"

    Parses Limelight's JSON results dump into a LimelightResults Object

## Exposed fields and types

### `public class LimelightHelpers`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L31)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static class LimelightTarget_Retro`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L35)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public double ta`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L93)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 22 times, so changing it can affect every control path that reads `ta`.

### `public double tx`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L96)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `tx`.

### `public double tx_pixels`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L99)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `tx_pixels`.

### `public double ty`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L102)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `ty`.

### `public double ty_pixels`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L105)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `ty_pixels`.

### `public double ts`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L108)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 5 times, so changing it can affect every control path that reads `ts`.

### `public static class LimelightTarget_Fiducial`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L119)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public double fiducialID`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L122)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `fiducialID`.

### `public String fiducialFamily`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L125)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `fiducialFamily`.

### `public double ta`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L183)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 22 times, so changing it can affect every control path that reads `ta`.

### `public double tx`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L186)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `tx`.

### `public double tx_pixels`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L189)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `tx_pixels`.

### `public double ty`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L192)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `ty`.

### `public double ty_pixels`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L195)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `ty_pixels`.

### `public double ts`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L198)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 5 times, so changing it can affect every control path that reads `ts`.

### `public static class LimelightTarget_Barcode`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L209)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static class LimelightTarget_Classifier`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L211)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public String className`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L214)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `className`.

### `public double classID`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L217)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `classID`.

### `public double confidence`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L220)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `confidence`.

### `public double zone`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L223)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `zone`.

### `public double tx`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L226)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `tx`.

### `public double tx_pixels`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L229)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `tx_pixels`.

### `public double ty`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L232)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `ty`.

### `public double ty_pixels`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L235)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `ty_pixels`.

### `public static class LimelightTarget_Detector`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L240)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public String className`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L243)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `className`.

### `public double classID`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L246)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `classID`.

### `public double confidence`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L249)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `confidence`.

### `public double ta`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L252)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 22 times, so changing it can affect every control path that reads `ta`.

### `public double tx`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L255)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `tx`.

### `public double tx_pixels`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L258)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `tx_pixels`.

### `public double ty`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L261)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `ty`.

### `public double ty_pixels`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L264)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `ty_pixels`.

### `public static class LimelightResults`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L269)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public String error`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L271)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `error`.

### `public double pipelineID`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L274)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `pipelineID`.

### `public double latency_pipeline`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L277)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `latency_pipeline`.

### `public double latency_capture`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L280)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `latency_capture`.

### `public double latency_jsonParse`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L282)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `latency_jsonParse`.

### `public double timestamp_LIMELIGHT_publish`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L285)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `timestamp_LIMELIGHT_publish`.

### `public double timestamp_RIOFPGA_capture`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L288)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `timestamp_RIOFPGA_capture`.

### `public boolean valid`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L292)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `valid`.

### `public double[] botpose`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L295)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 8 times, so changing it can affect every control path that reads `botpose`.

### `public double[] botpose_wpired`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L298)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `botpose_wpired`.

### `public double[] botpose_wpiblue`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L301)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `botpose_wpiblue`.

### `public double botpose_tagcount`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L304)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `botpose_tagcount`.

### `public double botpose_span`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L307)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `botpose_span`.

### `public double botpose_avgdist`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L310)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `botpose_avgdist`.

### `public double botpose_avgarea`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L313)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `botpose_avgarea`.

### `public double[] camerapose_robotspace`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L316)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `camerapose_robotspace`.

### `public LimelightTarget_Retro[] targets_Retro`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L343)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `targets_Retro`.

### `public LimelightTarget_Fiducial[] targets_Fiducials`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L346)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `targets_Fiducials`.

### `public LimelightTarget_Classifier[] targets_Classifier`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L349)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `targets_Classifier`.

### `public LimelightTarget_Detector[] targets_Detector`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L352)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `targets_Detector`.

### `public LimelightTarget_Barcode[] targets_Barcode`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L355)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `targets_Barcode`.

### `public static class RawFiducial`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L370)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public int id = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L371)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `id`.

### `public double txnc = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L372)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 15 times, so changing it can affect every control path that reads `txnc`.

### `public double tync = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L373)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 15 times, so changing it can affect every control path that reads `tync`.

### `public double ta = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L374)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 22 times, so changing it can affect every control path that reads `ta`.

### `public double distToCamera = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L375)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `distToCamera`.

### `public double distToRobot = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L376)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `distToRobot`.

### `public double ambiguity = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L377)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 9 times, so changing it can affect every control path that reads `ambiguity`.

### `public static class RawDetection`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L397)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public int classId = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L398)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `classId`.

### `public double txnc = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L399)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 15 times, so changing it can affect every control path that reads `txnc`.

### `public double tync = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L400)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 15 times, so changing it can affect every control path that reads `tync`.

### `public double ta = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L401)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 22 times, so changing it can affect every control path that reads `ta`.

### `public double corner0_X = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L402)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `corner0_X`.

### `public double corner0_Y = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L403)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `corner0_Y`.

### `public double corner1_X = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L404)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `corner1_X`.

### `public double corner1_Y = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L405)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `corner1_Y`.

### `public double corner2_X = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L406)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `corner2_X`.

### `public double corner2_Y = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L407)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `corner2_Y`.

### `public double corner3_X = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L408)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `corner3_X`.

### `public double corner3_Y = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L409)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `corner3_Y`.

### `public static class PoseEstimate`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L439)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public Pose2d pose`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L440)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 41 times, so changing it can affect every control path that reads `pose`.

### `public double timestampSeconds`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L441)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `timestampSeconds`.

### `public double latency`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L442)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 10 times, so changing it can affect every control path that reads `latency`.

### `public int tagCount`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L443)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 11 times, so changing it can affect every control path that reads `tagCount`.

### `public double tagSpan`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L444)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 8 times, so changing it can affect every control path that reads `tagSpan`.

### `public double avgTagDist`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L445)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `avgTagDist`.

### `public double avgTagArea`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L446)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `avgTagArea`.

### `public RawFiducial[] rawFiducials`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/vision/LimelightHelpers.java#L447)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 15 times, so changing it can affect every control path that reads `rawFiducials`.
