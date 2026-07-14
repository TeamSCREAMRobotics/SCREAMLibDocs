# PhoenixSwerveHelper

`com.teamscreamrobotics.drivers.PhoenixSwerveHelper`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java) · **20 callables** · **1 exposed fields/types** · **2 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2025: Use `PhoenixSwerveHelper` in `Drivetrain.java`

[`src/main/java/frc2025/subsystems/drivetrain/Drivetrain.java` lines 53–68](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/drivetrain/Drivetrain.java#L53-L68)

```java
super(driveTrainConstants, OdometryUpdateFrequency, modules);

CommandScheduler.getInstance().registerSubsystem(this);

helper =
    new PhoenixSwerveHelper(
        this::getEstimatedPose,
        DrivetrainConstants.MAX_SPEED,
        DrivetrainConstants.HEADING_CORRECTION_CONSTANTS,
        DrivetrainConstants.HEADING_CORRECTION_CONSTANTS);

RobotConfig config = DrivetrainConstants.ROBOT_CONFIG;
try {
  config = RobotConfig.fromGUISettings();
} catch (Exception e) {
  // TODO Auto-generated catch block
```

### 2026: Use `PhoenixSwerveHelper` in `Drivetrain.java`

[`src/main/java/frc2026/tars/subsystems/drivetrain/Drivetrain.java` lines 114–129](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/drivetrain/Drivetrain.java#L114-L129)

```java
if (Utils.isSimulation()) {
  startSimThread();
}

helper =
    new PhoenixSwerveHelper(
        this::getEstimatedPose,
        DrivetrainConstants.maxSpeed,
        DrivetrainConstants.headingCorrectionConstants,
        DrivetrainConstants.headingCorrectionConstants);

// RobotConfig config = DrivetrainConstants.robotConfig;
// try {
//   config = RobotConfig.fromGUISettings();
// } catch (Exception e) {
//   // TODO Auto-generated catch block
```

## Public and protected callables

### `public PhoenixSwerveHelper( Supplier&lt;Pose2d&gt; poseSup, double maxSpeed, ScreamPIDConstants snapConstants, ScreamPIDConstants headingCorrectionConstants)`

[Source lines 55–90](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L55)

**Detailed behavior**

- The implementation executes 27 non-blank source lines.
- It changes object/subclass state through `headingCorrectionController`, `poseSup`, `snapController`.
- Key collaborators/calls: `FieldCentricFacingAngle()`, `withDeadband()`, `withDriveRequestType()`, `withSteerRequestType()`, `FieldCentric()`, `RobotCentric()`, `ApplyRobotSpeeds()`, `ApplyFieldSpeeds()`, `snapConstants.getPhoenixPIDController()`, `headingCorrectionConstants.getPIDController()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `poseSup` | `Supplier&lt;Pose2d&gt;` | supplier of the robot's current field pose **Parameter `maxSpeed`:** drivetrain maximum speed in m/s (used to set deadbands) **Parameter `snapConstants`:** PID constants for the heading snap controller **Parameter `head… |
| `maxSpeed` | `double` | drivetrain maximum speed in m/s (used to set deadbands) **Parameter `snapConstants`:** PID constants for the heading snap controller **Parameter `headingCorrectionConstants`:** PID constants for the heading drift correc… |
| `snapConstants` | `ScreamPIDConstants` | PID constants for the heading snap controller **Parameter `headingCorrectionConstants`:** PID constants for the heading drift correction controller |
| `headingCorrectionConstants` | `ScreamPIDConstants` | PID constants for the heading drift correction controller |

**Result:** Constructs and initializes a `PhoenixSwerveHelper` instance.

??? example "Implementation (source lines 55–90)"

    ```java
    public PhoenixSwerveHelper(
        Supplier<Pose2d> poseSup,
        double maxSpeed,
        ScreamPIDConstants snapConstants,
        ScreamPIDConstants headingCorrectionConstants) {
      fieldCentricFacingAngle =
      new FieldCentricFacingAngle()
          .withDeadband(maxSpeed * 0.05)
          .withDriveRequestType(DriveRequestType.OpenLoopVoltage)
              .withSteerRequestType(SteerRequestType.MotionMagicExpo);
      fieldCentric =
          new FieldCentric()
              .withDeadband(maxSpeed * 0.05)
              .withDriveRequestType(DriveRequestType.OpenLoopVoltage)
              .withSteerRequestType(SteerRequestType.MotionMagicExpo);
      robotCentric =
          new RobotCentric()
              .withDeadband(maxSpeed * 0.05)
              .withDriveRequestType(DriveRequestType.OpenLoopVoltage)
              .withSteerRequestType(SteerRequestType.MotionMagicExpo);
      applyRobotSpeeds =
          new ApplyRobotSpeeds()
              .withDriveRequestType(DriveRequestType.Velocity)
              .withSteerRequestType(SteerRequestType.MotionMagicExpo);
      applyFieldSpeeds =
          new ApplyFieldSpeeds()
              .withDriveRequestType(DriveRequestType.Velocity)
              .withSteerRequestType(SteerRequestType.MotionMagicExpo);
    
      this.snapController = snapConstants.getPhoenixPIDController(-Math.PI, Math.PI);
      fieldCentricFacingAngle.HeadingController = snapController;
    
      this.headingCorrectionController = headingCorrectionConstants.getPIDController(-Math.PI, Math.PI);
    
      this.poseSup = poseSup;
    }
    ```

??? note "Author note from JavaDoc"

    Creates a new helper with configured swerve requests.
    
    **Parameter `poseSup`:** supplier of the robot's current field pose
    **Parameter `maxSpeed`:** drivetrain maximum speed in m/s (used to set deadbands)
    **Parameter `snapConstants`:** PID constants for the heading snap controller
    **Parameter `headingCorrectionConstants`:** PID constants for the heading drift correction controller

### `public void setLastAngle(Rotation2d angle)`

[Source lines 93–95](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L93)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `angle` | `Rotation2d` | `Rotation2d` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 93–95)"

    ```java
    public void setLastAngle(Rotation2d angle) {
      lastAngle = angle;
    }
    ```

??? note "Author note from JavaDoc"

    Overrides the heading correction hold angle — call this when intentionally changing heading.

### `public FieldCentricFacingAngle getFacingAngle(Translation2d translation, Rotation2d targetAngle)`

[Source lines 103–108](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L103)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `fieldCentricFacingAngle .withVelocityX(translation.getX()) .withVelocityY(translation.getY()) .withTargetDirection(targetAngle)`.
- Key collaborators/calls: `withVelocityX()`, `translation.getX()`, `withVelocityY()`, `translation.getY()`, `withTargetDirection()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `targetAngle`:** desired heading |
| `targetAngle` | `Rotation2d` | desired heading |

**Result:** Returns `FieldCentricFacingAngle`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 103–108)"

    ```java
    public FieldCentricFacingAngle getFacingAngle(Translation2d translation, Rotation2d targetAngle) {
      return fieldCentricFacingAngle
      .withVelocityX(translation.getX())
      .withVelocityY(translation.getY())
      .withTargetDirection(targetAngle);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a `FieldCentricFacingAngle` request using the built-in snap controller.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `targetAngle`:** desired heading

### `public FieldCentric getFacingAngle( Translation2d translation, Rotation2d targetAngle, PIDController headingController)`

[Source lines 117–123](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L117)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `getFieldCentric( translation, headingController .calculate(poseSup.get().getRotation().getRadians(), targetAngle.getRadians()))`.
- Key collaborators/calls: `getFieldCentric()`, `calculate()`, `poseSup.get()`, `getRotation()`, `getRadians()`, `targetAngle.getRadians()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `targetAngle`:** desired heading **Parameter `headingController`:** PID constants for heading control (uses a fresh controller per call) |
| `targetAngle` | `Rotation2d` | desired heading **Parameter `headingController`:** PID constants for heading control (uses a fresh controller per call) |
| `headingController` | `PIDController` | PID constants for heading control (uses a fresh controller per call) |

**Result:** Returns `FieldCentric`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 117–123)"

    ```java
    public FieldCentric getFacingAngle(
        Translation2d translation, Rotation2d targetAngle, PIDController headingController) {
      return getFieldCentric(
          translation,
          headingController
              .calculate(poseSup.get().getRotation().getRadians(), targetAngle.getRadians()));
    }
    ```

??? note "Author note from JavaDoc"

    Returns a `FieldCentric` request with angular velocity computed from a custom PID controller.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `targetAngle`:** desired heading
    **Parameter `headingController`:** PID constants for heading control (uses a fresh controller per call)

### `public FieldCentric getFacingAngleProfiled( Translation2d translation, Rotation2d targetAngle, ProfiledPIDController profile)`

[Source lines 132–137](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L132)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `getFieldCentric( translation, profile.calculate(poseSup.get().getRotation().getRadians(), targetAngle.getRadians()))`.
- Key collaborators/calls: `getFieldCentric()`, `profile.calculate()`, `poseSup.get()`, `getRotation()`, `getRadians()`, `targetAngle.getRadians()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `targetAngle`:** desired heading **Parameter `profile`:** profiled PID controller for smooth heading control |
| `targetAngle` | `Rotation2d` | desired heading **Parameter `profile`:** profiled PID controller for smooth heading control |
| `profile` | `ProfiledPIDController` | profiled PID controller for smooth heading control |

**Result:** Returns `FieldCentric`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 132–137)"

    ```java
    public FieldCentric getFacingAngleProfiled(
        Translation2d translation, Rotation2d targetAngle, ProfiledPIDController profile) {
      return getFieldCentric(
          translation,
          profile.calculate(poseSup.get().getRotation().getRadians(), targetAngle.getRadians()));
    }
    ```

??? note "Author note from JavaDoc"

    Returns a `FieldCentric` request with angular velocity from a profiled PID controller.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `targetAngle`:** desired heading
    **Parameter `profile`:** profiled PID controller for smooth heading control

### `public FieldCentricFacingAngle getFacingAngleCOR( Translation2d translation, Rotation2d targetAngle, Translation2d centerOfRotation)`

[Source lines 146–149](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L146)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getFacingAngle(translation, targetAngle).withCenterOfRotation(centerOfRotation)`.
- Key collaborators/calls: `getFacingAngle()`, `withCenterOfRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `targetAngle`:** desired heading **Parameter `centerOfRotation`:** offset from robot center for rotation |
| `targetAngle` | `Rotation2d` | desired heading **Parameter `centerOfRotation`:** offset from robot center for rotation |
| `centerOfRotation` | `Translation2d` | offset from robot center for rotation |

**Result:** Returns `FieldCentricFacingAngle`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 146–149)"

    ```java
    public FieldCentricFacingAngle getFacingAngleCOR(
        Translation2d translation, Rotation2d targetAngle, Translation2d centerOfRotation) {
      return getFacingAngle(translation, targetAngle).withCenterOfRotation(centerOfRotation);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a `FieldCentricFacingAngle` request using the built-in snap controller and a custom center of rotation.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `targetAngle`:** desired heading
    **Parameter `centerOfRotation`:** offset from robot center for rotation

### `public FieldCentric getFacingAngleProfiledCOR( Translation2d translation, Rotation2d targetAngle, ProfiledPIDController profile, Translation2d centerOfRotation)`

[Source lines 159–168](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L159)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `getFieldCentricCOR( translation, profile.calculate(poseSup.get().getRotation().getRadians(), targetAngle.getRadians()), centerOfRotation)`.
- Key collaborators/calls: `getFieldCentricCOR()`, `profile.calculate()`, `poseSup.get()`, `getRotation()`, `getRadians()`, `targetAngle.getRadians()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `targetAngle`:** desired heading **Parameter `profile`:** profiled PID controller **Parameter `centerOfRotation`:** offset from robot center for rotation |
| `targetAngle` | `Rotation2d` | desired heading **Parameter `profile`:** profiled PID controller **Parameter `centerOfRotation`:** offset from robot center for rotation |
| `profile` | `ProfiledPIDController` | profiled PID controller **Parameter `centerOfRotation`:** offset from robot center for rotation |
| `centerOfRotation` | `Translation2d` | offset from robot center for rotation |

