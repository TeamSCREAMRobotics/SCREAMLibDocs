# ScreamPIDConstants

`com.teamscreamrobotics.pid.ScreamPIDConstants`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java) · **59 callables** · **3 exposed fields/types** · **2 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2026: Build a Phoenix slot with PID and feedforward gains

[`src/main/java/frc2026/tars/subsystems/shooter/flywheel/FlywheelConstants.java` lines 40–55](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/flywheel/FlywheelConstants.java#L40-L55)

```java
// FLYWHEEL_CONFIG.slot0 =
//     new ScreamPIDConstants(12.0, 1.0, 0.0)
//         .getSlot0Configs(new FeedforwardConstants(kV, 0.34091, 0.0, (kV * 0.25) + 0.05));

FLYWHEEL_CONFIG.slot0 =
    new ScreamPIDConstants(12.5, 2.08, 0.0)
        .getSlot0Configs(new FeedforwardConstants(0.12248, 0.33734, 0.0, 0.5));

FLYWHEEL_CONFIG.neutralMode = NeutralModeValue.Coast;

FLYWHEEL_CONFIG.enableSupplyCurrentLimit = true;
FLYWHEEL_CONFIG.supplyCurrentLimit = 50;
FLYWHEEL_CONFIG.sensorToMechRatio = FLYWHEEL_REDUCTION;

FLYWHEEL_CONFIG.peakForwardTorqueCurrent = 160.0;
FLYWHEEL_CONFIG.peakReverseTorqueCurrent = 0.0;
```

### 2026: Configure position gains and Motion Magic values

[`src/main/java/frc2026/tars/subsystems/shooter/hood/HoodConstants.java` lines 30–47](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/hood/HoodConstants.java#L30-L47)

```java
HOOD_CONFIG.masterConstants =
    new TalonFXConstants(new CANDevice(8), InvertedValue.Clockwise_Positive);

HOOD_CONFIG.slot0 =
    new ScreamPIDConstants(90.0, 0, 0)
        .getSlot0Configs(new FeedforwardConstants(0, 0.0, 0.0, 0));

// P: 55.0

HOOD_CONFIG.neutralMode = NeutralModeValue.Brake;
HOOD_CONFIG.sensorToMechRatio = HOOD_REDUCTION;
HOOD_CONFIG.enableSupplyCurrentLimit = true;
HOOD_CONFIG.supplyCurrentLimit = 15;

HOOD_CONFIG.maxUnitsLimit = MAX_UNITS;

HOOD_CONFIG.acceleration = 20.0;
HOOD_CONFIG.cruiseVelocity = 30.0;
```

## Public and protected callables

### `public FeedforwardConstants(double kV, double kS, double kG, double kA)`

[Source lines 21–23](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L21)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It delegates initialization to another constructor in the same type with `kV, kS, kG, kA, GravityTypeValue.Elevator_Static`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `kV` | `double` | `double` input consumed by the implementation shown below. |
| `kS` | `double` | `double` input consumed by the implementation shown below. |
| `kG` | `double` | `double` input consumed by the implementation shown below. |
| `kA` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `FeedforwardConstants` instance.

??? example "Implementation (source lines 21–23)"

    ```java
    public FeedforwardConstants(double kV, double kS, double kG, double kA) {
      this(kV, kS, kG, kA, GravityTypeValue.Elevator_Static);
    }
    ```

### `public FeedforwardConstants()`

[Source lines 25–27](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L25)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It delegates initialization to another constructor in the same type with `0, 0, 0, 0, GravityTypeValue.Elevator_Static`.

**Inputs:** None.

**Result:** Constructs and initializes a `FeedforwardConstants` instance.

??? example "Implementation (source lines 25–27)"

    ```java
    public FeedforwardConstants() {
      this(0, 0, 0, 0, GravityTypeValue.Elevator_Static);
    }
    ```

### `public ScreamPIDConstants()`

[Source lines 39–39](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L39)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs:** None.

**Result:** Constructs and initializes a `ScreamPIDConstants` instance.

??? example "Implementation (source lines 39)"

    ```java
    public ScreamPIDConstants() {}
    ```

### `public ScreamPIDConstants(double p, double i, double d)`

[Source lines 48–52](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L48)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `kD`, `kI`, `kP`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `p` | `double` | `double` input consumed by the implementation shown below. |
| `i` | `double` | `double` input consumed by the implementation shown below. |
| `d` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `ScreamPIDConstants` instance.

??? example "Implementation (source lines 48–52)"

    ```java
    public ScreamPIDConstants(double p, double i, double d) {
      this.kP = p;
      this.kI = i;
      this.kD = d;
    }
    ```

### `public ScreamPIDConstants(double p, double i, double d, double f)`

[Source lines 62–67](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L62)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It changes object/subclass state through `kD`, `kF`, `kI`, `kP`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `p` | `double` | `double` input consumed by the implementation shown below. |
| `i` | `double` | `double` input consumed by the implementation shown below. |
| `d` | `double` | `double` input consumed by the implementation shown below. |
| `f` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `ScreamPIDConstants` instance.

??? example "Implementation (source lines 62–67)"

    ```java
    public ScreamPIDConstants(double p, double i, double d, double f) {
      this.kP = p;
      this.kI = i;
      this.kD = d;
      this.kF = f;
    }
    ```

### `public void setPID(double p, double i, double d)`

[Source lines 70–74](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L70)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `kD`, `kI`, `kP`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `p` | `double` | `double` input consumed by the implementation shown below. |
| `i` | `double` | `double` input consumed by the implementation shown below. |
| `d` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 70–74)"

    ```java
    public void setPID(double p, double i, double d) {
      this.kP = p;
      this.kI = i;
      this.kD = d;
    }
    ```

### `public void setPIDF(double p, double i, double d, double f)`

[Source lines 77–82](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L77)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It changes object/subclass state through `kD`, `kF`, `kI`, `kP`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `p` | `double` | `double` input consumed by the implementation shown below. |
| `i` | `double` | `double` input consumed by the implementation shown below. |
| `d` | `double` | `double` input consumed by the implementation shown below. |
| `f` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 77–82)"

    ```java
    public void setPIDF(double p, double i, double d, double f) {
      this.kP = p;
      this.kI = i;
      this.kD = d;
      this.kF = f;
    }
    ```

