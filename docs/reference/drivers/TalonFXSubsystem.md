# TalonFXSubsystem

`com.teamscreamrobotics.drivers.TalonFXSubsystem`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java) · **80 callables** · **81 exposed fields/types** · **3 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## How to use this subsystem base

`TalonFXSubsystem` owns one master TalonFX, optional followers, cached Phoenix status signals, control-request objects, configuration, goal state, telemetry, and simulation state. A mechanism subclass normally does **not** reimplement the motor loop. It supplies configuration and calls the appropriate setpoint method.

### 1. Build the configuration before construction

Create one `TalonFXSubsystemConfiguration` in the mechanism constants class. At minimum, set `name` and `masterConstants`. Then choose the mechanism ratio, neutral mode, current limits, PID slots, soft limits, Motion Magic values, and simulation constants that apply to that mechanism.

- `sensorToMechRatio` converts rotor sensor units into mechanism units.
- `rotorToSensorRatio` is used when a remote/feedback sensor has a separate ratio.
- `minUnitsLimit` and `maxUnitsLimit` become software limits when enabled.
- `slot0`, `slot1`, and `slot2` are Phoenix gains, commonly built through `ScreamPIDConstants`.
- `cruiseVelocity`, `acceleration`, and `jerk` configure Motion Magic.
- `codeEnabled`, `logTelemetry`, and `debugMode` control whether requests run and how much is logged.

The constructor copies these values into a `TalonFXConfiguration`, applies it to the master/followers, creates cached status signals, builds reusable control request objects, and registers simulation when configured. Configuration therefore needs to be complete **before** `super(config)` runs.

### 2. Choose one control path

| Intent | Method | Units/behavior |
| --- | --- | --- |
| Open-loop percent | `setDutyCycle(...)` | Duty cycle, normally `-1.0` to `1.0`, plus optional duty-cycle feedforward. |
| Direct voltage | `setVoltage(...)` | Volts, plus optional voltage feedforward. |
| Closed-loop position | `setSetpointPosition(...)` | Mechanism units after the configured sensor/mechanism ratios. |
| Motion Magic position | `setSetpointMotionMagicPosition(...)` | Mechanism units, using configured cruise velocity/acceleration/jerk. |
| Closed-loop velocity | `setSetpointVelocity(...)` | Mechanism units per second. |
| Motion Magic velocity | `setSetpointMotionMagicVelocity(...)` | Velocity target using Motion Magic velocity shaping. |
| Arbitrary Phoenix request | `setMaster(...)` / `applyControlCommand(...)` | Passes the supplied CTRE `ControlRequest` through directly. |

Each setpoint method updates the library's cached `setpoint`, marks whether velocity mode is active, fills the matching reusable CTRE request, and sends it through `setMaster`. `setMaster` is the final gate: it respects emergency-stop/code-enabled state before writing to hardware.

### 3. Use goals when the mechanism has named states

Implement `TalonFXSubsystemGoal` as an enum. `target()` supplies the live target, `controlType()` selects the request type, and `feedForward()` can supply a changing feedforward. `applyGoal(...)` switches on the goal's control type and dispatches to the corresponding setter. `applyGoalCommand(...)` wraps that work in a WPILib command for bindings and command groups.

### 4. Read state and determine completion

`getPosition()` and `getVelocity()` return mechanism-side values; rotor-specific accessors return rotor-side values. `getError()` subtracts measured position/velocity from the cached setpoint according to the current mode. `atGoal()` uses the configuration tolerance, while `atGoal(absTolerance)` lets the caller override it.

### 5. Safety, runtime reconfiguration, and simulation

- `stop()` sends a neutral request. `stopAll(...)` applies it to multiple SCREAMLib mechanisms.
- `emergencyStop()` latches the subsystem's emergency-stop flag and stops output; inspect `isActive()` before assuming later requests are accepted.
- Checked configuration mutators route Phoenix status through `ErrorChecker`; `Unchecked` variants skip that reporting and should be used only when the caller handles failure.
- `periodic()` refreshes cached signals, applies the active goal, and emits telemetry when enabled.
- `simulationPeriodic()` advances the configured `SimWrapper`; `setSimState(...)` pushes simulated position/velocity back to the subsystem and registered callback.

!!! warning "Units are configuration-dependent"
    Position and velocity setters use the mechanism units implied by the configured feedback ratios. Simulation backends also use different native units (for example meters for an elevator and rotations for a DC motor). Read the individual method's implementation notes below before mixing rotor, sensor, mechanism, or simulation values.


## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2026: Configure a TalonFX mechanism, PID slot, limits, and Motion Magic

[`src/main/java/frc2026/tars/subsystems/shooter/hood/HoodConstants.java` lines 20–48](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/hood/HoodConstants.java#L20-L48)

```java
public static final TalonFXSubsystemConfiguration HOOD_CONFIG =
    new TalonFXSubsystemConfiguration();

static {
  HOOD_CONFIG.name = "Hood";

  HOOD_CONFIG.codeEnabled = true;
  HOOD_CONFIG.logTelemetry = false;
  HOOD_CONFIG.debugMode = false;

  HOOD_CONFIG.masterConstants =
      new TalonFXConstants(new CANDevice(8), InvertedValue.Clockwise_Positive);

  HOOD_CONFIG.slot0 =
      new ScreamPIDConstants(90.0, 0, 0)
          .getSlot0Configs(new FeedforwardConstants(0, 0.0, 0.0, 0));

  // P: 55.0

  HOOD_CONFIG.neutralMode = NeutralModeValue.Brake;
  HOOD_CONFIG.sensorToMechRatio = HOOD_REDUCTION;
  HOOD_CONFIG.enableSupplyCurrentLimit = true;
  HOOD_CONFIG.supplyCurrentLimit = 15;

  HOOD_CONFIG.maxUnitsLimit = MAX_UNITS;

  HOOD_CONFIG.acceleration = 20.0;
  HOOD_CONFIG.cruiseVelocity = 30.0;
}
```

### 2026: Create a mechanism by subclassing TalonFXSubsystem

[`src/main/java/frc2026/tars/subsystems/shooter/hood/Hood.java` lines 1–50](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/hood/Hood.java#L1-L50)

```java
package frc2026.tars.subsystems.shooter.hood;

import com.teamscreamrobotics.drivers.TalonFXSubsystem;
import edu.wpi.first.math.geometry.Rotation2d;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.InstantCommand;
import edu.wpi.first.wpilibj2.command.SequentialCommandGroup;
import edu.wpi.first.wpilibj2.command.WaitUntilCommand;
import frc2026.tars.Robot;

public class Hood extends TalonFXSubsystem {
  public Hood(TalonFXSubsystemConfiguration config) {
    super(config);
    resetPosition(0);
  }

  public Command moveToAngleCommand(Rotation2d targetAngle) {
    return run(
        () -> {
          setSetpointMotionMagicPosition(targetAngle.getRotations());
        });
  }

  public void moveToAngle(Rotation2d targetAngle) {
    setSetpointMotionMagicPosition(targetAngle.getRotations());
  }

  private double startTime = 0.0;

  public Command zero() {

    return new SequentialCommandGroup(
        new InstantCommand(() -> startTime = Timer.getFPGATimestamp()),
        applyVoltageCommand(() -> -1.0)
            .withDeadline(
                new WaitUntilCommand(() -> ((Timer.getFPGATimestamp() - startTime) > 1.0))),
        new InstantCommand(() -> resetPosition(0)));
  }

  @Override
  public synchronized double getPosition() {
    return Robot.isSimulation() ? getSetpoint() : super.getPosition();
  }

  @Override
  public void periodic() {
    super.periodic();
  }
}
```

### 2025: Model semantic goals and apply them as commands (legacy package names)

[`src/main/java/frc2025/subsystems/superstructure/elevator/Elevator.java` lines 16–73](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/elevator/Elevator.java#L16-L73)

```java
public class Elevator extends TalonFXSubsystem {

  public Elevator(TalonFXSubsystemConfiguration config) {
    super(config, ElevatorGoal.FEED);

    resetPosition(0.0);
  }

  public enum ElevatorGoal implements TalonFXSubsystemGoal {
    HOME(Length.kZero),
    FEED(Length.kZero),
    TROUGH_FEED(Length.fromInches(13.0)),
    TROUGH(Length.fromInches(2.0)), // 2.0
    L2(Length.fromInches(24.5)),
    L3(Length.fromInches(40.5)),
    L4(Length.fromInches(64.8)),
    CLEAR_ALGAE_L1(Length.fromInches(14.1)),
    CLEAR_ALGAE_L2(Length.fromInches(29.611)),
    BARGE(Length.fromInches(70.203)),
    MAX(ElevatorConstants.MAX_HEIGHT);

    public Length height;
    public DoubleSupplier targetRotations;

    private ElevatorGoal(Length targetHeight) {
      this.height = targetHeight;
      this.targetRotations =
          () ->
              Conversions.linearDistanceToRotations(
                  targetHeight, ElevatorConstants.PULLEY_CIRCUMFERENCE);
    }

    @Override
    public ControlType controlType() {
      return ControlType.MOTION_MAGIC_POSITION;
    }

    @Override
    public DoubleSupplier target() {
      return targetRotations;
    }

    @Override
    public DoubleSupplier feedForward() {
      return () -> 0.0;
    }
  }

  @Override
  public synchronized Command applyGoalCommand(TalonFXSubsystemGoal goal) {
    return super.applyGoalCommand(goal).beforeStarting(() -> super.goal = goal);
  }

  public Command applyUntilAtGoalCommand(ElevatorGoal goal) {
    return super.applyGoalCommand(goal)
        .until(() -> atGoal())
        .beforeStarting(() -> super.goal = goal);
  }
```

## Public and protected callables

### `public CANDevice()`

[Source lines 83–85](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L83)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It delegates initialization to another constructor in the same type with `null, null`.

**Inputs:** None.

**Result:** Constructs and initializes a `CANDevice` instance.

??? example "Implementation (source lines 83–85)"

    ```java
    public CANDevice() {
      this(null, null);
    }
    ```

### `public CANDevice(Integer id)`

[Source lines 86–88](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L86)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It delegates initialization to another constructor in the same type with `id, ""`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | `Integer` | `Integer` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `CANDevice` instance.

??? example "Implementation (source lines 86–88)"

    ```java
    public CANDevice(Integer id){
      this(id, "");
    }
    ```

### `public TalonFXConstants()`

[Source lines 98–100](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L98)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It delegates initialization to another constructor in the same type with `null, null`.

**Inputs:** None.

**Result:** Constructs and initializes a `TalonFXConstants` instance.

??? example "Implementation (source lines 98–100)"

    ```java
    public TalonFXConstants() {
      this(null, null);
    }
    ```

### `DoubleSupplier target()`

[Source lines 112–112](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L112)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs:** None.

**Result:** Returns `DoubleSupplier`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 112)"

    ```java
    DoubleSupplier target();
    ```

### `ControlType controlType()`

[Source lines 114–114](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L114)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs:** None.

**Result:** Returns `ControlType`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 114)"

    ```java
    ControlType controlType();
    ```

### `default DoubleSupplier feedForward()`

[Source lines 116–118](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L116)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `() -> 0.0`.

**Inputs:** None.

**Result:** Returns `DoubleSupplier`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 116–118)"

    ```java
    default DoubleSupplier feedForward() {
      return () -> 0.0;
    }
    ```

