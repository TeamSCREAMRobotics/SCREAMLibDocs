# PigeonHelper

`com.teamscreamrobotics.drivers.PigeonHelper`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java) · **7 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public PigeonHelper(Pigeon2 pigeon)`

[Source lines 20–25](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L20)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- Key collaborators/calls: `pigeon.getAngularVelocityXWorld()`, `pigeon.getAngularVelocityYWorld()`, `pigeon.getAngularVelocityZWorld()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pigeon` | `Pigeon2` | `Pigeon2` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `PigeonHelper` instance.

??? example "Implementation (source lines 20–25)"

    ```java
    public PigeonHelper(Pigeon2 pigeon) {
        // Get velocity status signals
        velocityX = pigeon.getAngularVelocityXWorld();
        velocityY = pigeon.getAngularVelocityYWorld();
        velocityZ = pigeon.getAngularVelocityZWorld();
    }
    ```

### `public double getVelocityX()`

[Source lines 30–33](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L30)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `velocityX.getValueAsDouble()`.
- Key collaborators/calls: `velocityX.refresh()`, `velocityX.getValueAsDouble()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 30–33)"

    ```java
    public double getVelocityX() {
        velocityX.refresh();
        return velocityX.getValueAsDouble();
    }
    ```

### `public double getVelocityY()`

[Source lines 38–41](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L38)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `velocityY.getValueAsDouble()`.
- Key collaborators/calls: `velocityY.refresh()`, `velocityY.getValueAsDouble()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 38–41)"

    ```java
    public double getVelocityY() {
        velocityY.refresh();
        return velocityY.getValueAsDouble();
    }
    ```

### `public double getVelocityZ()`

[Source lines 46–49](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L46)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `velocityZ.getValueAsDouble()`.
- Key collaborators/calls: `velocityZ.refresh()`, `velocityZ.getValueAsDouble()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 46–49)"

    ```java
    public double getVelocityZ() {
        velocityZ.refresh();
        return velocityZ.getValueAsDouble();
    }
    ```

### `public double[] getAllVelocities()`

[Source lines 55–66](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L55)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- Return path: `new double[] { velocityX.getValueAsDouble(), velocityY.getValueAsDouble(), velocityZ.getValueAsDouble() }`.
- Key collaborators/calls: `velocityX.refresh()`, `velocityY.refresh()`, `velocityZ.refresh()`, `velocityX.getValueAsDouble()`, `velocityY.getValueAsDouble()`, `velocityZ.getValueAsDouble()`.

**Inputs:** None.

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 55–66)"

    ```java
    public double[] getAllVelocities() {
        // Refresh all signals together for better performance
        velocityX.refresh();
        velocityY.refresh();
        velocityZ.refresh();
    
        return new double[] {
            velocityX.getValueAsDouble(),
            velocityY.getValueAsDouble(),
            velocityZ.getValueAsDouble()
        };
    }
    ```

### `public double getYawRate()`

[Source lines 71–73](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L71)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getVelocityZ()`.
- Key collaborators/calls: `getVelocityZ()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 71–73)"

    ```java
    public double getYawRate() {
        return getVelocityZ();
    }
    ```

### `public double getYawRateRadians()`

[Source lines 78–81](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L78)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `Math.toRadians(velocityZ.getValueAsDouble())`.
- Key collaborators/calls: `velocityZ.refresh()`, `Math.toRadians()`, `velocityZ.getValueAsDouble()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 78–81)"

    ```java
    public double getYawRateRadians() {
        velocityZ.refresh();
        return Math.toRadians(velocityZ.getValueAsDouble());
    }
    ```

## Exposed fields and types

### `public class PigeonHelper`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/drivers/PigeonHelper.java#L9)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
