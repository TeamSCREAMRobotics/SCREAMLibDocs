# AllianceFlipUtil

`com.teamscreamrobotics.util.AllianceFlipUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java) · **18 callables** · **4 exposed fields/types** · **2 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

!!! note "2025 package names"
    The 2025 robot used SCREAMLib's earlier short packages such as `data`, `drivers`, and `util`. With SCREAMLib 26.3.7, prefix those imports with `com.teamscreamrobotics.`; the implementation pattern remains applicable.

### 2026: Select alliance-correct shooting and ferry targets

[`src/main/java/frc2026/tars/subsystems/shooter/Shooter.java` lines 260–330](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/Shooter.java#L260-L330)

```java
}
}

private void idleCase(RobotState.Area area, Pose2d robotPose, ChassisSpeeds robotSpeeds) {
  if (area == null) return;
  switch (area) {
    case ALLIANCEZONE:
      applyAimingSetpoints(
          robotPose,
          robotSpeeds,
          AllianceFlipUtil.get(FieldConstants.Hub.hubCenter, FieldConstants.Hub.oppHubCenter),
          wantShoot);
      setIdleState(IdleState.IDLE_HUB);
      led.wave(
          Color.kBlack,
          AllianceFlipUtil.get(
              new Color(1.0f, 0.49803922f, 0.83137256f),
              new Color(0.26078432f, 1.0f, 0.36078432f)),
          0.1,
          1.25);
      break;
    case DEPOT_SIDE_NEUTRALZONE:
      applyAimingSetpoints(
          robotPose,
          robotSpeeds,
          AllianceFlipUtil.get(
              FieldConstants.AllianceZones.leftAllianceZone,
              FieldConstants.AllianceZones.oppRightAllianceZone),
          wantShoot);
      setIdleState(IdleState.IDLE_FERRY_DEPOT);
      led.wave(Color.kBlack, new Color(0.0f, 0.5019608f, 0.5019608f), 0.1, 1.25);
      break;
    case OUTPOST_SIDE_NEUTRALZONE:
      applyAimingSetpoints(
          robotPose,
          robotSpeeds,
          AllianceFlipUtil.get(
              FieldConstants.AllianceZones.rightAllianceZone,
              FieldConstants.AllianceZones.oppLeftAllianceZone),
          wantShoot);
      setIdleState(IdleState.IDLE_FERRY_OUTPOST);
      led.wave(Color.kBlack, new Color(0.0f, 0.5019608f, 0.5019608f), 0.1, 1.25);
      break;
    case OTHER_ALLIANCEZONE_DEPOT:
      applyAimingSetpoints(
          robotPose,
          robotSpeeds,
          AllianceFlipUtil.get(FieldConstants.rightMiddle, FieldConstants.leftMiddle),
          wantShoot);
      setIdleState(IdleState.IDLE_FERRY_DEPOT);
      led.wave(
          Color.kBlack,
          AllianceFlipUtil.get(
              new Color(0.26078432f, 1.0f, 0.36078432f),
              new Color(1.0f, 0.49803922f, 0.83137256f)),
          0.1,
          1.25);
      break;
    case OTHER_ALLIANCEZONE_OUTPOST:
      applyAimingSetpoints(
          robotPose,
          robotSpeeds,
          AllianceFlipUtil.get(FieldConstants.leftMiddle, FieldConstants.rightMiddle),
          wantShoot);
      setIdleState(IdleState.IDLE_FERRY_OUTPOST);
      led.wave(
          Color.kBlack,
          AllianceFlipUtil.get(
              new Color(0.26078432f, 1.0f, 0.36078432f),
              new Color(1.0f, 0.49803922f, 0.83137256f)),
          0.1,
```

### 2025: Select alliance-specific headings and poses (legacy package names)

[`src/main/java/frc2025/RobotContainer.java` lines 190–228](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/RobotContainer.java#L190-L228)

```java
if (Robot.isSimulation()) {
    configureSimulationOverrides();
    drivetrain.resetPose(
        AllianceFlipUtil.get(
            Pose2d.kZero, new Pose2d(FieldConstants.FIELD_DIMENSIONS, Rotation2d.k180deg)));
  }
}

private void configureBindings() {

  Controlboard.driveController
      .back()
      .onTrue(Commands.runOnce(() -> drivetrain.resetRotation(AllianceFlipUtil.getFwdHeading())));

  // Auto aligning controls
  Controlboard.alignToReef()
      .and(() -> robotState.getReefZone().isPresent())
      .toggleOnTrue(autoAlign);

  Controlboard.driveController
      .rightStick()
      .whileTrue(
          /* Commands.parallel(
          new DriveToPose(
                  subsystems,
                  () ->
                      AllianceFlipUtil.get(
                          FieldConstants.BLUE_BARGE_ALIGN, FieldConstants.RED_BARGE_ALIGN),
                  () -> Controlboard.getTranslation().get().getY())
              .onlyIf(() -> !Dashboard.disableAutoFeatures.get()), */
          /* Commands.sequence(
          Commands.waitUntil(
              () ->
                  AllianceFlipUtil.get(
                          drivetrain.getEstimatedPose().getX()
                              > FieldConstants.BLUE_BARGE_ALIGN
                                  .getTranslation()
                                  .minus(new Translation2d(3.0, 0))
```

## Public and protected callables

### `public static BooleanSupplier shouldFlip()`

[Source lines 24–26](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L24)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.
- Return path: `() -> DriverStation.getAlliance().filter(value -> value == Alliance.Red).isPresent()`.
- Key collaborators/calls: `DriverStation.getAlliance()`, `filter()`, `isPresent()`.

**Inputs:** None.

**Result:** Returns `BooleanSupplier`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 24–26)"

    ```java
    public static BooleanSupplier shouldFlip() {
      return () -> DriverStation.getAlliance().filter(value -> value == Alliance.Red).isPresent();
    }
    ```

### `public static Rotation2d getFwdHeading()`

[Source lines 29–31](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L29)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `get(Rotation2d.kZero, Rotation2d.k180deg)`.
- Key collaborators/calls: `get()`.

**Inputs:** None.

**Result:** Returns `Rotation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 29–31)"

    ```java
    public static Rotation2d getFwdHeading() {
      return get(Rotation2d.kZero, Rotation2d.k180deg);
    }
    ```

### `public static int getDirectionCoefficient()`

[Source lines 34–36](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L34)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `(int) get(1, -1)`.
- Key collaborators/calls: `get()`.

**Inputs:** None.

**Result:** Returns `int`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 34–36)"

    ```java
    public static int getDirectionCoefficient() {
      return (int) get(1, -1);
    }
    ```

### `public static &lt;T&gt; T get(T blueValue, T redValue)`

[Source lines 39–41](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L39)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `get(blueValue, redValue, false)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `T` | `T` input consumed by the implementation shown below. |
| `redValue` | `T` | `T` input consumed by the implementation shown below. |

**Result:** Returns `&lt;T&gt; T`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 39–41)"

    ```java
    public static <T> T get(T blueValue, T redValue) {
      return get(blueValue, redValue, false);
    }
    ```

### `public static &lt;T&gt; T get(T blueValue, T redValue, boolean inverse)`

[Source lines 50–54](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L50)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `(inverse && !shouldFlip().getAsBoolean() || !inverse && shouldFlip().getAsBoolean()) ? redValue : blueValue`.
- Key collaborators/calls: `shouldFlip()`, `getAsBoolean()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `T` | `T` input consumed by the implementation shown below. |
| `redValue` | `T` | `T` input consumed by the implementation shown below. |
| `inverse` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** Returns `&lt;T&gt; T`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 50–54)"

    ```java
    public static <T> T get(T blueValue, T redValue, boolean inverse) {
      return (inverse && !shouldFlip().getAsBoolean() || !inverse && shouldFlip().getAsBoolean())
          ? redValue
          : blueValue;
    }
    ```

### `public static Rotation2d FlippedRotation2d(Rotation2d blueValue)`

[Source lines 57–59](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L57)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `get(blueValue, blueValue.plus(Rotation2d.k180deg))`.
- Key collaborators/calls: `get()`, `blueValue.plus()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Rotation2d` | `Rotation2d` input consumed by the implementation shown below. |

**Result:** Returns `Rotation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 57–59)"

    ```java
    public static Rotation2d FlippedRotation2d(Rotation2d blueValue) {
      return get(blueValue, blueValue.plus(Rotation2d.k180deg));
    }
    ```

### `public static Rotation3d FlippedRotation3d(Rotation3d blueValue)`

[Source lines 62–67](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L62)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `new Rotation3d( blueValue.getX(), blueValue.getY(), FlippedRotation2d(Rotation2d.fromRadians(blueValue.getZ())).getRadians())`.
- Key collaborators/calls: `Rotation3d()`, `blueValue.getX()`, `blueValue.getY()`, `FlippedRotation2d()`, `Rotation2d.fromRadians()`, `blueValue.getZ()`, `getRadians()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Rotation3d` | `Rotation3d` input consumed by the implementation shown below. |

**Result:** Returns `Rotation3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 62–67)"

    ```java
    public static Rotation3d FlippedRotation3d(Rotation3d blueValue) {
      return new Rotation3d(
          blueValue.getX(),
          blueValue.getY(),
          FlippedRotation2d(Rotation2d.fromRadians(blueValue.getZ())).getRadians());
    }
    ```

### `public static Translation2d FlippedTranslation2d(Translation2d blueValue)`

[Source lines 70–76](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L70)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `get( blueValue, new Translation2d( FIELD_LENGTH - blueValue.getX(), FIELD_WIDTH - blueValue.getY()))`.
- Key collaborators/calls: `get()`, `Translation2d()`, `blueValue.getX()`, `blueValue.getY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Translation2d` | `Translation2d` input consumed by the implementation shown below. |

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 70–76)"

    ```java
    public static Translation2d FlippedTranslation2d(Translation2d blueValue) {
      return get(
          blueValue,
          new Translation2d(
              FIELD_LENGTH - blueValue.getX(),
              FIELD_WIDTH - blueValue.getY()));
    }
    ```

### `public static Pose2d FlippedPose2d(Pose2d blueValue)`

[Source lines 79–83](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L79)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `new Pose2d( FlippedTranslation2d(blueValue.getTranslation()), FlippedRotation2d(blueValue.getRotation()))`.
- Key collaborators/calls: `Pose2d()`, `FlippedTranslation2d()`, `blueValue.getTranslation()`, `FlippedRotation2d()`, `blueValue.getRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Pose2d` | `Pose2d` input consumed by the implementation shown below. |

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 79–83)"

    ```java
    public static Pose2d FlippedPose2d(Pose2d blueValue) {
      return new Pose2d(
          FlippedTranslation2d(blueValue.getTranslation()),
          FlippedRotation2d(blueValue.getRotation()));
    }
    ```

### `public static Translation3d FlippedTranslation3d(Translation3d blueValue)`

[Source lines 86–93](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L86)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- Return path: `get( blueValue, new Translation3d( FIELD_LENGTH - blueValue.getX(), FIELD_WIDTH - blueValue.getY(), blueValue.getZ()))`.
- Key collaborators/calls: `get()`, `Translation3d()`, `blueValue.getX()`, `blueValue.getY()`, `blueValue.getZ()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Translation3d` | `Translation3d` input consumed by the implementation shown below. |

**Result:** Returns `Translation3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 86–93)"

    ```java
    public static Translation3d FlippedTranslation3d(Translation3d blueValue) {
      return get(
          blueValue,
          new Translation3d(
              FIELD_LENGTH - blueValue.getX(),
              FIELD_WIDTH - blueValue.getY(),
              blueValue.getZ()));
    }
    ```

### `public static Pose3d FlippedPose3d(Pose3d blueValue)`

[Source lines 96–100](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L96)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `new Pose3d( FlippedTranslation3d(blueValue.getTranslation()), FlippedRotation3d(blueValue.getRotation()))`.
- Key collaborators/calls: `Pose3d()`, `FlippedTranslation3d()`, `blueValue.getTranslation()`, `FlippedRotation3d()`, `blueValue.getRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Pose3d` | `Pose3d` input consumed by the implementation shown below. |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 96–100)"

    ```java
    public static Pose3d FlippedPose3d(Pose3d blueValue) {
      return new Pose3d(
          FlippedTranslation3d(blueValue.getTranslation()),
          FlippedRotation3d(blueValue.getRotation()));
    }
    ```

### `public static Rotation2d MirroredRotation2d(Rotation2d blueValue)`

[Source lines 103–105](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L103)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `get(blueValue, Rotation2d.k180deg.minus(blueValue))`.
- Key collaborators/calls: `get()`, `Rotation2d.k180deg.minus()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Rotation2d` | `Rotation2d` input consumed by the implementation shown below. |

**Result:** Returns `Rotation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 103–105)"

    ```java
    public static Rotation2d MirroredRotation2d(Rotation2d blueValue) {
      return get(blueValue, Rotation2d.k180deg.minus(blueValue));
    }
    ```

### `public static Rotation3d MirroredRotation3d(Rotation3d blueValue)`

[Source lines 108–113](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L108)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `new Rotation3d( blueValue.getX(), blueValue.getY(), MirroredRotation2d(Rotation2d.fromRadians(blueValue.getZ())).getRadians())`.
- Key collaborators/calls: `Rotation3d()`, `blueValue.getX()`, `blueValue.getY()`, `MirroredRotation2d()`, `Rotation2d.fromRadians()`, `blueValue.getZ()`, `getRadians()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Rotation3d` | `Rotation3d` input consumed by the implementation shown below. |

**Result:** Returns `Rotation3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 108–113)"

    ```java
    public static Rotation3d MirroredRotation3d(Rotation3d blueValue) {
      return new Rotation3d(
          blueValue.getX(),
          blueValue.getY(),
          MirroredRotation2d(Rotation2d.fromRadians(blueValue.getZ())).getRadians());
    }
    ```

### `public static Translation2d MirroredTranslation2d(Translation2d blueValue)`

[Source lines 116–119](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L116)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `get( blueValue, new Translation2d(FIELD_DIMENSIONS.getX() - blueValue.getX(), blueValue.getY()))`.
- Key collaborators/calls: `get()`, `Translation2d()`, `FIELD_DIMENSIONS.getX()`, `blueValue.getX()`, `blueValue.getY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Translation2d` | `Translation2d` input consumed by the implementation shown below. |

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 116–119)"

    ```java
    public static Translation2d MirroredTranslation2d(Translation2d blueValue) {
      return get(
          blueValue, new Translation2d(FIELD_DIMENSIONS.getX() - blueValue.getX(), blueValue.getY()));
    }
    ```

### `blueValue, new Translation2d(FIELD_DIMENSIONS.getX() - blueValue.getX(), blueValue.getY()))`

[Source lines 118–118](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L118)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue.getX()` | `FIELD_DIMENSIONS.getX() -` | `FIELD_DIMENSIONS.getX() -` input consumed by the implementation shown below. |

**Result:** Returns `blueValue, new`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 118)"

    ```java
    blueValue, new Translation2d(FIELD_DIMENSIONS.getX() - blueValue.getX(), blueValue.getY()));
    ```

### `public static Pose2d MirroredPose2d(Pose2d blueValue)`

[Source lines 122–126](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L122)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `new Pose2d( MirroredTranslation2d(blueValue.getTranslation()), MirroredRotation2d(blueValue.getRotation()))`.
- Key collaborators/calls: `Pose2d()`, `MirroredTranslation2d()`, `blueValue.getTranslation()`, `MirroredRotation2d()`, `blueValue.getRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Pose2d` | `Pose2d` input consumed by the implementation shown below. |

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 122–126)"

    ```java
    public static Pose2d MirroredPose2d(Pose2d blueValue) {
      return new Pose2d(
          MirroredTranslation2d(blueValue.getTranslation()),
          MirroredRotation2d(blueValue.getRotation()));
    }
    ```

### `public static Translation3d MirroredTranslation3d(Translation3d blueValue)`

[Source lines 129–134](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L129)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `get( blueValue, new Translation3d( FIELD_DIMENSIONS.getX() - blueValue.getX(), blueValue.getY(), blueValue.getZ()))`.
- Key collaborators/calls: `get()`, `Translation3d()`, `FIELD_DIMENSIONS.getX()`, `blueValue.getX()`, `blueValue.getY()`, `blueValue.getZ()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Translation3d` | `Translation3d` input consumed by the implementation shown below. |

**Result:** Returns `Translation3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 129–134)"

    ```java
    public static Translation3d MirroredTranslation3d(Translation3d blueValue) {
      return get(
          blueValue,
          new Translation3d(
              FIELD_DIMENSIONS.getX() - blueValue.getX(), blueValue.getY(), blueValue.getZ()));
    }
    ```

### `public static Pose3d MirroredPose3d(Pose3d blueValue)`

[Source lines 137–141](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L137)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `new Pose3d( MirroredTranslation3d(blueValue.getTranslation()), MirroredRotation3d(blueValue.getRotation()))`.
- Key collaborators/calls: `Pose3d()`, `MirroredTranslation3d()`, `blueValue.getTranslation()`, `MirroredRotation3d()`, `blueValue.getRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `blueValue` | `Pose3d` | `Pose3d` input consumed by the implementation shown below. |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 137–141)"

    ```java
    public static Pose3d MirroredPose3d(Pose3d blueValue) {
      return new Pose3d(
          MirroredTranslation3d(blueValue.getTranslation()),
          MirroredRotation3d(blueValue.getRotation()));
    }
    ```

## Exposed fields and types

### `public final class AllianceFlipUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L14)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static final Translation2d FIELD_DIMENSIONS = new Translation2d(16.541, 8.211)`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L17)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 5 times, so changing it can affect every control path that reads `FIELD_DIMENSIONS`.

### `public static final double FIELD_WIDTH = FIELD_DIMENSIONS.getY()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L19)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `FIELD_WIDTH`.

### `public static final double FIELD_LENGTH = FIELD_DIMENSIONS.getX()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L21)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `FIELD_LENGTH`.
