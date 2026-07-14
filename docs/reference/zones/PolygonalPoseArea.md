# PolygonalPoseArea

`com.teamscreamrobotics.zones.PolygonalPoseArea`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java) · **4 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public PolygonalPoseArea(List&lt;Translation2d&gt; vertices)`

[Source lines 17–19](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java#L17)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `vertices`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `vertices` | `List&lt;Translation2d&gt;` | polygon corners in field coordinates (meters), ordered consistently (CW or CCW) |

**Result:** Constructs and initializes a `PolygonalPoseArea` instance.

??? example "Implementation (source lines 17–19)"

    ```java
    public PolygonalPoseArea(List<Translation2d> vertices) {
      this.vertices = vertices;
    }
    ```

??? note "Author note from JavaDoc"

    Creates a polygonal zone from an ordered list of vertices.
    
    **Parameter `vertices`:** polygon corners in field coordinates (meters), ordered consistently (CW or CCW)

### `public boolean contains(Pose2d pose)`

[Source lines 22–24](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java#L22)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `contains(pose.getTranslation())`.
- Key collaborators/calls: `pose.getTranslation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pose` | `Pose2d` | `Pose2d` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 22–24)"

    ```java
    public boolean contains(Pose2d pose) {
      return contains(pose.getTranslation());
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if the pose's translation is inside the polygon.

### `public boolean contains(Translation2d point)`

[Source lines 27–41](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java#L27)

**Detailed behavior**

- The implementation executes 13 non-blank source lines.
- It has 1 conditional path: `(vertices.get(i`.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `result`.
- Key collaborators/calls: `vertices.size()`, `vertices.get()`, `getY()`, `point.getY()`, `point.getX()`, `getX()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `point` | `Translation2d` | `Translation2d` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 27–41)"

    ```java
    public boolean contains(Translation2d point) {
      int n = vertices.size();
      boolean result = false;
      for (int i = 0, j = n - 1; i < n; j = i++) {
        if ((vertices.get(i).getY() > point.getY()) != (vertices.get(j).getY() > point.getY())
            && (point.getX()
                < (vertices.get(j).getX() - vertices.get(i).getX())
                        * (point.getY() - vertices.get(i).getY())
                        / (vertices.get(j).getY() - vertices.get(i).getY())
                    + vertices.get(i).getX())) {
          result = !result;
        }
      }
      return result;
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if the point is inside the polygon (ray-casting algorithm).

### `public Translation2d getCenter()`

[Source lines 44–71](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java#L44)

**Detailed behavior**

- The implementation executes 23 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `new Translation2d(centerX, centerY)`.
- Key collaborators/calls: `vertices.size()`, `vertices.get()`, `getX()`, `getY()`, `Translation2d()`.

**Inputs:** None.

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 44–71)"

    ```java
    public Translation2d getCenter() {
      double centerX = 0.0;
      double centerY = 0.0;
      double signedArea = 0.0;
      double currentX;
      double currentY;
      double nextX;
      double nextY;
      double a;
    
      int n = vertices.size();
      for (int i = 0; i < n; i++) {
        currentX = vertices.get(i).getX();
        currentY = vertices.get(i).getY();
        nextX = vertices.get((i + 1) % n).getX();
        nextY = vertices.get((i + 1) % n).getY();
        a = currentX * nextY - nextX * currentY;
        signedArea += a;
        centerX += (currentX + nextX) * a;
        centerY += (currentY + nextY) * a;
      }
    
      signedArea *= 0.5;
      centerX /= (6.0 * signedArea);
      centerY /= (6.0 * signedArea);
    
      return new Translation2d(centerX, centerY);
    }
    ```

??? note "Author note from JavaDoc"

    Returns the geometric centroid of the polygon in field coordinates.

## Exposed fields and types

### `public class PolygonalPoseArea`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/PolygonalPoseArea.java#L8)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    An arbitrary convex or concave 2D polygon zone on the field used for pose containment checks.
