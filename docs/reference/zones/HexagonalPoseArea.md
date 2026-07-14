# HexagonalPoseArea

`com.teamscreamrobotics.zones.HexagonalPoseArea`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java) · **4 callables** · **1 exposed fields/types** · **1 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2025: Use `HexagonalPoseArea` in `FieldConstants.java`

[`src/main/java/frc2025/constants/FieldConstants.java` lines 86–101](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/constants/FieldConstants.java#L86-L101)

```java
public static final Translation2d BLUE_REEF_CENTER =
    new Translation2d(Units.inchesToMeters(176.746), FIELD_DIMENSIONS.getY() / 2.0);
public static final Translation2d RED_REEF_CENTER = FIELD_DIMENSIONS.minus(BLUE_REEF_CENTER);

public static final HexagonalPoseArea BLUE_REEF =
    new HexagonalPoseArea(BLUE_REEF_CENTER, Length.fromMeters(10), Rotation2d.fromDegrees(-30));
public static final HexagonalPoseArea RED_REEF =
    new HexagonalPoseArea(RED_REEF_CENTER, Length.fromMeters(10), Rotation2d.fromDegrees(-30));

public static final Map<Integer, Pair<Pose2d, Pose2d>> BLUE_PRE_REEF_LOCATIONS = new HashMap<>();
public static final Map<Integer, Pair<Pose2d, Pose2d>> RED_PRE_REEF_LOCATIONS = new HashMap<>();

public static final Map<Integer, Pair<Pose2d, Pose2d>> BLUE_REEF_LOCATIONS = new HashMap<>();
public static final Map<Integer, Pair<Pose2d, Pose2d>> RED_REEF_LOCATIONS = new HashMap<>();

public static final Map<Integer, Pair<Pose2d, Pose2d>> BLUE_REEF_LOCATIONS_FLIPPED =
```

## Public and protected callables

### `public HexagonalPoseArea(Translation2d origin, Length radius)`

[Source lines 21–23](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java#L21)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It delegates initialization to another constructor in the same type with `origin, radius, Rotation2d.kZero`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `origin` | `Translation2d` | center of the hexagon in field coordinates **Parameter `radius`:** circumradius (center to vertex) of the hexagon |
| `radius` | `Length` | circumradius (center to vertex) of the hexagon |

**Result:** Constructs and initializes a `HexagonalPoseArea` instance.

??? example "Implementation (source lines 21–23)"

    ```java
    public HexagonalPoseArea(Translation2d origin, Length radius) {
        this(origin, radius, Rotation2d.kZero);
    }
    ```

??? note "Author note from JavaDoc"

    Creates an axis-aligned regular hexagon.
    
    **Parameter `origin`:** center of the hexagon in field coordinates
    **Parameter `radius`:** circumradius (center to vertex) of the hexagon

### `public HexagonalPoseArea(Translation2d origin, Length radius, Rotation2d rotation)`

[Source lines 32–36](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java#L32)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `origin`, `radius`.
- Key collaborators/calls: `calculateVertices()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `origin` | `Translation2d` | center of the hexagon in field coordinates **Parameter `radius`:** circumradius (center to vertex) **Parameter `rotation`:** rotation to apply to the hexagon |
| `radius` | `Length` | circumradius (center to vertex) **Parameter `rotation`:** rotation to apply to the hexagon |
| `rotation` | `Rotation2d` | rotation to apply to the hexagon |

**Result:** Constructs and initializes a `HexagonalPoseArea` instance.

??? example "Implementation (source lines 32–36)"

    ```java
    public HexagonalPoseArea(Translation2d origin, Length radius, Rotation2d rotation) {
        this.origin = origin;
        this.radius = radius;
        calculateVertices(rotation);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a regular hexagon with an angular offset applied to all vertices.
    
    **Parameter `origin`:** center of the hexagon in field coordinates
    **Parameter `radius`:** circumradius (center to vertex)
    **Parameter `rotation`:** rotation to apply to the hexagon

### `public Translation2d[] getVertices()`

[Source lines 58–60](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java#L58)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `vertices`.

**Inputs:** None.

**Result:** Returns `Translation2d[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 58–60)"

    ```java
    public Translation2d[] getVertices() {
        return vertices;
    }
    ```

??? note "Author note from JavaDoc"

    Returns the six vertex positions of the hexagon in field coordinates.

### `public OptionalInt contains(Translation2d position)`

[Source lines 70–85](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java#L70)

**Detailed behavior**

- The implementation executes 12 non-blank source lines.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- It has 2 conditional paths: `origin.getDistance(position`; `isPointInTriangle(position, origin, vertices[i], vertices[(i + 1`.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return paths: `OptionalInt.empty()`; `OptionalInt.of(i)`; `OptionalInt.empty()`.
- Key collaborators/calls: `origin.getDistance()`, `radius.getMeters()`, `OptionalInt.empty()`, `isPointInTriangle()`, `OptionalInt.of()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `position` | `Translation2d` | The position to check. **Returns:** An OptionalInt containing the index of the triangle within the hexagon that contains the position, or an empty OptionalInt if the position is outside the hexagon. |

**Result:** Returns `OptionalInt`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 70–85)"

    ```java
    public OptionalInt contains(Translation2d position) {
        if (origin.getDistance(position) > radius.getMeters()) {
            return OptionalInt.empty();
        }
    
        for (int i = 0; i < 6; i++) {
            if (isPointInTriangle(position, 
                                origin, 
                                vertices[i], 
                                vertices[(i + 1) % 6])) {
                return OptionalInt.of(i);
            }
        }
    
        return OptionalInt.empty();
    }
    ```

??? note "Author note from JavaDoc"

    Determines if a given position is within the hexagonal area.
    
    **Parameter `position`:** The position to check.
    **Returns:** An OptionalInt containing the index of the triangle within the hexagon
    that contains the position, or an empty OptionalInt if the position is
    outside the hexagon.

## Exposed fields and types

### `public class HexagonalPoseArea`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/zones/HexagonalPoseArea.java#L10)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    A regular hexagonal 2D zone on the field used for pose containment checks.
