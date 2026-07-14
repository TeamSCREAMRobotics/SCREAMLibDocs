# Ligament

`com.teamscreamrobotics.dashboard.Ligament`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java) · **15 callables** · **4 exposed fields/types**

## Competition usage

**2026:** [`IntakeWrist.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/intake/IntakeWrist.java#L3)

## Public and protected callables

### `public Ligament()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L30)*

Creates a Ligament with default zero angle and length; configure with `with*` methods.

### `protected void initialize(int index, MechanismRoot2d measured, MechanismRoot2d setpoint)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L32)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `protected void initialize(int index, MechanismLigament2d previousMeasured, MechanismLigament2d previousSetpoint)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L39)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public Ligament withOverrideAppend(boolean override)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L50)*

When `true`, this ligament is appended directly to the root instead of its predecessor.
Useful for multi-branch mechanisms that share a common root but diverge.

### `public Ligament withStaticAngle(Rotation2d angle)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L60)*

Sets a fixed angle for both the measured and setpoint ligaments.

**Parameter `angle`:** the constant angle to display

### `public Ligament withDynamicAngle(Supplier&lt;Rotation2d&gt; measured, Supplier&lt;Rotation2d&gt; setpoint)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L72)*

Sets independent angle suppliers for the measured and setpoint ligaments.

**Parameter `measured`:** supplier for the actual/measured angle
**Parameter `setpoint`:** supplier for the goal/setpoint angle

### `public Ligament withDynamicAngle(Supplier&lt;Rotation2d&gt; angle)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L83)*

Sets a single angle supplier used for both measured and setpoint ligaments.

**Parameter `angle`:** supplier for the angle to display

### `public Ligament withStaticLength(Length length)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L94)*

Sets a fixed length for both the measured and setpoint ligaments.

**Parameter `length`:** the constant length to display

### `public Ligament withDynamicLength(Supplier&lt;Length&gt; measured, Supplier&lt;Length&gt; setpoint)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L106)*

Sets independent length suppliers for the measured and setpoint ligaments.

**Parameter `measured`:** supplier for the actual/measured length
**Parameter `setpoint`:** supplier for the goal/setpoint length

### `public Ligament withDynamicLength(Supplier&lt;Length&gt; length)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L117)*

Sets a single length supplier used for both measured and setpoint ligaments.

**Parameter `length`:** supplier for the length to display

### `public void setAngle(Rotation2d angle)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L128)*

Imperatively sets the same fixed angle for both measured and setpoint ligaments.

**Parameter `angle`:** the angle to display

### `public void setAngle(Rotation2d measured, Rotation2d setpoint)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L139)*

Imperatively sets independent fixed angles for the measured and setpoint ligaments.

**Parameter `measured`:** the actual/measured angle
**Parameter `setpoint`:** the goal/setpoint angle

### `public void setLength(Length length)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L149)*

Imperatively sets the same fixed length for both measured and setpoint ligaments.

**Parameter `length`:** the length to display

### `public void setLength(Length measured, Length setpoint)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L160)*

Imperatively sets independent fixed lengths for the measured and setpoint ligaments.

**Parameter `measured`:** the actual/measured length
**Parameter `setpoint`:** the goal/setpoint length

### `protected void update()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L165)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

## Exposed fields and types

### `public class Ligament`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L17)*

Represents a single joint segment in a `Mechanism`, tracking both a measured (red) and
setpoint (green) `MechanismLigament2d`. Use the `with*` builder methods to configure
angle and length sources, then attach to a `Mechanism`.

### `protected MechanismLigament2d measuredLig`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L19)*

### `protected MechanismLigament2d setpointLig`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L20)*

### `protected boolean overrideAppend`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L27)*
