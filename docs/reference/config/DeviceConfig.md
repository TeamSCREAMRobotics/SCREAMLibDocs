# DeviceConfig

`com.teamscreamrobotics.config.DeviceConfig`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java) · **20 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public static void configureTalonFX(String name, TalonFX fx, TalonFXConfiguration config)`

[Source lines 40–59](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L40)

**Detailed behavior**

- The implementation executes 18 non-blank source lines.
- It interacts with a Phoenix device configurator; this can perform CAN configuration I/O and report vendor status codes.
- Return path: `ErrorChecker.hasConfiguredWithoutErrors( fx.clearStickyFaults(), fx.getConfigurator().apply(config))`.
- Key collaborators/calls: `DeviceConfiguration()`, `configureSettings()`, `ErrorChecker.hasConfiguredWithoutErrors()`, `fx.clearStickyFaults()`, `fx.getConfigurator()`, `apply()`, `ErrorChecker.configureDevice()`, `fx.getDescription()`, `fx.getVersion()`, `fx.getNetwork()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | `String` | readable label used in DS error messages **Parameter `fx`:** the TalonFX to configure **Parameter `config`:** the configuration to apply |
| `fx` | `TalonFX` | the TalonFX to configure **Parameter `config`:** the configuration to apply |
| `config` | `TalonFXConfiguration` | the configuration to apply |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 40–59)"

    ```java
    public static void configureTalonFX(String name, TalonFX fx, TalonFXConfiguration config) {
      DeviceConfiguration deviceConfig =
          new DeviceConfiguration() {
            @Override
            public boolean configureSettings() {
              return ErrorChecker.hasConfiguredWithoutErrors(
                  fx.clearStickyFaults(), fx.getConfigurator().apply(config));
            }
          };
      ErrorChecker.configureDevice(
          deviceConfig,
          name
              + " "
              + fx.getDescription()
              + " version "
              + fx.getVersion()
              + "network"
              + fx.getNetwork(),
          true);
    }
    ```

??? note "Author note from JavaDoc"

    Applies a `TalonFXConfiguration` to a TalonFX, retrying until success or timeout.
    
    **Parameter `name`:** readable label used in DS error messages
    **Parameter `fx`:** the TalonFX to configure
    **Parameter `config`:** the configuration to apply

### `public boolean configureSettings()`

[Source lines 44–47](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L44)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It interacts with a Phoenix device configurator; this can perform CAN configuration I/O and report vendor status codes.
- Return path: `ErrorChecker.hasConfiguredWithoutErrors( fx.clearStickyFaults(), fx.getConfigurator().apply(config))`.
- Key collaborators/calls: `ErrorChecker.hasConfiguredWithoutErrors()`, `fx.clearStickyFaults()`, `fx.getConfigurator()`, `apply()`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 44–47)"

    ```java
    public boolean configureSettings() {
      return ErrorChecker.hasConfiguredWithoutErrors(
          fx.clearStickyFaults(), fx.getConfigurator().apply(config));
    }
    ```

### `public static void configureCANcoder( String name, CANcoder encoder, CANcoderConfiguration config)`

[Source lines 68–87](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L68)

**Detailed behavior**

