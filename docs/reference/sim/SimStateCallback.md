# SimStateCallback

`com.teamscreamrobotics.sim.SimStateCallback`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimStateCallback.java) · **1 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `void accept(double position, double velocity)`

[Source lines 6–6](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimStateCallback.java#L6)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `position` | `double` | Position in the units required by this API and configuration. |
| `velocity` | `double` | Velocity/speed in the units required by this API and configuration. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 6)"

    ```java
    void accept(double position, double velocity);
    ```

## Exposed fields and types

### `public interface SimStateCallback`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/sim/SimStateCallback.java#L5)*

This exposed `interface` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Callback invoked after each simulation step with the updated position and velocity.
