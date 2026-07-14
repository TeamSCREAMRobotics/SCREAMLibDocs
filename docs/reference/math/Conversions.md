# Conversions

`com.teamscreamrobotics.math.Conversions`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java) · **7 callables** · **1 exposed fields/types** · **2 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2025: Use `Conversions` in `Elevator.java`

[`src/main/java/frc2025/subsystems/superstructure/elevator/Elevator.java` lines 39–54](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/elevator/Elevator.java#L39-L54)

```java
private ElevatorGoal(Length targetHeight) {
  this.height = targetHeight;
  this.targetRotations =
      () ->
          Conversions.linearDistanceToRotations(
              targetHeight, ElevatorConstants.PULLEY_CIRCUMFERENCE);
}

@Override
public ControlType controlType() {
  return ControlType.MOTION_MAGIC_POSITION;
}

@Override
public DoubleSupplier target() {
```

### 2026: Use `Conversions` in `Shooter.java`

[`src/main/java/frc2026/tars/subsystems/shooter/Shooter.java` lines 500–515](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/Shooter.java#L500-L515)

```java
.plus(Util.transform3dTo2dXY(ShooterConstants.flywheelToRobot)));
}

public double getTimeOfFlight(double distance, double velocity, double hoodAngleDeg) {
  double exitVelocity =
      Conversions.rpsToMPS(
              velocity,
              FlywheelConstants.FLYWHEEL_CIRCUMFERENCE.getMeters(),
              FlywheelConstants.FLYWHEEL_REDUCTION)
          * 0.8;
  double exitAngle = 90.0 - hoodAngleDeg;
  double horizontalVelocity = exitVelocity * Math.cos(Units.degreesToRadians(exitAngle));

  if (horizontalVelocity < 0.01) return distance / 0.01;
  return distance / horizontalVelocity;
}
```

## Public and protected callables

### `public static double rpsToRPM(double falconRPS, double gearRatio)`

[Source lines 14–17](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L14)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `motorRPM / gearRatio`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `falconRPS` | `double` | Falcon rotations per second **Parameter `gearRatio`:** gear ratio between Falcon and mechanism (set to 1 for Falcon RPM) **Returns:** RPM of mechanism |
| `gearRatio` | `double` | gear ratio between Falcon and mechanism (set to 1 for Falcon RPM) **Returns:** RPM of mechanism |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 14–17)"

    ```java
    public static double rpsToRPM(double falconRPS, double gearRatio) {
      double motorRPM = falconRPS * 60.0;
      return motorRPM / gearRatio;
    }
    ```

??? note "Author note from JavaDoc"

    **Parameter `falconRPS`:** Falcon rotations per second
    **Parameter `gearRatio`:** gear ratio between Falcon and mechanism (set to 1 for Falcon RPM)
    **Returns:** RPM of mechanism

### `public static double rpmToRPS(double rpm, double gearRatio)`

[Source lines 24–27](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L24)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `motorRPM / 60.0`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `rpm` | `double` | RPM of mechanism **Parameter `gearRatio`:** Gear ratio between Falcon and mechanism (set to 1 for Falcon RPS) **Returns:** Falcon rotations per second |
| `gearRatio` | `double` | Gear ratio between Falcon and mechanism (set to 1 for Falcon RPS) **Returns:** Falcon rotations per second |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 24–27)"

    ```java
    public static double rpmToRPS(double rpm, double gearRatio) {
      double motorRPM = rpm * gearRatio;
      return motorRPM / 60.0;
    }
    ```

??? note "Author note from JavaDoc"

    **Parameter `rpm`:** RPM of mechanism
    **Parameter `gearRatio`:** Gear ratio between Falcon and mechanism (set to 1 for Falcon RPS)
    **Returns:** Falcon rotations per second

### `public static double rpsToMPS(double falconRPS, double circumference, double gearRatio)`

