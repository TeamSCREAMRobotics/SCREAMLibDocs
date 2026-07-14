# Logger

`com.teamscreamrobotics.util.Logger`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java) · **69 callables** · **1 exposed fields/types** · **4 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## How logging dispatch works

`Logger` is a static overload layer over DogLog. Each `log(...)` overload converts or forwards one supported WPILib/Java value type to DogLog under the supplied key. Geometry arrays are flattened through `DataConversions`; structured objects such as trajectories and swerve states are converted to the numeric representation expected by dashboards and log readers. Timed overloads rate-limit publication through a per-key timestamp map. Review the exact overload below because array shape and unit representation differ by type.


## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

!!! note "2025 package names"
    The 2025 robot used SCREAMLib's earlier short packages such as `data`, `drivers`, and `util`. With SCREAMLib 26.3.7, prefix those imports with `com.teamscreamrobotics.`; the implementation pattern remains applicable.

### 2025: Use `Logger` in `Robot.java`

[`src/main/java/frc2025/Robot.java` lines 35–50](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/Robot.java#L35-L50)

```java
public Robot() {
  // super(0.0225);
  robotContainer = new RobotContainer();

  Logger.setOptions(
      new DogLogOptions()
          .withCaptureDs(true)
          .withCaptureNt(true)
          .withLogExtras(true)
          .withNtPublish(true)
          .withLogEntryQueueCapacity(2000));
  Logger.setEnabled(true);

  SignalLogger.enableAutoLogging(true);
```

### 2025: Use `Logger` in `RobotState.java`

[`src/main/java/frc2025/RobotState.java` lines 134–149](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/RobotState.java#L134-L149)

```java
if (drivetrain.getEstimatedPose().getY() <= FieldConstants.FIELD_DIMENSIONS.getY() / 2.0) {
    angle = AllianceFlipUtil.get(Rotation2d.fromDegrees(54), Rotation2d.fromDegrees(126));
  } else {
    angle = AllianceFlipUtil.get(Rotation2d.fromDegrees(-54), Rotation2d.fromDegrees(-126));
  }
  Logger.log("RobotState/StationAlignAngle", angle.getDegrees());
  return angle;
}

public void logTelemetry() {
  /* getReefZone()
  .ifPresent(
      reefZone -> {
        Logger.log(
            "Field/ScoringLocations",
            new Pose2d[] {
```

### 2026: Use `Logger` in `Robot.java`

[`src/main/java/frc2026/tars/Robot.java` lines 17–32](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/Robot.java#L17-L32)

```java
public Robot() {
  m_robotContainer = new RobotContainer();

  Dashboard.initialize();

  Logger.setOptions(
      new DogLogOptions()
          .withCaptureDs(true)
          .withCaptureNt(false)
          .withLogExtras(true)
          .withNtPublish(true)
          .withUseLogThread(false)
          .withLogEntryQueueCapacity(2000));
  Logger.setEnabled(true);

  SignalLogger.start();
```

### 2026: Use `Logger` in `RobotContainer.java`

[`src/main/java/frc2026/tars/RobotContainer.java` lines 313–328](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/RobotContainer.java#L313-L328)

```java
public Command getAutonomousCommand() {
  return routines.getRoutineChooser().getSelected();
}

public static void telemeterizeMechanisms(Mechanism2d measured, Mechanism2d setpoint) {
  Logger.log("RobotState/Mechanisms/Measured", measured);
  Logger.log("RobotState/Mechanisms/Setpoint", setpoint);
}

public void periodic() {
  visionManager.periodic();
  robotState.logArea();

  SmartDashboard.putNumber("Match Time", DriverStation.getMatchTime());
  HubTracker.timeRemainingInCurrentShift()
      .ifPresentOrElse(
```

## Public and protected callables

### `public static void enableDebug(boolean enable)`

[Source lines 16–18](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L16)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `enable` | `boolean` | Enables the behavior when `true`; disables it when `false`. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 16–18)"

    ```java
    public static void enableDebug(boolean enable) {
      debug = enable;
    }
    ```

### `public static void log(String key, Mechanism2d value, double frequencySeconds)`

[Source lines 36–40](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L36)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `SmartDashboard.putData()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `Mechanism2d` | `Mechanism2d` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 36–40)"

    ```java
    public static void log(String key, Mechanism2d value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        SmartDashboard.putData(key, value);
      }
    }
    ```

### `public static void log(String key, Mechanism2d value)`

[Source lines 42–44](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L42)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `Mechanism2d` | `Mechanism2d` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 42–44)"

    ```java
    public static void log(String key, Mechanism2d value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, boolean value, double frequencySeconds)`

[Source lines 47–51](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L47)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `boolean` | `boolean` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 47–51)"

    ```java
    public static void log(String key, boolean value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, boolean value)`

[Source lines 53–55](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L53)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 53–55)"

    ```java
    public static void log(String key, boolean value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, double value, double frequencySeconds)`

[Source lines 58–62](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L58)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `double` | `double` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 58–62)"

    ```java
    public static void log(String key, double value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, double value)`

[Source lines 64–66](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L64)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 64–66)"

    ```java
    public static void log(String key, double value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, float value, double frequencySeconds)`

[Source lines 69–73](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L69)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `float` | `float` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 69–73)"

    ```java
    public static void log(String key, float value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, float value)`

[Source lines 75–77](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L75)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `float` | `float` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 75–77)"

    ```java
    public static void log(String key, float value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, int value, double frequencySeconds)`

[Source lines 80–84](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L80)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `int` | `int` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 80–84)"

    ```java
    public static void log(String key, int value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, int value)`

[Source lines 86–88](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L86)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `int` | `int` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 86–88)"

    ```java
    public static void log(String key, int value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, long value, double frequencySeconds)`

[Source lines 91–95](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L91)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `long` | `long` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 91–95)"

    ```java
    public static void log(String key, long value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, long value)`

[Source lines 97–99](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L97)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `long` | `long` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 97–99)"

    ```java
    public static void log(String key, long value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, String value, double frequencySeconds)`

[Source lines 102–106](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L102)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `String` | `String` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 102–106)"

    ```java
    public static void log(String key, String value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, String value)`

[Source lines 108–110](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L108)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `String` | `String` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 108–110)"

    ```java
    public static void log(String key, String value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static &lt;E extends Enum&lt;E&gt;&gt; void log(String key, E value, double frequencySeconds)`

[Source lines 113–117](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L113)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `E` | `E` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** Returns `&lt;E extends Enum&lt;E&gt;&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 113–117)"

    ```java
    public static <E extends Enum<E>> void log(String key, E value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static &lt;E extends Enum&lt;E&gt;&gt; void log(String key, E value)`

[Source lines 119–121](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L119)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `E` | `E` input consumed by the implementation shown below. |

**Result:** Returns `&lt;E extends Enum&lt;E&gt;&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 119–121)"

    ```java
    public static <E extends Enum<E>> void log(String key, E value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static &lt;T extends StructSerializable&gt; void log( String key, T value, double frequencySeconds)`

[Source lines 124–129](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L124)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `T` | `T` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** Returns `&lt;T extends StructSerializable&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 124–129)"

    ```java
    public static <T extends StructSerializable> void log(
        String key, T value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static &lt;T extends StructSerializable&gt; void log(String key, T value)`

[Source lines 131–133](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L131)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `T` | `T` input consumed by the implementation shown below. |

**Result:** Returns `&lt;T extends StructSerializable&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 131–133)"

    ```java
    public static <T extends StructSerializable> void log(String key, T value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, boolean[] value, double frequencySeconds)`

[Source lines 138–142](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L138)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `boolean[]` | `boolean[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 138–142)"

    ```java
    public static void log(String key, boolean[] value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, boolean[] value)`

[Source lines 144–146](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L144)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `boolean[]` | `boolean[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 144–146)"

    ```java
    public static void log(String key, boolean[] value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, double[] value, double frequencySeconds)`

[Source lines 149–153](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L149)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `double[]` | `double[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 149–153)"

    ```java
    public static void log(String key, double[] value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, double[] value)`

[Source lines 155–157](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L155)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `double[]` | `double[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 155–157)"

    ```java
    public static void log(String key, double[] value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, float[] value, double frequencySeconds)`

[Source lines 160–164](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L160)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `float[]` | `float[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 160–164)"

    ```java
    public static void log(String key, float[] value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, float[] value)`

[Source lines 166–168](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L166)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `float[]` | `float[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 166–168)"

    ```java
    public static void log(String key, float[] value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, int[] value, double frequencySeconds)`

[Source lines 171–175](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L171)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `int[]` | `int[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 171–175)"

    ```java
    public static void log(String key, int[] value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, int[] value)`

[Source lines 177–179](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L177)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `int[]` | `int[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 177–179)"

    ```java
    public static void log(String key, int[] value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, long[] value, double frequencySeconds)`

[Source lines 182–186](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L182)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `long[]` | `long[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 182–186)"

    ```java
    public static void log(String key, long[] value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, long[] value)`

[Source lines 188–190](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L188)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `long[]` | `long[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 188–190)"

    ```java
    public static void log(String key, long[] value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void log(String key, String[] value, double frequencySeconds)`

[Source lines 193–197](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L193)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `String[]` | `String[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 193–197)"

    ```java
    public static void log(String key, String[] value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static void log(String key, String[] value)`

[Source lines 199–201](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L199)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `String[]` | `String[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 199–201)"

    ```java
    public static void log(String key, String[] value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static &lt;E extends Enum&lt;E&gt;&gt; void log(String key, E[] value, double frequencySeconds)`

[Source lines 204–208](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L204)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `E[]` | `E[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** Returns `&lt;E extends Enum&lt;E&gt;&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 204–208)"

    ```java
    public static <E extends Enum<E>> void log(String key, E[] value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static &lt;E extends Enum&lt;E&gt;&gt; void log(String key, E[] value)`

[Source lines 210–212](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L210)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `E[]` | `E[]` input consumed by the implementation shown below. |

**Result:** Returns `&lt;E extends Enum&lt;E&gt;&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 210–212)"

    ```java
    public static <E extends Enum<E>> void log(String key, E[] value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static &lt;T extends StructSerializable&gt; void log( String key, T[] value, double frequencySeconds)`

[Source lines 215–220](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L215)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `T[]` | `T[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** Returns `&lt;T extends StructSerializable&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 215–220)"

    ```java
    public static <T extends StructSerializable> void log(
        String key, T[] value, double frequencySeconds) {
      if (shouldLog(key, frequencySeconds)) {
        DogLog.log(key, value);
      }
    }
    ```

### `public static &lt;T extends StructSerializable&gt; void log(String key, T[] value)`

[Source lines 222–224](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L222)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `T[]` | `T[]` input consumed by the implementation shown below. |

**Result:** Returns `&lt;T extends StructSerializable&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 222–224)"

    ```java
    public static <T extends StructSerializable> void log(String key, T[] value) {
      log(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, Mechanism2d value, double frequencySeconds)`

[Source lines 229–233](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L229)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `SmartDashboard.putData()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `Mechanism2d` | `Mechanism2d` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 229–233)"

    ```java
    public static void logDebug(String key, Mechanism2d value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        SmartDashboard.putData(key, value);
      }
    }
    ```

### `public static void logDebug(String key, Mechanism2d value)`

[Source lines 235–237](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L235)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `Mechanism2d` | `Mechanism2d` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 235–237)"

    ```java
    public static void logDebug(String key, Mechanism2d value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, boolean value, double frequencySeconds)`

[Source lines 240–244](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L240)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `boolean` | `boolean` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 240–244)"

    ```java
    public static void logDebug(String key, boolean value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, boolean value)`

[Source lines 246–248](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L246)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 246–248)"

    ```java
    public static void logDebug(String key, boolean value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, double value, double frequencySeconds)`

[Source lines 251–255](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L251)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `double` | `double` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 251–255)"

    ```java
    public static void logDebug(String key, double value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, double value)`

