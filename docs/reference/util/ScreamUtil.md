# ScreamUtil

`com.teamscreamrobotics.util.ScreamUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java) · **13 callables** · **2 exposed fields/types** · **4 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2025: Use `ScreamUtil` in `Controlboard.java`

[`src/main/java/frc2025/controlboard/Controlboard.java` lines 75–90](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/controlboard/Controlboard.java#L75-L90)

```java
}

public static Translation2d snapTranslationToPole(Translation2d translation) {
  if (!translation.equals(Translation2d.kZero)) {
    for (int i = 0; i < 4; i++) {
      if (ScreamUtil.withinAngleThreshold(
          Rotation2d.kCCW_90deg.times(i), translation.getAngle(), SNAP_TO_POLE_THRESHOLD)) {
        return new Translation2d(translation.getNorm(), Rotation2d.kCCW_90deg.times(i));
      }
    }
    return translation;
  } else {
    return Translation2d.kZero;
  }
}
```

### 2025: Use `ScreamUtil` in `Drivetrain.java`

[`src/main/java/frc2025/subsystems/drivetrain/Drivetrain.java` lines 115–130](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/drivetrain/Drivetrain.java#L115-L130)

```java
});
  simThread.startPeriodic(Constants.SIM_PERIOD_SEC);
}

public boolean getWithinAngleThreshold(Rotation2d targetAngle, Rotation2d threshold) {
  return ScreamUtil.withinAngleThreshold(targetAngle, getHeading(), threshold);
}

public Pose2d getEstimatedPose() {
  return getState().Pose;
}

public Rotation2d getHeading() {
  return getEstimatedPose().getRotation();
}
```

### 2026: Use `ScreamUtil` in `Controlboard.java`

[`src/main/java/frc2026/tars/controlboard/Controlboard.java` lines 46–61](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/controlboard/Controlboard.java#L46-L61)

```java
}

public static Translation2d snapTranslationToPole(Translation2d translation) {
  if (!translation.equals(Translation2d.kZero)) {
    for (int i = 0; i < 4; i++) {
      if (ScreamUtil.withinAngleThreshold(
          Rotation2d.kCCW_90deg.times(i), translation.getAngle(), SNAP_TO_POLE_THRESHOLD)) {
        return new Translation2d(translation.getNorm(), Rotation2d.kCCW_90deg.times(i));
      }
    }
    return translation;
  } else {
    return Translation2d.kZero;
  }
}
```

### 2026: Use `ScreamUtil` in `Drivetrain.java`

[`src/main/java/frc2026/tars/subsystems/drivetrain/Drivetrain.java` lines 178–193](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/drivetrain/Drivetrain.java#L178-L193)

```java
});
  m_simNotifier.startPeriodic(kSimLoopPeriod);
}

public boolean getWithinAngleThreshold(Rotation2d targetAngle, Rotation2d threshold) {
  return ScreamUtil.withinAngleThreshold(targetAngle, getHeading(), threshold);
}

public Pose2d getEstimatedPose() {
  return getState().Pose;
}

public Rotation2d getHeading() {
  return getEstimatedPose().getRotation();
}
```

## Public and protected callables

### `public static Rotation2d boundRotation(Rotation2d rotation)`

[Source lines 15–17](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L15)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Rotation2d(MathUtil.angleModulus(rotation.getRadians()))`.
- Key collaborators/calls: `Rotation2d()`, `MathUtil.angleModulus()`, `rotation.getRadians()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `rotation` | `Rotation2d` | Mechanism or rotor rotations; verify the configured ratio. |

**Result:** Returns `Rotation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 15–17)"

    ```java
    public static Rotation2d boundRotation(Rotation2d rotation) {
      return new Rotation2d(MathUtil.angleModulus(rotation.getRadians()));
    }
    ```

??? note "Author note from JavaDoc"

    Wraps `rotation` to the range `(-π, π]`.

### `public static Rotation2d boundRotation0_360(Rotation2d rotation)`

[Source lines 20–24](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L20)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `rotation.getDegrees(`.
- Return paths: `Rotation2d.fromDegrees(rotation.getDegrees() + 360.0)`; `rotation`.
- Key collaborators/calls: `boundRotation()`, `rotation.getDegrees()`, `Rotation2d.fromDegrees()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `rotation` | `Rotation2d` | Mechanism or rotor rotations; verify the configured ratio. |

**Result:** Returns `Rotation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 20–24)"

    ```java
    public static Rotation2d boundRotation0_360(Rotation2d rotation) {
      rotation = boundRotation(rotation);
      if (rotation.getDegrees() < 0) return Rotation2d.fromDegrees(rotation.getDegrees() + 360.0);
      return rotation;
    }
    ```

??? note "Author note from JavaDoc"

    Wraps `rotation` to the range `[0°, 360°)`.

### `public static Rotation2d getTangent(Translation2d start, Translation2d end)`

