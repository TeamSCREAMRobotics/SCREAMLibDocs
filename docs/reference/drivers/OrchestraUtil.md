# OrchestraUtil

`com.teamscreamrobotics.drivers.OrchestraUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java) · **5 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public static void add(TalonFX... FXs)`

[Source lines 16–20](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L16)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `orchestra.addInstrument()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `FXs` | `TalonFX...` | the motors to add |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 16–20)"

    ```java
    public static void add(TalonFX... FXs) {
      for (TalonFX fx : FXs) {
        orchestra.addInstrument(fx);
      }
    }
    ```

??? note "Author note from JavaDoc"

    Registers one or more TalonFX motors as instruments in the orchestra.
    
    **Parameter `FXs`:** the motors to add

### `public static void play(String fileName)`

[Source lines 27–30](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L27)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Key collaborators/calls: `orchestra.loadMusic()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `fileName` | `String` | the file name without the `.chrp` extension |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 27–30)"

    ```java
    public static void play(String fileName) {
      orchestra.loadMusic(fileName + ".chrp");
      orchestra.play();
    }
    ```

??? note "Author note from JavaDoc"

    Loads and plays a `.chrp` music file from the deploy directory.
    
    **Parameter `fileName`:** the file name without the `.chrp` extension

### `public static boolean isPlaying()`

[Source lines 33–35](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L33)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `orchestra.isPlaying()`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 33–35)"

    ```java
    public static boolean isPlaying() {
      return orchestra.isPlaying();
    }
    ```

??? note "Author note from JavaDoc"

    Returns `true` if the orchestra is currently playing.

### `public static void pause()`

[Source lines 38–40](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L38)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 38–40)"

    ```java
    public static void pause() {
      orchestra.pause();
    }
    ```

??? note "Author note from JavaDoc"

    Pauses playback without resetting the track position.

### `public static void stop()`

[Source lines 43–45](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L43)

**Detailed behavior**

- The implementation executes 1 non-blank source line.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 43–45)"

    ```java
    public static void stop() {
      orchestra.stop();
    }
    ```

??? note "Author note from JavaDoc"

    Stops playback and resets the track position to the beginning.

## Exposed fields and types

### `public class OrchestraUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/OrchestraUtil.java#L7)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Singleton wrapper around a CTRE `Orchestra` for playing `.chrp` music files.
