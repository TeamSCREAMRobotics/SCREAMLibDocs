# DashboardNumber

`com.teamscreamrobotics.dashboard.DashboardNumber`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardNumber.java) · **3 callables** · **1 exposed fields/types** · **3 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

!!! note "2025 package names"
    The 2025 robot used SCREAMLib's earlier short packages such as `data`, `drivers`, and `util`. With SCREAMLib 26.3.7, prefix those imports with `com.teamscreamrobotics.`; the implementation pattern remains applicable.

### 2025: Use `DashboardNumber` in `Dashboard.java`

[`src/main/java/frc2025/Dashboard.java` lines 51–66](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/Dashboard.java#L51-L66)

```java
}

private static void initialize() {
  manualMode = new DashboardBoolean(overrides, "Manual Mode", false);
  resetVoltage = new DashboardBoolean(overrides, "Reset Voltage", false);
  elevatorVoltage = new DashboardNumber(overrides, "Elevator Voltage", 0);
  wristVoltage = new DashboardNumber(overrides, "Wrist Voltage", 0);
  climberVoltage = new DashboardNumber(overrides, "Climber Voltage", 0);
  wristRollersVoltage = new DashboardNumber(overrides, "Rollers Voltage", 0);
  funnelServoPosition = new DashboardNumber(overrides, "Funnel Servo Position", 1);
  climbRollersVoltage = new DashboardNumber(overrides, "Climb Rollers Volatage", 0.0);
  disableAllVisionUpdates = new DashboardBoolean(vision, "Disable Vision Updates", false);
  // disableMegatag2 = new DashboardBoolean(overrides, "Disable MegaTag2", false);
  disableAutoFeatures = new DashboardBoolean(overrides, "Disable Auto Features", false);
  disableCoralRequirement = new DashboardBoolean(overrides, "Disable Coral Requirement", false);
  zeroElevator = new DashboardBoolean(overrides, "Zero Elevator", false);
```

### 2025: Use `DashboardNumber` in `DashboardNumber.java`

[`src/main/java/com/team4522/DashboardNumber.java` lines 2–17](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/com/team4522/DashboardNumber.java#L2-L17)

```java
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTableInstance;

public class DashboardNumber {
  private final NetworkTableEntry entry;
  private double currentValue;

  public DashboardNumber(String tableName, String key, double defaultValue) {
    NetworkTable table = NetworkTableInstance.getDefault().getTable(tableName);
    entry = table.getEntry(key);
    currentValue = defaultValue;
    entry.setDefaultDouble(defaultValue);
  }
```

### 2026: Use `DashboardNumber` in `Dashboard.java`

[`src/main/java/frc2026/tars/controlboard/Dashboard.java` lines 80–95](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/controlboard/Dashboard.java#L80-L95)

```java
zeroHood = new DashboardBoolean(overrides, "Zero Hood", false);
disableWaitUntilAtVelocity =
    new DashboardBoolean(overrides, "Disable Wait Until At Velocity", false);
manualMode = new DashboardBoolean(overrides, "Manual Mode", false);
resetManuals = new DashboardBoolean(overrides, "Reset Manuals", false);
manualHoodAngle = new DashboardNumber(overrides, "Manual Hood Angle", 0.0);
manualFlywheelVelocity = new DashboardNumber(overrides, "Manual Flywheel Velocity", 0.0);
manualIntakeRollers = new DashboardNumber(overrides, "Manual Intake Rollers", 0.0);
manualIntakeWrist = new DashboardNumber(overrides, "Manual Intake Wrist", 90.0);
manualFloorRollers = new DashboardNumber(overrides, "Manual Floor Rollers", 0);
manualFeeder = new DashboardNumber(overrides, "Manual Feeder", 0);
bumperShoot = new DashboardBoolean(overrides, "Bumper Shoot", false);
disableWaitUntilAim = new DashboardBoolean(overrides, "Dissable Wait until aim", false);

closeMapNudge =
    new DashboardNumber(overrides, "Close Tree Map Nudge", ShooterConstants.CLOSE_MAP_NUDGE);
```

## Public and protected callables

### `public DashboardNumber(String tableName, String key, double defaultValue)`

[Source lines 19–24](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardNumber.java#L19)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It reads or writes NetworkTables data, so the result depends on live robot/network state.
- Key collaborators/calls: `NetworkTableInstance.getDefault()`, `getTable()`, `table.getEntry()`, `entry.setDefaultDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `defaultValue` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `DashboardNumber` instance.

??? example "Implementation (source lines 19–24)"

    ```java
    public DashboardNumber(String tableName, String key, double defaultValue) {
      NetworkTable table = NetworkTableInstance.getDefault().getTable(tableName);
      entry = table.getEntry(key);
      currentValue = defaultValue;
      entry.setDefaultDouble(defaultValue);
    }
    ```

### `public void set(double value)`

[Source lines 27–30](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardNumber.java#L27)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It reads or writes NetworkTables data, so the result depends on live robot/network state.
- Key collaborators/calls: `entry.setDouble()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | `double` | `double` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 27–30)"

    ```java
    public void set(double value) {
      currentValue = value;
      entry.setDouble(value);
    }
    ```

### `public double get()`

[Source lines 33–35](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardNumber.java#L33)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `entry.getDouble(currentValue)`.
- Key collaborators/calls: `entry.getDouble()`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 33–35)"

    ```java
    public double get() {
      return entry.getDouble(currentValue);
    }
    ```

## Exposed fields and types

### `public class DashboardNumber`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardNumber.java#L8)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
