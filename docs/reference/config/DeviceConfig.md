# DeviceConfig

`com.teamscreamrobotics.config.DeviceConfig`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java) · **20 callables** · **1 exposed fields/types**

## Public and protected callables

### `public static void configureTalonFX(String name, TalonFX fx, TalonFXConfiguration config)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L40)*

Applies a `TalonFXConfiguration` to a TalonFX, retrying until success or timeout.

**Parameter `name`:** readable label used in DS error messages
**Parameter `fx`:** the TalonFX to configure
**Parameter `config`:** the configuration to apply

### `public boolean configureSettings()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L44)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public static void configureCANcoder( String name, CANcoder encoder, CANcoderConfiguration config)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L68)*

Applies a `CANcoderConfiguration` to a CANcoder, retrying until success or timeout.

**Parameter `name`:** readable label used in DS error messages
**Parameter `encoder`:** the CANcoder to configure
**Parameter `config`:** the configuration to apply

### `public boolean configureSettings()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L73)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public static void configurePigeon2( String name, Pigeon2 pigeon, Pigeon2Configuration config, double updateFrequencyHz)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L97)*

Applies a `Pigeon2Configuration` and sets yaw/pitch/roll signal update rates.

**Parameter `name`:** human-readable label used in DS error messages
**Parameter `pigeon`:** the Pigeon2 to configure
**Parameter `config`:** the configuration to apply
**Parameter `updateFrequencyHz`:** signal update frequency in Hz for yaw, pitch, roll, and supply voltage

### `public boolean configureSettings()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L102)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public static AudioConfigs FXAudioConfigs( boolean beepOnBoot, boolean beepOnConfig, boolean allowMusicDuringDisabled)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L123)*

Builds an `AudioConfigs` object for a TalonFX.

**Parameter `beepOnBoot`:** whether the motor beeps on boot
**Parameter `beepOnConfig`:** whether the motor beeps on configuration
**Parameter `allowMusicDuringDisabled`:** whether Orchestra playback is allowed while disabled

### `public static MotorOutputConfigs FXMotorOutputConfig( InvertedValue invert, NeutralModeValue neutralMode)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L138)*

Builds a `MotorOutputConfigs` for direction and neutral behavior.

**Parameter `invert`:** `InvertedValue` for motor direction
**Parameter `neutralMode`:** `NeutralModeValue` (brake or coast) when output is zero

### `public static FeedbackConfigs FXFeedbackConfig( FeedbackSensorSourceValue sensor, int remoteSensorID, double sensorToMechGR, double rotorToSensorGR, Rotation2d sensorOffset)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L155)*

Builds a `FeedbackConfigs` for sensor source and gear ratios.

**Parameter `sensor`:** the feedback sensor source
**Parameter `remoteSensorID`:** CAN ID of the remote sensor (ignored if not using a remote sensor)
**Parameter `sensorToMechGR`:** gear ratio from sensor to mechanism output
**Parameter `rotorToSensorGR`:** gear ratio from rotor to sensor
**Parameter `sensorOffset`:** rotational offset applied to the feedback sensor reading

### `public static Slot0Configs FXPIDConfig( ScreamPIDConstants constants, FeedforwardConstants ffConstants)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L176)*

Builds `Slot0Configs` from PID and feedforward constants.

**Parameter `constants`:** PID gains
**Parameter `ffConstants`:** feedforward constants (kV, kS, kG, kA, gravity type)

### `public static Slot0Configs FXPIDConfig(ScreamPIDConstants constants)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L186)*

Builds `Slot0Configs` from PID constants with zeroed feedforward values.

**Parameter `constants`:** PID gains

### `public static OpenLoopRampsConfigs FXOpenLoopRampConfig(double ramp)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L195)*

Builds an `OpenLoopRampsConfigs` with the given duty-cycle ramp period.

**Parameter `ramp`:** time in seconds from 0 to full output

### `public static ClosedLoopRampsConfigs FXClosedLoopRampConfig(double ramp)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L206)*