- The implementation executes 17 non-blank source lines.
- It interacts with a Phoenix device configurator; this can perform CAN configuration I/O and report vendor status codes.
- Return path: `ErrorChecker.hasConfiguredWithoutErrors(encoder.getConfigurator().apply(config))`.
- Key collaborators/calls: `DeviceConfiguration()`, `configureSettings()`, `ErrorChecker.hasConfiguredWithoutErrors()`, `encoder.getConfigurator()`, `apply()`, `ErrorChecker.configureDevice()`, `encoder.getDeviceID()`, `encoder.getVersion()`, `encoder.getNetwork()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | `String` | readable label used in DS error messages **Parameter `encoder`:** the CANcoder to configure **Parameter `config`:** the configuration to apply |
| `encoder` | `CANcoder` | the CANcoder to configure **Parameter `config`:** the configuration to apply |
| `config` | `CANcoderConfiguration` | the configuration to apply |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 68–87)"

    ```java
    public static void configureCANcoder(
        String name, CANcoder encoder, CANcoderConfiguration config) {
      DeviceConfiguration deviceConfig =
          new DeviceConfiguration() {
            @Override
            public boolean configureSettings() {
              return ErrorChecker.hasConfiguredWithoutErrors(encoder.getConfigurator().apply(config));
            }
          };
      ErrorChecker.configureDevice(
          deviceConfig,
          name
              + " "
              + encoder.getDeviceID()
              + " version "
              + encoder.getVersion()
              + " network "
              + encoder.getNetwork(),
          true);
    }
    ```

??? note "Author note from JavaDoc"

    Applies a `CANcoderConfiguration` to a CANcoder, retrying until success or timeout.
    
    **Parameter `name`:** readable label used in DS error messages
    **Parameter `encoder`:** the CANcoder to configure
    **Parameter `config`:** the configuration to apply

### `public boolean configureSettings()`

[Source lines 73–75](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L73)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It interacts with a Phoenix device configurator; this can perform CAN configuration I/O and report vendor status codes.
- Return path: `ErrorChecker.hasConfiguredWithoutErrors(encoder.getConfigurator().apply(config))`.
- Key collaborators/calls: `ErrorChecker.hasConfiguredWithoutErrors()`, `encoder.getConfigurator()`, `apply()`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 73–75)"

    ```java
    public boolean configureSettings() {
      return ErrorChecker.hasConfiguredWithoutErrors(encoder.getConfigurator().apply(config));
    }
    ```

### `public static void configurePigeon2( String name, Pigeon2 pigeon, Pigeon2Configuration config, double updateFrequencyHz)`

[Source lines 97–114](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L97)

**Detailed behavior**

- The implementation executes 15 non-blank source lines.
- It interacts with a Phoenix device configurator; this can perform CAN configuration I/O and report vendor status codes.
- Return path: `ErrorChecker.hasConfiguredWithoutErrors( pigeon.getConfigurator().apply(config), pigeon.setYaw(0), pigeon.getYaw().setUpdateFrequency(updateFrequencyHz), pigeon.getPitch().setUpda…`.
- Key collaborators/calls: `DeviceConfiguration()`, `configureSettings()`, `ErrorChecker.hasConfiguredWithoutErrors()`, `pigeon.getConfigurator()`, `apply()`, `pigeon.setYaw()`, `pigeon.getYaw()`, `setUpdateFrequency()`, `pigeon.getPitch()`, `pigeon.getRoll()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | `String` | human-readable label used in DS error messages **Parameter `pigeon`:** the Pigeon2 to configure **Parameter `config`:** the configuration to apply **Parameter `updateFrequencyHz`:** signal update frequency in Hz for yaw… |
| `pigeon` | `Pigeon2` | the Pigeon2 to configure **Parameter `config`:** the configuration to apply **Parameter `updateFrequencyHz`:** signal update frequency in Hz for yaw, pitch, roll, and supply voltage |
| `config` | `Pigeon2Configuration` | the configuration to apply **Parameter `updateFrequencyHz`:** signal update frequency in Hz for yaw, pitch, roll, and supply voltage |
| `updateFrequencyHz` | `double` | signal update frequency in Hz for yaw, pitch, roll, and supply voltage |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 97–114)"

    ```java
    public static void configurePigeon2(
        String name, Pigeon2 pigeon, Pigeon2Configuration config, double updateFrequencyHz) {
      DeviceConfiguration deviceConfig =
          new DeviceConfiguration() {
            @Override
            public boolean configureSettings() {
              return ErrorChecker.hasConfiguredWithoutErrors(
                  pigeon.getConfigurator().apply(config),
                  pigeon.setYaw(0),
                  pigeon.getYaw().setUpdateFrequency(updateFrequencyHz),
                  pigeon.getPitch().setUpdateFrequency(updateFrequencyHz),
                  pigeon.getRoll().setUpdateFrequency(updateFrequencyHz),
                  pigeon.getSupplyVoltage().setUpdateFrequency(updateFrequencyHz));
            }
          };
      ErrorChecker.configureDevice(
          deviceConfig, name + " " + pigeon.getDeviceID() + " version " + pigeon.getVersion(), true);
    }
    ```

??? note "Author note from JavaDoc"

    Applies a `Pigeon2Configuration` and sets yaw/pitch/roll signal update rates.
    
    **Parameter `name`:** human-readable label used in DS error messages
    **Parameter `pigeon`:** the Pigeon2 to configure
    **Parameter `config`:** the configuration to apply
    **Parameter `updateFrequencyHz`:** signal update frequency in Hz for yaw, pitch, roll, and supply voltage

### `public boolean configureSettings()`

