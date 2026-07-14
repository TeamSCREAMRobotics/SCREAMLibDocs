# GeomUtil

`com.teamscreamrobotics.util.GeomUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java) · **15 callables** · **1 exposed fields/types** · **2 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2026: Compose robot, turret, hood, and shooter transforms

[`src/main/java/frc2026/tars/subsystems/shooter/Shooter.java` lines 490–505](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/Shooter.java#L490-L505)

```java
}

  Logger.log(logPrefix + "beam", beamDebouncer.calculate(beam.getIsDetected().getValue()));
}

public Pose2d getFieldToShooter() {
  Pose2d pose = robotPose;

  return GeomUtil.transformToPose(
      GeomUtil.poseToTransform(pose)
          .plus(Util.transform3dTo2dXY(ShooterConstants.flywheelToRobot)));
}

public double getTimeOfFlight(double distance, double velocity, double hoodAngleDeg) {
  double exitVelocity =
      Conversions.rpsToMPS(
```

### 2025: Convert translations into transforms while calculating an alignment setpoint

[`src/main/java/frc2025/commands/AutoAlign.java` lines 195–229](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/commands/AutoAlign.java#L195-L229)

```java
if (currentDistance < driveTolerance) {
  driveVelocityScalar = 0.0;
}

lastSetpointTranslation =
    new Pose2d(
            targetPose.getTranslation(),
            currentPose.getTranslation().minus(targetPose.getTranslation()).getAngle())
        .transformBy(
            GeomUtil.translationToTransform(driveController.getSetpoint().position, 0.0))
        .getTranslation();

double thetaVelocity =
    headingController.getSetpoint().velocity * ffScalar
        + headingController.calculate(
            currentPose.getRotation().getRadians(), targetPose.getRotation().getRadians());
headingErrorAbs =
    Math.abs(currentPose.getRotation().minus(targetPose.getRotation()).getRadians());
if (headingErrorAbs < headingTolerance) {
  thetaVelocity = 0.0;
}

Translation2d driveVelocity =
    new Pose2d(
            Translation2d.kZero,
            currentPose.getTranslation().minus(targetPose.getTranslation()).getAngle())
        .transformBy(GeomUtil.translationToTransform(driveVelocityScalar, 0.0))
        .getTranslation();

drivetrain.setControl(
    drivetrain
        .getHelper()
        .getApplyRobotSpeeds(
            ChassisSpeeds.fromFieldRelativeSpeeds(
```

## Public and protected callables

### `public static Transform2d translationToTransform(Translation2d translation)`

[Source lines 28–30](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L28)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Transform2d(translation, Rotation2d.kZero)`.
- Key collaborators/calls: `Transform2d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | The translation to create the transform with **Returns:** The resulting transform |

**Result:** Returns `Transform2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 28–30)"

    ```java
    public static Transform2d translationToTransform(Translation2d translation) {
      return new Transform2d(translation, Rotation2d.kZero);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a pure translating transform
    
    **Parameter `translation`:** The translation to create the transform with
    **Returns:** The resulting transform

### `public static Transform2d translationToTransform(double x, double y)`

[Source lines 39–41](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L39)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Transform2d(new Translation2d(x, y), Rotation2d.kZero)`.
- Key collaborators/calls: `Transform2d()`, `Translation2d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `x` | `double` | The x componenet of the translation **Parameter `y`:** The y componenet of the translation **Returns:** The resulting transform |
| `y` | `double` | The y componenet of the translation **Returns:** The resulting transform |

**Result:** Returns `Transform2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 39–41)"

    ```java
    public static Transform2d translationToTransform(double x, double y) {
      return new Transform2d(new Translation2d(x, y), Rotation2d.kZero);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a pure translating transform
    
    **Parameter `x`:** The x componenet of the translation
    **Parameter `y`:** The y componenet of the translation
    **Returns:** The resulting transform

### `public static Transform2d rotationToTransform(Rotation2d rotation)`

[Source lines 49–51](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L49)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Transform2d(Translation2d.kZero, rotation)`.
- Key collaborators/calls: `Transform2d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `rotation` | `Rotation2d` | The rotation to create the transform with **Returns:** The resulting transform |

**Result:** Returns `Transform2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 49–51)"

    ```java
    public static Transform2d rotationToTransform(Rotation2d rotation) {
      return new Transform2d(Translation2d.kZero, rotation);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a pure rotating transform
    
    **Parameter `rotation`:** The rotation to create the transform with
    **Returns:** The resulting transform

### `public static Transform2d poseToTransform(Pose2d pose)`

[Source lines 59–61](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L59)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Transform2d(pose.getTranslation(), pose.getRotation())`.
- Key collaborators/calls: `Transform2d()`, `pose.getTranslation()`, `pose.getRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pose` | `Pose2d` | The pose that will represent the transform **Returns:** The resulting transform |

**Result:** Returns `Transform2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 59–61)"

    ```java
    public static Transform2d poseToTransform(Pose2d pose) {
      return new Transform2d(pose.getTranslation(), pose.getRotation());
    }
    ```

??? note "Author note from JavaDoc"

    Converts a Pose2d to a Transform2d to be used in a kinematic chain
    
    **Parameter `pose`:** The pose that will represent the transform
    **Returns:** The resulting transform

### `public static Pose2d transformToPose(Transform2d transform)`

[Source lines 70–72](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L70)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Pose2d(transform.getTranslation(), transform.getRotation())`.
- Key collaborators/calls: `Pose2d()`, `transform.getTranslation()`, `transform.getRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `transform` | `Transform2d` | The transform that will represent the pose **Returns:** The resulting pose |

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 70–72)"

    ```java
    public static Pose2d transformToPose(Transform2d transform) {
      return new Pose2d(transform.getTranslation(), transform.getRotation());
    }
    ```

??? note "Author note from JavaDoc"

    Converts a Transform2d to a Pose2d to be used as a position or as the start of a kinematic
    chain
    
    **Parameter `transform`:** The transform that will represent the pose
    **Returns:** The resulting pose

### `public static Pose2d translationToPose(Translation2d translation)`

[Source lines 80–82](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L80)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Pose2d(translation, Rotation2d.kZero)`.
- Key collaborators/calls: `Pose2d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | The translation to create the pose with **Returns:** The resulting pose |

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 80–82)"

    ```java
    public static Pose2d translationToPose(Translation2d translation) {
      return new Pose2d(translation, Rotation2d.kZero);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a pure translated pose
    
    **Parameter `translation`:** The translation to create the pose with
    **Returns:** The resulting pose

### `public static Pose2d rotationToPose(Rotation2d rotation)`

[Source lines 90–92](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L90)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Pose2d(Translation2d.kZero, rotation)`.
- Key collaborators/calls: `Pose2d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `rotation` | `Rotation2d` | The rotation to create the pose with **Returns:** The resulting pose |

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 90–92)"

    ```java
    public static Pose2d rotationToPose(Rotation2d rotation) {
      return new Pose2d(Translation2d.kZero, rotation);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a pure rotated pose
    
    **Parameter `rotation`:** The rotation to create the pose with
    **Returns:** The resulting pose

### `public static Twist2d multiplyTwist(Twist2d twist, double factor)`

[Source lines 101–103](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L101)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Twist2d(twist.dx * factor, twist.dy * factor, twist.dtheta * factor)`.
- Key collaborators/calls: `Twist2d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `twist` | `Twist2d` | The twist to multiply **Parameter `factor`:** The scaling factor for the twist components **Returns:** The new twist |
| `factor` | `double` | The scaling factor for the twist components **Returns:** The new twist |

**Result:** Returns `Twist2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 101–103)"

    ```java
    public static Twist2d multiplyTwist(Twist2d twist, double factor) {
      return new Twist2d(twist.dx * factor, twist.dy * factor, twist.dtheta * factor);
    }
    ```

??? note "Author note from JavaDoc"

    Multiplies a twist by a scaling factor
    
    **Parameter `twist`:** The twist to multiply
    **Parameter `factor`:** The scaling factor for the twist components
    **Returns:** The new twist

### `public static Transform3d pose3dToTransform3d(Pose3d pose)`

[Source lines 111–113](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L111)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Transform3d(pose.getTranslation(), pose.getRotation())`.
- Key collaborators/calls: `Transform3d()`, `pose.getTranslation()`, `pose.getRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pose` | `Pose3d` | The pose that will represent the transform **Returns:** The resulting transform |

**Result:** Returns `Transform3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 111–113)"

    ```java
    public static Transform3d pose3dToTransform3d(Pose3d pose) {
      return new Transform3d(pose.getTranslation(), pose.getRotation());
    }
    ```

