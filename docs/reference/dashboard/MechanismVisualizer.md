# MechanismVisualizer

`com.teamscreamrobotics.dashboard.MechanismVisualizer`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java) · **3 callables** · **3 exposed fields/types** · **1 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2026: Use `MechanismVisualizer` in `RobotContainer.java`

[`src/main/java/frc2026/tars/RobotContainer.java` lines 89–104](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/RobotContainer.java#L89-L104)

```java
private final VisionManager visionManager = new VisionManager(drivetrain);

private final SwerveRequest.SwerveDriveBrake brake = new SwerveDriveBrake();

private final MechanismVisualizer mechVisualizer =
    new MechanismVisualizer(
        SimConstants.MEASURED_MECHANISM,
        SimConstants.SETPOINT_MECHANISM,
        RobotContainer::telemeterizeMechanisms,
        intakeWrist.intakeMech);

private final Routines routines = new Routines(drivetrain, shooter, robotState, this);

public RobotContainer() {
  configureBindings();
  configureManualOverrides();
```

## Public and protected callables

### `public MechanismVisualizer( Mechanism2d measuredMechanism, Mechanism2d setpointMechanism, BiConsumer&lt;Mechanism2d, Mechanism2d&gt; telemetryConsumer, Mechanism... mechanisms)`

[Source lines 31–41](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L31)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It changes object/subclass state through `MEASURED_MECHANISM`, `SETPOINT_MECHANISM`, `mechanisms`, `telemetryCons`.
- Key collaborators/calls: `Arrays.asList()`, `this.mechanisms.forEach()`, `mech.initialize()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `measuredMechanism` | `Mechanism2d` | `Mechanism2d` input consumed by the implementation shown below. |
| `setpointMechanism` | `Mechanism2d` | `Mechanism2d` input consumed by the implementation shown below. |
| `telemetryConsumer` | `BiConsumer&lt;Mechanism2d, Mechanism2d&gt;` | `BiConsumer<Mechanism2d, Mechanism2d>` input consumed by the implementation shown below. |
| `mechanisms` | `Mechanism...` | `Mechanism...` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `MechanismVisualizer` instance.

??? example "Implementation (source lines 31–41)"

    ```java
    public MechanismVisualizer(
        Mechanism2d measuredMechanism,
        Mechanism2d setpointMechanism,
        BiConsumer<Mechanism2d, Mechanism2d> telemetryConsumer,
        Mechanism... mechanisms) {
      MEASURED_MECHANISM = measuredMechanism;
      SETPOINT_MECHANISM = setpointMechanism;
      this.telemetryCons = telemetryConsumer;
      this.mechanisms = new ArrayList<>(Arrays.asList(mechanisms));
      this.mechanisms.forEach((mech) -> mech.initialize(MEASURED_MECHANISM, SETPOINT_MECHANISM));
    }
    ```

### `public void setEnabled(boolean enabled)`

[Source lines 44–46](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L44)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `enabled`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `enabled` | `boolean` | Enables the behavior when `true`; disables it when `false`. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 44–46)"

    ```java
    public void setEnabled(boolean enabled) {
      this.enabled = enabled;
    }
    ```

### `public void periodic()`

[Source lines 49–54](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L49)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It has 1 conditional path: `enabled`.
- Key collaborators/calls: `mechanisms.forEach()`, `telemetryCons.accept()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 49–54)"

    ```java
    public void periodic() {
      if (enabled) {
        mechanisms.forEach(Mechanism::update);
        telemetryCons.accept(MEASURED_MECHANISM, SETPOINT_MECHANISM);
      }
    }
    ```

## Exposed fields and types

### `public class MechanismVisualizer extends SubsystemBase`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L13)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public Mechanism2d MEASURED_MECHANISM`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L15)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `MEASURED_MECHANISM`.

### `public Mechanism2d SETPOINT_MECHANISM`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/MechanismVisualizer.java#L16)*

This is a **public** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 4 times, so changing it can affect every control path that reads `SETPOINT_MECHANISM`.
