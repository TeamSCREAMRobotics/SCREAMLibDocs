# DataConversions

`com.teamscreamrobotics.data.DataConversions`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java) · **10 callables** · **1 exposed fields/types**

## Public and protected callables

### `public static double[] pose2dToArray(Pose2d pose)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L18)*

Converts a `Pose2d` to a `[x, y, headingDegrees]` array.

**Parameter `pose`:** the pose to convert

### `public static double[] translation3dToArray(Translation3d translation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L28)*

Converts a `Translation3d` to a 7-element array `[x, y, z, 0, 0, 0, 0]`
(position only, quaternion zeroed).

**Parameter `translation`:** the translation to convert

### `public static double[] translation3dToArray(Translation3d translation, Rotation3d rot)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L39)*

Converts a `Translation3d` and `Rotation3d` to a 7-element pose array
`[x, y, z, qx, qy, qz, qw]`.

**Parameter `translation`:** the position
**Parameter `rot`:** the rotation (converted to quaternion)

### `public static Translation3d pose3dArrayToTranslation3d(double[] array)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L57)*

Extracts the first three elements of a pose array as a `Translation3d`.

**Parameter `array`:** array with at least 3 elements: `[x, y, z, ...]`

### `public static double[] translation3dArrayToNumArray(Translation3d[] translations)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L67)*

Packs an array of `Translation3d` objects into a flat `double[]` with 7 slots per
translation (x, y, z at indices 0–2; remaining 4 slots zeroed).

**Parameter `translations`:** the translations to pack

### `public static double[] translation2dArrayToNumArray(Translation2d[] translations)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L93)*

Packs an array of `Translation2d` objects into a flat `double[]` with 7 slots per
translation (x, y at indices 0–1; remaining 5 slots zeroed).

**Parameter `translations`:** the translations to pack

### `public static double[] translation2dArrayToNumArray(Translation2d[] translations, double z)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L114)*

Packs an array of `Translation2d` objects into a flat `double[]` with 7 slots per
translation, inserting a constant `z` value at index 2.

**Parameter `translations`:** the translations to pack
**Parameter `z`:** z value to insert at index 2 of each slot

### `public static double[] chassisSpeedsToArray(ChassisSpeeds speeds)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L134)*

Converts a `ChassisSpeeds` to a `[vx, vy, omega]` array.

**Parameter `speeds`:** the chassis speeds to convert

### `public static Translation2d projectTo2d(Translation3d translation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L145)*

Projects a `Translation3d` onto the XZ plane, returning `(x, z)` as a `Translation2d`.

**Parameter `translation`:** the 3D translation to project

### `public static Translation3d projectTo3d(Translation2d translation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L154)*

Lifts a `Translation2d` into 3D as `(x, 0, y)`.

**Parameter `translation`:** the 2D translation to lift

## Exposed fields and types

### `public class DataConversions`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L11)*

Utility methods for converting geometry and kinematics objects to primitive arrays and back.
