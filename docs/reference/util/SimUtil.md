# SimUtil

`com.teamscreamrobotics.util.SimUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java) · **4 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public static DCMotorSim createDCMotorSim( DCMotor gearbox, double gearing, double JKgMetersSquaredMOI)`

[Source lines 18–22](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java#L18)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `new DCMotorSim( LinearSystemId.createDCMotorSystem(gearbox, JKgMetersSquaredMOI, gearing), gearbox)`.
- Key collaborators/calls: `DCMotorSim()`, `LinearSystemId.createDCMotorSystem()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `gearbox` | `DCMotor` | `DCMotor` input consumed by the implementation shown below. |
| `gearing` | `double` | `double` input consumed by the implementation shown below. |
| `JKgMetersSquaredMOI` | `double` | Linear value in meters. |

**Result:** Returns `DCMotorSim`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 18–22)"

    ```java
    public static DCMotorSim createDCMotorSim(
        DCMotor gearbox, double gearing, double JKgMetersSquaredMOI) {
      return new DCMotorSim(
          LinearSystemId.createDCMotorSystem(gearbox, JKgMetersSquaredMOI, gearing), gearbox);
    }
    ```

### `public static DCMotorSim createDCMotorSim( DCMotor gearbox, double gearing, double JKgMetersSquaredMOI, double positionStdDev, double velocityStdDev)`

[Source lines 33–44](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java#L33)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `new DCMotorSim( LinearSystemId.createDCMotorSystem(gearbox, JKgMetersSquaredMOI, gearing), gearbox, positionStdDev, velocityStdDev)`.
- Key collaborators/calls: `DCMotorSim()`, `LinearSystemId.createDCMotorSystem()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `gearbox` | `DCMotor` | `DCMotor` input consumed by the implementation shown below. |
| `gearing` | `double` | `double` input consumed by the implementation shown below. |
| `JKgMetersSquaredMOI` | `double` | Linear value in meters. |
| `positionStdDev` | `double` | Position in the units required by this API and configuration. |
| `velocityStdDev` | `double` | Velocity/speed in the units required by this API and configuration. |

**Result:** Returns `DCMotorSim`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 33–44)"

    ```java
    public static DCMotorSim createDCMotorSim(
        DCMotor gearbox,
        double gearing,
        double JKgMetersSquaredMOI,
        double positionStdDev,
        double velocityStdDev) {
      return new DCMotorSim(
          LinearSystemId.createDCMotorSystem(gearbox, JKgMetersSquaredMOI, gearing),
          gearbox,
          positionStdDev,
          velocityStdDev);
    }
    ```

### `public static FlywheelSim createFlywheelSim( DCMotor gearbox, double gearing, double JKgMetersSquaredMOI)`

[Source lines 53–57](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java#L53)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `new FlywheelSim( LinearSystemId.createFlywheelSystem(gearbox, JKgMetersSquaredMOI, gearing), gearbox)`.
- Key collaborators/calls: `FlywheelSim()`, `LinearSystemId.createFlywheelSystem()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `gearbox` | `DCMotor` | `DCMotor` input consumed by the implementation shown below. |
| `gearing` | `double` | `double` input consumed by the implementation shown below. |
| `JKgMetersSquaredMOI` | `double` | Linear value in meters. |

**Result:** Returns `FlywheelSim`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 53–57)"

    ```java
    public static FlywheelSim createFlywheelSim(
        DCMotor gearbox, double gearing, double JKgMetersSquaredMOI) {
      return new FlywheelSim(
          LinearSystemId.createFlywheelSystem(gearbox, JKgMetersSquaredMOI, gearing), gearbox);
    }
    ```

### `public static FlywheelSim createFlywheelSim( DCMotor gearbox, double gearing, double JKgMetersSquaredMOI, double positionStdDev, double velocityStdDev)`

[Source lines 68–79](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java#L68)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `new FlywheelSim( LinearSystemId.createFlywheelSystem(gearbox, JKgMetersSquaredMOI, gearing), gearbox, positionStdDev, velocityStdDev)`.
- Key collaborators/calls: `FlywheelSim()`, `LinearSystemId.createFlywheelSystem()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `gearbox` | `DCMotor` | `DCMotor` input consumed by the implementation shown below. |
| `gearing` | `double` | `double` input consumed by the implementation shown below. |
| `JKgMetersSquaredMOI` | `double` | Linear value in meters. |
| `positionStdDev` | `double` | Position in the units required by this API and configuration. |
| `velocityStdDev` | `double` | Velocity/speed in the units required by this API and configuration. |

**Result:** Returns `FlywheelSim`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 68–79)"

    ```java
    public static FlywheelSim createFlywheelSim(
        DCMotor gearbox,
        double gearing,
        double JKgMetersSquaredMOI,
        double positionStdDev,
        double velocityStdDev) {
      return new FlywheelSim(
          LinearSystemId.createFlywheelSystem(gearbox, JKgMetersSquaredMOI, gearing),
          gearbox,
          positionStdDev,
          velocityStdDev);
    }
    ```

## Exposed fields and types

### `public class SimUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/SimUtil.java#L9)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
