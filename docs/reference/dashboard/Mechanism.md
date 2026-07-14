# Mechanism

`com.teamscreamrobotics.dashboard.Mechanism`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java) · **6 callables** · **4 exposed fields/types** · **2 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2026: Use `Mechanism` in `IntakeWrist.java`

[`src/main/java/frc2026/tars/subsystems/intake/IntakeWrist.java` lines 34–49](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/intake/IntakeWrist.java#L34-L49)

```java
() ->
                Rotation2d.fromRotations(getSetpoint())
                    .unaryMinus()
                    .minus(Rotation2d.fromDegrees(90)));
public final Mechanism intakeMech =
    new Mechanism("Intake Mech", intakeOne, intakeTwo)
        .withStaticPosition(
            new Translation2d(
                (SimConstants.MECH_WIDTH / 2.0) + Units.inchesToMeters(12.125),
                Units.inchesToMeters(8)));

public IntakeWrist(TalonFXSubsystemConfiguration config) {
  super(config, IntakeWristGoal.EXTENDED);
}

public enum IntakeWristGoal implements TalonFXSubsystemGoal {
```

### 2026: Use `Mechanism` in `Drivetrain.java`

[`src/main/java/frc2026/tars/subsystems/drivetrain/Drivetrain.java` lines 64–79](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/drivetrain/Drivetrain.java#L64-L79)

```java
null, // Use default ramp rate (1 V/s)
            Volts.of(4), // Reduce dynamic step voltage to 4 V to prevent brownout
            null, // Use default timeout (10 s)
            // Log state with SignalLogger class
            state -> SignalLogger.writeString("SysIdTranslation_State", state.toString())),
        new SysIdRoutine.Mechanism(
            output -> setControl(m_translationCharacterization.withVolts(output)), null, this));

/* SysId routine for characterizing steer. This is used to find PID gains for the steer motors. */
@SuppressWarnings("unused")
private final SysIdRoutine m_sysIdRoutineSteer =
    new SysIdRoutine(
        new SysIdRoutine.Config(
            null, // Use default ramp rate (1 V/s)
            Volts.of(7), // Use dynamic voltage of 7 V
            null, // Use default timeout (10 s)
```

## Public and protected callables

### `public Mechanism(String key, Ligament... ligaments)`

[Source lines 33–36](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L33)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `key`, `ligaments`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | identifier used as the root name in the `Mechanism2d` widget **Parameter `ligaments`:** one or more ligaments, in chain order from root outward |
| `ligaments` | `Ligament...` | one or more ligaments, in chain order from root outward |

**Result:** Constructs and initializes a `Mechanism` instance.

??? example "Implementation (source lines 33–36)"

    ```java
    public Mechanism(String key, Ligament... ligaments) {
      this.key = key;
      this.ligaments = ligaments;
    }
    ```

??? note "Author note from JavaDoc"

    Creates a mechanism with the given dashboard key and ordered ligament chain.
    
    **Parameter `key`:** identifier used as the root name in the `Mechanism2d` widget
    **Parameter `ligaments`:** one or more ligaments, in chain order from root outward

### `protected void initialize(Mechanism2d measured, Mechanism2d setpoint)`

[Source lines 38–55](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L38)

**Detailed behavior**

- The implementation executes 14 non-blank source lines.
- It changes object/subclass state through `measured`, `setpoint`.
- It has 2 conditional paths: `ligaments.length > 1`; `ligaments[i].overrideAppend`.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `measured.getRoot()`, `setpoint.getRoot()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `measured` | `Mechanism2d` | `Mechanism2d` input consumed by the implementation shown below. |
| `setpoint` | `Mechanism2d` | `Mechanism2d` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 38–55)"

    ```java
    protected void initialize(Mechanism2d measured, Mechanism2d setpoint) {
      this.measured = measured;
      this.setpoint = setpoint;
    
      measuredRoot = measured.getRoot(key + " Actual", 0, 0);
      setpointRoot = setpoint.getRoot(key + " Setpoint", 0, 0);
    
      ligaments[0].initialize(0, measuredRoot, setpointRoot);
      if(ligaments.length > 1){
        for(int i = 1; i < ligaments.length; i++){
          if(ligaments[i].overrideAppend){
            ligaments[i].initialize(i, measuredRoot, setpointRoot);
            continue;
          }
          ligaments[i].initialize(i, ligaments[i - 1].measuredLig, ligaments[i - 1].setpointLig);
        }
      }
    }
    ```

### `public Mechanism withStaticPosition(Translation2d position)`

[Source lines 62–65](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L62)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `position`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `position` | `Translation2d` | the constant (x, y) position of the root |

**Result:** Returns `Mechanism`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 62–65)"

    ```java
    public Mechanism withStaticPosition(Translation2d position) {
      this.position = () -> position;
      return this;
    }
    ```

??? note "Author note from JavaDoc"

    Sets a fixed root position for the mechanism in the 2D widget.
    
    **Parameter `position`:** the constant (x, y) position of the root

### `public Mechanism withDynamicPosition(Supplier&lt;Translation2d&gt; position)`

[Source lines 72–75](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L72)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `position`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `position` | `Supplier&lt;Translation2d&gt;` | supplier for the (x, y) root position |

**Result:** Returns `Mechanism`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 72–75)"

    ```java
    public Mechanism withDynamicPosition(Supplier<Translation2d> position) {
      this.position = position;
      return this;
    }
    ```

??? note "Author note from JavaDoc"

    Sets a dynamic root position supplier, updated each periodic cycle.
    
    **Parameter `position`:** supplier for the (x, y) root position

### `public void setPosition(Translation2d position)`

[Source lines 82–84](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L82)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `position`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `position` | `Translation2d` | the new (x, y) root position |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 82–84)"

    ```java
    public void setPosition(Translation2d position) {
      this.position = () -> position;
    }
    ```

??? note "Author note from JavaDoc"

    Imperatively overrides the root position with a new fixed value.
    
    **Parameter `position`:** the new (x, y) root position

### `protected void update()`

[Source lines 86–92](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L86)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `this.setpointRoot.setPosition()`, `position.get()`, `getX()`, `getY()`, `this.measuredRoot.setPosition()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 86–92)"

    ```java
    protected void update() {
      for(Ligament lig : ligaments){
        lig.update();
      }
      this.setpointRoot.setPosition(position.get().getX(), position.get().getY());
      this.measuredRoot.setPosition(position.get().getX(), position.get().getY());
    }
    ```

## Exposed fields and types

### `public class Mechanism`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L13)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    A named group of `Ligament`s forming a kinematic chain for `MechanismVisualizer`.
    The first ligament is anchored at a root; subsequent ones chain from their predecessor unless
    `Ligament#withOverrideAppend(boolean)` is set.

### `public Mechanism2d measured`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L15)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 5 times, so changing it can affect every control path that reads `measured`.

### `public Mechanism2d setpoint`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L16)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 5 times, so changing it can affect every control path that reads `setpoint`.

### `public String key`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Mechanism.java#L18)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 8 times, so changing it can affect every control path that reads `key`.