### `public void setPeriod(double period)`

[Source lines 85–87](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L85)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `period`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `period` | `double` | Time value in seconds. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 85–87)"

    ```java
    public void setPeriod(double period) {
      this.period = period;
    }
    ```

### `public void setP(double p)`

[Source lines 90–92](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L90)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `kP`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `p` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 90–92)"

    ```java
    public void setP(double p) {
      this.kP = p;
    }
    ```

### `public void setI(double i)`

[Source lines 95–97](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L95)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `kI`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `i` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 95–97)"

    ```java
    public void setI(double i) {
      this.kI = i;
    }
    ```

### `public void setD(double d)`

[Source lines 100–102](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L100)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `kD`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `d` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 100–102)"

    ```java
    public void setD(double d) {
      this.kD = d;
    }
    ```

### `public void setF(double f)`

[Source lines 105–107](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L105)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `kF`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `f` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 105–107)"

    ```java
    public void setF(double f) {
      this.kF = f;
    }
    ```

### `public void setIntegralZone(double Izone)`

[Source lines 110–112](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L110)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `integralZone`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `Izone` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 110–112)"

    ```java
    public void setIntegralZone(double Izone) {
      this.integralZone = Izone;
    }
    ```

### `public void setIntegralAccumulatorBounds(double max, double min)`

