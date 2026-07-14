# PPUtil

`com.teamscreamrobotics.util.PPUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPUtil.java) · **2 callables** · **1 exposed fields/types** · **1 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2025: Use `PPUtil` in `DrivetrainConstants.java`

[`src/main/java/frc2025/subsystems/drivetrain/DrivetrainConstants.java` lines 53–60](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/drivetrain/DrivetrainConstants.java#L53-L60)

```java
new RobotConfig(
          Units.lbsToKilograms(150), 6.883, MODULE_CONFIG, TunerConstants.TRACK_WIDTH.getMeters());

  public static final PathFollowingController PATH_FOLLOWING_CONTROLLER =
      new PPHolonomicDriveController(
          PPUtil.screamPIDConstantsToPPConstants(PATH_TRANSLATION_CONSTANTS),
          PPUtil.screamPIDConstantsToPPConstants(PATH_ROTATION_CONSTANTS));
}
```

## Public and protected callables

### `public static PIDConstants screamPIDConstantsToPPConstants( ScreamPIDConstants screamPIDConstants)`

[Source lines 17–24](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPUtil.java#L17)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `new PIDConstants( screamPIDConstants.kP(), screamPIDConstants.kI(), screamPIDConstants.kD(), screamPIDConstants.integralZone())`.
- Key collaborators/calls: `PIDConstants()`, `screamPIDConstants.kP()`, `screamPIDConstants.kI()`, `screamPIDConstants.kD()`, `screamPIDConstants.integralZone()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `screamPIDConstants` | `ScreamPIDConstants` | the source constants |

**Result:** Returns `PIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 17–24)"

    ```java
    public static PIDConstants screamPIDConstantsToPPConstants(
        ScreamPIDConstants screamPIDConstants) {
      return new PIDConstants(
          screamPIDConstants.kP(),
          screamPIDConstants.kI(),
          screamPIDConstants.kD(),
          screamPIDConstants.integralZone());
    }
    ```

??? note "Author note from JavaDoc"

    Converts a `ScreamPIDConstants` to PathPlanner's `PIDConstants`.
    
    **Parameter `screamPIDConstants`:** the source constants

### `public static Optional&lt;PathPlannerPath&gt; loadPathFile(String pathName)`

[Source lines 31–39](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPUtil.java#L31)

**Detailed behavior**

- The implementation executes 7 non-blank source lines.
- It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.
- Return paths: `Optional.of(PathPlannerPath.fromPathFile(pathName))`; `Optional.empty()`.
- Key collaborators/calls: `Optional.of()`, `PathPlannerPath.fromPathFile()`, `DriverStation.reportError()`, `e.getMessage()`, `e.getStackTrace()`, `Optional.empty()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pathName` | `String` | the path name (no file extension) |

**Result:** Returns `Optional&lt;PathPlannerPath&gt;`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 31–39)"

    ```java
    public static Optional<PathPlannerPath> loadPathFile(String pathName) {
      try {
        return Optional.of(PathPlannerPath.fromPathFile(pathName));
      } catch (Exception e) {
        DriverStation.reportError(
            "Failed to load path: " + pathName + " | " + e.getMessage(), e.getStackTrace());
        return Optional.empty();
      }
    }
    ```

??? note "Author note from JavaDoc"

    Loads a PathPlanner path file, returning `Optional#empty()` and logging a DS error on failure.
    
    **Parameter `pathName`:** the path name (no file extension)

## Exposed fields and types

### `public class PPUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPUtil.java#L10)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Utilities for integrating `ScreamPIDConstants` and PathPlanner.
