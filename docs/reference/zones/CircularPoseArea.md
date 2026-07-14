# CircularPoseArea

`com.teamscreamrobotics.zones.CircularPoseArea`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java) · **5 callables** · **1 exposed fields/types**

## Public and protected callables

### `public CircularPoseArea(Translation2d center, double diameter)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L18)*

Creates a circular zone.

**Parameter `center`:** center of the circle in field coordinates (meters)
**Parameter `diameter`:** diameter of the circle in meters

### `public Translation2d getCenter()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L24)*

Returns the center of the circle in field coordinates.

### `public double getDiameter()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L29)*

Returns the diameter of the circle in meters.

### `public boolean contains(Pose2d pose)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L34)*

Returns `true` if the pose's translation is inside the circle.

### `public boolean contains(Translation2d translation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L39)*

Returns `true` if the translation is inside the circle.

## Exposed fields and types

### `public class CircularPoseArea`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L7)*

A circular 2D zone on the field used for pose containment checks.