[Source lines 120–123](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L120)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `maxIntegralAccumulator`, `minIntegralAccumulator`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `max` | `double` | `double` input consumed by the implementation shown below. |
| `min` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 120–123)"

    ```java
    public void setIntegralAccumulatorBounds(double max, double min) {
      this.maxIntegralAccumulator = max;
      this.minIntegralAccumulator = min;
    }
    ```

### `public void setOutputBounds(double max, double min)`

[Source lines 131–134](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L131)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `maxOutput`, `minOutput`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `max` | `double` | `double` input consumed by the implementation shown below. |
| `min` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 131–134)"

    ```java
    public void setOutputBounds(double max, double min) {
      this.maxOutput = max;
      this.minOutput = min;
    }
    ```

### `public ScreamPIDConstants withPID(double p, double i, double d)`

[Source lines 137–142](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L137)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It changes object/subclass state through `kD`, `kI`, `kP`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `p` | `double` | `double` input consumed by the implementation shown below. |
| `i` | `double` | `double` input consumed by the implementation shown below. |
| `d` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 137–142)"

    ```java
    public ScreamPIDConstants withPID(double p, double i, double d) {
      this.kP = p;
      this.kI = i;
      this.kD = d;
      return this;
    }
    ```

### `public ScreamPIDConstants withPIDF(double p, double i, double d, double f)`

[Source lines 145–151](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L145)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It changes object/subclass state through `kD`, `kF`, `kI`, `kP`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `p` | `double` | `double` input consumed by the implementation shown below. |
| `i` | `double` | `double` input consumed by the implementation shown below. |
| `d` | `double` | `double` input consumed by the implementation shown below. |
| `f` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 145–151)"

    ```java
    public ScreamPIDConstants withPIDF(double p, double i, double d, double f) {
      this.kP = p;
      this.kI = i;
      this.kD = d;
      this.kF = f;
      return this;
    }
    ```

### `public ScreamPIDConstants withPeriod(double period)`

[Source lines 154–157](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L154)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `period`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `period` | `double` | Time value in seconds. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 154–157)"

    ```java
    public ScreamPIDConstants withPeriod(double period) {
      this.period = period;
      return this;
    }
    ```

### `public ScreamPIDConstants withP(double p)`

[Source lines 160–163](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L160)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `kP`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `p` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 160–163)"

    ```java
    public ScreamPIDConstants withP(double p) {
      this.kP = p;
      return this;
    }
    ```

### `public ScreamPIDConstants withI(double i)`

[Source lines 166–169](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L166)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `kI`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `i` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 166–169)"

    ```java
    public ScreamPIDConstants withI(double i) {
      this.kI = i;
      return this;
    }
    ```

### `public ScreamPIDConstants withD(double d)`

[Source lines 172–175](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L172)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `kD`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `d` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 172–175)"

    ```java
    public ScreamPIDConstants withD(double d) {
      this.kD = d;
      return this;
    }
    ```

### `public ScreamPIDConstants withF(double f)`

[Source lines 178–181](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L178)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `kF`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `f` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 178–181)"

    ```java
    public ScreamPIDConstants withF(double f) {
      this.kF = f;
      return this;
    }
    ```

### `public ScreamPIDConstants withIntegralZone(double Izone)`

[Source lines 184–187](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L184)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `integralZone`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `Izone` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 184–187)"

    ```java
    public ScreamPIDConstants withIntegralZone(double Izone) {
      this.integralZone = Izone;
      return this;
    }
    ```

### `public ScreamPIDConstants withIntegralAccumulatorBounds(double max, double min)`

[Source lines 190–194](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L190)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `maxIntegralAccumulator`, `minIntegralAccumulator`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `max` | `double` | `double` input consumed by the implementation shown below. |
| `min` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 190–194)"

    ```java
    public ScreamPIDConstants withIntegralAccumulatorBounds(double max, double min) {
      this.maxIntegralAccumulator = max;
      this.minIntegralAccumulator = min;
      return this;
    }
    ```

### `public ScreamPIDConstants withOutputBounds(double max, double min)`