**Result:** Returns `FieldCentric`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 159–168)"

    ```java
    public FieldCentric getFacingAngleProfiledCOR(
        Translation2d translation,
        Rotation2d targetAngle,
        ProfiledPIDController profile,
        Translation2d centerOfRotation) {
      return getFieldCentricCOR(
          translation,
          profile.calculate(poseSup.get().getRotation().getRadians(), targetAngle.getRadians()),
          centerOfRotation);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a `FieldCentric` request with profiled heading and a custom center of rotation.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `targetAngle`:** desired heading
    **Parameter `profile`:** profiled PID controller
    **Parameter `centerOfRotation`:** offset from robot center for rotation

### `public FieldCentricFacingAngle getPointingAt( Translation2d translation, Translation2d targetPoint)`

[Source lines 176–179](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L176)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getPointingAt(translation, targetPoint, Rotation2d.kZero)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `targetPoint`:** the field point to face |
| `targetPoint` | `Translation2d` | the field point to face |

**Result:** Returns `FieldCentricFacingAngle`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 176–179)"

    ```java
    public FieldCentricFacingAngle getPointingAt(
        Translation2d translation, Translation2d targetPoint) {
      return getPointingAt(translation, targetPoint, Rotation2d.kZero);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a `FieldCentricFacingAngle` request that keeps the robot aimed at a field point.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `targetPoint`:** the field point to face

### `public FieldCentricFacingAngle getPointingAt( Translation2d translation, Translation2d targetPoint, Rotation2d offset)`

[Source lines 189–195](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L189)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `getFacingAngle( translation, ScreamMath.calculateAngleToPoint(poseSup.get().getTranslation(), targetPoint) .plus(offset))`.
- Key collaborators/calls: `getFacingAngle()`, `ScreamMath.calculateAngleToPoint()`, `poseSup.get()`, `getTranslation()`, `plus()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `targetPoint`:** the field point to face **Parameter `offset`:** additional rotation added to the target heading |
| `targetPoint` | `Translation2d` | the field point to face **Parameter `offset`:** additional rotation added to the target heading |
| `offset` | `Rotation2d` | additional rotation added to the target heading |

**Result:** Returns `FieldCentricFacingAngle`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 189–195)"

    ```java
    public FieldCentricFacingAngle getPointingAt(
        Translation2d translation, Translation2d targetPoint, Rotation2d offset) {
      return getFacingAngle(
          translation,
          ScreamMath.calculateAngleToPoint(poseSup.get().getTranslation(), targetPoint)
                  .plus(offset));
    }
    ```

??? note "Author note from JavaDoc"

    Returns a `FieldCentricFacingAngle` request that keeps the robot aimed at a field point
    with an angular offset added to the computed heading.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `targetPoint`:** the field point to face
    **Parameter `offset`:** additional rotation added to the target heading

### `public FieldCentric getPointingAtProfiled( Translation2d translation, Translation2d targetPoint, ProfiledPIDController profile)`

[Source lines 204–207](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L204)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getPointingAtProfiled(translation, targetPoint, new Rotation2d(), profile)`.
- Key collaborators/calls: `Rotation2d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `targetPoint`:** the field point to face **Parameter `profile`:** profiled PID controller for smooth heading tracking |
| `targetPoint` | `Translation2d` | the field point to face **Parameter `profile`:** profiled PID controller for smooth heading tracking |
| `profile` | `ProfiledPIDController` | profiled PID controller for smooth heading tracking |

**Result:** Returns `FieldCentric`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 204–207)"

    ```java
    public FieldCentric getPointingAtProfiled(
        Translation2d translation, Translation2d targetPoint, ProfiledPIDController profile) {
      return getPointingAtProfiled(translation, targetPoint, new Rotation2d(), profile);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a `FieldCentric` request that aims at a field point using a profiled controller.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `targetPoint`:** the field point to face
    **Parameter `profile`:** profiled PID controller for smooth heading tracking

### `public FieldCentric getPointingAtProfiled( Translation2d translation, Translation2d targetPoint, Rotation2d offset, ProfiledPIDController profile)`

[Source lines 218–221](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L218)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getFacingAngleProfiled(translation, ScreamMath.calculateAngleToPoint(poseSup.get().getTranslation(), targetPoint).plus(offset), profile)`.
- Key collaborators/calls: `getFacingAngleProfiled()`, `ScreamMath.calculateAngleToPoint()`, `poseSup.get()`, `getTranslation()`, `plus()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `targetPoint`:** the field point to face **Parameter `offset`:** additional rotation added to the target heading **Parameter `profile`:** profiled PID controller |
| `targetPoint` | `Translation2d` | the field point to face **Parameter `offset`:** additional rotation added to the target heading **Parameter `profile`:** profiled PID controller |
| `offset` | `Rotation2d` | additional rotation added to the target heading **Parameter `profile`:** profiled PID controller |
| `profile` | `ProfiledPIDController` | profiled PID controller |

**Result:** Returns `FieldCentric`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 218–221)"

    ```java
    public FieldCentric getPointingAtProfiled(
        Translation2d translation, Translation2d targetPoint, Rotation2d offset, ProfiledPIDController profile) {
      return getFacingAngleProfiled(translation, ScreamMath.calculateAngleToPoint(poseSup.get().getTranslation(), targetPoint).plus(offset), profile);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a `FieldCentric` request that aims at a field point with an offset, using a
    profiled controller.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `targetPoint`:** the field point to face
    **Parameter `offset`:** additional rotation added to the target heading
    **Parameter `profile`:** profiled PID controller

### `public FieldCentric getHeadingCorrectedFieldCentric( Translation2d translation, double angularVelocity)`

[Source lines 231–247](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L231)

**Detailed behavior**

- The implementation executes 14 non-blank source lines.
- It has 1 conditional path: `correctionDebouncer.calculate(Math.abs(angularVelocity`.
- Return path: `fieldCentric .withVelocityX(translation.getX()) .withVelocityY(translation.getY()) .withRotationalRate(omega) .withCenterOfRotation(Translation2d.kZero)`.
- Key collaborators/calls: `correctionDebouncer.calculate()`, `Math.abs()`, `headingCorrectionController.calculate()`, `poseSup.get()`, `getRotation()`, `getRadians()`, `lastAngle.getRadians()`, `withVelocityX()`, `translation.getX()`, `withVelocityY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `angularVelocity`:** driver-commanded rotation rate (rad/s) |
| `angularVelocity` | `double` | driver-commanded rotation rate (rad/s) |

**Result:** Returns `FieldCentric`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 231–247)"

    ```java
    public FieldCentric getHeadingCorrectedFieldCentric(
        Translation2d translation, double angularVelocity) {
      double omega;
      if (correctionDebouncer.calculate(Math.abs(angularVelocity) < 0.05)) {
        omega =
            headingCorrectionController.calculate(
                poseSup.get().getRotation().getRadians(), lastAngle.getRadians());
      } else {
        omega = angularVelocity;
        lastAngle = poseSup.get().getRotation();
      }
      return fieldCentric
          .withVelocityX(translation.getX())
          .withVelocityY(translation.getY())
          .withRotationalRate(omega)
          .withCenterOfRotation(Translation2d.kZero);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a field-centric request with automatic heading drift correction.
    While `angularVelocity` is near zero the correction controller holds the last known
    heading; otherwise the driver input is passed through and the hold angle is updated.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `angularVelocity`:** driver-commanded rotation rate (rad/s)

### `public FieldCentric getFieldCentric(Translation2d translation, double angularVelocity)`

[Source lines 255–261](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L255)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `fieldCentric .withVelocityX(translation.getX()) .withVelocityY(translation.getY()) .withRotationalRate(angularVelocity) .withCenterOfRotation(Translation2d.kZero)`.
- Key collaborators/calls: `withVelocityX()`, `translation.getX()`, `withVelocityY()`, `translation.getY()`, `withRotationalRate()`, `withCenterOfRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `angularVelocity`:** rotation rate in rad/s |
| `angularVelocity` | `double` | rotation rate in rad/s |

**Result:** Returns `FieldCentric`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 255–261)"

    ```java
    public FieldCentric getFieldCentric(Translation2d translation, double angularVelocity) {
      return fieldCentric
          .withVelocityX(translation.getX())
          .withVelocityY(translation.getY())
          .withRotationalRate(angularVelocity)
          .withCenterOfRotation(Translation2d.kZero);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a basic field-centric drive request.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `angularVelocity`:** rotation rate in rad/s

### `public FieldCentric getFieldCentricCOR( Translation2d translation, double angularVelocity, Translation2d centerOfRotation)`

[Source lines 270–277](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L270)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `fieldCentric .withVelocityX(translation.getX()) .withVelocityY(translation.getY()) .withRotationalRate(angularVelocity) .withCenterOfRotation(Translation2d.kZero)`.
- Key collaborators/calls: `withVelocityX()`, `translation.getX()`, `withVelocityY()`, `translation.getY()`, `withRotationalRate()`, `withCenterOfRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | field-relative XY velocity vector **Parameter `angularVelocity`:** rotation rate in rad/s **Parameter `centerOfRotation`:** offset from robot center for rotation |
| `angularVelocity` | `double` | rotation rate in rad/s **Parameter `centerOfRotation`:** offset from robot center for rotation |
| `centerOfRotation` | `Translation2d` | offset from robot center for rotation |

**Result:** Returns `FieldCentric`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 270–277)"

    ```java
    public FieldCentric getFieldCentricCOR(
        Translation2d translation, double angularVelocity, Translation2d centerOfRotation) {
      return fieldCentric
          .withVelocityX(translation.getX())
          .withVelocityY(translation.getY())
          .withRotationalRate(angularVelocity)
          .withCenterOfRotation(Translation2d.kZero);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a field-centric drive request with a custom center of rotation.
    
    **Parameter `translation`:** field-relative XY velocity vector
    **Parameter `angularVelocity`:** rotation rate in rad/s
    **Parameter `centerOfRotation`:** offset from robot center for rotation

### `public RobotCentric getRobotCentric(Translation2d translation, double angularVelocity)`

[Source lines 285–291](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L285)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `robotCentric .withVelocityX(translation.getX()) .withVelocityY(translation.getY()) .withRotationalRate(angularVelocity) .withCenterOfRotation(Translation2d.kZero)`.
- Key collaborators/calls: `withVelocityX()`, `translation.getX()`, `withVelocityY()`, `translation.getY()`, `withRotationalRate()`, `withCenterOfRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | robot-relative XY velocity vector **Parameter `angularVelocity`:** rotation rate in rad/s |
| `angularVelocity` | `double` | rotation rate in rad/s |

