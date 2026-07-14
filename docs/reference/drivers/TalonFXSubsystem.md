# TalonFXSubsystem

`com.teamscreamrobotics.drivers.TalonFXSubsystem`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java) · **64 callables** · **81 exposed fields/types**

## Competition usage

**2025:** [`Routines.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/autonomous/Routines.java#L3), [`Climber.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/climber/Climber.java#L4), [`ClimberConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/climber/ClimberConstants.java#L8), [`IntakeConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/intake/IntakeConstants.java#L6), [`IntakeDeploy.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/intake/IntakeDeploy.java#L4), [`IntakeRollers.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/intake/IntakeRollers.java#L3), [`Elevator.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/elevator/Elevator.java#L4), [`ElevatorConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/elevator/ElevatorConstants.java#L7), [`Superstructure.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/Superstructure.java#L4), [`Wrist.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/wrist/Wrist.java#L3), [`WristConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/wrist/WristConstants.java#L10), [`WristRollers.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/superstructure/wrist/WristRollers.java#L4)

**2026:** [`IntakeConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/intake/IntakeConstants.java#L7), [`IntakeRollers.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/intake/IntakeRollers.java#L3), [`IntakeWrist.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/intake/IntakeWrist.java#L6), [`Feeder.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/feeder/Feeder.java#L3), [`FeederConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/feeder/FeederConstants.java#L5), [`Flywheel.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/flywheel/Flywheel.java#L4), [`FlywheelConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/flywheel/FlywheelConstants.java#L6), [`Hood.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/hood/Hood.java#L3), [`HoodConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/hood/HoodConstants.java#L5), [`Rollers.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/rollers/Rollers.java#L3), [`RollersConstants.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/rollers/RollersConstants.java#L5)

## Public and protected callables

### `public CANDevice()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L83)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public CANDevice(Integer id)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L86)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public TalonFXConstants()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L98)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `DoubleSupplier target()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L112)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `ControlType controlType()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L114)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public TalonFXSubsystemSimConstants(SimWrapper sim, double gearing, PIDController simController)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L127)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public TalonFXSubsystemSimConstants(SimWrapper sim, double gearing, PIDController simController, double minInput, double maxInput)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L131)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public DoubleSupplier target()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L248)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public ControlType controlType()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L253)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public TalonFXSubsystem( final TalonFXSubsystemConfiguration config, final TalonFXSubsystemGoal defaultGoal)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L263)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public TalonFXSubsystem(TalonFXSubsystemConfiguration config)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L398)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public void configMaster(TalonFXConfiguration motorConfig)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L407)*

Configures the master motor with the given configuration.

**Parameter `motorConfig`:** - The config to apply to the master.

### `public void configSlave(TalonFX slave, TalonFXConfiguration motorConfig)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L417)*

Configures a slave motor with the given configuration.

**Parameter `slave`:** - The slave to apply the config to.
**Parameter `motorConfig`:** - The config to apply to the slave.

### `public void setStatorCurrentLimit(double currentLimit, boolean enable)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L427)*

Reconfigures the motors with the given stator current limits.

**Parameter `currentLimit`:** - Stator current limit to apply.
**Parameter `enable`:** - Whether the current limit should be enabled.

### `public void enableSoftLimits(boolean enable)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L441)*

Reconfigures the motors to enable soft limits.

**Parameter `enable`:** - Whether the soft limits should be enabled.

### `public void setNeutralMode(NeutralModeValue mode)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L455)*

Sets the neutral mode of the motors.

**Parameter `mode`:** - The neutral mode to apply to the motors.

### `public synchronized void setSupplyCurrentLimit(double value, boolean enable)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L462)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setSupplyCurrentLimitUnchecked(double value, boolean enable)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L469)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setStatorCurrentLimitUnchecked(double value, boolean enable)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L476)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setMotionMagicConfigsUnchecked(MotionMagicConstants configs)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L483)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setMotionMagicConfigs(MotionMagicConstants configs)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L491)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public void changeTalonConfig(UnaryOperator&lt;TalonFXConfiguration&gt; configChanger)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L499)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public void writeConfigs()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L507)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `protected boolean shouldSimulate()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L516)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized ControlModeValue getControlMode()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L520)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized double getRotorPosition()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L524)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized double getPosition()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L528)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized double getRotorVelocity()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L532)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized double getVelocity()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L536)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized double getSetpoint()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L540)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized TalonFXSubsystemGoal getGoal()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L544)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized double getError()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L548)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized Rotation2d getAngle()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L560)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized boolean atGoal()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L564)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized boolean atGoal(double absTolerance)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L574)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized boolean isActive()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L582)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized Command applyGoalCommand(TalonFXSubsystemGoal goal)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L586)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void applyGoal(TalonFXSubsystemGoal goal)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L591)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized Command applyVoltageCommand(DoubleSupplier voltage)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L618)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized Command applyVoltageCommand( DoubleSupplier voltage, DoubleSupplier voltageFeedforward)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L622)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized Command applyControlCommand(ControlRequest control)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L628)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setDutyCycle(double dutyCycle, double dutyCycleFeedforward)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L632)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setDutyCycle(double dutyCycle)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L639)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setVoltage(double volts, double voltageFeedForward)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L643)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setVoltage(double volts)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L650)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setSetpointPosition(double position, double voltageFeedForward)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L654)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setSetpointPosition(double position)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L658)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setSetpointMotionMagicPosition( double position, double voltageFeedForward)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L662)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setSetpointMotionMagicPosition(double position)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L667)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setSetpointVelocity(double velocity, double voltageFeedForward)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L671)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setSetpointVelocity(double velocity)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L675)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setSetpointMotionMagicVelocity( double velocity, double voltageFeedForward)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L679)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setSetpointMotionMagicVelocity(double velocity)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L684)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setMaster(ControlRequest control)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L716)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void setSimState(double position, double velocity)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L748)*

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

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L755)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public void setSimFeedforwardSupplier(DoubleSupplier supplier)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L759)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public synchronized void resetPosition(double position)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L763)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public void periodic()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L768)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public void simulationPeriodic()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L792)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public void outputTelemetry()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L798)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public void emergencyStop()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L818)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public void stop()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L826)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public static void stopAll(TalonFXSubsystem... subsystems)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L833)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

