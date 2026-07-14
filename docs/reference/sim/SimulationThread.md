# SimulationThread

`com.teamscreamrobotics.sim.SimulationThread`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java) · **5 callables** · **1 exposed fields/types**

## Public and protected callables

### `public SimulationThread( TalonFXSubsystemSimConstants constants, SimStateCallback stateConsumer, double periodSec, String name)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L42)*

Creates a simulation thread. If `TalonFXSubsystemSimConstants#useSeparateThread()` is
`true` the notifier is started immediately.

**Parameter `constants`:** simulation constants from the subsystem configuration
**Parameter `stateConsumer`:** called with `(position, velocity)` after each sim step (no boxing)
**Parameter `periodSec`:** update period in seconds
**Parameter `name`:** thread/notifier name for diagnostics

### `public void setSimVoltage(DoubleSupplier simVoltage)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L65)*

Sets the voltage supplier used to drive the simulation each step.
If `TalonFXSubsystemSimConstants#limitVoltage()` is `true`, the value is clamped to ±12V.

**Parameter `simVoltage`:** supplier returning the desired input voltage

### `public DoubleSupplier getSimVoltage()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L74)*

Returns the current sim voltage supplier (already wrapped with optional clamping).

### `public void update()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L82)*

Manually steps the simulation. Must only be called when not using a separate thread;
logs a DS error and returns early if the notifier is active.

### `public void startSimThread(String name)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L102)*

Starts the background `Notifier` thread at the configured period.

**Parameter `name`:** the notifier thread name

## Exposed fields and types

### `public class SimulationThread`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L15)*

Drives a `SimInterface` at a fixed period, either inline (called from `periodic()`)
or on a dedicated background thread using a WPILib `Notifier`.