[Source lines 257–259](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L257)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 257–259)"

    ```java
    public static void logDebug(String key, double value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, float value, double frequencySeconds)`

[Source lines 262–266](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L262)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `float` | `float` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 262–266)"

    ```java
    public static void logDebug(String key, float value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, float value)`

[Source lines 268–270](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L268)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `float` | `float` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 268–270)"

    ```java
    public static void logDebug(String key, float value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, int value, double frequencySeconds)`

[Source lines 273–277](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L273)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `int` | `int` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 273–277)"

    ```java
    public static void logDebug(String key, int value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, int value)`

[Source lines 279–281](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L279)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `int` | `int` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 279–281)"

    ```java
    public static void logDebug(String key, int value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, long value, double frequencySeconds)`

[Source lines 284–288](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L284)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `long` | `long` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 284–288)"

    ```java
    public static void logDebug(String key, long value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, long value)`

[Source lines 290–292](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L290)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `long` | `long` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 290–292)"

    ```java
    public static void logDebug(String key, long value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, String value, double frequencySeconds)`

[Source lines 295–299](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L295)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `String` | `String` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 295–299)"

    ```java
    public static void logDebug(String key, String value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, String value)`

[Source lines 301–303](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L301)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `String` | `String` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 301–303)"

    ```java
    public static void logDebug(String key, String value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static &lt;E extends Enum&lt;E&gt;&gt; void logDebug(String key, E value, double frequencySeconds)`