[Source lines 197–201](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L197)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `maxOutput`, `minOutput`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `max` | `double` | `double` input consumed by the implementation shown below. |
| `min` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 197–201)"

    ```java
    public ScreamPIDConstants withOutputBounds(double max, double min) {
      this.maxOutput = max;
      this.minOutput = min;
      return this;
    }
    ```

### `public double period()`

[Source lines 204–206](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L204)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `period`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 204–206)"

    ```java
    public double period() {
      return period;
    }
    ```

### `public double kP()`

[Source lines 209–211](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L209)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `kP`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 209–211)"

    ```java
    public double kP() {
      return kP;
    }
    ```

### `public double kI()`

[Source lines 214–216](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L214)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `kI`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 214–216)"

    ```java
    public double kI() {
      return kI;
    }
    ```

### `public double kD()`

[Source lines 219–221](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L219)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `kD`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 219–221)"

    ```java
    public double kD() {
      return kD;
    }
    ```

### `public double kF()`

[Source lines 224–226](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L224)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `kF`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 224–226)"

    ```java
    public double kF() {
      return kF;
    }
    ```

### `public double integralZone()`

[Source lines 229–231](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L229)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `integralZone`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 229–231)"

    ```java
    public double integralZone() {
      return integralZone;
    }
    ```

### `public double maxIntegralAccumulator()`

[Source lines 234–236](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L234)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `maxIntegralAccumulator`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 234–236)"

    ```java
    public double maxIntegralAccumulator() {
      return maxIntegralAccumulator;
    }
    ```

### `public double minIntegralAccumulator()`

[Source lines 239–241](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L239)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `minIntegralAccumulator`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 239–241)"

    ```java
    public double minIntegralAccumulator() {
      return minIntegralAccumulator;
    }
    ```

### `public double maxOutput()`

[Source lines 244–246](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L244)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `maxOutput`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 244–246)"

    ```java
    public double maxOutput() {
      return maxOutput;
    }
    ```

### `public double minOutput()`

[Source lines 249–251](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L249)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `minOutput`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 249–251)"

    ```java
    public double minOutput() {
      return minOutput;
    }
    ```

### `public Slot0Configs getSlot0Configs(FeedforwardConstants ffConstants)`

[Source lines 258–269](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L258)

**Detailed behavior**

- The implementation executes 10 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `Slot0Configs()`, `ffConstants.kV()`, `ffConstants.kA()`, `ffConstants.kG()`, `ffConstants.kS()`, `ffConstants.gravityType()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `ffConstants` | `FeedforwardConstants` | `FeedforwardConstants` input consumed by the implementation shown below. |

**Result:** Returns `Slot0Configs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 258–269)"

    ```java
    public Slot0Configs getSlot0Configs(FeedforwardConstants ffConstants) {
      Slot0Configs config = new Slot0Configs();
      config.kP = kP;
      config.kI = kI;
      config.kD = kD;
      config.kV = ffConstants.kV();
      config.kA = ffConstants.kA();
      config.kG = ffConstants.kG();
      config.kS = ffConstants.kS();
      config.GravityType = ffConstants.gravityType();
      return config;
    }
    ```

### `public static ScreamPIDConstants fromSlot0Configs(Slot0Configs configs)`

[Source lines 276–278](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L276)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new ScreamPIDConstants(configs.kP, configs.kI, configs.kD)`.
- Key collaborators/calls: `ScreamPIDConstants()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `configs` | `Slot0Configs` | `Slot0Configs` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 276–278)"

    ```java
    public static ScreamPIDConstants fromSlot0Configs(Slot0Configs configs) {
      return new ScreamPIDConstants(configs.kP, configs.kI, configs.kD);
    }
    ```

### `public Slot1Configs getSlot1Configs(FeedforwardConstants ffConstants)`

