# ErrorChecker

`com.teamscreamrobotics.config.ErrorChecker`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java) · **4 callables** · **4 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public static boolean hasConfiguredWithoutErrors(StatusCode... statusCodes)`

[Source lines 19–25](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L19)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `okay`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `statusCodes` | `StatusCode...` | `StatusCode...` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 19–25)"

    ```java
    public static boolean hasConfiguredWithoutErrors(StatusCode... statusCodes) {
      boolean okay = true;
      for (StatusCode statusCode : statusCodes) {
        okay = okay && StatusCode.OK == statusCode;
      }
      return okay;
    }
    ```

### `public static void configureDevice( DeviceConfiguration config, String name, double bootAllowanceSeconds, boolean printInfo)`

[Source lines 38–67](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L38)

**Detailed behavior**

- The implementation executes 25 non-blank source lines.
- It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.
- It has 5 conditional paths: `Timer.getFPGATimestamp(`; `printInfo`; `!goodConfiguration` plus 2 more.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `Timer.getFPGATimestamp()`, `DriverStation.reportError()`, `config.configureSettings()`, `Thread.sleep()`, `e.printStackTrace()`, `DriverStation.reportWarning()`, `System.out.println()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `config` | `DeviceConfiguration` | `DeviceConfiguration` input consumed by the implementation shown below. |
| `name` | `String` | `String` input consumed by the implementation shown below. |
| `bootAllowanceSeconds` | `double` | Time value in seconds. |
| `printInfo` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 38–67)"

    ```java
    public static void configureDevice(
        DeviceConfiguration config, String name, double bootAllowanceSeconds, boolean printInfo) {
      boolean goodConfiguration = false;
      double startTime = Timer.getFPGATimestamp();
    
      int tries = 0;
      while (!goodConfiguration) {
        tries++;
    
        if (Timer.getFPGATimestamp() - startTime > bootAllowanceSeconds) {
          if (printInfo)
            DriverStation.reportError(
                "failed configuration for " + name + " initialization, took " + tries + " tries.",
                false);
          return;
        }
        goodConfiguration = config.configureSettings();
        if (!goodConfiguration)
          try {
            Thread.sleep(100);
          } catch (InterruptedException e) {
            e.printStackTrace();
          }
      }
      if (printInfo && tries > TRIES_TO_GENERATE_WARNING)
        DriverStation.reportWarning(
            "Possible issue with " + name + ". Configuration took " + tries + " tries", false);
      else if (printInfo)
        System.out.println("   " + name + " | configuration took " + tries + " tries. ");
    }
    ```

### `public static void configureDevice(DeviceConfiguration config, String name, boolean printInfo)`

[Source lines 74–76](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L74)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `config` | `DeviceConfiguration` | `DeviceConfiguration` input consumed by the implementation shown below. |
| `name` | `String` | `String` input consumed by the implementation shown below. |
| `printInfo` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 74–76)"

    ```java
    public static void configureDevice(DeviceConfiguration config, String name, boolean printInfo) {
      configureDevice(config, name, BOOT_ALLOWANCE_SECONDS, printInfo);
    }
    ```

### `public boolean configureSettings()`

[Source lines 84–84](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L84)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 84)"

    ```java
    public boolean configureSettings();
    ```

## Exposed fields and types

### `public class ErrorChecker`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L7)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static final double BOOT_ALLOWANCE_SECONDS = 3.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L10)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 2 times, so changing it can affect every control path that reads `BOOT_ALLOWANCE_SECONDS`.

### `public static final int TRIES_TO_GENERATE_WARNING = 5`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L12)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 2 times, so changing it can affect every control path that reads `TRIES_TO_GENERATE_WARNING`.

### `public static interface DeviceConfiguration`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L79)*

This exposed `interface` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