### `public TalonFXSubsystemSimConstants(SimWrapper sim, double gearing, PIDController simController)`

[Source lines 127–129](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L127)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It delegates initialization to another constructor in the same type with `sim, gearing, new ProfiledPIDController(simController.getP(), simController.getI(), simController.getD(), new Constraints(Double.MAX_VALUE, Double.MAX_VALUE)), false, false`.
- Key collaborators/calls: `ProfiledPIDController()`, `simController.getP()`, `simController.getI()`, `simController.getD()`, `Constraints()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `sim` | `SimWrapper` | `SimWrapper` input consumed by the implementation shown below. |
| `gearing` | `double` | `double` input consumed by the implementation shown below. |
| `simController` | `PIDController` | `PIDController` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `TalonFXSubsystemSimConstants` instance.

??? example "Implementation (source lines 127–129)"

    ```java
    public TalonFXSubsystemSimConstants(SimWrapper sim, double gearing, PIDController simController) {
      this(sim, gearing, new ProfiledPIDController(simController.getP(), simController.getI(), simController.getD(), new Constraints(Double.MAX_VALUE, Double.MAX_VALUE)), false, false);
    }
    ```

### `public TalonFXSubsystemSimConstants(SimWrapper sim, double gearing, PIDController simController, double minInput, double maxInput)`

[Source lines 131–133](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L131)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It delegates initialization to another constructor in the same type with `sim, gearing, createContinuousController(simController, minInput, maxInput), false, false`.
- Key collaborators/calls: `createContinuousController()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `sim` | `SimWrapper` | `SimWrapper` input consumed by the implementation shown below. |
| `gearing` | `double` | `double` input consumed by the implementation shown below. |
| `simController` | `PIDController` | `PIDController` input consumed by the implementation shown below. |
| `minInput` | `double` | `double` input consumed by the implementation shown below. |
| `maxInput` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `TalonFXSubsystemSimConstants` instance.

??? example "Implementation (source lines 131–133)"

    ```java
    public TalonFXSubsystemSimConstants(SimWrapper sim, double gearing, PIDController simController, double minInput, double maxInput) {
      this(sim, gearing, createContinuousController(simController, minInput, maxInput), false, false);
    }
    ```

### `public DoubleSupplier target()`

[Source lines 248–250](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L248)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `() -> 0.0`.

**Inputs:** None.

**Result:** Returns `DoubleSupplier`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 248–250)"

    ```java
    public DoubleSupplier target() {
      return () -> 0.0;
    }
    ```

### `public ControlType controlType()`

[Source lines 253–255](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L253)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `ControlType.VOLTAGE`.

**Inputs:** None.

**Result:** Returns `ControlType`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 253–255)"

    ```java
    public ControlType controlType() {
      return ControlType.VOLTAGE;
    }
    ```

### `public TalonFXSubsystem( final TalonFXSubsystemConfiguration config, final TalonFXSubsystemGoal defaultGoal)`

[Source lines 263–396](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L263)

**Detailed behavior**