[Source lines 306–310](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L306)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `E` | `E` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** Returns `&lt;E extends Enum&lt;E&gt;&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 306–310)"

    ```java
    public static <E extends Enum<E>> void logDebug(String key, E value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static &lt;E extends Enum&lt;E&gt;&gt; void logDebug(String key, E value)`

[Source lines 312–314](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L312)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `E` | `E` input consumed by the implementation shown below. |

**Result:** Returns `&lt;E extends Enum&lt;E&gt;&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 312–314)"

    ```java
    public static <E extends Enum<E>> void logDebug(String key, E value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static &lt;T extends StructSerializable&gt; void logDebug( String key, T value, double frequencySeconds)`

[Source lines 317–322](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L317)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `T` | `T` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** Returns `&lt;T extends StructSerializable&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 317–322)"

    ```java
    public static <T extends StructSerializable> void logDebug(
        String key, T value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static &lt;T extends StructSerializable&gt; void logDebug(String key, T value)`

[Source lines 324–326](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L324)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `T` | `T` input consumed by the implementation shown below. |

**Result:** Returns `&lt;T extends StructSerializable&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 324–326)"

    ```java
    public static <T extends StructSerializable> void logDebug(String key, T value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, boolean[] value, double frequencySeconds)`

[Source lines 331–335](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L331)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `boolean[]` | `boolean[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 331–335)"

    ```java
    public static void logDebug(String key, boolean[] value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, boolean[] value)`

[Source lines 337–339](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L337)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `boolean[]` | `boolean[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 337–339)"

    ```java
    public static void logDebug(String key, boolean[] value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, double[] value, double frequencySeconds)`

