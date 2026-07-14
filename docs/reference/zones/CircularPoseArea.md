# CircularPoseArea

`com.teamscreamrobotics.zones.CircularPoseArea`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java) · **5 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public CircularPoseArea(Translation2d center, double diameter)`

[Source lines 18–21](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L18)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `center`, `diameter`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `center` | `Translation2d` | `Translation2d` input consumed by the implementation shown below. |
| `diameter` | `double` | Linear value in meters. |

**Result:** Constructs and initializes a `CircularPoseArea` instance.

??? example "Implementation (source lines 18–21)"

    ```java
    public CircularPoseArea(Translation2d center, double diameter) {
      this.center = center;
      this.diameter = diameter;
    }
    ```

### `public Translation2d getCenter()`

[Source lines 24–26](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L24)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `center`.

**Inputs:** None.

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 24–26)"

    ```java
    public Translation2d getCenter() {
      return center;
    }
    ```

### `public double getDiameter()`

[Source lines 29–31](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L29)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `diameter`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 29–31)"

    ```java
    public double getDiameter() {
      return diameter;
    }
    ```

### `public boolean contains(Pose2d pose)`

[Source lines 34–36](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L34)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `contains(pose.getTranslation())`.
- Key collaborators/calls: `pose.getTranslation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pose` | `Pose2d` | `Pose2d` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 34–36)"

    ```java
    public boolean contains(Pose2d pose) {
      return contains(pose.getTranslation());
    }
    ```

### `public boolean contains(Translation2d translation)`

[Source lines 39–41](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L39)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `center.getDistance(translation) <= (diameter / 2.0)`.
- Key collaborators/calls: `center.getDistance()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | `Translation2d` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 39–41)"

    ```java
    public boolean contains(Translation2d translation) {
      return center.getDistance(translation) <= (diameter / 2.0);
    }
    ```

## Exposed fields and types

### `public class CircularPoseArea`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/CircularPoseArea.java#L7)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