- The implementation executes 107 non-blank source lines.
- It changes object/subclass state through `cancoder`, `config`, `dutyCycleRequest`, `forwardSoftLimitRotations`, `goal`, `logPrefix`, `master`, `masterConfig`, `masterPositionSignal`, `masterRotorPositionSignal`, `masterRotorVelocitySignal`, `masterVelocitySignal`, `motionMagicPositionRequest`, `motionMagicVelocityRequest`, `positionRequest`, `reverseSoftLimitRotations`, `sim`, `simController`, `simFeedforwardSup`, `simulating`, `simulationThread`, `slaveConfigs`, `slaves`, `velocityRequest`, `voltageRequest`.
- It issues a CTRE control request to the master motor; calling it can immediately change actuator output.
- It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.
- It has 8 conditional paths: `config.forceSimulation && config.simConstants == null`; `config.cancoderConstants != null`; `config.maxUnitsLimit != null` plus 5 more.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `DriverStation.reportError()`, `Utils.isSimulation()`, `TalonFX()`, `CANcoder()`, `DeviceConfig.configureCANcoder()`, `TalonFXConfiguration()`, `slave.setControl()`, `Follower()`, `configSlave()`, `configMaster()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `config` | `TalonFXSubsystemConfiguration` | `TalonFXSubsystemConfiguration` input consumed by the implementation shown below. |
| `defaultGoal` | `TalonFXSubsystemGoal` | `TalonFXSubsystemGoal` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `TalonFXSubsystem` instance.

??? example "Implementation (source lines 263–396)"

    ```java
    public TalonFXSubsystem(
        final TalonFXSubsystemConfiguration config, final TalonFXSubsystemGoal defaultGoal) {
      this.config = config;
      if (config.forceSimulation && config.simConstants == null) {
        DriverStation.reportError(
            "Could not force simulation in " + config.name + ", simulation constants were not provided",
            true);
      }
      this.simulating = (Utils.isSimulation() && config.simConstants != null) || config.forceSimulation;
      master =
          new TalonFX(config.masterConstants.device.id, config.masterConstants.device.canbus);
      slaves = new TalonFX[config.slaveConstants.length];
      slaveConfigs = new TalonFXConfiguration[config.slaveConstants.length];
      if (config.cancoderConstants != null) {
        cancoder =
            new CANcoder(
                config.cancoderConstants.device.id, config.cancoderConstants.device.canbus);
        CANcoderConfiguration cancoderConfig = config.cancoderConstants.config;
        DeviceConfig.configureCANcoder(config.name + " CANcoder", cancoder, cancoderConfig);
      }
    
      masterConfig = new TalonFXConfiguration();
    
      masterConfig.Feedback.FeedbackSensorSource = config.feedbackSensorSource;
      masterConfig.Feedback.FeedbackRemoteSensorID = config.feedbackRemoteSensorId;
      masterConfig.Feedback.FeedbackRotorOffset = config.feedbackRotorOffset;
    
      masterConfig.ClosedLoopGeneral.ContinuousWrap = config.continuousWrap;
    
      if(config.maxUnitsLimit != null){
        forwardSoftLimitRotations = (config.maxUnitsLimit - config.softLimitDeadband);
        masterConfig.SoftwareLimitSwitch.ForwardSoftLimitThreshold = forwardSoftLimitRotations;
        masterConfig.SoftwareLimitSwitch.ForwardSoftLimitEnable = true;
      }
    
      if(config.minUnitsLimit != null){
        reverseSoftLimitRotations = (config.minUnitsLimit + config.softLimitDeadband);
        masterConfig.SoftwareLimitSwitch.ReverseSoftLimitThreshold = reverseSoftLimitRotations;
        masterConfig.SoftwareLimitSwitch.ReverseSoftLimitEnable = true;
      }
    
      masterConfig.Slot0 = config.slot0;
      masterConfig.Slot1 = config.slot1;
      masterConfig.Slot2 = config.slot2;
    
      masterConfig.MotionMagic.MotionMagicCruiseVelocity = config.cruiseVelocity;
      masterConfig.MotionMagic.MotionMagicAcceleration = config.acceleration;
      masterConfig.MotionMagic.MotionMagicJerk = config.jerk;
    
      masterConfig.OpenLoopRamps.DutyCycleOpenLoopRampPeriod = config.rampRate;
      masterConfig.OpenLoopRamps.VoltageOpenLoopRampPeriod = config.rampRate;
      masterConfig.OpenLoopRamps.TorqueOpenLoopRampPeriod = config.rampRate;
    
      masterConfig.CurrentLimits.SupplyCurrentLimit = config.supplyCurrentLimit;
      masterConfig.CurrentLimits.SupplyCurrentLimitEnable = config.enableSupplyCurrentLimit;
      masterConfig.CurrentLimits.StatorCurrentLimit = config.statorCurrentLimit;
      masterConfig.CurrentLimits.StatorCurrentLimitEnable = config.enableStatorCurrentLimit;
    
      masterConfig.MotorOutput.Inverted = config.masterConstants.invert;
      masterConfig.Feedback.SensorToMechanismRatio = config.sensorToMechRatio;
      masterConfig.Feedback.RotorToSensorRatio = config.rotorToSensorRatio;
      masterConfig.MotorOutput.NeutralMode = config.neutralMode;
    
      masterConfig.TorqueCurrent.PeakForwardTorqueCurrent = config.peakForwardTorqueCurrent;
      masterConfig.TorqueCurrent.PeakReverseTorqueCurrent = config.peakReverseTorqueCurrent;
    
      for (int i = 0; i < slaves.length; ++i) {
        slaves[i] =
            new TalonFX(
                config.slaveConstants[i].device.id, config.slaveConstants[i].device.canbus);
    
        TalonFX slave = slaves[i];
        TalonFXConfiguration slaveConfig = new TalonFXConfiguration();
    
        slaveConfig.MotorOutput.Inverted = config.slaveConstants[i].invert;
        slaveConfig.MotorOutput.NeutralMode = config.neutralMode;
        if(config.slavesAsFollower){
          slave.setControl(
            new Follower(
              config.masterConstants.device.id,
              (config.slaveConstants[i].invert != config.masterConstants.invert) ? MotorAlignmentValue.Opposed : MotorAlignmentValue.Aligned));
        }
    
        configSlave(slave, slaveConfig);
      }
    
      configMaster(masterConfig);
    
      dutyCycleRequest = new DutyCycleOut(0.0);
      voltageRequest = new VoltageOut(0.0);
      positionRequest = new PositionVoltage(0.0);
      motionMagicPositionRequest = new MotionMagicVoltage(0.0);
      velocityRequest = new VelocityVoltage(0.0);
      motionMagicVelocityRequest = new MotionMagicVelocityVoltage(0.0);
    
      master.getRotorPosition().setUpdateFrequency(25.0);
      master.getRotorVelocity().setUpdateFrequency(25.0);
      master.getPosition().setUpdateFrequency(100.0);
      master.getVelocity().setUpdateFrequency(100.0);
    
      masterPositionSignal = master.getPosition();
      masterVelocitySignal = master.getVelocity();
      masterRotorPositionSignal = master.getRotorPosition();
      masterRotorVelocitySignal = master.getRotorVelocity();
    
      if (shouldSimulate()) {
        sim = config.simConstants.sim();
        simulationThread =
            new SimulationThread(
                config.simConstants,
                this::setSimState,
                config.simPeriodSec,
                config.name + " Sim Thread");
        simController = config.simConstants.simController();
        simFeedforwardSup = () -> 0.0;
      }
    
      if(defaultGoal != null){
        goal = defaultGoal;
        setDefaultCommand(applyGoalCommand(goal));
      }
    
      logPrefix = config.logPrefix != null ? config.logPrefix : "Subsystems/" + config.name + "/";
    
      if(config.debugMode && shouldSimulate()){
        SmartDashboard.putNumber(config.name + " kP", simController.getP());
        SmartDashboard.putNumber(config.name + " kI", simController.getI());
        SmartDashboard.putNumber(config.name + " kD", simController.getD());
        SmartDashboard.putNumber(config.name + " Velocity", simController.getConstraints().maxVelocity); 
        SmartDashboard.putNumber(config.name + " Acceleration", simController.getConstraints().maxAcceleration);
      }
    
      System.out.println("[Init] " + config.name + " initialization complete!");
    }
    ```

### `public TalonFXSubsystem(TalonFXSubsystemConfiguration config)`

[Source lines 398–400](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L398)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It delegates initialization to another constructor in the same type with `config, null`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `config` | `TalonFXSubsystemConfiguration` | `TalonFXSubsystemConfiguration` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `TalonFXSubsystem` instance.

??? example "Implementation (source lines 398–400)"

    ```java
    public TalonFXSubsystem(TalonFXSubsystemConfiguration config){
      this(config, null);
    }
    ```

### `public void configMaster(TalonFXConfiguration motorConfig)`

[Source lines 407–409](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L407)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `DeviceConfig.configureTalonFX()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `motorConfig` | `TalonFXConfiguration` | - The config to apply to the master. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 407–409)"

    ```java
    public void configMaster(TalonFXConfiguration motorConfig) {
      DeviceConfig.configureTalonFX(config.name + " Master", master, motorConfig);
    }
    ```

??? note "Author note from JavaDoc"

    Configures the master motor with the given configuration.
    
    **Parameter `motorConfig`:** - The config to apply to the master.

### `public void configSlave(TalonFX slave, TalonFXConfiguration motorConfig)`

[Source lines 417–419](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L417)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `DeviceConfig.configureTalonFX()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `slave` | `TalonFX` | - The slave to apply the config to. **Parameter `motorConfig`:** - The config to apply to the slave. |
| `motorConfig` | `TalonFXConfiguration` | - The config to apply to the slave. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 417–419)"

    ```java
    public void configSlave(TalonFX slave, TalonFXConfiguration motorConfig) {
      DeviceConfig.configureTalonFX(config.name + " Slave", slave, motorConfig);
    }
    ```

??? note "Author note from JavaDoc"

    Configures a slave motor with the given configuration.
    
    **Parameter `slave`:** - The slave to apply the config to.
    **Parameter `motorConfig`:** - The config to apply to the slave.

### `public void setStatorCurrentLimit(double currentLimit, boolean enable)`

[Source lines 427–434](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L427)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- Return path: `conf`.
- Key collaborators/calls: `changeTalonConfig()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `currentLimit` | `double` | - Stator current limit to apply. **Parameter `enable`:** - Whether the current limit should be enabled. |
| `enable` | `boolean` | - Whether the current limit should be enabled. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 427–434)"

    ```java
    public void setStatorCurrentLimit(double currentLimit, boolean enable) {
      changeTalonConfig(
          (conf) -> {
            conf.CurrentLimits.StatorCurrentLimit = currentLimit;
            conf.CurrentLimits.StatorCurrentLimitEnable = enable;
            return conf;
          });
    }
    ```

??? note "Author note from JavaDoc"

    Reconfigures the motors with the given stator current limits.
    
    **Parameter `currentLimit`:** - Stator current limit to apply.
    **Parameter `enable`:** - Whether the current limit should be enabled.

### `public void enableSoftLimits(boolean enable)`

[Source lines 441–448](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L441)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- Return path: `conf`.
- Key collaborators/calls: `changeTalonConfig()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `enable` | `boolean` | - Whether the soft limits should be enabled. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 441–448)"

    ```java
    public void enableSoftLimits(boolean enable) {
      changeTalonConfig(
          (conf) -> {
            conf.SoftwareLimitSwitch.ForwardSoftLimitEnable = enable;
            conf.SoftwareLimitSwitch.ReverseSoftLimitEnable = enable;
            return conf;
          });
    }
    ```

??? note "Author note from JavaDoc"

    Reconfigures the motors to enable soft limits.
    
    **Parameter `enable`:** - Whether the soft limits should be enabled.

### `public void setNeutralMode(NeutralModeValue mode)`

[Source lines 455–460](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L455)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `mode` | `NeutralModeValue` | - The neutral mode to apply to the motors. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 455–460)"

    ```java
    public void setNeutralMode(NeutralModeValue mode) {
      master.setNeutralMode(mode);
      for (TalonFX slave : slaves) {
        slave.setNeutralMode(mode);
      }
    }
    ```

??? note "Author note from JavaDoc"

    Sets the neutral mode of the motors.
    
    **Parameter `mode`:** - The neutral mode to apply to the motors.

### `public synchronized void setSupplyCurrentLimit(double value, boolean enable)`

[Source lines 462–467](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L462)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Key collaborators/calls: `configMaster()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | `double` | `double` input consumed by the implementation shown below. |
| `enable` | `boolean` | Enables the behavior when `true`; disables it when `false`. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 462–467)"

    ```java
    public synchronized void setSupplyCurrentLimit(double value, boolean enable) {
      masterConfig.CurrentLimits.SupplyCurrentLimit = value;
      masterConfig.CurrentLimits.SupplyCurrentLimitEnable = enable;
    
      configMaster(masterConfig);
    }
    ```

