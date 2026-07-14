# ErrorChecker

`com.teamscreamrobotics.config.ErrorChecker`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java) · **4 callables** · **4 exposed fields/types**

## Public and protected callables

### `public static boolean hasConfiguredWithoutErrors(StatusCode... statusCodes)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L19)*

This method takes a list of StatusCodes and returns true if they are all OK. When we configure
our devices, we wrap all our our calls to the devices in this method to tell us if the device
has configured correctly, or if there are errors.

### `public static void configureDevice( DeviceConfiguration config, String name, double bootAllowanceSeconds, boolean printInfo)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L38)*

This method does the actual configuration for the device. It repeatedly calls
config.configureSettings() until there is a successful configuration or until it times out. If
printInfo is true, it will print if the configuration succeeded and how many tries it took

### `public static void configureDevice(DeviceConfiguration config, String name, boolean printInfo)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L74)*

This method does the actual configuration for the device. It repeatedly calls
config.configureSettings() until there is a successful configuration or until it times out. If
printInfo is true, it will print if the configuration succeeded and how many tries it took

### `public boolean configureSettings()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L84)*

This method does all of the configuration logic for the device and returns true only if the
configuration is good.

## Exposed fields and types

### `public class ErrorChecker`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L7)*

### `public static final double BOOT_ALLOWANCE_SECONDS = 3.0`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L10)*

Seconds after robot start during which configuration retries are allowed.

### `public static final int TRIES_TO_GENERATE_WARNING = 5`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L12)*

Number of configuration attempts before a DS warning is generated.

### `public static interface DeviceConfiguration`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/config/ErrorChecker.java#L79)*

This interface is where all of our logic for configuring each device goes.
