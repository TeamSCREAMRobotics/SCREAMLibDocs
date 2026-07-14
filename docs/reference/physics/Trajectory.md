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

??? note "Author note from JavaDoc"

    Returns the cross-sectional area of the game piece in m² (used for drag calculation).

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

??? note "Author note from JavaDoc"

    Sets the muzzle velocity of the shot in m/s.

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

??? note "Author note from JavaDoc"

    Sets the launch angle in degrees (above horizontal).

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

??? note "Author note from JavaDoc"

    Sets the robot's forward velocity in m/s (added to shot velocity for moving shots).

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

??? note "Author note from JavaDoc"

    Sets the robot's travel direction in degrees relative to the shot direction.

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

??? note "Author note from JavaDoc"

    Sets the horizontal distance to the target in meters.

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

??? note "Author note from JavaDoc"

    Sets the height of the target opening in meters.

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

??? note "Author note from JavaDoc"

    Sets the launch height above the ground in meters.

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

??? note "Author note from JavaDoc"

    Sets the game piece type to use for physics calculations.

### `public TrajectoryConfig setCustomGamePiece(double massKg, double diameterMeters, double dragCoefficient)`

[Source lines 134–140](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L134)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It changes object/subclass state through `customDiameter`, `customDragCoeff`, `customMass`, `gamePiece`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `massKg` | `double` | Mass in kilograms **Parameter `diameterMeters`:** Diameter in meters **Parameter `dragCoefficient`:** Drag coefficient (sphere ≈ 0.47) |
| `diameterMeters` | `double` | Diameter in meters **Parameter `dragCoefficient`:** Drag coefficient (sphere ≈ 0.47) |
| `dragCoefficient` | `double` | Drag coefficient (sphere ≈ 0.47) |

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

??? note "Author note from JavaDoc"

    Set custom game piece properties
    **Parameter `massKg`:** Mass in kilograms
    **Parameter `diameterMeters`:** Diameter in meters
    **Parameter `dragCoefficient`:** Drag coefficient (sphere ≈ 0.47)

### `public TrajectoryConfig setCustomGamePieceImperial(double massLbs, double diameterInches, double dragCoefficient)`

[Source lines 148–154](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L148)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It changes object/subclass state through `customDiameter`, `customDragCoeff`, `customMass`, `gamePiece`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `massLbs` | `double` | Mass in pounds **Parameter `diameterInches`:** Diameter in inches **Parameter `dragCoefficient`:** Drag coefficient |
| `diameterInches` | `double` | Diameter in inches **Parameter `dragCoefficient`:** Drag coefficient |
| `dragCoefficient` | `double` | Drag coefficient |

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

??? note "Author note from JavaDoc"

    Convenience method to set custom game piece from imperial units
    **Parameter `massLbs`:** Mass in pounds
    **Parameter `diameterInches`:** Diameter in inches
    **Parameter `dragCoefficient`:** Drag coefficient

### `public TrajectoryPoint(double time, double x, double y, double vx, double vy)`

[Source lines 198–204](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L198)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It changes object/subclass state through `time`, `vx`, `vy`, `x`, `y`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `time` | `double` | time since launch (s) **Parameter `x`:** horizontal position (m) **Parameter `y`:** vertical position (m) **Parameter `vx`:** horizontal velocity (m/s) **Parameter `vy`:** vertical velocity (m/s) |
| `x` | `double` | horizontal position (m) **Parameter `y`:** vertical position (m) **Parameter `vx`:** horizontal velocity (m/s) **Parameter `vy`:** vertical velocity (m/s) |
| `y` | `double` | vertical position (m) **Parameter `vx`:** horizontal velocity (m/s) **Parameter `vy`:** vertical velocity (m/s) |
| `vx` | `double` | horizontal velocity (m/s) **Parameter `vy`:** vertical velocity (m/s) |
| `vy` | `double` | vertical velocity (m/s) |

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

??? note "Author note from JavaDoc"

    Creates a trajectory sample point.
    
    **Parameter `time`:** time since launch (s)
    **Parameter `x`:** horizontal position (m)
    **Parameter `y`:** vertical position (m)
    **Parameter `vx`:** horizontal velocity (m/s)
    **Parameter `vy`:** vertical velocity (m/s)

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

??? note "Author note from JavaDoc"

    Get the configuration builder

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

??? note "Author note from JavaDoc"

    Get the current configuration (read-only access)

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

??? note "Author note from JavaDoc"

    Main method to get the desired trajectory based on current configuration
    **Returns:** List of trajectory points

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

??? note "Author note from JavaDoc"

    Get the optimal angle to hit the configured target
    **Returns:** Optimal angle in degrees, or -1 if no solution found

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

??? note "Author note from JavaDoc"

    Get the required velocity to hit the configured target at the configured angle
    **Returns:** Required velocity in m/s, or -1 if no solution found

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

??? note "Author note from JavaDoc"

    Get the time of flight for the configured shot
    **Returns:** Time in seconds

## Exposed fields and types

### `public class Trajectory`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L22)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Trajectory calculator for projectile motion with air resistance
    Designed for scoring with a ball
    
    Usage:
    Trajectory.configure()
    .setShotVelocity(12.0)
    .setShotAngle(45.0)
    .setTargetDistance(4.0)
    .setGamePiece(GamePiece.FUEL);
    
    List path = Trajectory.getDesiredTrajectory();
    double angle = Trajectory.getOptimalAngle();

### `public static final double HUB_HEIGHT = Units.inchesToMeters(72.0)`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L30)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 2 times, so changing it can affect every control path that reads `HUB_HEIGHT`.

### `public static final double HUB_DISTANCE_FROM_ALLIANCE_WALL = Units.inchesToMeters(158.6)`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L31)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 1 time, so changing it can affect every control path that reads `HUB_DISTANCE_FROM_ALLIANCE_WALL`.

### `public enum GamePiece`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L39)*

This exposed `enum` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Game piece types with their physical properties

### `public final double mass`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L44)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 16 times, so changing it can affect every control path that reads `mass`.

??? note "Author note from JavaDoc"

    Mass of the game piece in kilograms.

### `public final double diameter`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L46)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 7 times, so changing it can affect every control path that reads `diameter`.

??? note "Author note from JavaDoc"

    Diameter of the game piece in meters.

### `public final double dragCoefficient`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L48)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 11 times, so changing it can affect every control path that reads `dragCoefficient`.

??? note "Author note from JavaDoc"

    Aerodynamic drag coefficient (sphere ≈ 0.47).

### `public static class TrajectoryConfig`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L65)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Configuration builder for trajectory calculations

### `public static class TrajectoryPoint`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L177)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Represents a point in the trajectory

### `public final double time`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L179)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 11 times, so changing it can affect every control path that reads `time`.

??? note "Author note from JavaDoc"

    Time since launch in seconds.

### `public final double x`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L181)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 20 times, so changing it can affect every control path that reads `x`.

??? note "Author note from JavaDoc"

    Horizontal distance traveled in meters.

### `public final double y`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L183)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 20 times, so changing it can affect every control path that reads `y`.

??? note "Author note from JavaDoc"

    Height above ground in meters.

### `public final double vx`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L185)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 21 times, so changing it can affect every control path that reads `vx`.

??? note "Author note from JavaDoc"

    Horizontal velocity component in m/s.

### `public final double vy`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/physics/Trajectory.java#L187)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 21 times, so changing it can affect every control path that reads `vy`.

??? note "Author note from JavaDoc"

    Vertical velocity component in m/s.