??? note "Author note from JavaDoc"

    Converts a Pose3d to a Transform3d to be used in a kinematic chain
    
    **Parameter `pose`:** The pose that will represent the transform
    **Returns:** The resulting transform

### `public static Pose3d transform3dToPose3d(Transform3d transform)`

[Source lines 122–124](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L122)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Pose3d(transform.getTranslation(), transform.getRotation())`.
- Key collaborators/calls: `Pose3d()`, `transform.getTranslation()`, `transform.getRotation()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `transform` | `Transform3d` | The transform that will represent the pose **Returns:** The resulting pose |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 122–124)"

    ```java
    public static Pose3d transform3dToPose3d(Transform3d transform) {
      return new Pose3d(transform.getTranslation(), transform.getRotation());
    }
    ```

??? note "Author note from JavaDoc"

    Converts a Transform3d to a Pose3d to be used as a position or as the start of a kinematic
    chain
    
    **Parameter `transform`:** The transform that will represent the pose
    **Returns:** The resulting pose

### `public static Translation2d translation3dTo2dXY(Translation3d translation)`

[Source lines 132–134](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L132)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Translation2d(translation.getX(), translation.getY())`.
- Key collaborators/calls: `Translation2d()`, `translation.getX()`, `translation.getY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation3d` | The original translation **Returns:** The resulting translation |

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 132–134)"

    ```java
    public static Translation2d translation3dTo2dXY(Translation3d translation) {
      return new Translation2d(translation.getX(), translation.getY());
    }
    ```

??? note "Author note from JavaDoc"

    Converts a Translation3d to a Translation2d by extracting two dimensions (X and Y). chain
    
    **Parameter `translation`:** The original translation
    **Returns:** The resulting translation

### `public static Translation2d translation3dTo2dXZ(Translation3d translation)`

[Source lines 142–144](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L142)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Translation2d(translation.getX(), translation.getZ())`.
- Key collaborators/calls: `Translation2d()`, `translation.getX()`, `translation.getZ()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation3d` | The original translation **Returns:** The resulting translation |

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 142–144)"

    ```java
    public static Translation2d translation3dTo2dXZ(Translation3d translation) {
      return new Translation2d(translation.getX(), translation.getZ());
    }
    ```