**Result:** Returns `RobotCentric`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 285–291)"

    ```java
    public RobotCentric getRobotCentric(Translation2d translation, double angularVelocity) {
      return robotCentric
          .withVelocityX(translation.getX())
          .withVelocityY(translation.getY())
          .withRotationalRate(angularVelocity)
          .withCenterOfRotation(Translation2d.kZero);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a robot-centric drive request.
    
    **Parameter `translation`:** robot-relative XY velocity vector
    **Parameter `angularVelocity`:** rotation rate in rad/s

### `public RobotCentric getRobotCentricCOR( Translation2d translation, double angularVelocity, Translation2d centerOfRotation)`

[Source lines 300–307](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L300)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `robotCentric .withVelocityX(translation.getX()) .withVelocityY(translation.getY()) .withRotationalRate(angularVelocity) .withCenterOfRotation(centerOfRotation)`.
- Key collaborators/calls: `withVelocityX()`, `translation.getX()`, `withVelocityY()`, `translation.getY()`, `withRotationalRate()`, `withCenterOfRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | robot-relative XY velocity vector **Parameter `angularVelocity`:** rotation rate in rad/s **Parameter `centerOfRotation`:** offset from robot center for rotation |
| `angularVelocity` | `double` | rotation rate in rad/s **Parameter `centerOfRotation`:** offset from robot center for rotation |
| `centerOfRotation` | `Translation2d` | offset from robot center for rotation |