[Source lines 102–110](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L102)

**Detailed behavior**

- The implementation executes 7 non-blank source lines.
- It interacts with a Phoenix device configurator; this can perform CAN configuration I/O and report vendor status codes.
- Return path: `ErrorChecker.hasConfiguredWithoutErrors( pigeon.getConfigurator().apply(config), pigeon.setYaw(0), pigeon.getYaw().setUpdateFrequency(updateFrequencyHz), pigeon.getPitch().setUpda…`.
- Key collaborators/calls: `ErrorChecker.hasConfiguredWithoutErrors()`, `pigeon.getConfigurator()`, `apply()`, `pigeon.setYaw()`, `pigeon.getYaw()`, `setUpdateFrequency()`, `pigeon.getPitch()`, `pigeon.getRoll()`, `pigeon.getSupplyVoltage()`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 102–110)"

    ```java
    public boolean configureSettings() {
      return ErrorChecker.hasConfiguredWithoutErrors(
          pigeon.getConfigurator().apply(config),
          pigeon.setYaw(0),
          pigeon.getYaw().setUpdateFrequency(updateFrequencyHz),
          pigeon.getPitch().setUpdateFrequency(updateFrequencyHz),
          pigeon.getRoll().setUpdateFrequency(updateFrequencyHz),
          pigeon.getSupplyVoltage().setUpdateFrequency(updateFrequencyHz));
    }
    ```

### `public static AudioConfigs FXAudioConfigs( boolean beepOnBoot, boolean beepOnConfig, boolean allowMusicDuringDisabled)`

[Source lines 123–130](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L123)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `AudioConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `beepOnBoot` | `boolean` | whether the motor beeps on boot **Parameter `beepOnConfig`:** whether the motor beeps on configuration **Parameter `allowMusicDuringDisabled`:** whether Orchestra playback is allowed while disabled |
| `beepOnConfig` | `boolean` | whether the motor beeps on configuration **Parameter `allowMusicDuringDisabled`:** whether Orchestra playback is allowed while disabled |
| `allowMusicDuringDisabled` | `boolean` | whether Orchestra playback is allowed while disabled |

**Result:** Returns `AudioConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 123–130)"

    ```java
    public static AudioConfigs FXAudioConfigs(
        boolean beepOnBoot, boolean beepOnConfig, boolean allowMusicDuringDisabled) {
      AudioConfigs config = new AudioConfigs();
      config.BeepOnBoot = beepOnBoot;
      config.BeepOnConfig = beepOnConfig;
      config.AllowMusicDurDisable = allowMusicDuringDisabled;
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds an `AudioConfigs` object for a TalonFX.
    
    **Parameter `beepOnBoot`:** whether the motor beeps on boot
    **Parameter `beepOnConfig`:** whether the motor beeps on configuration
    **Parameter `allowMusicDuringDisabled`:** whether Orchestra playback is allowed while disabled

### `public static MotorOutputConfigs FXMotorOutputConfig( InvertedValue invert, NeutralModeValue neutralMode)`

[Source lines 138–144](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L138)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `MotorOutputConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `invert` | `InvertedValue` | `InvertedValue` for motor direction **Parameter `neutralMode`:** `NeutralModeValue` (brake or coast) when output is zero |
| `neutralMode` | `NeutralModeValue` | `NeutralModeValue` (brake or coast) when output is zero |

