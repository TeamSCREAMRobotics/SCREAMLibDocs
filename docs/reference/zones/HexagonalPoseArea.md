# HexagonalPoseArea

`com.teamscreamrobotics.zones.HexagonalPoseArea`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java) · **4 callables** · **1 exposed fields/types**

## Competition usage

**2025:** [`FieldConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/constants/FieldConstants.java#L15)

## Public and protected callables

### `public HexagonalPoseArea(Translation2d origin, Length radius)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java#L21)*

Creates an axis-aligned regular hexagon.

**Parameter `origin`:** center of the hexagon in field coordinates
**Parameter `radius`:** circumradius (center to vertex) of the hexagon

### `public HexagonalPoseArea(Translation2d origin, Length radius, Rotation2d rotation)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java#L32)*

Creates a regular hexagon with an angular offset applied to all vertices.

**Parameter `origin`:** center of the hexagon in field coordinates
**Parameter `radius`:** circumradius (center to vertex)
**Parameter `rotation`:** rotation to apply to the hexagon

### `public Translation2d[] getVertices()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java#L58)*

Returns the six vertex positions of the hexagon in field coordinates.

### `public OptionalInt contains(Translation2d position)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java#L70)*

Determines if a given position is within the hexagonal area.

**Parameter `position`:** The position to check.
**Returns:** An OptionalInt containing the index of the triangle within the hexagon
that contains the position, or an empty OptionalInt if the position is
outside the hexagon.

## Exposed fields and types

### `public class HexagonalPoseArea`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java#L10)*

A regular hexagonal 2D zone on the field used for pose containment checks.