[Source lines 285–295](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L285)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `Slot1Configs()`, `ffConstants.kV()`, `ffConstants.kA()`, `ffConstants.kG()`, `ffConstants.kS()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `ffConstants` | `FeedforwardConstants` | `FeedforwardConstants` input consumed by the implementation shown below. |

**Result:** Returns `Slot1Configs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 285–295)"

    ```java
    public Slot1Configs getSlot1Configs(FeedforwardConstants ffConstants) {
      Slot1Configs config = new Slot1Configs();
      config.kP = kP;
      config.kI = kI;
      config.kD = kD;
      config.kV = ffConstants.kV();
      config.kA = ffConstants.kA();
      config.kG = ffConstants.kG();
      config.kS = ffConstants.kS();
      return config;
    }
    ```

### `public static ScreamPIDConstants fromSlot1Configs(Slot1Configs configs)`

[Source lines 302–304](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L302)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new ScreamPIDConstants(configs.kP, configs.kI, configs.kD)`.
- Key collaborators/calls: `ScreamPIDConstants()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `configs` | `Slot1Configs` | `Slot1Configs` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 302–304)"

    ```java
    public static ScreamPIDConstants fromSlot1Configs(Slot1Configs configs) {
      return new ScreamPIDConstants(configs.kP, configs.kI, configs.kD);
    }
    ```

### `public Slot2Configs getSlot2Configs(FeedforwardConstants ffConstants)`

[Source lines 311–321](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L311)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- Return path: `config`.
- Key collaborators/calls: `Slot2Configs()`, `ffConstants.kV()`, `ffConstants.kA()`, `ffConstants.kG()`, `ffConstants.kS()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `ffConstants` | `FeedforwardConstants` | `FeedforwardConstants` input consumed by the implementation shown below. |

**Result:** Returns `Slot2Configs`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 311–321)"

    ```java
    public Slot2Configs getSlot2Configs(FeedforwardConstants ffConstants) {
      Slot2Configs config = new Slot2Configs();
      config.kP = kP;
      config.kI = kI;
      config.kD = kD;
      config.kV = ffConstants.kV();
      config.kA = ffConstants.kA();
      config.kG = ffConstants.kG();
      config.kS = ffConstants.kS();
      return config;
    }
    ```

### `public static ScreamPIDConstants fromSlot2Configs(Slot2Configs configs)`

[Source lines 328–330](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L328)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new ScreamPIDConstants(configs.kP, configs.kI, configs.kD)`.
- Key collaborators/calls: `ScreamPIDConstants()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `configs` | `Slot2Configs` | `Slot2Configs` input consumed by the implementation shown below. |

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 328–330)"

    ```java
    public static ScreamPIDConstants fromSlot2Configs(Slot2Configs configs) {
      return new ScreamPIDConstants(configs.kP, configs.kI, configs.kD);
    }
    ```

### `public PIDController getPIDController()`

[Source lines 333–335](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L333)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new PIDController(kP, kI, kD, period)`.
- Key collaborators/calls: `PIDController()`.

**Inputs:** None.

**Result:** Returns `PIDController`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 333–335)"

    ```java
    public PIDController getPIDController() {
      return new PIDController(kP, kI, kD, period);
    }
    ```

### `public PIDController getPIDController(double minInput, double maxInput)`

