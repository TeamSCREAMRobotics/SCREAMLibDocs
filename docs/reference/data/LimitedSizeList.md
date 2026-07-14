# LimitedSizeList

`com.teamscreamrobotics.data.LimitedSizeList`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/LimitedSizeList.java) · **3 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public LimitedSizeList(int maxSize)`

[Source lines 20–23](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/LimitedSizeList.java#L20)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It delegates initialization to the superclass constructor with `maxSize`.
- It changes object/subclass state through `maxSize`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `maxSize` | `int` | the maximum number of elements to retain |

**Result:** Constructs and initializes a `LimitedSizeList` instance.

??? example "Implementation (source lines 20–23)"

    ```java
    public LimitedSizeList(int maxSize) {
      super(maxSize);
      this.maxSize = maxSize;
    }
    ```

??? note "Author note from JavaDoc"

    Creates a new limited-size list.
    
    **Parameter `maxSize`:** the maximum number of elements to retain

### `public boolean add(T element)`

[Source lines 26–31](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/LimitedSizeList.java#L26)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It has 1 conditional path: `this.size(`.
- Return path: `super.add(element)`.
- Key collaborators/calls: `this.size()`, `this.removeFirst()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `element` | `T` | `T` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 26–31)"

    ```java
    public boolean add(T element) {
      if (this.size() >= maxSize) {
        this.removeFirst();
      }
      return super.add(element);
    }
    ```

### `public boolean addAll(Collection&lt;? extends T&gt; c)`

[Source lines 34–39](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/LimitedSizeList.java#L34)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `true`.
- Key collaborators/calls: `add()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `c` | `Collection&lt;? extends T&gt;` | `Collection<? extends T>` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 34–39)"

    ```java
    public boolean addAll(Collection<? extends T> c) {
      for (T element : c) {
        add(element);
      }
      return true;
    }
    ```

## Exposed fields and types

### `public class LimitedSizeList&lt;T&gt; extends ArrayDeque&lt;T&gt;`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/LimitedSizeList.java#L12)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    A fixed-capacity deque that automatically evicts the oldest element when full.
    Useful for rolling windows of sensor readings or log history.
    
    **Parameter `the`:** type of elements held in this list
