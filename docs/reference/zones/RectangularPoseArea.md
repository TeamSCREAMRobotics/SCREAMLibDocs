# RectangularPoseArea

`com.teamscreamrobotics.zones.RectangularPoseArea`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java) · **9 callables** · **1 exposed fields/types** · **3 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2025: Use `RectangularPoseArea` in `FieldConstants.java`

[`src/main/java/frc2025/constants/FieldConstants.java` lines 18–33](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/constants/FieldConstants.java#L18-L33)

```java
public class FieldConstants {

  public static final Translation2d FIELD_DIMENSIONS = new Translation2d(17.548225, 8.0518);

  public static final RectangularPoseArea FIELD_AREA =
      new RectangularPoseArea(Translation2d.kZero, FIELD_DIMENSIONS);

  public enum AlgaeLevel {
    L1,
    L2;
  }

  public enum ReefLocation {
    A(0),
    B(1),
    C(2),
```

### 2026: Use `RectangularPoseArea` in `FieldConstants.java`

[`src/main/java/com/teamscreamrobotics/gameutil/FieldConstants.java` lines 49–64](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/com/teamscreamrobotics/gameutil/FieldConstants.java#L49-L64)

```java
new Translation2d(fieldLength / 2, (fieldWidth * 3) / 4);

public static final Translation2d fieldDimensions = new Translation2d(fieldLength, fieldWidth);

public static final RectangularPoseArea fieldArea =
    new RectangularPoseArea(new Translation2d(0, 0), fieldDimensions);

public static final Translation2d BLUEALLIANCE_NEAR_RIGHT_CORNER = new Translation2d(0, 0);

public static final Translation2d BLUEALLIANCE_FAR_RIGHT_CORNER =
    new Translation2d(Units.inchesToMeters(156.406250), 0);

public static final Translation2d BLUEALLIANCE_NEAR_LEFT_CORNER =
    new Translation2d(0, Units.inchesToMeters(317.437500 + 0.25));

public static final Translation2d BLUEALLIANCE_FAR_LEFT_CORNER =
```

### 2026: Use `RectangularPoseArea` in `RobotState.java`

[`src/main/java/frc2026/tars/RobotState.java` lines 79–94](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/RobotState.java#L79-L94)

```java
this.suppliers = suppliers;
}

void resolve() {

  resolved = new RectangularPoseArea[suppliers.length];

  for (int i = 0; i < suppliers.length; i++) {
    resolved[i] = suppliers[i].get();
  }
}

boolean contains(Pose2d pose) {

  if (resolved == null) return false;
```

## Public and protected callables

### `public RectangularPoseArea(Translation2d bottomLeft, Translation2d topRight)`

[Source lines 20–23](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L20)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `bottomLeft`, `topRight`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `bottomLeft` | `Translation2d` | bottom left corner of the rectangle. **Parameter `topRight`:** top right corner of the rectangle. |
| `topRight` | `Translation2d` | top right corner of the rectangle. |

**Result:** Constructs and initializes a `RectangularPoseArea` instance.

??? example "Implementation (source lines 20–23)"

    ```java
    public RectangularPoseArea(Translation2d bottomLeft, Translation2d topRight) {
      this.bottomLeft = bottomLeft;
      this.topRight = topRight;
    }
    ```

??? note "Author note from JavaDoc"

    Create a 2D rectangular area for pose calculations.
    
    **Parameter `bottomLeft`:** bottom left corner of the rectangle.
    **Parameter `topRight`:** top right corner of the rectangle.

### `public double getMinX()`

[Source lines 26–28](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L26)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `bottomLeft.getX()`.
- Key collaborators/calls: `bottomLeft.getX()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 26–28)"

    ```java
    public double getMinX() {
      return bottomLeft.getX();
    }
    ```

??? note "Author note from JavaDoc"

    Returns the minimum X coordinate (left edge) in meters.

### `public double getMaxX()`

[Source lines 31–33](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L31)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `topRight.getX()`.
- Key collaborators/calls: `topRight.getX()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 31–33)"

    ```java
    public double getMaxX() {
      return topRight.getX();
    }
    ```

??? note "Author note from JavaDoc"

    Returns the maximum X coordinate (right edge) in meters.

### `public double getMinY()`

[Source lines 36–38](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L36)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `bottomLeft.getY()`.
- Key collaborators/calls: `bottomLeft.getY()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 36–38)"

    ```java
    public double getMinY() {
      return bottomLeft.getY();
    }
    ```

??? note "Author note from JavaDoc"

    Returns the minimum Y coordinate (bottom edge) in meters.

### `public double getMaxY()`

[Source lines 41–43](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L41)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `topRight.getY()`.
- Key collaborators/calls: `topRight.getY()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 41–43)"

    ```java
    public double getMaxY() {
      return topRight.getY();
    }
    ```

??? note "Author note from JavaDoc"

    Returns the maximum Y coordinate (top edge) in meters.

### `public Translation2d getBottomLeftPoint()`

[Source lines 46–48](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L46)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `bottomLeft`.

**Inputs:** None.

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 46–48)"

    ```java
    public Translation2d getBottomLeftPoint() {
      return bottomLeft;
    }
    ```

??? note "Author note from JavaDoc"

    Returns the bottom-left corner of the rectangle.

### `public Translation2d getTopRightPoint()`

[Source lines 51–53](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L51)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `topRight`.

**Inputs:** None.

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 51–53)"

    ```java
    public Translation2d getTopRightPoint() {
      return topRight;
    }
    ```

??? note "Author note from JavaDoc"

    Returns the top-right corner of the rectangle.

### `public boolean contains(Pose2d pose)`

[Source lines 56–58](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L56)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `contains(pose.getTranslation())`.
- Key collaborators/calls: `pose.getTranslation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pose` | `Pose2d` | `Pose2d` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 56–58)"

    ```java
    public boolean contains(Pose2d pose) {
      return contains(pose.getTranslation());
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if the pose's translation is within the rectangle.

### `public boolean contains(Translation2d pose)`

[Source lines 61–66](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L61)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `pose.getX() >= bottomLeft.getX() && pose.getX() <= topRight.getX() && pose.getY() >= bottomLeft.getY() && pose.getY() <= topRight.getY()`.
- Key collaborators/calls: `pose.getX()`, `bottomLeft.getX()`, `topRight.getX()`, `pose.getY()`, `bottomLeft.getY()`, `topRight.getY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pose` | `Translation2d` | `Translation2d` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 61–66)"

    ```java
    public boolean contains(Translation2d pose) {
      return pose.getX() >= bottomLeft.getX()
          && pose.getX() <= topRight.getX()
          && pose.getY() >= bottomLeft.getY()
          && pose.getY() <= topRight.getY();
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if the translation is within the rectangle (inclusive bounds).

## Exposed fields and types

### `public class RectangularPoseArea`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/RectangularPoseArea.java#L7)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    An axis-aligned rectangular 2D zone on the field used for pose containment checks.