[Source lines 32–35](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L32)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `new Rotation2d(dist.getX(), dist.getY())`.
- Key collaborators/calls: `end.minus()`, `Rotation2d()`, `dist.getX()`, `dist.getY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `start` | `Translation2d` | the starting point **Parameter `end`:** the ending point |
| `end` | `Translation2d` | the ending point |

**Result:** Returns `Rotation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 32–35)"

    ```java
    public static Rotation2d getTangent(Translation2d start, Translation2d end) {
      Translation2d dist = end.minus(start);
      return new Rotation2d(dist.getX(), dist.getY());
    }
    ```

??? note "Author note from JavaDoc"

    Returns the tangent (heading) angle of the vector from `start` to `end`.
    
    **Parameter `start`:** the starting point
    **Parameter `end`:** the ending point

### `public static boolean epsilonEquals(double a, double b, final double epsilon)`

[Source lines 44–46](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L44)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `(a - epsilon <= b) && (a + epsilon >= b)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `a` | `double` | first value **Parameter `b`:** second value **Parameter `epsilon`:** tolerance |
| `b` | `double` | second value **Parameter `epsilon`:** tolerance |
| `epsilon` | `double` | tolerance |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 44–46)"

    ```java
    public static boolean epsilonEquals(double a, double b, final double epsilon) {
      return (a - epsilon <= b) && (a + epsilon >= b);
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if `|a - b| <= epsilon`.
    
    **Parameter `a`:** first value
    **Parameter `b`:** second value
    **Parameter `epsilon`:** tolerance

### `public static boolean epsilonEquals(double a, double b)`

[Source lines 49–51](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L49)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `epsilonEquals(a, b, EPSILON)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `a` | `double` | `double` input consumed by the implementation shown below. |
| `b` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 49–51)"

    ```java
    public static boolean epsilonEquals(double a, double b) {
      return epsilonEquals(a, b, EPSILON);
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if `|a - b| <= EPSILON`.

### `public static boolean epsilonEquals(int a, int b, int epsilon)`

[Source lines 54–56](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L54)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `(a - epsilon <= b) && (a + epsilon >= b)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `a` | `int` | `int` input consumed by the implementation shown below. |
| `b` | `int` | `int` input consumed by the implementation shown below. |
| `epsilon` | `int` | Allowed absolute error around the target. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 54–56)"

    ```java
    public static boolean epsilonEquals(int a, int b, int epsilon) {
      return (a - epsilon <= b) && (a + epsilon >= b);
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if `|a - b| <= epsilon` (integer overload).

### `public double getStallTorque(double stallTorque, double freeSpeed, double speed)`

[Source lines 65–67](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L65)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `-stallTorque / freeSpeed * speed + stallTorque`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `stallTorque` | `double` | maximum torque at zero speed (N·m) **Parameter `freeSpeed`:** no-load speed (rad/s or RPM — must match units of `speed`) **Parameter `speed`:** current speed |
| `freeSpeed` | `double` | no-load speed (rad/s or RPM — must match units of `speed`) **Parameter `speed`:** current speed |
| `speed` | `double` | current speed |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 65–67)"

    ```java
    public double getStallTorque(double stallTorque, double freeSpeed, double speed) {
      return -stallTorque / freeSpeed * speed + stallTorque;
    }
    ```

??? note "Author note from JavaDoc"

    Estimates output torque at the given speed using a linear motor model.
    
    **Parameter `stallTorque`:** maximum torque at zero speed (N·m)
    **Parameter `freeSpeed`:** no-load speed (rad/s or RPM — must match units of `speed`)
    **Parameter `speed`:** current speed

### `public static Twist2d chassisSpeedsToTwist2d(ChassisSpeeds chassisSpeeds)`

[Source lines 74–79](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L74)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `new Twist2d( chassisSpeeds.vxMetersPerSecond, chassisSpeeds.vyMetersPerSecond, chassisSpeeds.omegaRadiansPerSecond)`.
- Key collaborators/calls: `Twist2d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `chassisSpeeds` | `ChassisSpeeds` | the speeds to convert |

**Result:** Returns `Twist2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 74–79)"

    ```java
    public static Twist2d chassisSpeedsToTwist2d(ChassisSpeeds chassisSpeeds) {
      return new Twist2d(
          chassisSpeeds.vxMetersPerSecond,
          chassisSpeeds.vyMetersPerSecond,
          chassisSpeeds.omegaRadiansPerSecond);
    }
    ```

??? note "Author note from JavaDoc"

    Converts a `ChassisSpeeds` to a `Twist2d` with the same vx, vy, and omega.
    
    **Parameter `chassisSpeeds`:** the speeds to convert

### `public static boolean epsilonEquals(final Twist2d twist, final Twist2d other, double epsilon)`

[Source lines 88–92](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L88)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `ScreamUtil.epsilonEquals(twist.dx, other.dx, epsilon) && ScreamUtil.epsilonEquals(twist.dy, other.dy, epsilon) && ScreamUtil.epsilonEquals(twist.dtheta, other.dtheta, epsilon)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `twist` | `Twist2d` | first twist **Parameter `other`:** second twist **Parameter `epsilon`:** per-component tolerance |
| `other` | `Twist2d` | second twist **Parameter `epsilon`:** per-component tolerance |
| `epsilon` | `double` | per-component tolerance |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 88–92)"

    ```java
    public static boolean epsilonEquals(final Twist2d twist, final Twist2d other, double epsilon) {
      return ScreamUtil.epsilonEquals(twist.dx, other.dx, epsilon)
          && ScreamUtil.epsilonEquals(twist.dy, other.dy, epsilon)
          && ScreamUtil.epsilonEquals(twist.dtheta, other.dtheta, epsilon);
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if all components of two twists are within `epsilon` of each other.
    
    **Parameter `twist`:** first twist
    **Parameter `other`:** second twist
    **Parameter `epsilon`:** per-component tolerance

### `public static boolean epsilonEquals(final Twist2d twist, final Twist2d other)`

[Source lines 95–97](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L95)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `epsilonEquals(twist, other, EPSILON)`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `twist` | `Twist2d` | `Twist2d` input consumed by the implementation shown below. |
| `other` | `Twist2d` | `Twist2d` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 95–97)"

    ```java
    public static boolean epsilonEquals(final Twist2d twist, final Twist2d other) {
      return epsilonEquals(twist, other, EPSILON);
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if all twist components are within `#EPSILON` of each other.

### `public static boolean valueBetween(double value, double upper, double lower)`

[Source lines 106–108](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L106)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `value < upper && value > lower`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | `double` | the value to test **Parameter `upper`:** the exclusive upper bound **Parameter `lower`:** the exclusive lower bound |
| `upper` | `double` | the exclusive upper bound **Parameter `lower`:** the exclusive lower bound |
| `lower` | `double` | the exclusive lower bound |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 106–108)"

    ```java
    public static boolean valueBetween(double value, double upper, double lower) {
      return value < upper && value > lower;
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if `lower < value < upper` (exclusive).
    
    **Parameter `value`:** the value to test
    **Parameter `upper`:** the exclusive upper bound
    **Parameter `lower`:** the exclusive lower bound

### `public static boolean withinAngleThreshold( Rotation2d targetAngle, Rotation2d currentAngle, Rotation2d threshold)`

[Source lines 118–122](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L118)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `MathUtil.isNear( targetAngle.getDegrees(), currentAngle.getDegrees(), threshold.getDegrees(), -180, 180)`.
- Key collaborators/calls: `MathUtil.isNear()`, `targetAngle.getDegrees()`, `currentAngle.getDegrees()`, `threshold.getDegrees()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `targetAngle` | `Rotation2d` | the desired angle **Parameter `currentAngle`:** the measured angle **Parameter `threshold`:** the maximum allowable error |
| `currentAngle` | `Rotation2d` | the measured angle **Parameter `threshold`:** the maximum allowable error |
| `threshold` | `Rotation2d` | the maximum allowable error |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 118–122)"

    ```java
    public static boolean withinAngleThreshold(
        Rotation2d targetAngle, Rotation2d currentAngle, Rotation2d threshold) {
      return MathUtil.isNear(
          targetAngle.getDegrees(), currentAngle.getDegrees(), threshold.getDegrees(), -180, 180);
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if `currentAngle` is within `threshold` of `targetAngle`,
    accounting for wrap-around.
    
    **Parameter `targetAngle`:** the desired angle
    **Parameter `currentAngle`:** the measured angle
    **Parameter `threshold`:** the maximum allowable error

### `public static double random(double lower, double upper)`

[Source lines 130–137](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L130)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- It has 1 conditional path: `lower >= upper`.
- Return path: `(Math.random() * (upper - lower + 1)) + lower`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `lower` | `double` | lower bound **Parameter `upper`:** upper bound |
| `upper` | `double` | upper bound |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 130–137)"

    ```java
    public static double random(double lower, double upper) {
      if (lower >= upper) {
        double temp = upper;
        upper = lower;
        lower = temp;
      }
      return (Math.random() * (upper - lower + 1)) + lower;
    }
    ```

??? note "Author note from JavaDoc"

    Returns a random double in `[lower, upper]`, swapping bounds if `lower >= upper`.
    
    **Parameter `lower`:** lower bound
    **Parameter `upper`:** upper bound

## Exposed fields and types

### `public class ScreamUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L10)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Various utility methods

### `public static final double EPSILON = 1e-3`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/ScreamUtil.java#L12)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 5 times, so changing it can affect every control path that reads `EPSILON`.

??? note "Author note from JavaDoc"

    Default epsilon used by the no-argument `#epsilonEquals` overloads.