### `public synchronized void setSupplyCurrentLimitUnchecked(double value, boolean enable)`

[Source lines 469–474](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L469)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It interacts with a Phoenix device configurator; this can perform CAN configuration I/O and report vendor status codes.
- Key collaborators/calls: `master.getConfigurator()`, `apply()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | `double` | `double` input consumed by the implementation shown below. |
| `enable` | `boolean` | Enables the behavior when `true`; disables it when `false`. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 469–474)"

    ```java
    public synchronized void setSupplyCurrentLimitUnchecked(double value, boolean enable) {
      masterConfig.CurrentLimits.SupplyCurrentLimit = value;
      masterConfig.CurrentLimits.SupplyCurrentLimitEnable = enable;
    
      master.getConfigurator().apply(masterConfig);
    }
    ```

### `public synchronized void setStatorCurrentLimitUnchecked(double value, boolean enable)`

[Source lines 476–481](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L476)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It interacts with a Phoenix device configurator; this can perform CAN configuration I/O and report vendor status codes.
- Key collaborators/calls: `master.getConfigurator()`, `apply()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | `double` | `double` input consumed by the implementation shown below. |
| `enable` | `boolean` | Enables the behavior when `true`; disables it when `false`. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 476–481)"

    ```java
    public synchronized void setStatorCurrentLimitUnchecked(double value, boolean enable) {
      masterConfig.CurrentLimits.StatorCurrentLimit = value;
      masterConfig.CurrentLimits.StatorCurrentLimitEnable = enable;
    
      master.getConfigurator().apply(masterConfig);
    }
    ```

### `public synchronized void setMotionMagicConfigsUnchecked(MotionMagicConstants configs)`

[Source lines 483–489](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L483)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It interacts with a Phoenix device configurator; this can perform CAN configuration I/O and report vendor status codes.
- Key collaborators/calls: `configs.acceleration()`, `configs.jerk()`, `configs.cruiseVelocity()`, `master.getConfigurator()`, `apply()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `configs` | `MotionMagicConstants` | `MotionMagicConstants` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 483–489)"

    ```java
    public synchronized void setMotionMagicConfigsUnchecked(MotionMagicConstants configs) {
      masterConfig.MotionMagic.MotionMagicAcceleration = configs.acceleration();
      masterConfig.MotionMagic.MotionMagicJerk = configs.jerk();
      masterConfig.MotionMagic.MotionMagicCruiseVelocity = configs.cruiseVelocity();
    
      master.getConfigurator().apply(masterConfig.MotionMagic);
    }
    ```

### `public synchronized void setMotionMagicConfigs(MotionMagicConstants configs)`

[Source lines 491–497](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L491)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Key collaborators/calls: `configs.acceleration()`, `configs.jerk()`, `configs.cruiseVelocity()`, `configMaster()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `configs` | `MotionMagicConstants` | `MotionMagicConstants` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 491–497)"

    ```java
    public synchronized void setMotionMagicConfigs(MotionMagicConstants configs) {
      masterConfig.MotionMagic.MotionMagicAcceleration = configs.acceleration();
      masterConfig.MotionMagic.MotionMagicJerk = configs.jerk();
      masterConfig.MotionMagic.MotionMagicCruiseVelocity = configs.cruiseVelocity();
    
      configMaster(masterConfig);
    }
    ```

### `public void changeTalonConfig(UnaryOperator&lt;TalonFXConfiguration&gt; configChanger)`

[Source lines 499–505](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L499)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It changes object/subclass state through `masterConfig`.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `configChanger.apply()`, `writeConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `configChanger` | `UnaryOperator&lt;TalonFXConfiguration&gt;` | `UnaryOperator<TalonFXConfiguration>` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 499–505)"

    ```java
    public void changeTalonConfig(UnaryOperator<TalonFXConfiguration> configChanger) {
      for (int i = 0; i < slaves.length; ++i) {
        slaveConfigs[i] = configChanger.apply(slaveConfigs[i]);
      }
      masterConfig = configChanger.apply(masterConfig);
      writeConfigs();
    }
    ```

### `public void writeConfigs()`

[Source lines 507–514](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L507)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `configSlave()`, `configMaster()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 507–514)"

    ```java
    public void writeConfigs() {
      for (int i = 0; i < slaves.length; ++i) {
        TalonFX slave = slaves[i];
        TalonFXConfiguration slaveConfig = slaveConfigs[i];
        configSlave(slave, slaveConfig);
      }
      configMaster(masterConfig);
    }
    ```

### `protected boolean shouldSimulate()`

[Source lines 516–518](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L516)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `simulating`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 516–518)"

    ```java
    protected boolean shouldSimulate() {
      return simulating;
    }
    ```

### `public synchronized ControlModeValue getControlMode()`

[Source lines 520–522](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L520)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `master.getControlMode().getValue()`.
- Key collaborators/calls: `getValue()`.

**Inputs:** None.

**Result:** Returns `ControlModeValue`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 520–522)"

    ```java
    public synchronized ControlModeValue getControlMode() {
      return master.getControlMode().getValue();
    }
    ```

### `public synchronized double getRotorPosition()`

[Source lines 524–526](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L524)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `shouldSimulate() ? simPosition : masterRotorPositionSignal.refresh().getValueAsDouble()`.
- Key collaborators/calls: `shouldSimulate()`, `masterRotorPositionSignal.refresh()`, `getValueAsDouble()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 524–526)"

    ```java
    public synchronized double getRotorPosition() {
      return shouldSimulate() ? simPosition : masterRotorPositionSignal.refresh().getValueAsDouble();
    }
    ```

### `public synchronized double getPosition()`

[Source lines 528–530](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L528)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `shouldSimulate() ? simPosition / config.simConstants.gearing : masterPositionSignal.refresh().getValueAsDouble()`.
- Key collaborators/calls: `shouldSimulate()`, `masterPositionSignal.refresh()`, `getValueAsDouble()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 528–530)"

    ```java
    public synchronized double getPosition() {
      return shouldSimulate() ? simPosition / config.simConstants.gearing  : masterPositionSignal.refresh().getValueAsDouble();
    }
    ```

### `public synchronized double getRotorVelocity()`

[Source lines 532–534](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L532)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `shouldSimulate() ? simVelocity : masterRotorVelocitySignal.refresh().getValueAsDouble()`.
- Key collaborators/calls: `shouldSimulate()`, `masterRotorVelocitySignal.refresh()`, `getValueAsDouble()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 532–534)"

    ```java
    public synchronized double getRotorVelocity() {
      return shouldSimulate() ? simVelocity : masterRotorVelocitySignal.refresh().getValueAsDouble();
    }
    ```

### `public synchronized double getVelocity()`

[Source lines 536–538](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L536)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `shouldSimulate() ? simVelocity / config.simConstants.gearing : masterVelocitySignal.refresh().getValueAsDouble()`.
- Key collaborators/calls: `shouldSimulate()`, `masterVelocitySignal.refresh()`, `getValueAsDouble()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 536–538)"

    ```java
    public synchronized double getVelocity() {
      return shouldSimulate() ? simVelocity / config.simConstants.gearing : masterVelocitySignal.refresh().getValueAsDouble();
    }
    ```

### `public synchronized double getSetpoint()`

[Source lines 540–542](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L540)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `setpoint`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 540–542)"

    ```java
    public synchronized double getSetpoint() {
      return setpoint;
    }
    ```

### `public synchronized TalonFXSubsystemGoal getGoal()`

[Source lines 544–546](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L544)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `goal`.

**Inputs:** None.

**Result:** Returns `TalonFXSubsystemGoal`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 544–546)"

    ```java
    public synchronized TalonFXSubsystemGoal getGoal() {
      return goal;
    }
    ```

### `public synchronized double getError()`

[Source lines 548–558](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L548)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- It has 1 conditional path: `goal != null`.
- Return paths: `inVelocityMode ? goal.target().getAsDouble() - getVelocity() : goal.target().getAsDouble() - getPosition()`; `inVelocityMode ? setpoint - getVelocity() : setpoint - getPosition()`.
- Key collaborators/calls: `goal.target()`, `getAsDouble()`, `getVelocity()`, `getPosition()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 548–558)"

    ```java
    public synchronized double getError() {
      if(goal != null){
        return inVelocityMode
        ? goal.target().getAsDouble() - getVelocity()
        : goal.target().getAsDouble() - getPosition();
      } else {
        return inVelocityMode
        ? setpoint - getVelocity()
        : setpoint - getPosition();
      }
    }
    ```

### `public synchronized Rotation2d getAngle()`

[Source lines 560–562](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L560)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `Rotation2d.fromRotations(getPosition())`.
- Key collaborators/calls: `Rotation2d.fromRotations()`, `getPosition()`.

**Inputs:** None.

**Result:** Returns `Rotation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 560–562)"

    ```java
    public synchronized Rotation2d getAngle() {
      return Rotation2d.fromRotations(getPosition());
    }
    ```

