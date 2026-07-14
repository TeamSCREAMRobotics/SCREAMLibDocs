# DashboardNumber

`com.teamscreamrobotics.dashboard.DashboardNumber`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardNumber.java) · **3 callables** · **1 exposed fields/types**

## Competition usage

**2025:** [`DashboardNumber.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/com/team4522/DashboardNumber.java#L7), [`Dashboard.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/Dashboard.java#L4)

**2026:** [`Dashboard.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/controlboard/Dashboard.java#L4)

## Public and protected callables

### `public DashboardNumber(String tableName, String key, double defaultValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardNumber.java#L19)*

Creates a dashboard-linked number.

**Parameter `tableName`:** NetworkTables table to publish under
**Parameter `key`:** entry key within the table
**Parameter `defaultValue`:** initial value written to the table

### `public void set(double value)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardNumber.java#L27)*

Pushes `value` to the dashboard and caches it locally.

### `public double get()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardNumber.java#L33)*

Returns the current dashboard value, falling back to the last locally set value.

## Exposed fields and types

### `public class DashboardNumber`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/DashboardNumber.java#L8)*

A double value backed by a NetworkTables entry for dashboard interaction.
