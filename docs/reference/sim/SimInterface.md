# SimInterface

`com.teamscreamrobotics.sim.SimInterface`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java) · **4 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `void update(double deltaTime)`

[Source lines 10–10](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java#L10)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `deltaTime` | `double` | elapsed time since the last call, in seconds |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 10)"

    ```java
    void update(double deltaTime);
    ```

??? note "Author note from JavaDoc"

    Advances the simulation by `deltaTime` seconds.
    
    **Parameter `deltaTime`:** elapsed time since the last call, in seconds

### `void setInputVoltage(double voltage)`

[Source lines 17–17](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java#L17)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `voltage` | `double` | input voltage in volts |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 17)"

    ```java
    void setInputVoltage(double voltage);
    ```

??? note "Author note from JavaDoc"

    Applies the motor input voltage to the simulation.
    
    **Parameter `voltage`:** input voltage in volts

### `double getPosition()`

[Source lines 20–20](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java#L20)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 20)"

    ```java
    double getPosition();
    ```

??? note "Author note from JavaDoc"

    Returns the simulated mechanism position in rotations.

### `double getVelocity()`

[Source lines 23–23](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java#L23)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 23)"

    ```java
    double getVelocity();
    ```

??? note "Author note from JavaDoc"

    Returns the simulated mechanism velocity in rotations per second.

## Exposed fields and types

### `public interface SimInterface`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimInterface.java#L4)*

This exposed `interface` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Common interface for physics simulation backends (DC motor, elevator, arm, flywheel).
