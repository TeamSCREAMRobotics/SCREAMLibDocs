# MechanismVisualizer

`com.teamscreamrobotics.dashboard.MechanismVisualizer`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java) · **3 callables** · **3 exposed fields/types**

## Competition usage

**2026:** [`RobotContainer.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/RobotContainer.java#L8)

## Public and protected callables

### `public MechanismVisualizer( Mechanism2d measuredMechanism, Mechanism2d setpointMechanism, BiConsumer&lt;Mechanism2d, Mechanism2d&gt; telemetryConsumer, Mechanism... mechanisms)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L31)*

Creates the visualizer and initializes all mechanisms.

**Parameter `measuredMechanism`:** the `Mechanism2d` widget for actual state (typically logged red)
**Parameter `setpointMechanism`:** the `Mechanism2d` widget for setpoint state (typically logged green)
**Parameter `telemetryConsumer`:** called each periodic cycle with (measured, setpoint) to publish data
**Parameter `mechanisms`:** one or more `Mechanism`s to update and display

### `public void setEnabled(boolean enabled)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L44)*

Enables or disables periodic updates. Disable to suppress logging overhead when not needed.

### `public void periodic()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L49)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

## Exposed fields and types

### `public class MechanismVisualizer extends SubsystemBase`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L13)*

A WPILib subsystem that periodically updates one or more `Mechanism`s and publishes
their measured and setpoint `Mechanism2d` widgets via a telemetry consumer.

### `public Mechanism2d MEASURED_MECHANISM`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L15)*

### `public Mechanism2d SETPOINT_MECHANISM`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L16)*
