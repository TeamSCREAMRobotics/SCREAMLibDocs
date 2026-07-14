# PolygonalPoseArea

`com.teamscreamrobotics.zones.PolygonalPoseArea`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java) · **4 callables** · **1 exposed fields/types**

## Public and protected callables

### `public PolygonalPoseArea(List&lt;Translation2d&gt; vertices)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java#L17)*

Creates a polygonal zone from an ordered list of vertices.

**Parameter `vertices`:** polygon corners in field coordinates (meters), ordered consistently (CW or CCW)

### `public boolean contains(Pose2d pose)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java#L22)*

Returns `true` if the pose's translation is inside the polygon.

### `public boolean contains(Translation2d point)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java#L27)*

Returns `true` if the point is inside the polygon (ray-casting algorithm).

### `public Translation2d getCenter()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java#L44)*

Returns the geometric centroid of the polygon in field coordinates.

## Exposed fields and types

### `public class PolygonalPoseArea`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java#L8)*

An arbitrary convex or concave 2D polygon zone on the field used for pose containment checks.
