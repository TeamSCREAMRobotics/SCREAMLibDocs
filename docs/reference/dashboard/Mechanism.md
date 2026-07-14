# Mechanism

`com.teamscreamrobotics.dashboard.Mechanism`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java) · **6 callables** · **4 exposed fields/types**

## Competition usage

**2026:** [`Drivetrain.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/drivetrain/Drivetrain.java#L69), [`IntakeWrist.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/intake/IntakeWrist.java#L4)

## Public and protected callables

### `public Mechanism(String key, Ligament... ligaments)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L33)*

Creates a mechanism with the given dashboard key and ordered ligament chain.

**Parameter `key`:** identifier used as the root name in the `Mechanism2d` widget
**Parameter `ligaments`:** one or more ligaments, in chain order from root outward

### `protected void initialize(Mechanism2d measured, Mechanism2d setpoint)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L38)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public Mechanism withStaticPosition(Translation2d position)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L62)*

Sets a fixed root position for the mechanism in the 2D widget.

**Parameter `position`:** the constant (x, y) position of the root

### `public Mechanism withDynamicPosition(Supplier&lt;Translation2d&gt; position)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L72)*

Sets a dynamic root position supplier, updated each periodic cycle.

**Parameter `position`:** supplier for the (x, y) root position

### `public void setPosition(Translation2d position)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L82)*

Imperatively overrides the root position with a new fixed value.

**Parameter `position`:** the new (x, y) root position

### `protected void update()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L86)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

## Exposed fields and types

### `public class Mechanism`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L13)*

A named group of `Ligament`s forming a kinematic chain for `MechanismVisualizer`.
The first ligament is anchored at a root; subsequent ones chain from their predecessor unless
`Ligament#withOverrideAppend(boolean)` is set.

### `public Mechanism2d measured`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L15)*

### `public Mechanism2d setpoint`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L16)*

### `public String key`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L18)*