[Source lines 343–347](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L343)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `controller`.
- Key collaborators/calls: `PIDController()`, `controller.enableContinuousInput()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `minInput` | `double` | `double` input consumed by the implementation shown below. |
| `maxInput` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `PIDController`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 343–347)"

    ```java
    public PIDController getPIDController(double minInput, double maxInput) {
      PIDController controller = new PIDController(kP, kI, kD, period);
      controller.enableContinuousInput(minInput, maxInput);
      return controller;
    }
    ```

### `public ProfiledPIDController getProfiledPIDController(Constraints constraints)`

[Source lines 354–356](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L354)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new ProfiledPIDController(kP, kI, kD, constraints, period)`.
- Key collaborators/calls: `ProfiledPIDController()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `constraints` | `Constraints` | `Constraints` input consumed by the implementation shown below. |

**Result:** Returns `ProfiledPIDController`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 354–356)"

    ```java
    public ProfiledPIDController getProfiledPIDController(Constraints constraints) {
      return new ProfiledPIDController(kP, kI, kD, constraints, period);
    }
    ```

### `public ProfiledPIDController getProfiledPIDController( Constraints constraints, double minInput, double maxInput)`

[Source lines 365–370](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L365)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `controller`.
- Key collaborators/calls: `ProfiledPIDController()`, `controller.enableContinuousInput()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `constraints` | `Constraints` | `Constraints` input consumed by the implementation shown below. |
| `minInput` | `double` | `double` input consumed by the implementation shown below. |
| `maxInput` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `ProfiledPIDController`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 365–370)"

    ```java
    public ProfiledPIDController getProfiledPIDController(
        Constraints constraints, double minInput, double maxInput) {
      ProfiledPIDController controller = new ProfiledPIDController(kP, kI, kD, constraints, period);
      controller.enableContinuousInput(minInput, maxInput);
      return controller;
    }
    ```

### `public PhoenixPIDController getPhoenixPIDController()`

[Source lines 373–375](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L373)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new PhoenixPIDController(kP, kI, kD)`.
- Key collaborators/calls: `PhoenixPIDController()`.

**Inputs:** None.

**Result:** Returns `PhoenixPIDController`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 373–375)"

    ```java
    public PhoenixPIDController getPhoenixPIDController() {
      return new PhoenixPIDController(kP, kI, kD);
    }
    ```

### `public PhoenixPIDController getPhoenixPIDController(double minInput, double maxInput)`

[Source lines 383–387](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L383)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `controller`.
- Key collaborators/calls: `PhoenixPIDController()`, `controller.enableContinuousInput()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `minInput` | `double` | `double` input consumed by the implementation shown below. |
| `maxInput` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `PhoenixPIDController`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 383–387)"

    ```java
    public PhoenixPIDController getPhoenixPIDController(double minInput, double maxInput) {
      PhoenixPIDController controller = new PhoenixPIDController(kP, kI, kD);
      controller.enableContinuousInput(minInput, maxInput);
      return controller;
    }
    ```

### `public boolean equals(ScreamPIDConstants other)`

[Source lines 390–401](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L390)

**Detailed behavior**

- The implementation executes 10 non-blank source lines.
- It changes object/subclass state through `integralZone`, `kD`, `kF`, `kI`, `kP`, `maxIntegralAccumulator`, `maxOutput`, `minIntegralAccumulator`, `minOutput`, `period`.
- Return path: `this.period == other.period && this.kP == other.kP && this.kI == other.kI && this.kD == other.kD && this.kF == other.kF && this.minOutput == other.minOutput && this.maxOutput == o…`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `other` | `ScreamPIDConstants` | `ScreamPIDConstants` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 390–401)"

    ```java
    public boolean equals(ScreamPIDConstants other) {
      return this.period == other.period
          && this.kP == other.kP
          && this.kI == other.kI
          && this.kD == other.kD
          && this.kF == other.kF
          && this.minOutput == other.minOutput
          && this.maxOutput == other.maxOutput
          && this.integralZone == other.integralZone
          && this.maxIntegralAccumulator == other.maxIntegralAccumulator
          && this.minIntegralAccumulator == other.minIntegralAccumulator;
    }
    ```

### `public ScreamPIDConstants clone()`

[Source lines 404–417](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L404)

**Detailed behavior**

- The implementation executes 12 non-blank source lines.
- Return path: `copy`.
- Key collaborators/calls: `ScreamPIDConstants()`.

**Inputs:** None.