**Result:** Returns `MotorOutputConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 138–144)"

    ```java
    public static MotorOutputConfigs FXMotorOutputConfig(
        InvertedValue invert, NeutralModeValue neutralMode) {
      MotorOutputConfigs config = new MotorOutputConfigs();
      config.Inverted = invert;
      config.NeutralMode = neutralMode;
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds a `MotorOutputConfigs` for direction and neutral behavior.
    
    **Parameter `invert`:** `InvertedValue` for motor direction
    **Parameter `neutralMode`:** `NeutralModeValue` (brake or coast) when output is zero

### `public static FeedbackConfigs FXFeedbackConfig( FeedbackSensorSourceValue sensor, int remoteSensorID, double sensorToMechGR, double rotorToSensorGR, Rotation2d sensorOffset)`

[Source lines 155–168](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L155)

**Detailed behavior**

- The implementation executes 7 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `FeedbackConfigs()`, `sensorOffset.getRotations()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `sensor` | `FeedbackSensorSourceValue` | the feedback sensor source **Parameter `remoteSensorID`:** CAN ID of the remote sensor (ignored if not using a remote sensor) **Parameter `sensorToMechGR`:** gear ratio from sensor to mechanism output **Parameter `rotor… |
| `remoteSensorID` | `int` | CAN ID of the remote sensor (ignored if not using a remote sensor) **Parameter `sensorToMechGR`:** gear ratio from sensor to mechanism output **Parameter `rotorToSensorGR`:** gear ratio from rotor to sensor **Parameter … |
| `sensorToMechGR` | `double` | gear ratio from sensor to mechanism output **Parameter `rotorToSensorGR`:** gear ratio from rotor to sensor **Parameter `sensorOffset`:** rotational offset applied to the feedback sensor reading |
| `rotorToSensorGR` | `double` | gear ratio from rotor to sensor **Parameter `sensorOffset`:** rotational offset applied to the feedback sensor reading |
| `sensorOffset` | `Rotation2d` | rotational offset applied to the feedback sensor reading |

**Result:** Returns `FeedbackConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 155–168)"

    ```java
    public static FeedbackConfigs FXFeedbackConfig(
        FeedbackSensorSourceValue sensor,
        int remoteSensorID,
        double sensorToMechGR,
        double rotorToSensorGR,
        Rotation2d sensorOffset) {
      FeedbackConfigs config = new FeedbackConfigs();
      config.FeedbackSensorSource = sensor;
      config.FeedbackRemoteSensorID = remoteSensorID;
      config.SensorToMechanismRatio = sensorToMechGR;
      config.RotorToSensorRatio = rotorToSensorGR;
      config.FeedbackRotorOffset = sensorOffset.getRotations();
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds a `FeedbackConfigs` for sensor source and gear ratios.
    
    **Parameter `sensor`:** the feedback sensor source
    **Parameter `remoteSensorID`:** CAN ID of the remote sensor (ignored if not using a remote sensor)
    **Parameter `sensorToMechGR`:** gear ratio from sensor to mechanism output
    **Parameter `rotorToSensorGR`:** gear ratio from rotor to sensor
    **Parameter `sensorOffset`:** rotational offset applied to the feedback sensor reading

### `public static Slot0Configs FXPIDConfig( ScreamPIDConstants constants, FeedforwardConstants ffConstants)`

[Source lines 176–179](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L176)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `constants.getSlot0Configs(ffConstants)`.
- Key collaborators/calls: `constants.getSlot0Configs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `constants` | `ScreamPIDConstants` | PID gains **Parameter `ffConstants`:** feedforward constants (kV, kS, kG, kA, gravity type) |
| `ffConstants` | `FeedforwardConstants` | feedforward constants (kV, kS, kG, kA, gravity type) |

**Result:** Returns `Slot0Configs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 176–179)"

    ```java
    public static Slot0Configs FXPIDConfig(
        ScreamPIDConstants constants, FeedforwardConstants ffConstants) {
      return constants.getSlot0Configs(ffConstants);
    }
    ```

??? note "Author note from JavaDoc"

    Builds `Slot0Configs` from PID and feedforward constants.
    
    **Parameter `constants`:** PID gains
    **Parameter `ffConstants`:** feedforward constants (kV, kS, kG, kA, gravity type)

### `public static Slot0Configs FXPIDConfig(ScreamPIDConstants constants)`

[Source lines 186–188](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L186)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `constants.getSlot0Configs(new FeedforwardConstants())`.
- Key collaborators/calls: `constants.getSlot0Configs()`, `FeedforwardConstants()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `constants` | `ScreamPIDConstants` | PID gains |

**Result:** Returns `Slot0Configs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 186–188)"

    ```java
    public static Slot0Configs FXPIDConfig(ScreamPIDConstants constants) {
      return constants.getSlot0Configs(new FeedforwardConstants());
    }
    ```

??? note "Author note from JavaDoc"

    Builds `Slot0Configs` from PID constants with zeroed feedforward values.
    
    **Parameter `constants`:** PID gains

### `public static OpenLoopRampsConfigs FXOpenLoopRampConfig(double ramp)`

