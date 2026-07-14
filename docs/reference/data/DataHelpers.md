# DataHelpers

`com.teamscreamrobotics.data.DataHelpers`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java) · **1 callables** · **4 exposed fields/types**

## Public and protected callables

### `void accept(T1 t1, T2 t2, T3 t3)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L8)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

## Exposed fields and types

### `public class DataHelpers`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L4)*

Miscellaneous data types and functional interfaces used across the library.

### `public static interface TriConsumer&lt;T1, T2, T3&gt;`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L7)*

A functional interface for a consumer accepting three arguments.

### `public static record Dimensions(double height, double width)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L12)*

A simple (height, width) size pair.

### `public static record LoggedOutput&lt;T&gt;(String key, T value)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L15)*

Associates a log key with a typed value for structured telemetry output.
