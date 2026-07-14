# DashboardString

`com.teamscreamrobotics.dashboard.DashboardString`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardString.java) · **3 callables** · **1 exposed fields/types** · **1 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2025: Use `DashboardString` in `DashboardString.java`

[`src/main/java/com/team4522/DashboardString.java` lines 2–17](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/com/team4522/DashboardString.java#L2-L17)

```java
import edu.wpi.first.networktables.NetworkTable;
import edu.wpi.first.networktables.NetworkTableEntry;
import edu.wpi.first.networktables.NetworkTableInstance;

public class DashboardString {
  private final NetworkTableEntry entry;
  private String currentValue;

  public DashboardString(String tableName, String key, String defaultValue) {
    NetworkTable table = NetworkTableInstance.getDefault().getTable(tableName);
    entry = table.getEntry(key);
    currentValue = defaultValue;
    entry.setDefaultString(defaultValue);
  }
```

## Public and protected callables

### `public DashboardString(String tableName, String key, String defaultValue)`

[Source lines 19–24](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardString.java#L19)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It reads or writes NetworkTables data, so the result depends on live robot/network state.
- Key collaborators/calls: `NetworkTableInstance.getDefault()`, `getTable()`, `table.getEntry()`, `entry.setDefaultString()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `tableName` | `String` | NetworkTables table to publish under **Parameter `key`:** entry key within the table **Parameter `defaultValue`:** initial value written to the table |
| `key` | `String` | entry key within the table **Parameter `defaultValue`:** initial value written to the table |
| `defaultValue` | `String` | initial value written to the table |

**Result:** Constructs and initializes a `DashboardString` instance.

??? example "Implementation (source lines 19–24)"

    ```java
    public DashboardString(String tableName, String key, String defaultValue) {
      NetworkTable table = NetworkTableInstance.getDefault().getTable(tableName);
      entry = table.getEntry(key);
      currentValue = defaultValue;
      entry.setDefaultString(defaultValue);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a dashboard-linked string.
    
    **Parameter `tableName`:** NetworkTables table to publish under
    **Parameter `key`:** entry key within the table
    **Parameter `defaultValue`:** initial value written to the table

### `public void set(String value)`

[Source lines 27–30](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardString.java#L27)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Key collaborators/calls: `entry.setString()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | `String` | `String` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 27–30)"

    ```java
    public void set(String value) {
      currentValue = value;
      entry.setString(value);
    }
    ```

??? note "Author note from JavaDoc"

    Pushes `value` to the dashboard and caches it locally.

### `public String get()`

[Source lines 33–35](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardString.java#L33)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `entry.getString(currentValue)`.
- Key collaborators/calls: `entry.getString()`.

**Inputs:** None.

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 33–35)"

    ```java
    public String get() {
      return entry.getString(currentValue);
    }
    ```

??? note "Author note from JavaDoc"

    Returns the current dashboard value, falling back to the last locally set value.

## Exposed fields and types

### `public class DashboardString`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardString.java#L8)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    A String value backed by a NetworkTables entry for dashboard interaction.