??? note "Author note from JavaDoc"

    Converts a Translation3d to a Translation2d by extracting two dimensions (X and Z). chain
    
    **Parameter `translation`:** The original translation
    **Returns:** The resulting translation

### `public static Pose3d translationToPose3d(Translation2d translation, double z)`

[Source lines 152–155](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L152)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `new Pose3d( new Translation3d(translation.getX(), translation.getY(), z), new Rotation3d())`.
- Key collaborators/calls: `Pose3d()`, `Translation3d()`, `translation.getX()`, `translation.getY()`, `Rotation3d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | the XY position **Parameter `z`:** the height in meters |
| `z` | `double` | the height in meters |

**Result:** Returns `Pose3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 152–155)"

    ```java
    public static Pose3d translationToPose3d(Translation2d translation, double z) {
      return new Pose3d(
          new Translation3d(translation.getX(), translation.getY(), z), new Rotation3d());
    }
    ```

??? note "Author note from JavaDoc"

    Creates a `Pose3d` from a 2D translation and a Z height, with zero rotation.
    
    **Parameter `translation`:** the XY position
    **Parameter `z`:** the height in meters

### `public static Translation2d normalize(Translation2d translation)`

[Source lines 162–164](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L162)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Translation2d(1, translation.getAngle())`.
- Key collaborators/calls: `Translation2d()`, `translation.getAngle()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | the vector to normalize |

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 162–164)"

    ```java
    public static Translation2d normalize(Translation2d translation){
      return new Translation2d(1, translation.getAngle());
    }
    ```

??? note "Author note from JavaDoc"

    Returns a unit vector in the same direction as `translation`.
    
    **Parameter `translation`:** the vector to normalize

### `public static Translation2d findClosest(Translation2d origin, Translation2d... others)`

[Source lines 172–185](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L172)

**Detailed behavior**

- The implementation executes 10 non-blank source lines.
- It has 1 conditional path: `distance < smallestDistance`.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `closest`.
- Key collaborators/calls: `origin.getDistance()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `origin` | `Translation2d` | the reference point **Parameter `others`:** the candidate points to search |
| `others` | `Translation2d...` | the candidate points to search |

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 172–185)"

    ```java
    public static Translation2d findClosest(Translation2d origin, Translation2d... others){
      Translation2d closest = null;
      double smallestDistance = Double.MAX_VALUE;
    
      for(Translation2d point : others){
        double distance = origin.getDistance(point);
        if(distance < smallestDistance){
          smallestDistance = distance;
          closest = point;
        }
      }
    
      return closest;
    }
    ```

??? note "Author note from JavaDoc"

    Returns the point in `others` nearest to `origin` by Euclidean distance.
    
    **Parameter `origin`:** the reference point
    **Parameter `others`:** the candidate points to search

## Exposed fields and types

### `public class GeomUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/GeomUtil.java#L21)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Geometry utilities for working with translations, rotations, transforms, and poses.