**Result:** Returns `ScreamPIDConstants`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 404–417)"

    ```java
    public ScreamPIDConstants clone() {
      ScreamPIDConstants copy = new ScreamPIDConstants();
      copy.period = this.period;
      copy.kP = this.kP;
      copy.kI = this.kI;
      copy.kD = this.kD;
      copy.kF = this.kF;
      copy.minOutput = this.minOutput;
      copy.maxOutput = this.maxOutput;
      copy.integralZone = this.integralZone;
      copy.maxIntegralAccumulator = this.maxIntegralAccumulator;
      copy.minIntegralAccumulator = this.minIntegralAccumulator;
      return copy;
    }
    ```

### `public MotionMagicConstants(double cruiseVelocity, double acceleration, int jerk)`

[Source lines 16–16](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L16)

**Detailed behavior**

- Java generates this record canonical constructor. It stores each argument in the corresponding final record component; Java also supplies component accessors, value-based `equals`, `hashCode`, and `toString`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `cruiseVelocity` | `double` | Velocity/speed in the units required by this API and configuration. |
| `acceleration` | `double` | `double` input consumed by the implementation shown below. |
| `jerk` | `int` | `int` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `MotionMagicConstants` instance.

??? example "Record declaration that generates this callable"

    ```java
    public record MotionMagicConstants(double cruiseVelocity, double acceleration, int jerk)
    ```

### `public double cruiseVelocity()`

[Source lines 16–16](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L16)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record MotionMagicConstants(double cruiseVelocity, double acceleration, int jerk)
    ```

### `public double acceleration()`

[Source lines 16–16](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L16)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record MotionMagicConstants(double cruiseVelocity, double acceleration, int jerk)
    ```

### `public int jerk()`

[Source lines 16–16](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L16)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `int`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record MotionMagicConstants(double cruiseVelocity, double acceleration, int jerk)
    ```

### `public FeedforwardConstants( double kV, double kS, double kG, double kA, GravityTypeValue gravityType)`

[Source lines 19–19](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L19)

**Detailed behavior**

- Java generates this record canonical constructor. It stores each argument in the corresponding final record component; Java also supplies component accessors, value-based `equals`, `hashCode`, and `toString`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `kV` | `double` | `double` input consumed by the implementation shown below. |
| `kS` | `double` | `double` input consumed by the implementation shown below. |
| `kG` | `double` | `double` input consumed by the implementation shown below. |
| `kA` | `double` | `double` input consumed by the implementation shown below. |
| `gravityType` | `GravityTypeValue` | `GravityTypeValue` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `FeedforwardConstants` instance.

??? example "Record declaration that generates this callable"

    ```java
    public record FeedforwardConstants( double kV, double kS, double kG, double kA, GravityTypeValue gravityType)
    ```

### `public double kV()`

[Source lines 19–19](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L19)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record FeedforwardConstants( double kV, double kS, double kG, double kA, GravityTypeValue gravityType)
    ```

### `public double kS()`

[Source lines 19–19](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L19)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record FeedforwardConstants( double kV, double kS, double kG, double kA, GravityTypeValue gravityType)
    ```

### `public double kG()`

[Source lines 19–19](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L19)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record FeedforwardConstants( double kV, double kS, double kG, double kA, GravityTypeValue gravityType)
    ```

### `public double kA()`

[Source lines 19–19](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L19)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record FeedforwardConstants( double kV, double kS, double kG, double kA, GravityTypeValue gravityType)
    ```

### `public GravityTypeValue gravityType()`

[Source lines 19–19](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L19)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `GravityTypeValue`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public record FeedforwardConstants( double kV, double kS, double kG, double kA, GravityTypeValue gravityType)
    ```

## Exposed fields and types

### `public class ScreamPIDConstants implements Cloneable`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L13)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public record MotionMagicConstants(double cruiseVelocity, double acceleration, int jerk)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L16)*

This exposed `record` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public record FeedforwardConstants( double kV, double kS, double kG, double kA, GravityTypeValue gravityType)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/pid/ScreamPIDConstants.java#L19)*

This exposed `record` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