### `public synchronized boolean atGoal()`

[Source lines 564–572](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L564)

**Detailed behavior**

- The implementation executes 7 non-blank source lines.
- Return path: `inVelocityMode ? Math.abs(error) <= config.velocityThreshold : Math.abs(error) <= config.positionThreshold`.
- Key collaborators/calls: `goal.target()`, `getAsDouble()`, `getVelocity()`, `getPosition()`, `Math.abs()`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 564–572)"

    ```java
    public synchronized boolean atGoal() {
      double error =
          inVelocityMode
              ? goal.target().getAsDouble() - getVelocity()
              : goal.target().getAsDouble() - getPosition();
      return inVelocityMode
          ? Math.abs(error) <= config.velocityThreshold
          : Math.abs(error) <= config.positionThreshold;
    }
    ```

### `public synchronized boolean atGoal(double absTolerance)`

[Source lines 574–580](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L574)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `Math.abs(error) <= absTolerance`.
- Key collaborators/calls: `goal.target()`, `getAsDouble()`, `getVelocity()`, `getPosition()`, `Math.abs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `absTolerance` | `double` | Allowed absolute error around the target. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 574–580)"

    ```java
    public synchronized boolean atGoal(double absTolerance) {
      double error =
          inVelocityMode
              ? goal.target().getAsDouble() - getVelocity()
              : goal.target().getAsDouble() - getPosition();
      return Math.abs(error) <= absTolerance;
    }
    ```

### `public synchronized boolean isActive()`

[Source lines 582–584](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L582)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `Math.abs(getRotorVelocity()) > 0.0`.
- Key collaborators/calls: `Math.abs()`, `getRotorVelocity()`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 582–584)"

    ```java
    public synchronized boolean isActive() {
      return Math.abs(getRotorVelocity()) > 0.0;
    }
    ```

### `public synchronized Command applyGoalCommand(TalonFXSubsystemGoal goal)`

[Source lines 586–589](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L586)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `run(() -> applyGoal(goal)).beforeStarting(Commands.runOnce(() -> simController.reset(getPosition(), getVelocity())).onlyIf(() -> shouldSimulate()) ).withName(config.name + " Apply…`.
- Key collaborators/calls: `run()`, `applyGoal()`, `beforeStarting()`, `Commands.runOnce()`, `simController.reset()`, `getPosition()`, `getVelocity()`, `onlyIf()`, `shouldSimulate()`, `withName()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `goal` | `TalonFXSubsystemGoal` | `TalonFXSubsystemGoal` input consumed by the implementation shown below. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 586–589)"

    ```java
    public synchronized Command applyGoalCommand(TalonFXSubsystemGoal goal) {
      return run(() -> applyGoal(goal)).beforeStarting(Commands.runOnce(() -> simController.reset(getPosition(), getVelocity())).onlyIf(() -> shouldSimulate())
      ).withName(config.name + " Apply Goal " + goal.toString());
    }
    ```

### `public synchronized void applyGoal(TalonFXSubsystemGoal goal)`

[Source lines 591–616](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L591)

**Detailed behavior**

- The implementation executes 24 non-blank source lines.
- It changes object/subclass state through `goal`.
- Key collaborators/calls: `goal.controlType()`, `setSetpointMotionMagicPosition()`, `goal.target()`, `getAsDouble()`, `goal.feedForward()`, `setSetpointMotionMagicVelocity()`, `setSetpointPosition()`, `setSetpointVelocity()`, `setVoltage()`, `setDutyCycle()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `goal` | `TalonFXSubsystemGoal` | `TalonFXSubsystemGoal` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 591–616)"

    ```java
    public synchronized void applyGoal(TalonFXSubsystemGoal goal) {
      this.goal = goal;
      switch (goal.controlType()) {
        case MOTION_MAGIC_POSITION:
          setSetpointMotionMagicPosition(goal.target().getAsDouble(), goal.feedForward().getAsDouble());
          break;
        case MOTION_MAGIC_VELOCITY:
          setSetpointMotionMagicVelocity(goal.target().getAsDouble(), goal.feedForward().getAsDouble());
          break;
        case POSITION:
          setSetpointPosition(goal.target().getAsDouble(), goal.feedForward().getAsDouble());
          break;
        case VELOCITY:
          setSetpointVelocity(goal.target().getAsDouble(), goal.feedForward().getAsDouble());
          break;
        case VOLTAGE:
          setVoltage(goal.target().getAsDouble(), goal.feedForward().getAsDouble());
          break;
        case DUTY_CYCLE:
          setDutyCycle(goal.target().getAsDouble(), goal.feedForward().getAsDouble());
          break;
        default:
          stop();
          break;
      }
    }
    ```

### `public synchronized Command applyVoltageCommand(DoubleSupplier voltage)`

[Source lines 618–620](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L618)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `run(() -> setVoltage(voltage.getAsDouble())).withName("applyVoltage")`.
- Key collaborators/calls: `run()`, `setVoltage()`, `voltage.getAsDouble()`, `withName()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `voltage` | `DoubleSupplier` | Voltage value in volts. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 618–620)"

    ```java
    public synchronized Command applyVoltageCommand(DoubleSupplier voltage) {
      return run(() -> setVoltage(voltage.getAsDouble())).withName("applyVoltage");
    }
    ```

### `public synchronized Command applyVoltageCommand( DoubleSupplier voltage, DoubleSupplier voltageFeedforward)`

[Source lines 622–626](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L622)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `run(() -> setVoltage(voltage.getAsDouble(), voltageFeedforward.getAsDouble())) .withName("applyVoltage")`.
- Key collaborators/calls: `run()`, `setVoltage()`, `voltage.getAsDouble()`, `voltageFeedforward.getAsDouble()`, `withName()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `voltage` | `DoubleSupplier` | Voltage value in volts. |
| `voltageFeedforward` | `DoubleSupplier` | Voltage value in volts. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 622–626)"

    ```java
    public synchronized Command applyVoltageCommand(
        DoubleSupplier voltage, DoubleSupplier voltageFeedforward) {
      return run(() -> setVoltage(voltage.getAsDouble(), voltageFeedforward.getAsDouble()))
          .withName("applyVoltage");
    }
    ```

### `public synchronized Command applyControlCommand(ControlRequest control)`

[Source lines 628–630](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L628)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It issues a CTRE control request to the master motor; calling it can immediately change actuator output.
- Return path: `run(() -> setMaster(control)).withName("applyControl")`.
- Key collaborators/calls: `run()`, `setMaster()`, `withName()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `control` | `ControlRequest` | `ControlRequest` input consumed by the implementation shown below. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 628–630)"

    ```java
    public synchronized Command applyControlCommand(ControlRequest control){
      return run(() -> setMaster(control)).withName("applyControl");
    }
    ```

### `public synchronized void setDutyCycle(double dutyCycle, double dutyCycleFeedforward)`

[Source lines 632–637](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L632)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It issues a CTRE control request to the master motor; calling it can immediately change actuator output.
- It has 1 conditional path: `shouldSimulate(`.
- Key collaborators/calls: `setMaster()`, `dutyCycleRequest.withOutput()`, `shouldSimulate()`, `simulationThread.setSimVoltage()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `dutyCycle` | `double` | `double` input consumed by the implementation shown below. |
| `dutyCycleFeedforward` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 632–637)"

    ```java
    public synchronized void setDutyCycle(double dutyCycle, double dutyCycleFeedforward) {
      setMaster(dutyCycleRequest.withOutput(dutyCycle + dutyCycleFeedforward));
      if(shouldSimulate()){
        simulationThread.setSimVoltage(() -> (dutyCycle * 12) + dutyCycleFeedforward);
      }
    }
    ```

### `public synchronized void setDutyCycle(double dutyCycle)`

[Source lines 639–641](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L639)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `dutyCycle` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 639–641)"

    ```java
    public synchronized void setDutyCycle(double dutyCycle) {
      setDutyCycle(dutyCycle, 0);
    }
    ```

### `public synchronized void setVoltage(double volts, double voltageFeedForward)`

