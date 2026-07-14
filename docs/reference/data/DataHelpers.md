# DataHelpers

`com.teamscreamrobotics.data.DataHelpers`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java) · **7 callables** · **4 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `void accept(T1 t1, T2 t2, T3 t3)`

[Source lines 8–8](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L8)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `t1` | `T1` | `T1` input consumed by the implementation shown below. |
| `t2` | `T2` | `T2` input consumed by the implementation shown below. |
| `t3` | `T3` | `T3` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 8)"

    ```java
    void accept(T1 t1, T2 t2, T3 t3);
    ```

### `public Dimensions(double height, double width)`

[Source lines 12–12](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L12)

**Detailed behavior**

- Java generates this record canonical constructor. It stores each argument in the corresponding final record component; Java also supplies component accessors, value-based `equals`, `hashCode`, and `toString`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `height` | `double` | `double` input consumed by the implementation shown below. |
| `width` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `Dimensions` instance.

??? example "Record declaration that generates this callable"

    ```java
    public static record Dimensions(double height, double width)
    ```

### `public double height()`

[Source lines 12–12](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L12)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public static record Dimensions(double height, double width)
    ```

### `public double width()`

[Source lines 12–12](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L12)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public static record Dimensions(double height, double width)
    ```

### `public LoggedOutput(String key, T value)`

[Source lines 15–15](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L15)

**Detailed behavior**

- Java generates this record canonical constructor. It stores each argument in the corresponding final record component; Java also supplies component accessors, value-based `equals`, `hashCode`, and `toString`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | `String` | `String` input consumed by the implementation shown below. |
| `value` | `T` | `T` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `LoggedOutput` instance.

??? example "Record declaration that generates this callable"

    ```java
    public static record LoggedOutput<T>(String key, T value)
    ```

### `public String key()`

[Source lines 15–15](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L15)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public static record LoggedOutput<T>(String key, T value)
    ```

### `public T value()`

[Source lines 15–15](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L15)

**Detailed behavior**

- Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor.

**Inputs:** None.

**Result:** Returns `T`. Exact return expressions are listed in the behavior section.

??? example "Record declaration that generates this callable"

    ```java
    public static record LoggedOutput<T>(String key, T value)
    ```

## Exposed fields and types

### `public class DataHelpers`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L4)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static interface TriConsumer&lt;T1, T2, T3&gt;`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L7)*

This exposed `interface` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static record Dimensions(double height, double width)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L12)*

This exposed `record` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static record LoggedOutput&lt;T&gt;(String key, T value)`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataHelpers.java#L15)*

This exposed `record` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