[Source lines 35–38](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L35)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `(wheelRPM * circumference) / 60.0`.
- Key collaborators/calls: `rpsToRPM()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `falconRPS` | `double` | Falcon rotations per second **Parameter `circumference`:** circumference of wheel in meters **Parameter `gearRatio`:** gear ratio between Falcon and mechanism **Returns:** mechanism linear velocity in meters per second |
| `circumference` | `double` | circumference of wheel in meters **Parameter `gearRatio`:** gear ratio between Falcon and mechanism **Returns:** mechanism linear velocity in meters per second |
| `gearRatio` | `double` | gear ratio between Falcon and mechanism **Returns:** mechanism linear velocity in meters per second |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 35–38)"

    ```java
    public static double rpsToMPS(double falconRPS, double circumference, double gearRatio) {
      double wheelRPM = rpsToRPM(falconRPS, gearRatio);
      return (wheelRPM * circumference) / 60.0;
    }
    ```

??? note "Author note from JavaDoc"

    **Parameter `falconRPS`:** Falcon rotations per second
    **Parameter `circumference`:** circumference of wheel in meters
    **Parameter `gearRatio`:** gear ratio between Falcon and mechanism
    **Returns:** mechanism linear velocity in meters per second

### `public static double mpsToRPS(double velocity, double circumference, double gearRatio)`

[Source lines 46–49](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L46)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `rpmToRPS(wheelRPM, gearRatio)`.
- Key collaborators/calls: `rpmToRPS()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `velocity` | `double` | velocity in meters per second **Parameter `circumference`:** circumference of wheel in meters **Parameter `gearRatio`:** gear ratio between Falcon and mechanism **Returns:** Falcon rotations per second |
| `circumference` | `double` | circumference of wheel in meters **Parameter `gearRatio`:** gear ratio between Falcon and mechanism **Returns:** Falcon rotations per second |
| `gearRatio` | `double` | gear ratio between Falcon and mechanism **Returns:** Falcon rotations per second |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 46–49)"

    ```java
    public static double mpsToRPS(double velocity, double circumference, double gearRatio) {
      double wheelRPM = ((velocity * 60) / circumference);
      return rpmToRPS(wheelRPM, gearRatio);
    }
    ```

??? note "Author note from JavaDoc"

    **Parameter `velocity`:** velocity in meters per second
    **Parameter `circumference`:** circumference of wheel in meters
    **Parameter `gearRatio`:** gear ratio between Falcon and mechanism
    **Returns:** Falcon rotations per second

### `public static double rpmToFTS(double rpm, double circumference)`

[Source lines 56–58](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L56)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `(circumference * rpm) / 60`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `rpm` | `double` | RPM of the mechanism **Parameter `circumference`:** circumference of the wheel in feet **Returns:** linear velocity in feet per second |
| `circumference` | `double` | circumference of the wheel in feet **Returns:** linear velocity in feet per second |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 56–58)"

    ```java
    public static double rpmToFTS(double rpm, double circumference) {
      return (circumference * rpm) / 60;
    }
    ```

??? note "Author note from JavaDoc"

    **Parameter `rpm`:** RPM of the mechanism
    **Parameter `circumference`:** circumference of the wheel in feet
    **Returns:** linear velocity in feet per second

### `public static double linearDistanceToRotations(Length distance, Length circumference)`

[Source lines 65–67](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L65)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Return path: `distance.getInches() / circumference.getInches()`.
- Key collaborators/calls: `distance.getInches()`, `circumference.getInches()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `distance` | `Length` | linear distance traveled **Parameter `circumference`:** circumference per rotation **Returns:** number of rotations |
| `circumference` | `Length` | circumference per rotation **Returns:** number of rotations |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 65–67)"

    ```java
    public static double linearDistanceToRotations(Length distance, Length circumference) {
      return distance.getInches() / circumference.getInches();
    }
    ```

??? note "Author note from JavaDoc"

    **Parameter `distance`:** linear distance traveled
    **Parameter `circumference`:** circumference per rotation
    **Returns:** number of rotations

### `public static Length rotationsToLinearDistance(double rotations, Length circumference)`

[Source lines 74–76](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L74)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `circumference.times(rotations)`.
- Key collaborators/calls: `circumference.times()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `rotations` | `double` | number of rotations **Parameter `circumference`:** circumference per rotation **Returns:** linear distance traveled |
| `circumference` | `Length` | circumference per rotation **Returns:** linear distance traveled |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 74–76)"

    ```java
    public static Length rotationsToLinearDistance(double rotations, Length circumference) {
      return circumference.times(rotations);
    }
    ```

??? note "Author note from JavaDoc"

    **Parameter `rotations`:** number of rotations
    **Parameter `circumference`:** circumference per rotation
    **Returns:** linear distance traveled

## Exposed fields and types

### `public class Conversions`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/Conversions.java#L8)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
