# BLineUtil

`com.teamscreamrobotics.util.BLineUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java) · **6 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public static Command driveToPose(FollowPath.Builder builder, Pose2d target)`

[Source lines 23–27](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L23)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `Commands.deferredProxy( () -> builder.build(new Path(new Path.Waypoint(target)))) .withName("BLineDriveToPose(" + target.getX() + ", " + target.getY() + ")")`.
- Key collaborators/calls: `Commands.deferredProxy()`, `builder.build()`, `Path()`, `Path.Waypoint()`, `withName()`, `target.getX()`, `target.getY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `builder` | `FollowPath.Builder` | `FollowPath.Builder` input consumed by the implementation shown below. |
| `target` | `Pose2d` | `Pose2d` input consumed by the implementation shown below. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 23–27)"

    ```java
    public static Command driveToPose(FollowPath.Builder builder, Pose2d target) {
        return Commands.deferredProxy(
                () -> builder.build(new Path(new Path.Waypoint(target))))
                .withName("BLineDriveToPose(" + target.getX() + ", " + target.getY() + ")");
    }
    ```

??? note "Author note from JavaDoc"

    Drives to a fixed pose; the path is constructed fresh each time the command is scheduled.

### `public static Command driveToPose(FollowPath.Builder builder, Supplier&lt;Pose2d&gt; target)`

[Source lines 32–36](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L32)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `Commands.deferredProxy( () -> builder.build(new Path(new Path.Waypoint(target.get())))) .withName("BLineDriveToPose(dynamic)")`.
- Key collaborators/calls: `Commands.deferredProxy()`, `builder.build()`, `Path()`, `Path.Waypoint()`, `target.get()`, `withName()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `builder` | `FollowPath.Builder` | `FollowPath.Builder` input consumed by the implementation shown below. |
| `target` | `Supplier&lt;Pose2d&gt;` | Callback evaluated at use time rather than construction time. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 32–36)"

    ```java
    public static Command driveToPose(FollowPath.Builder builder, Supplier<Pose2d> target) {
        return Commands.deferredProxy(
                () -> builder.build(new Path(new Path.Waypoint(target.get()))))
                .withName("BLineDriveToPose(dynamic)");
    }
    ```

??? note "Author note from JavaDoc"

    Drives to a dynamically-supplied pose; the supplier is called at schedule time.

### `public static Command driveToPose(FollowPath.Builder builder, Pose2d target, Path.PathConstraints constraints)`

[Source lines 41–46](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L41)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `Commands.deferredProxy( () -> builder.build(new Path(constraints, new Path.Waypoint(target)))) .withName("BLineDriveToPose(" + target.getX() + ", " + target.getY() + ")")`.
- Key collaborators/calls: `Commands.deferredProxy()`, `builder.build()`, `Path()`, `Path.Waypoint()`, `withName()`, `target.getX()`, `target.getY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `builder` | `FollowPath.Builder` | `FollowPath.Builder` input consumed by the implementation shown below. |
| `target` | `Pose2d` | `Pose2d` input consumed by the implementation shown below. |
| `constraints` | `Path.PathConstraints` | `Path.PathConstraints` input consumed by the implementation shown below. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 41–46)"

    ```java
    public static Command driveToPose(FollowPath.Builder builder, Pose2d target,
                                  Path.PathConstraints constraints) {
        return Commands.deferredProxy(
                () -> builder.build(new Path(constraints, new Path.Waypoint(target))))
                .withName("BLineDriveToPose(" + target.getX() + ", " + target.getY() + ")");
    }
    ```

??? note "Author note from JavaDoc"

    Drives to a fixed pose with custom per-path constraints (speed limits, tolerances).

### `public static Command driveToPose(FollowPath.Builder builder, Supplier&lt;Pose2d&gt; target, Path.PathConstraints constraints)`

[Source lines 51–56](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L51)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `Commands.deferredProxy( () -> builder.build(new Path(constraints, new Path.Waypoint(target.get())))) .withName("BLineDriveToPose(dynamic)")`.
- Key collaborators/calls: `Commands.deferredProxy()`, `builder.build()`, `Path()`, `Path.Waypoint()`, `target.get()`, `withName()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `builder` | `FollowPath.Builder` | `FollowPath.Builder` input consumed by the implementation shown below. |
| `target` | `Supplier&lt;Pose2d&gt;` | Callback evaluated at use time rather than construction time. |
| `constraints` | `Path.PathConstraints` | `Path.PathConstraints` input consumed by the implementation shown below. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 51–56)"

    ```java
    public static Command driveToPose(FollowPath.Builder builder, Supplier<Pose2d> target,
                                  Path.PathConstraints constraints) {
        return Commands.deferredProxy(
                () -> builder.build(new Path(constraints, new Path.Waypoint(target.get()))))
                .withName("BLineDriveToPose(dynamic)");
    }
    ```

??? note "Author note from JavaDoc"

    Drives to a dynamically-supplied pose with custom constraints; both are evaluated at schedule time.

### `public static Command driveToTranslation(FollowPath.Builder builder, Translation2d target)`

[Source lines 61–65](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L61)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `Commands.deferredProxy( () -> builder.build(new Path(new Path.TranslationTarget(target)))) .withName("BLineDriveToTranslation(" + target.getX() + ", " + target.getY() + ")")`.
- Key collaborators/calls: `Commands.deferredProxy()`, `builder.build()`, `Path()`, `Path.TranslationTarget()`, `withName()`, `target.getX()`, `target.getY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `builder` | `FollowPath.Builder` | `FollowPath.Builder` input consumed by the implementation shown below. |
| `target` | `Translation2d` | `Translation2d` input consumed by the implementation shown below. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 61–65)"

    ```java
    public static Command driveToTranslation(FollowPath.Builder builder, Translation2d target) {
        return Commands.deferredProxy(
                () -> builder.build(new Path(new Path.TranslationTarget(target))))
                .withName("BLineDriveToTranslation(" + target.getX() + ", " + target.getY() + ")");
    }
    ```

??? note "Author note from JavaDoc"

    Drives to a fixed translation without commanding any heading change.

### `public static Command driveToTranslation(FollowPath.Builder builder, Supplier&lt;Translation2d&gt; target)`

[Source lines 71–75](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L71)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `Commands.deferredProxy( () -> builder.build(new Path(new Path.TranslationTarget(target.get())))) .withName("BLineDriveToTranslation(dynamic)")`.
- Key collaborators/calls: `Commands.deferredProxy()`, `builder.build()`, `Path()`, `Path.TranslationTarget()`, `target.get()`, `withName()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `builder` | `FollowPath.Builder` | `FollowPath.Builder` input consumed by the implementation shown below. |
| `target` | `Supplier&lt;Translation2d&gt;` | Callback evaluated at use time rather than construction time. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 71–75)"

    ```java
    public static Command driveToTranslation(FollowPath.Builder builder, Supplier<Translation2d> target) {
        return Commands.deferredProxy(
                () -> builder.build(new Path(new Path.TranslationTarget(target.get()))))
                .withName("BLineDriveToTranslation(dynamic)");
    }
    ```

??? note "Author note from JavaDoc"

    Drives to a dynamically-supplied translation without commanding any heading change;
    the supplier is called at schedule time.

## Exposed fields and types

### `public final class BLineUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLineUtil.java#L19)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Static factory methods for BLine drive-to-pose commands.
    
    All methods return a `Commands.deferredProxy`-wrapped command so path construction
    is deferred until schedule time, making them safe to store and re-schedule without
    capturing a stale robot pose.