[Source lines 195–199](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L195)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `OpenLoopRampsConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `ramp` | `double` | time in seconds from 0 to full output |

**Result:** Returns `OpenLoopRampsConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 195–199)"

    ```java
    public static OpenLoopRampsConfigs FXOpenLoopRampConfig(double ramp) {
      OpenLoopRampsConfigs config = new OpenLoopRampsConfigs();
      config.DutyCycleOpenLoopRampPeriod = ramp;
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds an `OpenLoopRampsConfigs` with the given duty-cycle ramp period.
    
    **Parameter `ramp`:** time in seconds from 0 to full output

### `public static ClosedLoopRampsConfigs FXClosedLoopRampConfig(double ramp)`

[Source lines 206–210](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L206)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `ClosedLoopRampsConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `ramp` | `double` | time in seconds from 0 to full output |

**Result:** Returns `ClosedLoopRampsConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 206–210)"

    ```java
    public static ClosedLoopRampsConfigs FXClosedLoopRampConfig(double ramp) {
      ClosedLoopRampsConfigs config = new ClosedLoopRampsConfigs();
      config.DutyCycleClosedLoopRampPeriod = ramp;
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds a `ClosedLoopRampsConfigs` with the given duty-cycle ramp period.
    
    **Parameter `ramp`:** time in seconds from 0 to full output

### `public static CurrentLimitsConfigs FXSupplyCurrentLimitsConfig( boolean enable, double lowerLimit, double limit, double limitTime)`

[Source lines 220–228](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L220)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `CurrentLimitsConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `enable` | `boolean` | whether supply current limiting is enabled **Parameter `lowerLimit`:** supply current lower limit (amps) — the steady-state limit **Parameter `limit`:** peak supply current limit (amps) **Parameter `limitTime`:** time (… |
| `lowerLimit` | `double` | supply current lower limit (amps) — the steady-state limit **Parameter `limit`:** peak supply current limit (amps) **Parameter `limitTime`:** time (seconds) supply current may exceed `lowerLimit` before throttling |
| `limit` | `double` | peak supply current limit (amps) **Parameter `limitTime`:** time (seconds) supply current may exceed `lowerLimit` before throttling |
| `limitTime` | `double` | time (seconds) supply current may exceed `lowerLimit` before throttling |

**Result:** Returns `CurrentLimitsConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 220–228)"

    ```java
    public static CurrentLimitsConfigs FXSupplyCurrentLimitsConfig(
        boolean enable, double lowerLimit, double limit, double limitTime) {
      CurrentLimitsConfigs config = new CurrentLimitsConfigs();
      config.SupplyCurrentLimitEnable = enable;
      config.SupplyCurrentLowerLimit = lowerLimit;
      config.SupplyCurrentLimit = limit;
      config.SupplyCurrentLowerTime = limitTime;
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds a `CurrentLimitsConfigs` for supply current limiting only.
    
    **Parameter `enable`:** whether supply current limiting is enabled
    **Parameter `lowerLimit`:** supply current lower limit (amps) — the steady-state limit
    **Parameter `limit`:** peak supply current limit (amps)
    **Parameter `limitTime`:** time (seconds) supply current may exceed `lowerLimit` before throttling

### `public static CurrentLimitsConfigs FXCurrentLimitsConfig( boolean supplyEnable, double supplyLowerLimit, double supplyLimit, double supplyLimitTime, boolean statorEnable, double statorLimit)`

[Source lines 240–255](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L240)

**Detailed behavior**

- The implementation executes 8 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `CurrentLimitsConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `supplyEnable` | `boolean` | whether supply current limiting is enabled **Parameter `supplyLowerLimit`:** supply current lower (steady-state) limit in amps **Parameter `supplyLimit`:** peak supply current limit in amps **Parameter `supplyLimitTime`… |
| `supplyLowerLimit` | `double` | supply current lower (steady-state) limit in amps **Parameter `supplyLimit`:** peak supply current limit in amps **Parameter `supplyLimitTime`:** time (seconds) supply current may exceed `supplyLowerLimit` **Parameter `… |
| `supplyLimit` | `double` | peak supply current limit in amps **Parameter `supplyLimitTime`:** time (seconds) supply current may exceed `supplyLowerLimit` **Parameter `statorEnable`:** whether stator current limiting is enabled **Parameter `stator… |
| `supplyLimitTime` | `double` | time (seconds) supply current may exceed `supplyLowerLimit` **Parameter `statorEnable`:** whether stator current limiting is enabled **Parameter `statorLimit`:** stator current limit in amps |
| `statorEnable` | `boolean` | whether stator current limiting is enabled **Parameter `statorLimit`:** stator current limit in amps |
| `statorLimit` | `double` | stator current limit in amps |