## Exposed fields and types

### `public class TalonFXSubsystem extends SubsystemBase`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L60)*

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

Constants for a TalonFX motor controller.

**Parameter `device`:** CANDevice constants.
**Parameter `invert`:** InvertedValue of the device.

### `public static record CANCoderConstants(CANDevice device, CANcoderConfiguration config)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L109)*

Constants for a CANCoder.

**Parameter `device`:** CANDevice constants.
**Parameter `config`:** Configuration for the device.

### `public interface TalonFXSubsystemGoal`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L111)*

### `public record TalonFXSubsystemSimConstants( SimWrapper sim, double gearing, ProfiledPIDController simController, boolean useSeparateThread, boolean limitVoltage)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L121)*

### `public static enum ControlType`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L142)*

### `public static class TalonFXSubsystemConfiguration`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L151)*

### `public String name = &quot;ERROR_ASSIGN_A_NAME&quot;`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L152)*

### `public boolean codeEnabled = true`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L154)*

### `public boolean forceSimulation = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L155)*

### `public boolean logTelemetry = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L156)*

### `public boolean debugMode = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L157)*

### `public boolean useCustomSimCallback = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L158)*

### `public boolean slavesAsFollower = true`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L159)*

### `public String logPrefix = null`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L161)*

### `public double loopPeriodSec = 0.02`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L163)*

### `public double simPeriodSec = 0.001`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L164)*

### `public TalonFXSubsystemSimConstants simConstants = null`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L166)*

### `public TalonFXConstants masterConstants = new TalonFXConstants()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L168)*

