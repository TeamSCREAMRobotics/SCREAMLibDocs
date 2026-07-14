# Trajectory

`com.teamscreamrobotics.physics.Trajectory`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java) · **19 callables** · **14 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public double getArea()`

[Source lines 57–59](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L57)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `Math.PI * Math.pow(diameter / 2, 2)`.
- Key collaborators/calls: `Math.pow()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 57–59)"

    ```java
    public double getArea() {
        return Math.PI * Math.pow(diameter / 2, 2);
    }
    ```

### `public TrajectoryConfig setShotVelocity(double velocity)`

[Source lines 81–84](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L81)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `shotVelocity`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `velocity` | `double` | Velocity/speed in the units required by this API and configuration. |

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 81–84)"

    ```java
    public TrajectoryConfig setShotVelocity(double velocity) {
        this.shotVelocity = velocity;
        return this;
    }
    ```

### `public TrajectoryConfig setShotAngle(double angle)`

[Source lines 87–90](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L87)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `shotAngle`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `angle` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 87–90)"

    ```java
    public TrajectoryConfig setShotAngle(double angle) {
        this.shotAngle = angle;
        return this;
    }
    ```

### `public TrajectoryConfig setRobotVelocity(double velocity)`

[Source lines 93–96](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L93)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `robotVelocity`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `velocity` | `double` | Velocity/speed in the units required by this API and configuration. |

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 93–96)"

    ```java
    public TrajectoryConfig setRobotVelocity(double velocity) {
        this.robotVelocity = velocity;
        return this;
    }
    ```

### `public TrajectoryConfig setRobotAngle(double angle)`

[Source lines 99–102](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L99)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `robotAngle`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `angle` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 99–102)"

    ```java
    public TrajectoryConfig setRobotAngle(double angle) {
        this.robotAngle = angle;
        return this;
    }
    ```

### `public TrajectoryConfig setTargetDistance(double distance)`

[Source lines 105–108](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L105)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `targetDistance`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `distance` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 105–108)"

    ```java
    public TrajectoryConfig setTargetDistance(double distance) {
        this.targetDistance = distance;
        return this;
    }
    ```

### `public TrajectoryConfig setTargetHeight(double height)`

[Source lines 111–114](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L111)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `targetHeight`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `height` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 111–114)"

    ```java
    public TrajectoryConfig setTargetHeight(double height) {
        this.targetHeight = height;
        return this;
    }
    ```

### `public TrajectoryConfig setInitialHeight(double height)`

[Source lines 117–120](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L117)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `initialHeight`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `height` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 117–120)"

    ```java
    public TrajectoryConfig setInitialHeight(double height) {
        this.initialHeight = height;
        return this;
    }
    ```

### `public TrajectoryConfig setGamePiece(GamePiece piece)`

[Source lines 123–126](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L123)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `gamePiece`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `piece` | `GamePiece` | `GamePiece` input consumed by the implementation shown below. |

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 123–126)"

    ```java
    public TrajectoryConfig setGamePiece(GamePiece piece) {
        this.gamePiece = piece;
        return this;
    }
    ```

### `public TrajectoryConfig setCustomGamePiece(double massKg, double diameterMeters, double dragCoefficient)`

[Source lines 134–140](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L134)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It changes object/subclass state through `customDiameter`, `customDragCoeff`, `customMass`, `gamePiece`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `massKg` | `double` | `double` input consumed by the implementation shown below. |
| `diameterMeters` | `double` | Linear value in meters. |
| `dragCoefficient` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 134–140)"

    ```java
    public TrajectoryConfig setCustomGamePiece(double massKg, double diameterMeters, double dragCoefficient) {
        this.customMass = massKg;
        this.customDiameter = diameterMeters;
        this.customDragCoeff = dragCoefficient;
        this.gamePiece = GamePiece.CUSTOM;
        return this;
    }
    ```

### `public TrajectoryConfig setCustomGamePieceImperial(double massLbs, double diameterInches, double dragCoefficient)`

[Source lines 148–154](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L148)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It changes object/subclass state through `customDiameter`, `customDragCoeff`, `customMass`, `gamePiece`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `massLbs` | `double` | `double` input consumed by the implementation shown below. |
| `diameterInches` | `double` | Linear value in meters. |
| `dragCoefficient` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 148–154)"

    ```java
    public TrajectoryConfig setCustomGamePieceImperial(double massLbs, double diameterInches, double dragCoefficient) {
        this.customMass = massLbs * 0.453592; // lbs to kg
        this.customDiameter = diameterInches * 0.0254; // inches to meters
        this.customDragCoeff = dragCoefficient;
        this.gamePiece = GamePiece.CUSTOM;
        return this;
    }
    ```

### `public TrajectoryPoint(double time, double x, double y, double vx, double vy)`

[Source lines 198–204](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L198)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It changes object/subclass state through `time`, `vx`, `vy`, `x`, `y`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `time` | `double` | `double` input consumed by the implementation shown below. |
| `x` | `double` | `double` input consumed by the implementation shown below. |
| `y` | `double` | `double` input consumed by the implementation shown below. |
| `vx` | `double` | `double` input consumed by the implementation shown below. |
| `vy` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `TrajectoryPoint` instance.

??? example "Implementation (source lines 198–204)"

    ```java
    public TrajectoryPoint(double time, double x, double y, double vx, double vy) {
        this.time = time;
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
    }
    ```

### `public String toString()`

[Source lines 207–210](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L207)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `String.format("t=%.3f, x=%.3f, y=%.3f, vx=%.3f, vy=%.3f", time, x, y, vx, vy)`.
- Key collaborators/calls: `String.format()`.