**Result:** Returns `CurrentLimitsConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 240–255)"

    ```java
    public static CurrentLimitsConfigs FXCurrentLimitsConfig(
        boolean supplyEnable,
        double supplyLowerLimit,
        double supplyLimit,
        double supplyLimitTime,
        boolean statorEnable,
        double statorLimit) {
      CurrentLimitsConfigs config = new CurrentLimitsConfigs();
      config.SupplyCurrentLimitEnable = supplyEnable;
      config.SupplyCurrentLowerLimit = supplyLowerLimit;
      config.SupplyCurrentLimit = supplyLimit;
      config.SupplyCurrentLowerTime = supplyLimitTime;
      config.StatorCurrentLimitEnable = statorEnable;
      config.StatorCurrentLimit = statorLimit;
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds a `CurrentLimitsConfigs` for both supply and stator current limiting.
    
    **Parameter `supplyEnable`:** whether supply current limiting is enabled
    **Parameter `supplyLowerLimit`:** supply current lower (steady-state) limit in amps
    **Parameter `supplyLimit`:** peak supply current limit in amps
    **Parameter `supplyLimitTime`:** time (seconds) supply current may exceed `supplyLowerLimit`
    **Parameter `statorEnable`:** whether stator current limiting is enabled
    **Parameter `statorLimit`:** stator current limit in amps

### `public static ClosedLoopGeneralConfigs FXClosedLoopGeneralConfig(boolean continuousWrap)`

[Source lines 263–267](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L263)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `ClosedLoopGeneralConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `continuousWrap` | `boolean` | whether to enable continuous wrap for the closed-loop setpoint |

**Result:** Returns `ClosedLoopGeneralConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 263–267)"

    ```java
    public static ClosedLoopGeneralConfigs FXClosedLoopGeneralConfig(boolean continuousWrap) {
      ClosedLoopGeneralConfigs config = new ClosedLoopGeneralConfigs();
      config.ContinuousWrap = continuousWrap;
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds a `ClosedLoopGeneralConfigs` with continuous wrap enabled or disabled.
    Enable for mechanisms that rotate continuously (e.g. swerve steer); disable for limited-range arms.
    
    **Parameter `continuousWrap`:** whether to enable continuous wrap for the closed-loop setpoint

### `public static SoftwareLimitSwitchConfigs FXSoftwareLimitSwitchConfig( boolean enable, double forwardLimit, double reverseLimit)`

[Source lines 276–284](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L276)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `SoftwareLimitSwitchConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `enable` | `boolean` | whether both forward and reverse software limits are active **Parameter `forwardLimit`:** forward soft limit threshold in mechanism rotations **Parameter `reverseLimit`:** reverse soft limit threshold in mechanism rotat… |
| `forwardLimit` | `double` | forward soft limit threshold in mechanism rotations **Parameter `reverseLimit`:** reverse soft limit threshold in mechanism rotations |
| `reverseLimit` | `double` | reverse soft limit threshold in mechanism rotations |