### `public TalonFXConstants[] slaveConstants = new TalonFXConstants[0]`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L169)*

### `public CANCoderConstants cancoderConstants = null`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L171)*

### `public NeutralModeValue neutralMode = NeutralModeValue.Brake`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L173)*

### `public FeedbackSensorSourceValue feedbackSensorSource = FeedbackSensorSourceValue.RotorSensor`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L174)*

### `public int feedbackRemoteSensorId = 99`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L175)*

### `public double feedbackRotorOffset = 0.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L176)*

### `public double rotorToSensorRatio = 1.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L177)*

### `public double sensorToMechRatio = 1.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L178)*

### `public double softLimitDeadband = 0.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L179)*

### `public double velocityThreshold = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L180)*

### `public double positionThreshold = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L181)*

### `public boolean continuousWrap = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L183)*

### `public Slot0Configs slot0 = new Slot0Configs()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L185)*

### `public Slot1Configs slot1 = new Slot1Configs()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L186)*

### `public Slot2Configs slot2 = new Slot2Configs()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L187)*

### `public double velocityFeedforward = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L189)*

### `public double arbitraryFeedforward = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L190)*

### `public double cruiseVelocity = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L191)*

### `public double acceleration = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L192)*

### `public double jerk = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L193)*

### `public double rampRate = 0.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L194)*

### `public double maxVoltage = 12.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L195)*

### `public int supplyCurrentLimit = 40`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L197)*

### `public boolean enableSupplyCurrentLimit = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L198)*

### `public int statorCurrentLimit = 120`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L200)*

### `public boolean enableStatorCurrentLimit = true`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L201)*

### `public Double maxUnitsLimit = null`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L203)*

### `public Double minUnitsLimit = null`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L204)*

### `public double peakForwardTorqueCurrent = 0.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L206)*

### `public double peakReverseTorqueCurrent = 0.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L207)*

### `protected final TalonFXSubsystemConfiguration config`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L210)*

### `protected final boolean simulating`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L211)*

### `protected final TalonFX master`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L212)*

### `protected final TalonFX[] slaves`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L213)*

### `protected CANcoder cancoder`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L214)*

### `protected TalonFXSubsystemGoal goal`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L216)*

### `protected SimWrapper sim`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L218)*

### `protected SimulationThread simulationThread`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L219)*

### `protected ProfiledPIDController simController`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L220)*

### `protected DoubleSupplier simFeedforwardSup`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L221)*

### `protected double simPosition`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L222)*

### `protected double simVelocity`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L223)*

### `protected TalonFXConfiguration masterConfig`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L225)*

### `protected final TalonFXConfiguration[] slaveConfigs`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L226)*

### `protected final StatusSignal&lt;Angle&gt; masterPositionSignal`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L228)*

### `protected final StatusSignal&lt;AngularVelocity&gt; masterVelocitySignal`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L229)*

### `protected final StatusSignal&lt;Angle&gt; masterRotorPositionSignal`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L231)*

### `protected final StatusSignal&lt;AngularVelocity&gt; masterRotorVelocitySignal`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L232)*

### `protected double forwardSoftLimitRotations`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L234)*

### `protected double reverseSoftLimitRotations`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L235)*

### `protected final DutyCycleOut dutyCycleRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L237)*

### `protected final VoltageOut voltageRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L238)*

### `protected final PositionVoltage positionRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L239)*

### `protected final MotionMagicVoltage motionMagicPositionRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L240)*

### `protected final VelocityVoltage velocityRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L241)*

### `protected final MotionMagicVelocityVoltage motionMagicVelocityRequest`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L242)*

### `public final String logPrefix`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L244)*

### `public static final TalonFXSubsystemGoal defaultGoal = new TalonFXSubsystemGoal()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L246)*

### `protected double setpoint = 0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L258)*

### `public boolean inVelocityMode = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L259)*

### `protected boolean isEStopped = false`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/TalonFXSubsystem.java#L261)*
