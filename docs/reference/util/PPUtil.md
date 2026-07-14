# PPUtil

`com.teamscreamrobotics.util.PPUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPUtil.java) · **2 callables** · **1 exposed fields/types**

## Competition usage

**2025:** [`DrivetrainConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/drivetrain/DrivetrainConstants.java#L17)

## Public and protected callables

### `public static PIDConstants screamPIDConstantsToPPConstants( ScreamPIDConstants screamPIDConstants)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPUtil.java#L17)*

Converts a `ScreamPIDConstants` to PathPlanner's `PIDConstants`.

**Parameter `screamPIDConstants`:** the source constants

### `public static Optional&lt;PathPlannerPath&gt; loadPathFile(String pathName)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPUtil.java#L31)*

Loads a PathPlanner path file, returning `Optional#empty()` and logging a DS error on failure.

**Parameter `pathName`:** the path name (no file extension)

## Exposed fields and types

### `public class PPUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPUtil.java#L10)*

Utilities for integrating `ScreamPIDConstants` and PathPlanner.
