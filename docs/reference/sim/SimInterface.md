# SimInterface

`com.teamscreamrobotics.sim.SimInterface`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java) · **4 callables** · **1 exposed fields/types**

## Public and protected callables

### `void update(double deltaTime)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java#L10)*

Advances the simulation by `deltaTime` seconds.

**Parameter `deltaTime`:** elapsed time since the last call, in seconds

### `void setInputVoltage(double voltage)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java#L17)*

Applies the motor input voltage to the simulation.

**Parameter `voltage`:** input voltage in volts

### `double getPosition()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java#L20)*

Returns the simulated mechanism position in rotations.

### `double getVelocity()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java#L23)*

Returns the simulated mechanism velocity in rotations per second.

## Exposed fields and types

### `public interface SimInterface`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java#L4)*

Common interface for physics simulation backends (DC motor, elevator, arm, flywheel).
