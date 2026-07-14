# SimWrapper

`com.teamscreamrobotics.sim.SimWrapper`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java) · **10 callables** · **1 exposed fields/types** · **3 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

!!! note "2025 package names"
    The 2025 robot used SCREAMLib's earlier short packages such as `data`, `drivers`, and `util`. With SCREAMLib 26.3.7, prefix those imports with `com.teamscreamrobotics.`; the implementation pattern remains applicable.

### 2025: Use `SimWrapper` in `IntakeConstants.java`

[`src/main/java/frc2025/subsystems/intake/IntakeConstants.java` lines 48–63](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/intake/IntakeConstants.java#L48-L63)

```java
DEPLOY_CONFIG.codeEnabled = false;
DEPLOY_CONFIG.logTelemetry = false;

DEPLOY_CONFIG.simConstants =
    new TalonFXSubsystemSimConstants(
        new SimWrapper(SIM, PINION_CIRCUMFERENCE, DEPLOY_REDUCTION),
        DEPLOY_REDUCTION,
        SIM_GAINS.getProfiledPIDController(new Constraints(60.0, 30.0)),
        false,
        false);

DEPLOY_CONFIG.masterConstants =
    new TalonFXConstants(new CANDevice(10), InvertedValue.Clockwise_Positive);

DEPLOY_CONFIG.neutralMode = NeutralModeValue.Brake;
```

### 2025: Use `SimWrapper` in `ElevatorConstants.java`

[`src/main/java/frc2025/subsystems/superstructure/elevator/ElevatorConstants.java` lines 58–73](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/elevator/ElevatorConstants.java#L58-L73)

```java
CONFIGURATION.logTelemetry = false;
CONFIGURATION.debugMode = false;

CONFIGURATION.simConstants =
    new TalonFXSubsystemSimConstants(
        new SimWrapper(SIM, PULLEY_CIRCUMFERENCE, REDUCTION),
        REDUCTION,
        SIM_GAINS.getProfiledPIDController(new Constraints(1.5 * 0.7, 0.7)),
        true,
        true);

CONFIGURATION.masterConstants =
    new TalonFXConstants(
        new CANDevice(9, ""), InvertedValue.Clockwise_Positive); // Left Elevator Inside
CONFIGURATION.slaveConstants =
    new TalonFXConstants[] {
```

### 2026: Use `SimWrapper` in `IntakeConstants.java`

[`src/main/java/frc2026/tars/subsystems/intake/IntakeConstants.java` lines 56–71](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/intake/IntakeConstants.java#L56-L71)

```java
WRIST_CONFIG.logTelemetry = false;
WRIST_CONFIG.debugMode = false;

WRIST_CONFIG.simConstants =
    new TalonFXSubsystemSimConstants(
        new SimWrapper(SIM, INTAKE_REDUCTION),
        INTAKE_REDUCTION,
        SIM_GAINS.getProfiledPIDController(new Constraints(0.5, 0.1)),
        false,
        true);

WRIST_CONFIG.masterConstants =
    new TalonFXConstants(new CANDevice(10), InvertedValue.Clockwise_Positive);

WRIST_CONFIG.neutralMode = NeutralModeValue.Brake;
WRIST_CONFIG.sensorToMechRatio = INTAKE_REDUCTION;
```

## Public and protected callables

### `public SimWrapper(DCMotorSim sim)`

[Source lines 36–41](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L36)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Key collaborators/calls: `sim.setInput()`, `sim.getAngularPositionRotations()`, `sim.getGearing()`, `sim.getAngularVelocityRPM()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `sim` | `DCMotorSim` | `DCMotorSim` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `SimWrapper` instance.

??? example "Implementation (source lines 36–41)"

    ```java
    public SimWrapper(DCMotorSim sim) {
      updateConsumer = sim::update;
      voltageConsumer = (value) -> sim.setInput(0, value);
      positionSupplier = () -> sim.getAngularPositionRotations() * sim.getGearing();
      velocitySupplier = () -> (sim.getAngularVelocityRPM() / 60.0) * sim.getGearing();
    }
    ```

### `public SimWrapper(DCMotorSim sim, double gearing)`

[Source lines 50–55](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L50)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Key collaborators/calls: `sim.setInput()`, `sim.getAngularPositionRotations()`, `sim.getAngularVelocityRPM()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `sim` | `DCMotorSim` | `DCMotorSim` input consumed by the implementation shown below. |
| `gearing` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `SimWrapper` instance.

??? example "Implementation (source lines 50–55)"

    ```java
    public SimWrapper(DCMotorSim sim, double gearing) {
      updateConsumer = sim::update;
      voltageConsumer = (value) -> sim.setInput(0, value);
      positionSupplier = () -> sim.getAngularPositionRotations() * gearing;
      velocitySupplier = () -> (sim.getAngularVelocityRPM() / 60.0) * gearing;
    }
    ```

### `public SimWrapper(ElevatorSim sim, Length spoolCircumference, double gearing)`

[Source lines 65–70](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L65)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Key collaborators/calls: `sim.setInput()`, `sim.getPositionMeters()`, `spoolCircumference.getMeters()`, `sim.getVelocityMetersPerSecond()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `sim` | `ElevatorSim` | `ElevatorSim` input consumed by the implementation shown below. |
| `spoolCircumference` | `Length` | `Length` input consumed by the implementation shown below. |
| `gearing` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `SimWrapper` instance.

??? example "Implementation (source lines 65–70)"

    ```java
    public SimWrapper(ElevatorSim sim, Length spoolCircumference, double gearing) {
      updateConsumer = sim::update;
      voltageConsumer = (value) -> sim.setInput(0, value);
      positionSupplier = () -> (sim.getPositionMeters() / spoolCircumference.getMeters()) * gearing;
      velocitySupplier = () -> (sim.getVelocityMetersPerSecond() / spoolCircumference.getMeters()) * gearing;
    }
    ```

### `public SimWrapper(SingleJointedArmSim sim, double gearing)`

[Source lines 79–84](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L79)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Key collaborators/calls: `sim.setInput()`, `Units.radiansToRotations()`, `sim.getAngleRads()`, `sim.getVelocityRadPerSec()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `sim` | `SingleJointedArmSim` | `SingleJointedArmSim` input consumed by the implementation shown below. |
| `gearing` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `SimWrapper` instance.

??? example "Implementation (source lines 79–84)"

    ```java
    public SimWrapper(SingleJointedArmSim sim, double gearing) {
      updateConsumer = sim::update;
      voltageConsumer = (value) -> sim.setInput(0, value);
      positionSupplier = () -> Units.radiansToRotations(sim.getAngleRads()) * gearing;
      velocitySupplier = () -> Units.radiansToRotations(sim.getVelocityRadPerSec()) * gearing;
    }
    ```

### `public SimWrapper(FlywheelSim sim)`

[Source lines 92–97](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L92)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Key collaborators/calls: `sim.setInput()`, `sim.getAngularVelocityRPM()`, `sim.getGearing()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `sim` | `FlywheelSim` | `FlywheelSim` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `SimWrapper` instance.

??? example "Implementation (source lines 92–97)"

    ```java
    public SimWrapper(FlywheelSim sim) {
      updateConsumer = sim::update;
      voltageConsumer = (value) -> sim.setInput(0, value);
      positionSupplier = () -> 0.0;
      velocitySupplier = () -> (sim.getAngularVelocityRPM() / 60.0) * sim.getGearing();
    }
    ```

### `public SimWrapper(FlywheelSim sim, double gearing)`

[Source lines 106–111](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L106)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Key collaborators/calls: `sim.setInput()`, `sim.getAngularVelocityRPM()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `sim` | `FlywheelSim` | `FlywheelSim` input consumed by the implementation shown below. |
| `gearing` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `SimWrapper` instance.

??? example "Implementation (source lines 106–111)"

    ```java
    public SimWrapper(FlywheelSim sim, double gearing) {
      updateConsumer = sim::update;
      voltageConsumer = (value) -> sim.setInput(0, value);
      positionSupplier = () -> 0.0;
      velocitySupplier = () -> (sim.getAngularVelocityRPM() / 60.0) * gearing;
    }
    ```

### `public void update(double deltaTime)`

[Source lines 114–116](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L114)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `updateConsumer.accept()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `deltaTime` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 114–116)"

    ```java
    public void update(double deltaTime) {
      updateConsumer.accept(deltaTime);
    }
    ```

### `public void setInputVoltage(double inputVoltage)`

[Source lines 119–121](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L119)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `voltageConsumer.accept()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `inputVoltage` | `double` | Voltage value in volts. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 119–121)"

    ```java
    public void setInputVoltage(double inputVoltage) {
      voltageConsumer.accept(inputVoltage);
    }
    ```

### `public double getPosition()`

[Source lines 124–126](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L124)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `positionSupplier.getAsDouble()`.
- Key collaborators/calls: `positionSupplier.getAsDouble()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 124–126)"

    ```java
    public double getPosition() {
      return positionSupplier.getAsDouble();
    }
    ```

### `public double getVelocity()`

[Source lines 129–131](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L129)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `velocitySupplier.getAsDouble()`.
- Key collaborators/calls: `velocitySupplier.getAsDouble()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 129–131)"

    ```java
    public double getVelocity() {
      return velocitySupplier.getAsDouble();
    }
    ```

## Exposed fields and types

### `public class SimWrapper implements SimInterface`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimWrapper.java#L17)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