**Inputs:** None.

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 207–210)"

    ```java
    public String toString() {
        return String.format("t=%.3f, x=%.3f, y=%.3f, vx=%.3f, vy=%.3f", 
                            time, x, y, vx, vy);
    }
    ```

### `public static TrajectoryConfig configure()`

[Source lines 216–218](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L216)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `config`.

**Inputs:** None.

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 216–218)"

    ```java
    public static TrajectoryConfig configure() {
        return config;
    }
    ```

### `public static TrajectoryConfig getConfig()`

[Source lines 223–225](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L223)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `config`.

**Inputs:** None.

**Result:** Returns `TrajectoryConfig`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 223–225)"

    ```java
    public static TrajectoryConfig getConfig() {
        return config;
    }
    ```

### `public static List&lt;TrajectoryPoint&gt; getDesiredTrajectory()`

[Source lines 231–243](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L231)

**Detailed behavior**

- The implementation executes 11 non-blank source lines.
- Return path: `calculateTrajectory( config.shotVelocity, config.shotAngle, config.robotVelocity, config.robotAngle, config.targetDistance, config.initialHeight, config.getMass(), config.getArea(…`.
- Key collaborators/calls: `calculateTrajectory()`, `config.getMass()`, `config.getArea()`, `config.getDragCoefficient()`.

**Inputs:** None.

**Result:** Returns `List&lt;TrajectoryPoint&gt;`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 231–243)"

    ```java
    public static List<TrajectoryPoint> getDesiredTrajectory() {
        return calculateTrajectory(
            config.shotVelocity,
            config.shotAngle,
            config.robotVelocity,
            config.robotAngle,
            config.targetDistance,
            config.initialHeight,
            config.getMass(),
            config.getArea(),
            config.getDragCoefficient()
        );
    }
    ```

### `public static double getOptimalAngle()`

[Source lines 249–261](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L249)

**Detailed behavior**

- The implementation executes 11 non-blank source lines.
- Return path: `findOptimalAngle( config.shotVelocity, config.robotVelocity, config.robotAngle, config.targetDistance, config.targetHeight, config.initialHeight, config.getMass(), config.getArea(…`.
- Key collaborators/calls: `findOptimalAngle()`, `config.getMass()`, `config.getArea()`, `config.getDragCoefficient()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 249–261)"

    ```java
    public static double getOptimalAngle() {
        return findOptimalAngle(
            config.shotVelocity,
            config.robotVelocity,
            config.robotAngle,
            config.targetDistance,
            config.targetHeight,
            config.initialHeight,
            config.getMass(),
            config.getArea(),
            config.getDragCoefficient()
        );
    }
    ```

### `public static double getRequiredVelocity()`

[Source lines 267–279](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L267)

**Detailed behavior**

- The implementation executes 11 non-blank source lines.
- Return path: `calculateRequiredVelocity( config.shotAngle, config.robotVelocity, config.robotAngle, config.targetDistance, config.targetHeight, config.initialHeight, config.getMass(), config.ge…`.
- Key collaborators/calls: `calculateRequiredVelocity()`, `config.getMass()`, `config.getArea()`, `config.getDragCoefficient()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 267–279)"

    ```java
    public static double getRequiredVelocity() {
        return calculateRequiredVelocity(
            config.shotAngle,
            config.robotVelocity,
            config.robotAngle,
            config.targetDistance,
            config.targetHeight,
            config.initialHeight,
            config.getMass(),
            config.getArea(),
            config.getDragCoefficient()
        );
    }
    ```

### `public static double getTimeOfFlight()`

[Source lines 285–300](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L285)

**Detailed behavior**

- The implementation executes 11 non-blank source lines.
- It has 1 conditional path: `dist < minDist`.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `closestTime`.
- Key collaborators/calls: `getDesiredTrajectory()`, `Math.abs()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 285–300)"

    ```java
    public static double getTimeOfFlight() {
        List<TrajectoryPoint> traj = getDesiredTrajectory();
    
        double closestTime = 0;
        double minDist = Double.MAX_VALUE;
    
        for (TrajectoryPoint p : traj) {
            double dist = Math.abs(p.x - config.targetDistance);
            if (dist < minDist) {
                minDist = dist;
                closestTime = p.time;
            }
        }
    
        return closestTime;
    }
    ```

## Exposed fields and types

### `public class Trajectory`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L22)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static final double HUB_HEIGHT = Units.inchesToMeters(72.0)`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L30)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 2 times, so changing it can affect every control path that reads `HUB_HEIGHT`.

### `public static final double HUB_DISTANCE_FROM_ALLIANCE_WALL = Units.inchesToMeters(158.6)`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L31)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 1 time, so changing it can affect every control path that reads `HUB_DISTANCE_FROM_ALLIANCE_WALL`.

### `public enum GamePiece`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L39)*

This exposed `enum` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public final double mass`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L44)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 16 times, so changing it can affect every control path that reads `mass`.

### `public final double diameter`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L46)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 7 times, so changing it can affect every control path that reads `diameter`.

### `public final double dragCoefficient`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L48)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 11 times, so changing it can affect every control path that reads `dragCoefficient`.

### `public static class TrajectoryConfig`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L65)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static class TrajectoryPoint`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L177)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public final double time`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L179)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 11 times, so changing it can affect every control path that reads `time`.

### `public final double x`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L181)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 20 times, so changing it can affect every control path that reads `x`.

### `public final double y`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L183)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 20 times, so changing it can affect every control path that reads `y`.

### `public final double vx`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L185)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 21 times, so changing it can affect every control path that reads `vx`.

### `public final double vy`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L187)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 21 times, so changing it can affect every control path that reads `vy`.