[Source lines 643–648](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L643)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It issues a CTRE control request to the master motor; calling it can immediately change actuator output.
- It has 1 conditional path: `shouldSimulate(`.
- Key collaborators/calls: `setMaster()`, `voltageRequest.withOutput()`, `shouldSimulate()`, `simulationThread.setSimVoltage()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `volts` | `double` | Voltage value in volts. |
| `voltageFeedForward` | `double` | Voltage value in volts. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 643–648)"

    ```java
    public synchronized void setVoltage(double volts, double voltageFeedForward) {
      setMaster(voltageRequest.withOutput(volts + voltageFeedForward));
      if (shouldSimulate()) {
        simulationThread.setSimVoltage(() -> volts + voltageFeedForward);
      }
    }
    ```

### `public synchronized void setVoltage(double volts)`

[Source lines 650–652](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L650)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `volts` | `double` | Voltage value in volts. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 650–652)"

    ```java
    public synchronized void setVoltage(double volts) {
      setVoltage(volts, 0.0);
    }
    ```

### `public synchronized void setSetpointPosition(double position, double voltageFeedForward)`

[Source lines 654–656](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L654)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setTargetPosition()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `position` | `double` | Position in the units required by this API and configuration. |
| `voltageFeedForward` | `double` | Voltage value in volts. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 654–656)"

    ```java
    public synchronized void setSetpointPosition(double position, double voltageFeedForward) {
      setTargetPosition(position, voltageFeedForward, false);
    }
    ```

### `public synchronized void setSetpointPosition(double position)`

[Source lines 658–660](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L658)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `position` | `double` | Position in the units required by this API and configuration. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 658–660)"

    ```java
    public synchronized void setSetpointPosition(double position) {
      setSetpointPosition(position, 0.0);
    }
    ```

### `public synchronized void setSetpointMotionMagicPosition( double position, double voltageFeedForward)`

[Source lines 662–665](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L662)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setTargetPosition()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `position` | `double` | Position in the units required by this API and configuration. |
| `voltageFeedForward` | `double` | Voltage value in volts. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 662–665)"

    ```java
    public synchronized void setSetpointMotionMagicPosition(
        double position, double voltageFeedForward) {
      setTargetPosition(position, voltageFeedForward, true);
    }
    ```

### `public synchronized void setSetpointMotionMagicPosition(double position)`

[Source lines 667–669](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L667)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `position` | `double` | Position in the units required by this API and configuration. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 667–669)"

    ```java
    public synchronized void setSetpointMotionMagicPosition(double position) {
      setSetpointMotionMagicPosition(position, 0.0);
    }
    ```

### `public synchronized void setSetpointVelocity(double velocity, double voltageFeedForward)`

[Source lines 671–673](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L671)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setTargetVelocity()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `velocity` | `double` | Velocity/speed in the units required by this API and configuration. |
| `voltageFeedForward` | `double` | Voltage value in volts. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 671–673)"

    ```java
    public synchronized void setSetpointVelocity(double velocity, double voltageFeedForward) {
      setTargetVelocity(velocity, voltageFeedForward, false);
    }
    ```

### `public synchronized void setSetpointVelocity(double velocity)`

[Source lines 675–677](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L675)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `velocity` | `double` | Velocity/speed in the units required by this API and configuration. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 675–677)"

    ```java
    public synchronized void setSetpointVelocity(double velocity) {
      setSetpointVelocity(velocity, 0.0);
    }
    ```

### `public synchronized void setSetpointMotionMagicVelocity( double velocity, double voltageFeedForward)`

[Source lines 679–682](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L679)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `setTargetVelocity()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `velocity` | `double` | Velocity/speed in the units required by this API and configuration. |
| `voltageFeedForward` | `double` | Voltage value in volts. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 679–682)"

    ```java
    public synchronized void setSetpointMotionMagicVelocity(
        double velocity, double voltageFeedForward) {
      setTargetVelocity(velocity, voltageFeedForward, true);
    }
    ```

### `public synchronized void setSetpointMotionMagicVelocity(double velocity)`

[Source lines 684–686](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L684)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `velocity` | `double` | Velocity/speed in the units required by this API and configuration. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 684–686)"

    ```java
    public synchronized void setSetpointMotionMagicVelocity(double velocity) {
      setSetpointMotionMagicVelocity(velocity, 0.0);
    }
    ```

### `public synchronized void setMaster(ControlRequest control)`

[Source lines 716–725](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L716)

**Detailed behavior**

- The implementation executes 8 non-blank source lines.
- It issues a CTRE control request to the master motor; calling it can immediately change actuator output.
- It has 2 conditional paths: `config.codeEnabled && !isEStopped`; `!config.slavesAsFollower`.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `master.setControl()`, `slave.setControl()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `control` | `ControlRequest` | `ControlRequest` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 716–725)"

    ```java
    public synchronized void setMaster(ControlRequest control) {
      if (config.codeEnabled && !isEStopped) {
        master.setControl(control);
        if(!config.slavesAsFollower){
          for(TalonFX slave : slaves){
            slave.setControl(control);
          }
        }
      }
    }
    ```

### `public synchronized void setSimState(double position, double velocity)`

[Source lines 748–753](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L748)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It changes object/subclass state through `simPosition`, `simVelocity`.
- It has 1 conditional path: `config.codeEnabled && !isEStopped`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `position` | `double` | - DCMotorSim: Angular Position (Rotations) - ElevatorSim: Linear Position (Meters) - SingleJointedArmSim: Angular Position (Rotations) - FlywheelSim: N/A |
| `velocity` | `double` | - DCMotorSim: Angular Velocity (rot/s) - ElevatorSim: Linear Velocity (m/s) - SingleJointedArmSim: Angular Velocity (rot/s) - FlywheelSim: Angular Velocity (rot/s) |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 748–753)"

    ```java
    public synchronized void setSimState(double position, double velocity) {
      if (config.codeEnabled && !isEStopped) {
        simPosition = position;
        simVelocity = velocity;
      }
    }
    ```

??? note "Author note from JavaDoc"

    Sets the simulation state for the subsystem.
    
    The units for each simulation type are as follows:
    
    **Parameter `position`:** 
    
    - DCMotorSim: Angular Position (Rotations)
    - ElevatorSim: Linear Position (Meters)
    - SingleJointedArmSim: Angular Position (Rotations)
    - FlywheelSim: N/A
    
    **Parameter `velocity`:** 
    
    - DCMotorSim: Angular Velocity (rot/s)
    - ElevatorSim: Linear Velocity (m/s)
    - SingleJointedArmSim: Angular Velocity (rot/s)
    - FlywheelSim: Angular Velocity (rot/s)

### `protected void setGoal(TalonFXSubsystemGoal goal)`

[Source lines 755–757](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L755)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `goal`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `goal` | `TalonFXSubsystemGoal` | `TalonFXSubsystemGoal` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 755–757)"

    ```java
    protected void setGoal(TalonFXSubsystemGoal goal){
      this.goal = goal;
    }
    ```

### `public void setSimFeedforwardSupplier(DoubleSupplier supplier)`

[Source lines 759–761](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L759)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `simFeedforwardSup`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `supplier` | `DoubleSupplier` | Evaluated when the operation runs, so it may provide a changing value. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 759–761)"

    ```java
    public void setSimFeedforwardSupplier(DoubleSupplier supplier) {
      simFeedforwardSup = supplier;
    }
    ```

### `public synchronized void resetPosition(double position)`

[Source lines 763–765](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L763)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `master.setPosition()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `position` | `double` | Position in the units required by this API and configuration. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 763–765)"

    ```java
    public synchronized void resetPosition(double position) {
      master.setPosition(position);
    }
    ```

### `public void periodic()`

[Source lines 768–789](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L768)

**Detailed behavior**

- The implementation executes 20 non-blank source lines.
- It publishes telemetry/log data.
- It has 4 conditional paths: `config.logTelemetry`; `goal != null`; `getCurrentCommand(` plus 1 more.
- Key collaborators/calls: `outputTelemetry()`, `DogLog.log()`, `goal.toString()`, `goal.target()`, `getAsDouble()`, `getVelocity()`, `getPosition()`, `getCurrentCommand()`, `getName()`, `shouldSimulate()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 768–789)"

    ```java
    public void periodic() {
      if (config.logTelemetry) {
        outputTelemetry();
      }
      if(goal != null){
        DogLog.log(logPrefix + "Goal", goal.toString());
        DogLog.log(logPrefix + "GoalTarget", goal.target().getAsDouble());
      }
      DogLog.log(logPrefix + "Setpoint", setpoint);
      DogLog.log(logPrefix + "Measured", inVelocityMode ? getVelocity() : getPosition());
      if (getCurrentCommand() != null) {
        DogLog.log(logPrefix + "ActiveCommand", getCurrentCommand().getName());
      }
      if(config.debugMode && shouldSimulate()){
        simController.setP(SmartDashboard.getNumber(config.name + " kP", simController.getP()));
        simController.setI(SmartDashboard.getNumber(config.name + " kI", simController.getI()));
        simController.setD(SmartDashboard.getNumber(config.name + " kD", simController.getD()));
        simController.setConstraints(new Constraints(SmartDashboard.getNumber(config.name + " Velocity", simController.getConstraints().maxVelocity), SmartDashboard.getNumber(config.name + " Acceleration", simController.getConstraints().maxAcceleration)));
        DogLog.log(logPrefix + "ControllerPosition", simController.getSetpoint().position);
        DogLog.log(logPrefix + "ControllerVelocity", simController.getSetpoint().velocity);
      }
    }
    ```

### `public void simulationPeriodic()`

[Source lines 792–796](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L792)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `config.simConstants != null && !config.simConstants.useSeparateThread(`.
- Key collaborators/calls: `config.simConstants.useSeparateThread()`, `simulationThread.update()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 792–796)"

    ```java
    public void simulationPeriodic() {
      if (config.simConstants != null && !config.simConstants.useSeparateThread() && !config.useCustomSimCallback) {
        simulationThread.update();
      }
    }
    ```

### `public void outputTelemetry()`

[Source lines 798–816](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L798)

**Detailed behavior**