**Result:** Returns `RobotCentric`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 300–307)"

    ```java
    public RobotCentric getRobotCentricCOR(
        Translation2d translation, double angularVelocity, Translation2d centerOfRotation) {
      return robotCentric
          .withVelocityX(translation.getX())
          .withVelocityY(translation.getY())
          .withRotationalRate(angularVelocity)
          .withCenterOfRotation(centerOfRotation);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a robot-centric drive request with a custom center of rotation.
    
    **Parameter `translation`:** robot-relative XY velocity vector
    **Parameter `angularVelocity`:** rotation rate in rad/s
    **Parameter `centerOfRotation`:** offset from robot center for rotation

### `public ApplyRobotSpeeds getApplyRobotSpeeds(ChassisSpeeds chassisSpeeds)`

[Source lines 310–312](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L310)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `applyRobotSpeeds.withSpeeds(chassisSpeeds)`.
- Key collaborators/calls: `applyRobotSpeeds.withSpeeds()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `chassisSpeeds` | `ChassisSpeeds` | Velocity/speed in the units required by this API and configuration. |

**Result:** Returns `ApplyRobotSpeeds`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 310–312)"

    ```java
    public ApplyRobotSpeeds getApplyRobotSpeeds(ChassisSpeeds chassisSpeeds) {
      return applyRobotSpeeds.withSpeeds(chassisSpeeds);
    }
    ```

