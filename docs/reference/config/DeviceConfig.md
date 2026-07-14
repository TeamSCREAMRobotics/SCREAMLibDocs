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
| `name` | `String` | `String` input consumed by the implementation shown below. |
| `fx` | `TalonFX` | `TalonFX` input consumed by the implementation shown below. |
| `config` | `TalonFXConfiguration` | `TalonFXConfiguration` input consumed by the implementation shown below. |

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
| `name` | `String` | `String` input consumed by the implementation shown below. |
| `encoder` | `CANcoder` | `CANcoder` input consumed by the implementation shown below. |
| `config` | `CANcoderConfiguration` | `CANcoderConfiguration` input consumed by the implementation shown below. |

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
| `name` | `String` | `String` input consumed by the implementation shown below. |
| `pigeon` | `Pigeon2` | `Pigeon2` input consumed by the implementation shown below. |
| `config` | `Pigeon2Configuration` | `Pigeon2Configuration` input consumed by the implementation shown below. |
| `updateFrequencyHz` | `double` | `double` input consumed by the implementation shown below. |

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
| `beepOnBoot` | `boolean` | `boolean` input consumed by the implementation shown below. |
| `beepOnConfig` | `boolean` | `boolean` input consumed by the implementation shown below. |
| `allowMusicDuringDisabled` | `boolean` | `boolean` input consumed by the implementation shown below. |

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

### `public static MotorOutputConfigs FXMotorOutputConfig( InvertedValue invert, NeutralModeValue neutralMode)`

[Source lines 138–144](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L138)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `MotorOutputConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `invert` | `InvertedValue` | `InvertedValue` input consumed by the implementation shown below. |
| `neutralMode` | `NeutralModeValue` | `NeutralModeValue` input consumed by the implementation shown below. |

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

### `public static FeedbackConfigs FXFeedbackConfig( FeedbackSensorSourceValue sensor, int remoteSensorID, double sensorToMechGR, double rotorToSensorGR, Rotation2d sensorOffset)`

[Source lines 155–168](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L155)

**Detailed behavior**

- The implementation executes 7 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `FeedbackConfigs()`, `sensorOffset.getRotations()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `sensor` | `FeedbackSensorSourceValue` | `FeedbackSensorSourceValue` input consumed by the implementation shown below. |
| `remoteSensorID` | `int` | `int` input consumed by the implementation shown below. |
| `sensorToMechGR` | `double` | `double` input consumed by the implementation shown below. |
| `rotorToSensorGR` | `double` | `double` input consumed by the implementation shown below. |
| `sensorOffset` | `Rotation2d` | `Rotation2d` input consumed by the implementation shown below. |

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

### `public static Slot0Configs FXPIDConfig( ScreamPIDConstants constants, FeedforwardConstants ffConstants)`

[Source lines 176–179](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L176)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `constants.getSlot0Configs(ffConstants)`.
- Key collaborators/calls: `constants.getSlot0Configs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `constants` | `ScreamPIDConstants` | `ScreamPIDConstants` input consumed by the implementation shown below. |
| `ffConstants` | `FeedforwardConstants` | `FeedforwardConstants` input consumed by the implementation shown below. |

**Result:** Returns `Slot0Configs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 176–179)"

    ```java
    public static Slot0Configs FXPIDConfig(
        ScreamPIDConstants constants, FeedforwardConstants ffConstants) {
      return constants.getSlot0Configs(ffConstants);
    }
    ```

### `public static Slot0Configs FXPIDConfig(ScreamPIDConstants constants)`

[Source lines 186–188](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L186)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `constants.getSlot0Configs(new FeedforwardConstants())`.
- Key collaborators/calls: `constants.getSlot0Configs()`, `FeedforwardConstants()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `constants` | `ScreamPIDConstants` | `ScreamPIDConstants` input consumed by the implementation shown below. |

**Result:** Returns `Slot0Configs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 186–188)"

    ```java
    public static Slot0Configs FXPIDConfig(ScreamPIDConstants constants) {
      return constants.getSlot0Configs(new FeedforwardConstants());
    }
    ```

### `public static OpenLoopRampsConfigs FXOpenLoopRampConfig(double ramp)`

[Source lines 195–199](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L195)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `OpenLoopRampsConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `ramp` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `OpenLoopRampsConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 195–199)"

    ```java
    public static OpenLoopRampsConfigs FXOpenLoopRampConfig(double ramp) {
      OpenLoopRampsConfigs config = new OpenLoopRampsConfigs();
      config.DutyCycleOpenLoopRampPeriod = ramp;
      return config;
    }
    ```