- The implementation executes 17 non-blank source lines.
- It publishes telemetry/log data.
- It has 1 conditional path: `goal != null`.
- Key collaborators/calls: `DogLog.log()`, `shouldSimulate()`, `simulationThread.getSimVoltage()`, `getAsDouble()`, `simFeedforwardSup.getAsDouble()`, `master.getMotorVoltage()`, `getValueAsDouble()`, `getPosition()`, `getVelocity()`, `getRotorPosition()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 798–816)"

    ```java
    public void outputTelemetry() {
      DogLog.log(
          logPrefix + "AppliedVolts",
          shouldSimulate() ? simulationThread.getSimVoltage().getAsDouble() + simFeedforwardSup.getAsDouble() : master.getMotorVoltage().getValueAsDouble());
      DogLog.log(logPrefix + "Position", getPosition());
      DogLog.log(logPrefix + "Velocity", new double[] {getVelocity(), getVelocity() * 60.0});
      DogLog.log(logPrefix + "Rotor Position", getRotorPosition());
      DogLog.log(
          logPrefix + "Rotor Velocity", new double[] {getRotorVelocity(), getRotorVelocity() * 60.0});
      DogLog.log(logPrefix + "Supply Voltage", master.getSupplyVoltage().getValueAsDouble());
      DogLog.log(logPrefix + "Supply Current", master.getSupplyCurrent().getValueAsDouble());
      DogLog.log(logPrefix + "Setpoint", getSetpoint());
      DogLog.log(logPrefix + "Error", getError());
      if(goal != null){
        DogLog.log(logPrefix + "At Goal?", atGoal());
      }
      DogLog.log(logPrefix + "In Velocity Mode", inVelocityMode);
      DogLog.log(logPrefix + "Control Mode", getControlMode().toString());
    }
    ```

### `public void emergencyStop()`

[Source lines 818–824](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L818)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It changes object/subclass state through `isEStopped`.
- It has 1 conditional path: `current != null`.
- Key collaborators/calls: `stop()`, `setNeutralMode()`, `getCurrentCommand()`, `current.cancel()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 818–824)"

    ```java
    public void emergencyStop() {
      stop();
      setNeutralMode(NeutralModeValue.Coast);
      isEStopped = true;
      Command current = getCurrentCommand();
      if (current != null) current.cancel();
    }
    ```

### `public void stop()`

[Source lines 826–831](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L826)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `master.stopMotor()`, `slave.stopMotor()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 826–831)"

    ```java
    public void stop() {
      master.stopMotor();
      for (TalonFX slave : slaves) {
        slave.stopMotor();
      }
    }
    ```

### `public static void stopAll(TalonFXSubsystem... subsystems)`

[Source lines 833–837](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L833)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `sub.stop()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `subsystems` | `TalonFXSubsystem...` | `TalonFXSubsystem...` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 833–837)"

    ```java
    public static void stopAll(TalonFXSubsystem... subsystems) {
      for (TalonFXSubsystem sub : subsystems) {
        sub.stop();
      }
    }
    ```

### `public CANDevice(Integer id, String canbus)`

[Source lines 82–82](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L82)

**Detailed behavior**

- Java generates this record canonical constructor. It stores each argument in the corresponding final record component; Java also supplies component accessors, value-based `equals`, `hashCode`, and `toString`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | `Integer` | `Integer` input consumed by the implementation shown below. |
| `canbus` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `CANDevice` instance.

??? example "Record declaration that generates this callable"

    ```java
    public static record CANDevice(Integer id, String canbus)
    ```

??? note "Author note from JavaDoc"

    Java generates this canonical constructor from the record header.

### `public Integer id()`

[Source lines 82–82](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L82)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `Integer`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public static record CANDevice(Integer id, String canbus)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `id` record component.

### `public String canbus()`

[Source lines 82–82](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L82)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public static record CANDevice(Integer id, String canbus)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `canbus` record component.

### `public TalonFXConstants(CANDevice device, InvertedValue invert)`

[Source lines 97–97](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L97)

**Detailed behavior**

- Java generates this record canonical constructor. It stores each argument in the corresponding final record component; Java also supplies component accessors, value-based `equals`, `hashCode`, and `toString`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `device` | `CANDevice` | `CANDevice` input consumed by the implementation shown below. |
| `invert` | `InvertedValue` | `InvertedValue` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `TalonFXConstants` instance.

??? example "Record declaration that generates this callable"

    ```java
    public static record TalonFXConstants(CANDevice device, InvertedValue invert)
    ```

??? note "Author note from JavaDoc"

    Java generates this canonical constructor from the record header.

### `public CANDevice device()`

[Source lines 97–97](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L97)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `CANDevice`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public static record TalonFXConstants(CANDevice device, InvertedValue invert)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `device` record component.

### `public InvertedValue invert()`

[Source lines 97–97](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L97)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `InvertedValue`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public static record TalonFXConstants(CANDevice device, InvertedValue invert)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `invert` record component.

### `public CANCoderConstants(CANDevice device, CANcoderConfiguration config)`

[Source lines 109–109](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L109)

**Detailed behavior**

- Java generates this record canonical constructor. It stores each argument in the corresponding final record component; Java also supplies component accessors, value-based `equals`, `hashCode`, and `toString`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `device` | `CANDevice` | `CANDevice` input consumed by the implementation shown below. |
| `config` | `CANcoderConfiguration` | `CANcoderConfiguration` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `CANCoderConstants` instance.

??? example "Record declaration that generates this callable"

    ```java
    public static record CANCoderConstants(CANDevice device, CANcoderConfiguration config)
    ```

??? note "Author note from JavaDoc"

    Java generates this canonical constructor from the record header.

### `public CANDevice device()`

[Source lines 109–109](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L109)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `CANDevice`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public static record CANCoderConstants(CANDevice device, CANcoderConfiguration config)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `device` record component.

### `public CANcoderConfiguration config()`

[Source lines 109–109](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L109)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `CANcoderConfiguration`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public static record CANCoderConstants(CANDevice device, CANcoderConfiguration config)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `config` record component.

### `public TalonFXSubsystemSimConstants( SimWrapper sim, double gearing, ProfiledPIDController simController, boolean useSeparateThread, boolean limitVoltage)`

[Source lines 121–121](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L121)

**Detailed behavior**

- Java generates this record canonical constructor. It stores each argument in the corresponding final record component; Java also supplies component accessors, value-based `equals`, `hashCode`, and `toString`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `sim` | `SimWrapper` | `SimWrapper` input consumed by the implementation shown below. |
| `gearing` | `double` | `double` input consumed by the implementation shown below. |
| `simController` | `ProfiledPIDController` | `ProfiledPIDController` input consumed by the implementation shown below. |
| `useSeparateThread` | `boolean` | `boolean` input consumed by the implementation shown below. |
| `limitVoltage` | `boolean` | Voltage value in volts. |

**Result:** Constructs and initializes a `TalonFXSubsystemSimConstants` instance.

??? example "Record declaration that generates this callable"

    ```java
    public record TalonFXSubsystemSimConstants( SimWrapper sim, double gearing, ProfiledPIDController simController, boolean useSeparateThread, boolean limitVoltage)
    ```

??? note "Author note from JavaDoc"

    Java generates this canonical constructor from the record header.

### `public SimWrapper sim()`

[Source lines 121–121](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L121)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `SimWrapper`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record TalonFXSubsystemSimConstants( SimWrapper sim, double gearing, ProfiledPIDController simController, boolean useSeparateThread, boolean limitVoltage)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `sim` record component.

### `public double gearing()`

[Source lines 121–121](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L121)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record TalonFXSubsystemSimConstants( SimWrapper sim, double gearing, ProfiledPIDController simController, boolean useSeparateThread, boolean limitVoltage)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `gearing` record component.

### `public ProfiledPIDController simController()`

[Source lines 121–121](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L121)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `ProfiledPIDController`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record TalonFXSubsystemSimConstants( SimWrapper sim, double gearing, ProfiledPIDController simController, boolean useSeparateThread, boolean limitVoltage)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `simController` record component.

### `public boolean useSeparateThread()`

[Source lines 121–121](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L121)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record TalonFXSubsystemSimConstants( SimWrapper sim, double gearing, ProfiledPIDController simController, boolean useSeparateThread, boolean limitVoltage)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `useSeparateThread` record component.

### `public boolean limitVoltage()`

[Source lines 121–121](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L121)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record TalonFXSubsystemSimConstants( SimWrapper sim, double gearing, ProfiledPIDController simController, boolean useSeparateThread, boolean limitVoltage)
    ```

??? note "Author note from JavaDoc"

    Java generates this accessor for the `limitVoltage` record component.

## Exposed fields and types

### `public class TalonFXSubsystem extends SubsystemBase`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L60)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Base class for TalonFX based subsystems.
    Defines subsystems as a set of motors on a mechanism that do the same thing.
    This means that each DOF of a mechanism is represented as a separate subsystem.
     Supports:
    
    -  1 master TalonFX
    -  Any number of slave TalonFXs
    -  1 CANCoder (Complex systems with multiple CANCoders should be handled externally)
    -  Simple control requests -- both Motion Magic and non Motion Magic (Velocity, Position, Voltage, Duty Cycle)
    -  User-defined control requests
    -  Multi and single threaded simulation setup through configuration
    -  Logging with DogLog

### `public static record CANDevice(Integer id, String canbus)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L82)*

