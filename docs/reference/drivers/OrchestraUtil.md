# OrchestraUtil

`com.teamscreamrobotics.drivers.OrchestraUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java) · **5 callables** · **1 exposed fields/types**

## Public and protected callables

### `public static void add(TalonFX... FXs)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L16)*

Registers one or more TalonFX motors as instruments in the orchestra.

**Parameter `FXs`:** the motors to add

### `public static void play(String fileName)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L27)*

Loads and plays a `.chrp` music file from the deploy directory.

**Parameter `fileName`:** the file name without the `.chrp` extension

### `public static boolean isPlaying()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L33)*

Returns `true` if the orchestra is currently playing.

### `public static void pause()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L38)*

Pauses playback without resetting the track position.

### `public static void stop()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L43)*

Stops playback and resets the track position to the beginning.

## Exposed fields and types

### `public class OrchestraUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L7)*

Singleton wrapper around a CTRE `Orchestra` for playing `.chrp` music files.