??? note "Author note from JavaDoc"

    Returns an `ApplyRobotSpeeds` request for closed-loop velocity control.

### `public ApplyRobotSpeeds getApplyRobotSpeedsCOR( ChassisSpeeds chassisSpeeds, Translation2d centerOfRotation)`

[Source lines 320–323](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L320)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getApplyRobotSpeeds(chassisSpeeds).withCenterOfRotation(centerOfRotation)`.
- Key collaborators/calls: `getApplyRobotSpeeds()`, `withCenterOfRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `chassisSpeeds` | `ChassisSpeeds` | desired robot-relative speeds **Parameter `centerOfRotation`:** offset from robot center for rotation |
| `centerOfRotation` | `Translation2d` | offset from robot center for rotation |

**Result:** Returns `ApplyRobotSpeeds`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 320–323)"

    ```java
    public ApplyRobotSpeeds getApplyRobotSpeedsCOR(
        ChassisSpeeds chassisSpeeds, Translation2d centerOfRotation) {
      return getApplyRobotSpeeds(chassisSpeeds).withCenterOfRotation(centerOfRotation);
    }
    ```

??? note "Author note from JavaDoc"

    Returns an `ApplyRobotSpeeds` request with a custom center of rotation.
    
    **Parameter `chassisSpeeds`:** desired robot-relative speeds
    **Parameter `centerOfRotation`:** offset from robot center for rotation

