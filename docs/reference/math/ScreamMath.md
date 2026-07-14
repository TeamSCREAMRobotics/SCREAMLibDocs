# ScreamMath

`com.teamscreamrobotics.math.ScreamMath`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java) · **9 callables** · **2 exposed fields/types** · **4 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2025: Use `ScreamMath` in `DriveToPose.java`

[`src/main/java/frc2025/commands/DriveToPose.java` lines 101–116](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/commands/DriveToPose.java#L101-L116)

```java
double ffScalar = MathUtil.clamp((currentDistance) / (0.8), 0.0, 1.0);
double elevHeightScalar = elevator.getMeasuredHeight().getInches();
elevHeightScalar =
    MathUtil.clamp(elevHeightScalar, 0.0, ElevatorConstants.MAX_HEIGHT.getInches());
elevHeightScalar =
    ScreamMath.mapRange(
        elevHeightScalar, 0.0, ElevatorConstants.MAX_HEIGHT.getInches(), 1.0, 0.5);

driveErrorAbs = currentDistance;

lastSetpointTranslation =
    new Pose2d(
            targetPose.getTranslation(),
            currentPose.getTranslation().minus(targetPose.getTranslation()).getAngle())
        .transformBy(
            GeomUtil.translationToTransform(driveController.getSetpoint().position, 0.0))
```

### 2025: Use `ScreamMath` in `Controlboard.java`

[`src/main/java/frc2025/controlboard/Controlboard.java` lines 64–79](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/controlboard/Controlboard.java#L64-L79)

```java
.times(DrivetrainConstants.MAX_SPEED))
          .times(AllianceFlipUtil.getDirectionCoefficient())
          .times(
              driveController.getHID().getPOV() == 0
                  ? 0.5
                  : ScreamMath.mapRange(
                      elevHeightSup.getAsDouble(),
                      0.0,
                      ElevatorConstants.MAX_HEIGHT.getInches(),
                      1.0,
                      0.4));
}

public static Translation2d snapTranslationToPole(Translation2d translation) {
  if (!translation.equals(Translation2d.kZero)) {
    for (int i = 0; i < 4; i++) {
```

### 2026: Use `ScreamMath` in `LED.java`

[`src/main/java/frc2026/tars/subsystems/leds/LED.java` lines 117–132](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/leds/LED.java#L117-L132)

```java
}

public void scaledTarget(Color color, double currentValue, double targetValue) {
  if (targetValue == 0) return;

  int mapped = (int) Math.round(ScreamMath.mapRange(currentValue, 0, targetValue, 0, length));
  mapped = MathUtil.clamp(mapped, 0, length);

  for (int i = 0; i < mapped; i++) {
    buffer.setLED(i, color);
  }

  for (int i = mapped; i < length; i++) {
    buffer.setLED(i, Color.kBlack);
  }
}
```

### 2026: Use `ScreamMath` in `Shooter.java`

[`src/main/java/frc2026/tars/subsystems/shooter/Shooter.java` lines 194–209](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/Shooter.java#L194-L209)

```java
} else {
    flywheelSetpoint = flywheelMap * Dashboard.farMapNudge.get();
  }

  robotState.setDrivetrainTarget(
      ScreamMath.calculateAngleToPoint(robotPose.getTranslation(), target)
          .plus(Rotation2d.k180deg));

  hood.moveToAngle(Rotation2d.fromDegrees(wantShoot ? hoodAngleDeg : 0.0));
  flywheel.setTargetVelocityTorqueCurrent(flywheelSetpoint / multiplier, 0.0);

  Logger.log(logPrefix + "Hood Angle", hoodAngleDeg);
  Logger.log(logPrefix + "Flywheel Velocity", flywheelSetpoint);
  Logger.log(logPrefix + "Shot Distance", distanceMeters);
  // }
}
```

## Public and protected callables

### `public static double average(double... nums)`

[Source lines 24–32](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L24)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- It has 1 conditional path: `nums.length == 0`.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return paths: `0.0`; `sum / nums.length`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `nums` | `double...` | the values to average |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 24–32)"

    ```java
    public static double average(double... nums) {
      if (nums.length == 0) return 0.0;
    
      double sum = 0.0;
      for (double num : nums) {
        sum += num;
      }
      return sum / nums.length;
    }
    ```

??? note "Author note from JavaDoc"

    Returns the arithmetic mean of the given values, or `0.0` if the array is empty.
    
    **Parameter `nums`:** the values to average

### `public static double mapRange( double value, double fromLow, double fromHigh, double toLow, double toHigh)`

[Source lines 44–51](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L44)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It has 1 conditional path: `fromHigh - fromLow == 0`.
- It can explicitly throw `IllegalArgumentException`.
- Return path: `toLow + ((value - fromLow) * (toHigh - toLow)) / (fromHigh - fromLow)`.
- Key collaborators/calls: `IllegalArgumentException()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | `double` | the input value in the source range **Parameter `fromLow`:** lower bound of the source range **Parameter `fromHigh`:** upper bound of the source range **Parameter `toLow`:** lower bound of the target range **Parameter `… |
| `fromLow` | `double` | lower bound of the source range **Parameter `fromHigh`:** upper bound of the source range **Parameter `toLow`:** lower bound of the target range **Parameter `toHigh`:** upper bound of the target range **Throws `IllegalA… |
| `fromHigh` | `double` | upper bound of the source range **Parameter `toLow`:** lower bound of the target range **Parameter `toHigh`:** upper bound of the target range **Throws `IllegalArgumentException`:** if the source range has zero width |
| `toLow` | `double` | lower bound of the target range **Parameter `toHigh`:** upper bound of the target range **Throws `IllegalArgumentException`:** if the source range has zero width |
| `toHigh` | `double` | upper bound of the target range **Throws `IllegalArgumentException`:** if the source range has zero width |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 44–51)"

    ```java
    public static double mapRange(
        double value, double fromLow, double fromHigh, double toLow, double toHigh) {
      if (fromHigh - fromLow == 0) {
        throw new IllegalArgumentException("Input range has zero width");
      }
    
      return toLow + ((value - fromLow) * (toHigh - toLow)) / (fromHigh - fromLow);
    }
    ```

??? note "Author note from JavaDoc"

    Linearly maps `value` from one range to another.
    
    **Parameter `value`:** the input value in the source range
    **Parameter `fromLow`:** lower bound of the source range
    **Parameter `fromHigh`:** upper bound of the source range
    **Parameter `toLow`:** lower bound of the target range
    **Parameter `toHigh`:** upper bound of the target range
    **Throws `IllegalArgumentException`:** if the source range has zero width

### `public static double getLinearVelocity(ChassisSpeeds speeds)`

[Source lines 58–60](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L58)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `Math.hypot(speeds.vxMetersPerSecond, speeds.vyMetersPerSecond)`.
- Key collaborators/calls: `Math.hypot()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `speeds` | `ChassisSpeeds` | the chassis speed |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 58–60)"

    ```java
    public static double getLinearVelocity(ChassisSpeeds speeds) {
      return Math.hypot(speeds.vxMetersPerSecond, speeds.vyMetersPerSecond);
    }
    ```

??? note "Author note from JavaDoc"

    Returns the translational speed magnitude (vx² + vy²)^½ from a `ChassisSpeeds`.
    
    **Parameter `speeds`:** the chassis speed

### `public static Translation3d rotatePoint(Translation3d point, Rotation2d yaw)`

[Source lines 68–77](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L68)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- Return path: `new Translation3d(newX, newY, newZ)`.
- Key collaborators/calls: `yaw.getCos()`, `yaw.getSin()`, `point.getX()`, `point.getY()`, `point.getZ()`, `Translation3d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `point` | `Translation3d` | the point to rotate **Parameter `yaw`:** the rotation angle around the Z-axis |
| `yaw` | `Rotation2d` | the rotation angle around the Z-axis |

**Result:** Returns `Translation3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 68–77)"

    ```java
    public static Translation3d rotatePoint(Translation3d point, Rotation2d yaw) {
      double cosAngle = yaw.getCos();
      double sinAngle = yaw.getSin();
    
      double newX = point.getX() * cosAngle - point.getY() * sinAngle;
      double newY = point.getX() * sinAngle + point.getY() * cosAngle;
      double newZ = point.getZ();
    
      return new Translation3d(newX, newY, newZ);
    }
    ```

??? note "Author note from JavaDoc"

    Rotates a 3D point around the Z-axis by `yaw`, preserving Z.
    
    **Parameter `point`:** the point to rotate
    **Parameter `yaw`:** the rotation angle around the Z-axis

### `public static Translation2d rotatePoint(Translation2d point, Rotation2d yaw)`

[Source lines 85–88](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L85)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `t3d.toTranslation2d()`.
- Key collaborators/calls: `Translation3d()`, `point.getX()`, `point.getY()`, `t3d.toTranslation2d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `point` | `Translation2d` | the point to rotate **Parameter `yaw`:** the rotation angle |
| `yaw` | `Rotation2d` | the rotation angle |

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 85–88)"

    ```java
    public static Translation2d rotatePoint(Translation2d point, Rotation2d yaw) {
      Translation3d t3d = rotatePoint(new Translation3d(point.getX(), point.getY(), 0), yaw);
      return t3d.toTranslation2d();
    }
    ```

??? note "Author note from JavaDoc"

    Rotates a 2D point by `yaw`.
    
    **Parameter `point`:** the point to rotate
    **Parameter `yaw`:** the rotation angle

### `public static Rotation2d calculateAngleToPoint(Translation2d current, Translation2d target)`

[Source lines 96–100](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L96)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `Rotation2d.fromRadians(Math.atan2(targetY, targetX))`.
- Key collaborators/calls: `target.getX()`, `current.getX()`, `target.getY()`, `current.getY()`, `Rotation2d.fromRadians()`, `Math.atan2()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `current` | `Translation2d` | the observer position **Parameter `target`:** the target position |
| `target` | `Translation2d` | the target position |

**Result:** Returns `Rotation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 96–100)"

    ```java
    public static Rotation2d calculateAngleToPoint(Translation2d current, Translation2d target) {
      double targetX = target.getX() - current.getX();
      double targetY = target.getY() - current.getY();
      return Rotation2d.fromRadians(Math.atan2(targetY, targetX));
    }
    ```

??? note "Author note from JavaDoc"

    Returns the bearing angle from `current` to `target`.
    
    **Parameter `current`:** the observer position
    **Parameter `target`:** the target position

### `public static Rotation2d clamp(Rotation2d rotation, Rotation2d high, Rotation2d low)`

[Source lines 109–112](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L109)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It bounds at least one intermediate or output value before use.
- Return path: `Rotation2d.fromRadians( MathUtil.clamp(rotation.getRadians(), low.getRadians(), high.getRadians()))`.
- Key collaborators/calls: `Rotation2d.fromRadians()`, `rotation.getRadians()`, `low.getRadians()`, `high.getRadians()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `rotation` | `Rotation2d` | the rotation to clamp **Parameter `high`:** the upper bound **Parameter `low`:** the lower bound |
| `high` | `Rotation2d` | the upper bound **Parameter `low`:** the lower bound |
| `low` | `Rotation2d` | the lower bound |

**Result:** Returns `Rotation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 109–112)"

    ```java
    public static Rotation2d clamp(Rotation2d rotation, Rotation2d high, Rotation2d low) {
      return Rotation2d.fromRadians(
          MathUtil.clamp(rotation.getRadians(), low.getRadians(), high.getRadians()));
    }
    ```

??? note "Author note from JavaDoc"

    Clamps `rotation` to the range `[low, high]` in radians.
    
    **Parameter `rotation`:** the rotation to clamp
    **Parameter `high`:** the upper bound
    **Parameter `low`:** the lower bound

### `public static double square(double n)`

[Source lines 115–117](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L115)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `Math.pow(n, 2)`.
- Key collaborators/calls: `Math.pow()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `n` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 115–117)"

    ```java
    public static double square(double n){
      return Math.pow(n, 2);
    }
    ```

