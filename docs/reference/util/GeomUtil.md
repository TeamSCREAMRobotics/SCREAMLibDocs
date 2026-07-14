# GeomUtil

`com.teamscreamrobotics.util.GeomUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java) · **15 callables** · **1 exposed fields/types**

## Competition usage

**2025:** [`AutoAlign2.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/autonomous/auto_commands/AutoAlign2.java#L26), [`AutoAlign.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/commands/AutoAlign.java#L26), [`DriveToPose.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/commands/DriveToPose.java#L22), [`VisionManager.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/vision/VisionManager.java#L33)

**2026:** [`Shooter.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/Shooter.java#L10), [`VisionManager.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/vision/VisionManager.java#L4)

## Public and protected callables

### `public static Transform2d translationToTransform(Translation2d translation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L28)*

Creates a pure translating transform

**Parameter `translation`:** The translation to create the transform with
**Returns:** The resulting transform

### `public static Transform2d translationToTransform(double x, double y)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L39)*

Creates a pure translating transform

**Parameter `x`:** The x componenet of the translation
**Parameter `y`:** The y componenet of the translation
**Returns:** The resulting transform

### `public static Transform2d rotationToTransform(Rotation2d rotation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L49)*

Creates a pure rotating transform

**Parameter `rotation`:** The rotation to create the transform with
**Returns:** The resulting transform

### `public static Transform2d poseToTransform(Pose2d pose)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L59)*

Converts a Pose2d to a Transform2d to be used in a kinematic chain

**Parameter `pose`:** The pose that will represent the transform
**Returns:** The resulting transform

### `public static Pose2d transformToPose(Transform2d transform)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L70)*

Converts a Transform2d to a Pose2d to be used as a position or as the start of a kinematic
chain

**Parameter `transform`:** The transform that will represent the pose
**Returns:** The resulting pose

### `public static Pose2d translationToPose(Translation2d translation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L80)*

Creates a pure translated pose

**Parameter `translation`:** The translation to create the pose with
**Returns:** The resulting pose

### `public static Pose2d rotationToPose(Rotation2d rotation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L90)*

Creates a pure rotated pose

**Parameter `rotation`:** The rotation to create the pose with
**Returns:** The resulting pose

### `public static Twist2d multiplyTwist(Twist2d twist, double factor)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L101)*

Multiplies a twist by a scaling factor

**Parameter `twist`:** The twist to multiply
**Parameter `factor`:** The scaling factor for the twist components
**Returns:** The new twist

### `public static Transform3d pose3dToTransform3d(Pose3d pose)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L111)*

Converts a Pose3d to a Transform3d to be used in a kinematic chain

**Parameter `pose`:** The pose that will represent the transform
**Returns:** The resulting transform

### `public static Pose3d transform3dToPose3d(Transform3d transform)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L122)*

Converts a Transform3d to a Pose3d to be used as a position or as the start of a kinematic
chain

**Parameter `transform`:** The transform that will represent the pose
**Returns:** The resulting pose

### `public static Translation2d translation3dTo2dXY(Translation3d translation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L132)*

Converts a Translation3d to a Translation2d by extracting two dimensions (X and Y). chain

**Parameter `translation`:** The original translation
**Returns:** The resulting translation

### `public static Translation2d translation3dTo2dXZ(Translation3d translation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L142)*

Converts a Translation3d to a Translation2d by extracting two dimensions (X and Z). chain

**Parameter `translation`:** The original translation
**Returns:** The resulting translation

### `public static Pose3d translationToPose3d(Translation2d translation, double z)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L152)*

Creates a `Pose3d` from a 2D translation and a Z height, with zero rotation.

**Parameter `translation`:** the XY position
**Parameter `z`:** the height in meters

### `public static Translation2d normalize(Translation2d translation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L162)*

Returns a unit vector in the same direction as `translation`.

**Parameter `translation`:** the vector to normalize

### `public static Translation2d findClosest(Translation2d origin, Translation2d... others)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L172)*

Returns the point in `others` nearest to `origin` by Euclidean distance.

**Parameter `origin`:** the reference point
**Parameter `others`:** the candidate points to search

## Exposed fields and types

### `public class GeomUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L21)*

Geometry utilities for working with translations, rotations, transforms, and poses.
