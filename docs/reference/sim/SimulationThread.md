# SimulationThread

`com.teamscreamrobotics.sim.SimulationThread`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java) · **5 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public SimulationThread( TalonFXSubsystemSimConstants constants, SimStateCallback stateConsumer, double periodSec, String name)`

[Source lines 42–57](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L42)

**Detailed behavior**

- The implementation executes 10 non-blank source lines.
- It changes object/subclass state through `lastSimTime`, `limitVoltage`, `name`, `periodSec`, `simInterface`, `stateConsumer`, `useSeparateThread`.
- It has 1 conditional path: `useSeparateThread`.
- Key collaborators/calls: `constants.sim()`, `constants.useSeparateThread()`, `constants.limitVoltage()`, `Timer.getFPGATimestamp()`, `startSimThread()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `constants` | `TalonFXSubsystemSimConstants` | `TalonFXSubsystemSimConstants` input consumed by the implementation shown below. |
| `stateConsumer` | `SimStateCallback` | `SimStateCallback` input consumed by the implementation shown below. |
| `periodSec` | `double` | Time value in seconds. |
| `name` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `SimulationThread` instance.

??? example "Implementation (source lines 42–57)"

    ```java
    public SimulationThread(
        TalonFXSubsystemSimConstants constants,
        SimStateCallback stateConsumer,
        double periodSec,
        String name) {
      this.name = name;
      this.simInterface = constants.sim();
      this.useSeparateThread = constants.useSeparateThread();
      this.limitVoltage = constants.limitVoltage();
      this.stateConsumer = stateConsumer;
      this.periodSec = periodSec;
      this.lastSimTime = Timer.getFPGATimestamp();
      if (useSeparateThread) {
        startSimThread(name);
      }
    }
    ```

### `public void setSimVoltage(DoubleSupplier simVoltage)`

[Source lines 65–71](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L65)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It changes object/subclass state through `simVoltage`.
- It bounds at least one intermediate or output value before use.
- Key collaborators/calls: `MathUtil.clamp()`, `simVoltage.getAsDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `simVoltage` | `DoubleSupplier` | Voltage value in volts. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 65–71)"

    ```java
    public void setSimVoltage(DoubleSupplier simVoltage) {
      this.simVoltage =
          () ->
              limitVoltage
                  ? MathUtil.clamp(simVoltage.getAsDouble(), -12, 12)
                  : simVoltage.getAsDouble();
    }
    ```

### `public DoubleSupplier getSimVoltage()`

[Source lines 74–76](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L74)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `simVoltage`.

**Inputs:** None.

**Result:** Returns `DoubleSupplier`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 74–76)"

    ```java
    public DoubleSupplier getSimVoltage() {
      return simVoltage;
    }
    ```

### `public void update()`

[Source lines 82–95](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L82)

**Detailed behavior**

- The implementation executes 11 non-blank source lines.
- It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.
- It has 1 conditional path: `useSeparateThread`.
- Key collaborators/calls: `DriverStation.reportError()`, `Timer.getFPGATimestamp()`, `simInterface.setInputVoltage()`, `simVoltage.getAsDouble()`, `stateConsumer.accept()`, `simInterface.getPosition()`, `simInterface.getVelocity()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 82–95)"

    ```java
    public void update() {
      if (useSeparateThread) {
        DriverStation.reportError(
            "Simulation thread: " + name + " | Do not call update if using separate thread!", true);
        return;
      }
      final double currentTime = Timer.getFPGATimestamp();
      deltaTime = currentTime - lastSimTime;
      lastSimTime = currentTime;
    
      simInterface.setInputVoltage(simVoltage.getAsDouble());
      simInterface.update(deltaTime);
      stateConsumer.accept(simInterface.getPosition(), simInterface.getVelocity());
    }
    ```

### `public void startSimThread(String name)`

[Source lines 102–116](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L102)

**Detailed behavior**

- The implementation executes 12 non-blank source lines.
- Key collaborators/calls: `Notifier()`, `Timer.getFPGATimestamp()`, `simInterface.setInputVoltage()`, `simVoltage.getAsDouble()`, `simInterface.update()`, `stateConsumer.accept()`, `simInterface.getPosition()`, `simInterface.getVelocity()`, `simNotifier.setName()`, `simNotifier.startPeriodic()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | `String` | `String` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 102–116)"

    ```java
    public void startSimThread(String name) {
      simNotifier =
          new Notifier(
              () -> {
                final double currentTime = Timer.getFPGATimestamp();
                deltaTime = currentTime - lastSimTime;
                lastSimTime = currentTime;
    
                simInterface.setInputVoltage(simVoltage.getAsDouble());
                simInterface.update(deltaTime);
                stateConsumer.accept(simInterface.getPosition(), simInterface.getVelocity());
              });
      simNotifier.setName(name);
      simNotifier.startPeriodic(periodSec);
    }
    ```

## Exposed fields and types

### `public class SimulationThread`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimulationThread.java#L15)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