### `public ApplyFieldSpeeds getApplyFieldSpeeds(ChassisSpeeds chassisSpeeds)`

[Source lines 326–328](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L326)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `applyFieldSpeeds.withSpeeds(chassisSpeeds)`.
- Key collaborators/calls: `applyFieldSpeeds.withSpeeds()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `chassisSpeeds` | `ChassisSpeeds` | Velocity/speed in the units required by this API and configuration. |

**Result:** Returns `ApplyFieldSpeeds`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 326–328)"

    ```java
    public ApplyFieldSpeeds getApplyFieldSpeeds(ChassisSpeeds chassisSpeeds) {
      return applyFieldSpeeds.withSpeeds(chassisSpeeds);
    }
    ```

??? note "Author note from JavaDoc"

    Returns an `ApplyFieldSpeeds` request for closed-loop field-relative velocity control.

### `public ApplyFieldSpeeds getApplyFieldSpeedsCOR(ChassisSpeeds chassisSpeeds, Translation2d centerOfRotation)`

[Source lines 336–338](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L336)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getApplyFieldSpeeds(chassisSpeeds).withCenterOfRotation(centerOfRotation)`.
- Key collaborators/calls: `getApplyFieldSpeeds()`, `withCenterOfRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `chassisSpeeds` | `ChassisSpeeds` | desired field-relative speeds **Parameter `centerOfRotation`:** offset from robot center for rotation |
| `centerOfRotation` | `Translation2d` | offset from robot center for rotation |

**Result:** Returns `ApplyFieldSpeeds`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 336–338)"

    ```java
    public ApplyFieldSpeeds getApplyFieldSpeedsCOR(ChassisSpeeds chassisSpeeds, Translation2d centerOfRotation) {
      return getApplyFieldSpeeds(chassisSpeeds).withCenterOfRotation(centerOfRotation);
    }
    ```

??? note "Author note from JavaDoc"

    Returns an `ApplyFieldSpeeds` request with a custom center of rotation.
    
    **Parameter `chassisSpeeds`:** desired field-relative speeds
    **Parameter `centerOfRotation`:** offset from robot center for rotation

## Exposed fields and types

### `public class PhoenixSwerveHelper`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PhoenixSwerveHelper.java#L30)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Factory for CTRE Phoenix 6 swerve drive requests with built-in heading snap and correction.
    Wraps `FieldCentric`, `FieldCentricFacingAngle`, `RobotCentric`, and
    `ApplyRobotSpeeds`/`ApplyFieldSpeeds` requests with pre-configured deadbands and
    drive/steer request types.