This exposed `record` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Creates a new CANDevice.
    
    **Parameter `id`:** ID of the device.
    **Parameter `canbus`:** Name of the CAN bus this device is on. Possible CAN bus
    strings are:
    
    - "rio" for the native roboRIO CAN bus
    - CANivore name or serial number
    - SocketCAN interface (non-FRC Linux only)
    - "*" for any CANivore seen by the program
    - empty string (default) to select the default for the
    system:
    
    - "rio" on roboRIO
    - "can0" on Linux
    - "*" on Windows

### `public static record TalonFXConstants(CANDevice device, InvertedValue invert)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L97)*

This exposed `record` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Constants for a TalonFX motor controller.
    
    **Parameter `device`:** CANDevice constants.
    **Parameter `invert`:** InvertedValue of the device.

### `public static record CANCoderConstants(CANDevice device, CANcoderConfiguration config)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L109)*

This exposed `record` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Constants for a CANCoder.
    
    **Parameter `device`:** CANDevice constants.
    **Parameter `config`:** Configuration for the device.

### `public interface TalonFXSubsystemGoal`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L111)*

This exposed `interface` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public record TalonFXSubsystemSimConstants( SimWrapper sim, double gearing, ProfiledPIDController simController, boolean useSeparateThread, boolean limitVoltage)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L121)*

This exposed `record` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static enum ControlType`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L142)*

This exposed `enum` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static class TalonFXSubsystemConfiguration`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L151)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public String name = &quot;ERROR_ASSIGN_A_NAME&quot;`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L152)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 20 times, so changing it can affect every control path that reads `name`.

### `public boolean codeEnabled = true`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L154)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `codeEnabled`.

### `public boolean forceSimulation = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L155)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `forceSimulation`.

### `public boolean logTelemetry = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L156)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `logTelemetry`.

### `public boolean debugMode = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L157)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `debugMode`.

### `public boolean useCustomSimCallback = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L158)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `useCustomSimCallback`.

### `public boolean slavesAsFollower = true`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L159)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `slavesAsFollower`.

### `public String logPrefix = null`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L161)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 24 times, so changing it can affect every control path that reads `logPrefix`.

### `public double loopPeriodSec = 0.02`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L163)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `loopPeriodSec`.

### `public double simPeriodSec = 0.001`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L164)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `simPeriodSec`.

### `public TalonFXSubsystemSimConstants simConstants = null`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L166)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 10 times, so changing it can affect every control path that reads `simConstants`.

### `public TalonFXConstants masterConstants = new TalonFXConstants()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L168)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 6 times, so changing it can affect every control path that reads `masterConstants`.

### `public TalonFXConstants[] slaveConstants = new TalonFXConstants[0]`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L169)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 7 times, so changing it can affect every control path that reads `slaveConstants`.

### `public CANCoderConstants cancoderConstants = null`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L171)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 5 times, so changing it can affect every control path that reads `cancoderConstants`.

### `public NeutralModeValue neutralMode = NeutralModeValue.Brake`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L173)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `neutralMode`.

### `public FeedbackSensorSourceValue feedbackSensorSource = FeedbackSensorSourceValue.RotorSensor`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L174)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `feedbackSensorSource`.

### `public int feedbackRemoteSensorId = 99`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L175)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `feedbackRemoteSensorId`.

### `public double feedbackRotorOffset = 0.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L176)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `feedbackRotorOffset`.

### `public double rotorToSensorRatio = 1.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L177)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `rotorToSensorRatio`.

### `public double sensorToMechRatio = 1.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L178)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `sensorToMechRatio`.

### `public double softLimitDeadband = 0.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L179)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `softLimitDeadband`.

### `public double velocityThreshold = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L180)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `velocityThreshold`.

### `public double positionThreshold = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L181)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `positionThreshold`.

### `public boolean continuousWrap = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L183)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `continuousWrap`.

### `public Slot0Configs slot0 = new Slot0Configs()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L185)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `slot0`.

### `public Slot1Configs slot1 = new Slot1Configs()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L186)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `slot1`.

### `public Slot2Configs slot2 = new Slot2Configs()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L187)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `slot2`.

### `public double velocityFeedforward = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L189)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `velocityFeedforward`.

### `public double arbitraryFeedforward = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L190)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `arbitraryFeedforward`.

### `public double cruiseVelocity = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L191)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `cruiseVelocity`.

### `public double acceleration = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L192)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `acceleration`.

### `public double jerk = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L193)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `jerk`.

### `public double rampRate = 0.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L194)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `rampRate`.

### `public double maxVoltage = 12.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L195)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 1 time, so changing it can affect every control path that reads `maxVoltage`.

### `public int supplyCurrentLimit = 40`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L197)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `supplyCurrentLimit`.

### `public boolean enableSupplyCurrentLimit = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L198)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `enableSupplyCurrentLimit`.

### `public int statorCurrentLimit = 120`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L200)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `statorCurrentLimit`.

### `public boolean enableStatorCurrentLimit = true`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L201)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `enableStatorCurrentLimit`.

### `public Double maxUnitsLimit = null`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L203)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `maxUnitsLimit`.

### `public Double minUnitsLimit = null`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L204)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `minUnitsLimit`.

### `public double peakForwardTorqueCurrent = 0.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L206)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `peakForwardTorqueCurrent`.

### `public double peakReverseTorqueCurrent = 0.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L207)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `peakReverseTorqueCurrent`.

### `protected final TalonFXSubsystemConfiguration config`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L210)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 99 times, so changing it can affect every control path that reads `config`.

### `protected final boolean simulating`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L211)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `simulating`.

### `protected final TalonFX master`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L212)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 25 times, so changing it can affect every control path that reads `master`.

### `protected final TalonFX[] slaves`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L213)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 11 times, so changing it can affect every control path that reads `slaves`.

### `protected CANcoder cancoder`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L214)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `cancoder`.

### `protected TalonFXSubsystemGoal goal`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L216)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 37 times, so changing it can affect every control path that reads `goal`.

### `protected SimWrapper sim`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L218)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 10 times, so changing it can affect every control path that reads `sim`.

### `protected SimulationThread simulationThread`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L219)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 8 times, so changing it can affect every control path that reads `simulationThread`.

### `protected ProfiledPIDController simController`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L220)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 33 times, so changing it can affect every control path that reads `simController`.

### `protected DoubleSupplier simFeedforwardSup`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L221)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `simFeedforwardSup`.

### `protected double simPosition`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L222)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `simPosition`.

### `protected double simVelocity`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L223)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `simVelocity`.

### `protected TalonFXConfiguration masterConfig`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L225)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 50 times, so changing it can affect every control path that reads `masterConfig`.

### `protected final TalonFXConfiguration[] slaveConfigs`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L226)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 5 times, so changing it can affect every control path that reads `slaveConfigs`.

### `protected final StatusSignal&lt;Angle&gt; masterPositionSignal`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L228)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `masterPositionSignal`.

### `protected final StatusSignal&lt;AngularVelocity&gt; masterVelocitySignal`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L229)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `masterVelocitySignal`.

### `protected final StatusSignal&lt;Angle&gt; masterRotorPositionSignal`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L231)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `masterRotorPositionSignal`.

### `protected final StatusSignal&lt;AngularVelocity&gt; masterRotorVelocitySignal`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L232)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `masterRotorVelocitySignal`.

### `protected double forwardSoftLimitRotations`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L234)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `forwardSoftLimitRotations`.

### `protected double reverseSoftLimitRotations`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L235)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 3 times, so changing it can affect every control path that reads `reverseSoftLimitRotations`.

### `protected final DutyCycleOut dutyCycleRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L237)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `dutyCycleRequest`.

### `protected final VoltageOut voltageRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L238)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `voltageRequest`.

### `protected final PositionVoltage positionRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L239)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `positionRequest`.

### `protected final MotionMagicVoltage motionMagicPositionRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L240)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `motionMagicPositionRequest`.

### `protected final VelocityVoltage velocityRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L241)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `velocityRequest`.

### `protected final MotionMagicVelocityVoltage motionMagicVelocityRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L242)*

This is a **final protected** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `motionMagicVelocityRequest`.

### `public final String logPrefix`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L244)*

This is a **final public** field without an inline initializer. It is not reassigned after initialization. The declaring source references it 24 times, so changing it can affect every control path that reads `logPrefix`.

### `public static final TalonFXSubsystemGoal defaultGoal = new TalonFXSubsystemGoal()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L246)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 4 times, so changing it can affect every control path that reads `defaultGoal`.

### `protected double setpoint = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L258)*

This is a **protected** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 7 times, so changing it can affect every control path that reads `setpoint`.

### `public boolean inVelocityMode = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L259)*

This is a **public** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 10 times, so changing it can affect every control path that reads `inVelocityMode`.

### `protected boolean isEStopped = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L261)*

This is a **protected** field with an initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `isEStopped`.
