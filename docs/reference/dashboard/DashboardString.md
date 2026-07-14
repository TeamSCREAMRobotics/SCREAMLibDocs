# DashboardString

`com.teamscreamrobotics.dashboard.DashboardString`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardString.java) · **3 callables** · **1 exposed fields/types**

## Competition usage

**2025:** [`DashboardString.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/com/team4522/DashboardString.java#L7)

## Public and protected callables

### `public DashboardString(String tableName, String key, String defaultValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardString.java#L19)*

Creates a dashboard-linked string.

**Parameter `tableName`:** NetworkTables table to publish under
**Parameter `key`:** entry key within the table
**Parameter `defaultValue`:** initial value written to the table

### `public void set(String value)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardString.java#L27)*

Pushes `value` to the dashboard and caches it locally.

### `public String get()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardString.java#L33)*

Returns the current dashboard value, falling back to the last locally set value.

## Exposed fields and types

### `public class DashboardString`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardString.java#L8)*

A String value backed by a NetworkTables entry for dashboard interaction.
