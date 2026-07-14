# DashboardBoolean

`com.teamscreamrobotics.dashboard.DashboardBoolean`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardBoolean.java) · **3 callables** · **1 exposed fields/types** · **3 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

!!! note "2025 package names"
    The 2025 robot used SCREAMLib's earlier short packages such as `data`, `drivers`, and `util`. With SCREAMLib 26.3.7, prefix those imports with `com.teamscreamrobotics.`; the implementation pattern remains applicable.

### 2025: Use `DashboardBoolean` in `Dashboard.java`

[`src/main/java/frc2025/Dashboard.java` lines 49–64](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/Dashboard.java#L49-L64)

```java
Sim.initialize();
  }
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
```

### 2025: Use `DashboardBoolean` in `DashboardBoolean.java`

[`src/main/java/com/team4522/DashboardBoolean.java` lines 2–17](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/com/team4522/DashboardBoolean.java#L2-L17)

```java
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTableInstance;

public class DashboardBoolean {
  private final NetworkTableEntry entry;
  private boolean currentValue;

  public DashboardBoolean(String tableName, String key, boolean defaultValue) {
    NetworkTable table = NetworkTableInstance.getDefault().getTable(tableName);
    entry = table.getEntry(key);
    currentValue = defaultValue;
    entry.setDefaultBoolean(defaultValue);
  }
```

### 2026: Use `DashboardBoolean` in `Dashboard.java`

[`src/main/java/frc2026/tars/controlboard/Dashboard.java` lines 64–79](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/controlboard/Dashboard.java#L64-L79)

```java
static {
  initialize();
}

public static void initialize() {
  zeroHopper = new DashboardBoolean(overrides, "Zero Hopper", false);
  disableAmbiguityRejection = new DashboardBoolean(vision, "Disable Ambiguity Rejection", false);
  disableAllVisionUpdates = new DashboardBoolean(vision, "Disable All Vision Updates", false);
  runBackIntake = new DashboardBoolean(overrides, "Run Back Intake", false);
  runBackFlywheel = new DashboardBoolean(overrides, "Run Back Flywheel", false);
  disableWaitUntilHood = new DashboardBoolean(overrides, "Disable Wait Until Hood", false);

  runBackHopper = new DashboardBoolean(overrides, "Run Back Hopper", false);
  dissableShootOnTheMove = new DashboardBoolean(overrides, "Disable Shoot On The Move", false);

  zeroIntake = new DashboardBoolean(overrides, "Zero Intake", false);
```

## Public and protected callables

### `public DashboardBoolean(String tableName, String key, boolean defaultValue)`

[Source lines 19–24](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardBoolean.java#L19)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It reads or writes NetworkTables data, so the result depends on live robot/network state.
- Key collaborators/calls: `NetworkTableInstance.getDefault()`, `getTable()`, `table.getEntry()`, `entry.setDefaultBoolean()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | `String` input consumed by the implementation shown below. |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `defaultValue` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `DashboardBoolean` instance.

??? example "Implementation (source lines 19–24)"

    ```java
    public DashboardBoolean(String tableName, String key, boolean defaultValue) {
      NetworkTable table = NetworkTableInstance.getDefault().getTable(tableName);
      entry = table.getEntry(key);
      currentValue = defaultValue;
      entry.setDefaultBoolean(defaultValue);
    }
    ```

### `public void set(boolean value)`

[Source lines 27–30](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardBoolean.java#L27)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Key collaborators/calls: `entry.setBoolean()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 27–30)"

    ```java
    public void set(boolean value) {
      currentValue = value;
      entry.setBoolean(value);
    }
    ```

### `public boolean get()`

[Source lines 33–35](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardBoolean.java#L33)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `entry.getBoolean(currentValue)`.
- Key collaborators/calls: `entry.getBoolean()`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 33–35)"

    ```java
    public boolean get() {
      return entry.getBoolean(currentValue);
    }
    ```

## Exposed fields and types

### `public class DashboardBoolean`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardBoolean.java#L8)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
