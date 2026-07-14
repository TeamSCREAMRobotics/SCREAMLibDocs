# RectangularPoseArea

`com.teamscreamrobotics.zones.RectangularPoseArea`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java) · **9 callables** · **1 exposed fields/types**

## Competition usage

**2025:** [`FieldConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/constants/FieldConstants.java#L16)

**2026:** [`FieldConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/com/teamscreamrobotics/gameutil/FieldConstants.java#L12), [`RobotState.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/RobotState.java#L7)

## Public and protected callables

### `public RectangularPoseArea(Translation2d bottomLeft, Translation2d topRight)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L20)*

Create a 2D rectangular area for pose calculations.

**Parameter `bottomLeft`:** bottom left corner of the rectangle.
**Parameter `topRight`:** top right corner of the rectangle.

### `public double getMinX()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L26)*

Returns the minimum X coordinate (left edge) in meters.

### `public double getMaxX()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L31)*

Returns the maximum X coordinate (right edge) in meters.

### `public double getMinY()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L36)*

Returns the minimum Y coordinate (bottom edge) in meters.

### `public double getMaxY()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L41)*

Returns the maximum Y coordinate (top edge) in meters.

### `public Translation2d getBottomLeftPoint()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L46)*

Returns the bottom-left corner of the rectangle.

### `public Translation2d getTopRightPoint()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L51)*

Returns the top-right corner of the rectangle.

### `public boolean contains(Pose2d pose)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L56)*

Returns `true` if the pose's translation is within the rectangle.

### `public boolean contains(Translation2d pose)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L61)*

Returns `true` if the translation is within the rectangle (inclusive bounds).

## Exposed fields and types

### `public class RectangularPoseArea`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L7)*

An axis-aligned rectangular 2D zone on the field used for pose containment checks.