Builds a `ClosedLoopRampsConfigs` with the given duty-cycle ramp period.

**Parameter `ramp`:** time in seconds from 0 to full output

### `public static CurrentLimitsConfigs FXSupplyCurrentLimitsConfig( boolean enable, double lowerLimit, double limit, double limitTime)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L220)*

Builds a `CurrentLimitsConfigs` for supply current limiting only.

**Parameter `enable`:** whether supply current limiting is enabled
**Parameter `lowerLimit`:** supply current lower limit (amps) — the steady-state limit
**Parameter `limit`:** peak supply current limit (amps)
**Parameter `limitTime`:** time (seconds) supply current may exceed `lowerLimit` before throttling

### `public static CurrentLimitsConfigs FXCurrentLimitsConfig( boolean supplyEnable, double supplyLowerLimit, double supplyLimit, double supplyLimitTime, boolean statorEnable, double statorLimit)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L240)*

Builds a `CurrentLimitsConfigs` for both supply and stator current limiting.

**Parameter `supplyEnable`:** whether supply current limiting is enabled
**Parameter `supplyLowerLimit`:** supply current lower (steady-state) limit in amps
**Parameter `supplyLimit`:** peak supply current limit in amps
**Parameter `supplyLimitTime`:** time (seconds) supply current may exceed `supplyLowerLimit`
**Parameter `statorEnable`:** whether stator current limiting is enabled
**Parameter `statorLimit`:** stator current limit in amps

### `public static ClosedLoopGeneralConfigs FXClosedLoopGeneralConfig(boolean continuousWrap)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L263)*

Builds a `ClosedLoopGeneralConfigs` with continuous wrap enabled or disabled.
Enable for mechanisms that rotate continuously (e.g. swerve steer); disable for limited-range arms.

**Parameter `continuousWrap`:** whether to enable continuous wrap for the closed-loop setpoint

### `public static SoftwareLimitSwitchConfigs FXSoftwareLimitSwitchConfig( boolean enable, double forwardLimit, double reverseLimit)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L276)*

Builds a `SoftwareLimitSwitchConfigs` that applies the same enable state to both directions.

**Parameter `enable`:** whether both forward and reverse software limits are active
**Parameter `forwardLimit`:** forward soft limit threshold in mechanism rotations
**Parameter `reverseLimit`:** reverse soft limit threshold in mechanism rotations

### `public static HardwareLimitSwitchConfigs FXHardwareLimitSwitchConfig( boolean forwardEnable, boolean reverseEnable, double forwardPosition, double reversePosition)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L294)*

Builds a `HardwareLimitSwitchConfigs` that auto-sets position on limit switch trigger.

**Parameter `forwardEnable`:** whether the forward limit switch auto-sets position
**Parameter `reverseEnable`:** whether the reverse limit switch auto-sets position
**Parameter `forwardPosition`:** position (rotations) set when the forward limit is triggered
**Parameter `reversePosition`:** position (rotations) set when the reverse limit is triggered

### `public static MotionMagicConfigs FXMotionMagicConfig(MotionMagicConstants constants)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L312)*

Builds a `MotionMagicConfigs` from a `MotionMagicConstants` record.

**Parameter `constants`:** cruise velocity, acceleration, and jerk limits

### `public static VoltageConfigs FXVoltageConfig( double peakForwardVoltage, double peakReverseVoltage, double supplyVoltageTimeConstant)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L327)*

Builds a `VoltageConfigs` for peak output and supply filtering.

**Parameter `peakForwardVoltage`:** maximum forward output voltage
**Parameter `peakReverseVoltage`:** maximum reverse output voltage (typically negative)
**Parameter `supplyVoltageTimeConstant`:** low-pass filter time constant for supply voltage measurement

## Exposed fields and types

### `public class DeviceConfig`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L31)*

Factory methods for building CTRE Phoenix 6 configuration objects and configuring devices.
