# BLineUtil

`com.teamscreamrobotics.util.BLineUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java) · **6 callables** · **1 exposed fields/types**

## Public and protected callables

### `public static Command driveToPose(FollowPath.Builder builder, Pose2d target)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L23)*

Drives to a fixed pose; the path is constructed fresh each time the command is scheduled.

### `public static Command driveToPose(FollowPath.Builder builder, Supplier&lt;Pose2d&gt; target)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L32)*

Drives to a dynamically-supplied pose; the supplier is called at schedule time.

### `public static Command driveToPose(FollowPath.Builder builder, Pose2d target, Path.PathConstraints constraints)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L41)*

Drives to a fixed pose with custom per-path constraints (speed limits, tolerances).

### `public static Command driveToPose(FollowPath.Builder builder, Supplier&lt;Pose2d&gt; target, Path.PathConstraints constraints)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L51)*

Drives to a dynamically-supplied pose with custom constraints; both are evaluated at schedule time.

### `public static Command driveToTranslation(FollowPath.Builder builder, Translation2d target)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L61)*

Drives to a fixed translation without commanding any heading change.

### `public static Command driveToTranslation(FollowPath.Builder builder, Supplier&lt;Translation2d&gt; target)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L71)*

Drives to a dynamically-supplied translation without commanding any heading change;
the supplier is called at schedule time.

## Exposed fields and types

### `public final class BLineUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L19)*

Static factory methods for BLine drive-to-pose commands.

All methods return a `Commands.deferredProxy`-wrapped command so path construction
is deferred until schedule time, making them safe to store and re-schedule without
capturing a stale robot pose.