??? note "Author note from JavaDoc"

    Returns `n²`.

### `public static MomentOfInertia parallelAxisTheorem(MomentOfInertia moi, Mass mass, Length distance)`

[Source lines 127–129](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L127)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Return path: `Units.KilogramSquareMeters.of(moi.in(Units.KilogramSquareMeters) * mass.times(distance.squared().getMeters()).in(Units.Kilograms))`.
- Key collaborators/calls: `Units.KilogramSquareMeters.of()`, `moi.in()`, `mass.times()`, `distance.squared()`, `getMeters()`, `in()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `moi` | `MomentOfInertia` | moment of inertia about the center of mass **Parameter `mass`:** mass of the object **Parameter `distance`:** distance from the center of mass to the new axis **Returns:** the moment of inertia about the new parallel ax… |
| `mass` | `Mass` | mass of the object **Parameter `distance`:** distance from the center of mass to the new axis **Returns:** the moment of inertia about the new parallel axis |
| `distance` | `Length` | distance from the center of mass to the new axis **Returns:** the moment of inertia about the new parallel axis |

**Result:** Returns `MomentOfInertia`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 127–129)"

    ```java
    public static MomentOfInertia parallelAxisTheorem(MomentOfInertia moi, Mass mass, Length distance){
      return Units.KilogramSquareMeters.of(moi.in(Units.KilogramSquareMeters) * mass.times(distance.squared().getMeters()).in(Units.Kilograms));
    }
    ```

??? note "Author note from JavaDoc"

    Applies the parallel axis theorem: `I = I_cm + m * d²`.
    
    **Parameter `moi`:** moment of inertia about the center of mass
    **Parameter `mass`:** mass of the object
    **Parameter `distance`:** distance from the center of mass to the new axis
    **Returns:** the moment of inertia about the new parallel axis

## Exposed fields and types

### `public class ScreamMath`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L14)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    General-purpose math utilities for FRC calculations.

### `public static final double METERS_PER_INCH = 0.0254`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/ScreamMath.java#L17)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 1 time, so changing it can affect every control path that reads `METERS_PER_INCH`.

??? note "Author note from JavaDoc"

    Conversion factor: meters per inch ({@value} m/in).