**Result:** Returns `SoftwareLimitSwitchConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 276–284)"

    ```java
    public static SoftwareLimitSwitchConfigs FXSoftwareLimitSwitchConfig(
        boolean enable, double forwardLimit, double reverseLimit) {
      SoftwareLimitSwitchConfigs config = new SoftwareLimitSwitchConfigs();
      config.ForwardSoftLimitEnable = enable;
      config.ReverseSoftLimitEnable = enable;
      config.ForwardSoftLimitThreshold = forwardLimit;
      config.ReverseSoftLimitThreshold = reverseLimit;
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds a `SoftwareLimitSwitchConfigs` that applies the same enable state to both directions.
    
    **Parameter `enable`:** whether both forward and reverse software limits are active
    **Parameter `forwardLimit`:** forward soft limit threshold in mechanism rotations
    **Parameter `reverseLimit`:** reverse soft limit threshold in mechanism rotations

### `public static HardwareLimitSwitchConfigs FXHardwareLimitSwitchConfig( boolean forwardEnable, boolean reverseEnable, double forwardPosition, double reversePosition)`

[Source lines 294–305](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L294)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `HardwareLimitSwitchConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `forwardEnable` | `boolean` | whether the forward limit switch auto-sets position **Parameter `reverseEnable`:** whether the reverse limit switch auto-sets position **Parameter `forwardPosition`:** position (rotations) set when the forward limit is … |
| `reverseEnable` | `boolean` | whether the reverse limit switch auto-sets position **Parameter `forwardPosition`:** position (rotations) set when the forward limit is triggered **Parameter `reversePosition`:** position (rotations) set when the revers… |
| `forwardPosition` | `double` | position (rotations) set when the forward limit is triggered **Parameter `reversePosition`:** position (rotations) set when the reverse limit is triggered |
| `reversePosition` | `double` | position (rotations) set when the reverse limit is triggered |

**Result:** Returns `HardwareLimitSwitchConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 294–305)"

    ```java
    public static HardwareLimitSwitchConfigs FXHardwareLimitSwitchConfig(
        boolean forwardEnable,
        boolean reverseEnable,
        double forwardPosition,
        double reversePosition) {
      HardwareLimitSwitchConfigs config = new HardwareLimitSwitchConfigs();
      config.ForwardLimitAutosetPositionEnable = forwardEnable;
      config.ReverseLimitAutosetPositionEnable = reverseEnable;
      config.ForwardLimitAutosetPositionValue = forwardPosition;
      config.ReverseLimitAutosetPositionValue = reversePosition;
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds a `HardwareLimitSwitchConfigs` that auto-sets position on limit switch trigger.
    
    **Parameter `forwardEnable`:** whether the forward limit switch auto-sets position
    **Parameter `reverseEnable`:** whether the reverse limit switch auto-sets position
    **Parameter `forwardPosition`:** position (rotations) set when the forward limit is triggered
    **Parameter `reversePosition`:** position (rotations) set when the reverse limit is triggered

### `public static MotionMagicConfigs FXMotionMagicConfig(MotionMagicConstants constants)`

[Source lines 312–318](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L312)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `MotionMagicConfigs()`, `constants.acceleration()`, `constants.cruiseVelocity()`, `constants.jerk()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `constants` | `MotionMagicConstants` | cruise velocity, acceleration, and jerk limits |

**Result:** Returns `MotionMagicConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 312–318)"

    ```java
    public static MotionMagicConfigs FXMotionMagicConfig(MotionMagicConstants constants) {
      MotionMagicConfigs config = new MotionMagicConfigs();
      config.MotionMagicAcceleration = constants.acceleration();
      config.MotionMagicCruiseVelocity = constants.cruiseVelocity();
      config.MotionMagicJerk = constants.jerk();
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds a `MotionMagicConfigs` from a `MotionMagicConstants` record.
    
    **Parameter `constants`:** cruise velocity, acceleration, and jerk limits

### `public static VoltageConfigs FXVoltageConfig( double peakForwardVoltage, double peakReverseVoltage, double supplyVoltageTimeConstant)`

[Source lines 327–334](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L327)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `VoltageConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `peakForwardVoltage` | `double` | maximum forward output voltage **Parameter `peakReverseVoltage`:** maximum reverse output voltage (typically negative) **Parameter `supplyVoltageTimeConstant`:** low-pass filter time constant for supply voltage measurem… |
| `peakReverseVoltage` | `double` | maximum reverse output voltage (typically negative) **Parameter `supplyVoltageTimeConstant`:** low-pass filter time constant for supply voltage measurement |
| `supplyVoltageTimeConstant` | `double` | low-pass filter time constant for supply voltage measurement |

**Result:** Returns `VoltageConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 327–334)"

    ```java
    public static VoltageConfigs FXVoltageConfig(
        double peakForwardVoltage, double peakReverseVoltage, double supplyVoltageTimeConstant) {
      VoltageConfigs config = new VoltageConfigs();
      config.PeakForwardVoltage = peakForwardVoltage;
      config.PeakReverseVoltage = peakReverseVoltage;
      config.SupplyVoltageTimeConstant = supplyVoltageTimeConstant;
      return config;
    }
    ```

??? note "Author note from JavaDoc"

    Builds a `VoltageConfigs` for peak output and supply filtering.
    
    **Parameter `peakForwardVoltage`:** maximum forward output voltage
    **Parameter `peakReverseVoltage`:** maximum reverse output voltage (typically negative)
    **Parameter `supplyVoltageTimeConstant`:** low-pass filter time constant for supply voltage measurement

## Exposed fields and types

### `public class DeviceConfig`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L31)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Factory methods for building CTRE Phoenix 6 configuration objects and configuring devices.
