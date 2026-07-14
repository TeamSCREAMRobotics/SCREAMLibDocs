# AllianceFlipUtil

`com.teamscreamrobotics.util.AllianceFlipUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java) · **18 callables** · **4 exposed fields/types**

## Competition usage

**2025:** [`Routines.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/autonomous/Routines.java#L34), [`FieldConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/constants/FieldConstants.java#L14), [`Controlboard.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/controlboard/Controlboard.java#L17), [`RobotContainer.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/RobotContainer.java#L42), [`RobotState.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/RobotState.java#L25), [`Drivetrain.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/drivetrain/Drivetrain.java#L97), [`VisionManager.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/vision/VisionManager.java#L32)

**2026:** [`Controlboard.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/controlboard/Controlboard.java#L3), [`RobotContainer.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/RobotContainer.java#L9), [`RobotState.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/RobotState.java#L5), [`Drivetrain.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/drivetrain/Drivetrain.java#L12), [`Shooter.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/Shooter.java#L9)

## Public and protected callables

### `public static BooleanSupplier shouldFlip()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L24)*

Returns a supplier that is `true` when the robot is on the red alliance.

### `public static Rotation2d getFwdHeading()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L29)*

Returns `0°` for blue alliance and `180°` for red — the forward-facing heading.

### `public static int getDirectionCoefficient()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L34)*

Returns `+1` for blue and `-1` for red — useful for signed field-relative math.

### `public static &lt;T&gt; T get(T blueValue, T redValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L39)*

Returns `blueValue` on blue alliance and `redValue` on red.

### `public static &lt;T&gt; T get(T blueValue, T redValue, boolean inverse)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L50)*

Returns the alliance-appropriate value, optionally inverted.

**Parameter `blueValue`:** the value to return for blue (or red when `inverse` is true)
**Parameter `redValue`:** the value to return for red (or blue when `inverse` is true)
**Parameter `inverse`:** if `true`, swaps which alliance gets which value

### `public static Rotation2d FlippedRotation2d(Rotation2d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L57)*

Returns the blue rotation, or blue + 180° on red (rotationally-symmetric flip).

### `public static Rotation3d FlippedRotation3d(Rotation3d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L62)*

Returns the blue rotation, or the Z-flipped equivalent on red (rotationally-symmetric flip).

### `public static Translation2d FlippedTranslation2d(Translation2d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L70)*

Returns the blue translation, or `(fieldLength - x, fieldWidth - y)` on red.

### `public static Pose2d FlippedPose2d(Pose2d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L79)*

Returns the blue pose, or the rotationally-flipped equivalent on red.

### `public static Translation3d FlippedTranslation3d(Translation3d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L86)*

Returns the blue translation3d, or `(fieldLength - x, fieldWidth - y, z)` on red.

### `public static Pose3d FlippedPose3d(Pose3d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L96)*

Returns the blue pose3d, or the rotationally-flipped equivalent on red.

### `public static Rotation2d MirroredRotation2d(Rotation2d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L103)*

Returns the blue rotation, or `180° - blueValue` on red (bilaterally-symmetric mirror).

### `public static Rotation3d MirroredRotation3d(Rotation3d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L108)*

Returns the blue rotation3d, or the Z-mirrored equivalent on red (bilaterally-symmetric).

### `public static Translation2d MirroredTranslation2d(Translation2d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L116)*

Returns the blue translation, or `(fieldLength - x, y)` on red (X-axis mirror only).

### `blueValue, new Translation2d(FIELD_DIMENSIONS.getX() - blueValue.getX(), blueValue.getY()))`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L118)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public static Pose2d MirroredPose2d(Pose2d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L122)*

Returns the blue pose, or the X-axis-mirrored equivalent on red (bilaterally-symmetric).

### `public static Translation3d MirroredTranslation3d(Translation3d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L129)*

Returns the blue translation3d, or `(fieldLength - x, y, z)` on red (X-axis mirror).

### `public static Pose3d MirroredPose3d(Pose3d blueValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L137)*

Returns the blue pose3d, or the X-axis-mirrored equivalent on red.

## Exposed fields and types

### `public final class AllianceFlipUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L14)*

Utility for flipping or mirroring field-relative geometry between blue and red alliance.

### `public static final Translation2d FIELD_DIMENSIONS = new Translation2d(16.541, 8.211)`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L17)*

Full field dimensions (length × width) in meters.

### `public static final double FIELD_WIDTH = FIELD_DIMENSIONS.getY()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L19)*

Field width (Y axis) in meters.

### `public static final double FIELD_LENGTH = FIELD_DIMENSIONS.getX()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/AllianceFlipUtil.java#L21)*

Field length (X axis) in meters.