### `public static ClosedLoopRampsConfigs FXClosedLoopRampConfig(double ramp)`

[Source lines 206–210](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L206)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `ClosedLoopRampsConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `ramp` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `ClosedLoopRampsConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 206–210)"

    ```java
    public static ClosedLoopRampsConfigs FXClosedLoopRampConfig(double ramp) {
      ClosedLoopRampsConfigs config = new ClosedLoopRampsConfigs();
      config.DutyCycleClosedLoopRampPeriod = ramp;
      return config;
    }
    ```

### `public static CurrentLimitsConfigs FXSupplyCurrentLimitsConfig( boolean enable, double lowerLimit, double limit, double limitTime)`

[Source lines 220–228](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L220)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `CurrentLimitsConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `enable` | `boolean` | Enables the behavior when `true`; disables it when `false`. |
| `lowerLimit` | `double` | `double` input consumed by the implementation shown below. |
| `limit` | `double` | `double` input consumed by the implementation shown below. |
| `limitTime` | `double` | `double` input consumed by the implementation shown below. |

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

### `public static CurrentLimitsConfigs FXCurrentLimitsConfig( boolean supplyEnable, double supplyLowerLimit, double supplyLimit, double supplyLimitTime, boolean statorEnable, double statorLimit)`

[Source lines 240–255](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L240)

**Detailed behavior**

- The implementation executes 8 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `CurrentLimitsConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `supplyEnable` | `boolean` | Enables the behavior when `true`; disables it when `false`. |
| `supplyLowerLimit` | `double` | `double` input consumed by the implementation shown below. |
| `supplyLimit` | `double` | `double` input consumed by the implementation shown below. |
| `supplyLimitTime` | `double` | `double` input consumed by the implementation shown below. |
| `statorEnable` | `boolean` | Enables the behavior when `true`; disables it when `false`. |
| `statorLimit` | `double` | `double` input consumed by the implementation shown below. |

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

### `public static ClosedLoopGeneralConfigs FXClosedLoopGeneralConfig(boolean continuousWrap)`

[Source lines 263–267](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L263)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `ClosedLoopGeneralConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `continuousWrap` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** Returns `ClosedLoopGeneralConfigs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 263–267)"

    ```java
    public static ClosedLoopGeneralConfigs FXClosedLoopGeneralConfig(boolean continuousWrap) {
      ClosedLoopGeneralConfigs config = new ClosedLoopGeneralConfigs();
      config.ContinuousWrap = continuousWrap;
      return config;
    }
    ```

### `public static SoftwareLimitSwitchConfigs FXSoftwareLimitSwitchConfig( boolean enable, double forwardLimit, double reverseLimit)`

[Source lines 276–284](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L276)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `SoftwareLimitSwitchConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `enable` | `boolean` | Enables the behavior when `true`; disables it when `false`. |
| `forwardLimit` | `double` | `double` input consumed by the implementation shown below. |
| `reverseLimit` | `double` | `double` input consumed by the implementation shown below. |

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

### `public static HardwareLimitSwitchConfigs FXHardwareLimitSwitchConfig( boolean forwardEnable, boolean reverseEnable, double forwardPosition, double reversePosition)`

[Source lines 294–305](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L294)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `HardwareLimitSwitchConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `forwardEnable` | `boolean` | Enables the behavior when `true`; disables it when `false`. |
| `reverseEnable` | `boolean` | Enables the behavior when `true`; disables it when `false`. |
| `forwardPosition` | `double` | Position in the units required by this API and configuration. |
| `reversePosition` | `double` | Position in the units required by this API and configuration. |

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

### `public static MotionMagicConfigs FXMotionMagicConfig(MotionMagicConstants constants)`

[Source lines 312–318](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L312)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `MotionMagicConfigs()`, `constants.acceleration()`, `constants.cruiseVelocity()`, `constants.jerk()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `constants` | `MotionMagicConstants` | `MotionMagicConstants` input consumed by the implementation shown below. |

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

### `public static VoltageConfigs FXVoltageConfig( double peakForwardVoltage, double peakReverseVoltage, double supplyVoltageTimeConstant)`

[Source lines 327–334](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L327)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `VoltageConfigs()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `peakForwardVoltage` | `double` | Voltage value in volts. |
| `peakReverseVoltage` | `double` | Voltage value in volts. |
| `supplyVoltageTimeConstant` | `double` | Voltage value in volts. |

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

## Exposed fields and types

### `public class DeviceConfig`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/DeviceConfig.java#L31)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