[Source lines 342–346](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L342)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `double[]` | `double[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 342–346)"

    ```java
    public static void logDebug(String key, double[] value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, double[] value)`

[Source lines 348–350](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L348)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `double[]` | `double[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 348–350)"

    ```java
    public static void logDebug(String key, double[] value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, float[] value, double frequencySeconds)`

[Source lines 353–357](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L353)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `float[]` | `float[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 353–357)"

    ```java
    public static void logDebug(String key, float[] value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, float[] value)`

[Source lines 359–361](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L359)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `float[]` | `float[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 359–361)"

    ```java
    public static void logDebug(String key, float[] value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, int[] value, double frequencySeconds)`

[Source lines 364–368](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L364)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `int[]` | `int[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 364–368)"

    ```java
    public static void logDebug(String key, int[] value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, int[] value)`

[Source lines 370–372](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L370)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `int[]` | `int[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 370–372)"

    ```java
    public static void logDebug(String key, int[] value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, long[] value, double frequencySeconds)`

[Source lines 375–379](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L375)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `long[]` | `long[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 375–379)"

    ```java
    public static void logDebug(String key, long[] value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, long[] value)`

[Source lines 381–383](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L381)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `long[]` | `long[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 381–383)"

    ```java
    public static void logDebug(String key, long[] value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static void logDebug(String key, String[] value, double frequencySeconds)`

[Source lines 386–390](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L386)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `String[]` | `String[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 386–390)"

    ```java
    public static void logDebug(String key, String[] value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static void logDebug(String key, String[] value)`

[Source lines 392–394](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L392)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `String[]` | `String[]` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 392–394)"

    ```java
    public static void logDebug(String key, String[] value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static &lt;E extends Enum&lt;E&gt;&gt; void logDebug(String key, E[] value, double frequencySeconds)`

[Source lines 397–401](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L397)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `E[]` | `E[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** Returns `&lt;E extends Enum&lt;E&gt;&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 397–401)"

    ```java
    public static <E extends Enum<E>> void logDebug(String key, E[] value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static &lt;E extends Enum&lt;E&gt;&gt; void logDebug(String key, E[] value)`

[Source lines 403–405](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L403)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `E[]` | `E[]` input consumed by the implementation shown below. |

**Result:** Returns `&lt;E extends Enum&lt;E&gt;&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 403–405)"

    ```java
    public static <E extends Enum<E>> void logDebug(String key, E[] value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

### `public static &lt;T extends StructSerializable&gt; void logDebug( String key, T[] value, double frequencySeconds)`

[Source lines 408–413](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L408)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `debug && shouldLog(key, frequencySeconds`.
- Key collaborators/calls: `shouldLog()`, `log()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `T[]` | `T[]` input consumed by the implementation shown below. |
| `frequencySeconds` | `double` | Time value in seconds. |

**Result:** Returns `&lt;T extends StructSerializable&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 408–413)"

    ```java
    public static <T extends StructSerializable> void logDebug(
        String key, T[] value, double frequencySeconds) {
      if (debug && shouldLog(key, frequencySeconds)) {
        log(key, value);
      }
    }
    ```

### `public static &lt;T extends StructSerializable&gt; void logDebug(String key, T[] value)`

[Source lines 415–417](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L415)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `T[]` | `T[]` input consumed by the implementation shown below. |

**Result:** Returns `&lt;T extends StructSerializable&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 415–417)"

    ```java
    public static <T extends StructSerializable> void logDebug(String key, T[] value) {
      logDebug(key, value, DEFAULT_LOG_FREQUENCY);
    }
    ```

## Exposed fields and types

### `public class Logger extends DogLog`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/Logger.java#L11)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
