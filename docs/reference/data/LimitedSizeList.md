# LimitedSizeList

`com.teamscreamrobotics.data.LimitedSizeList`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/LimitedSizeList.java) · **3 callables** · **1 exposed fields/types**

## Public and protected callables

### `public LimitedSizeList(int maxSize)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/LimitedSizeList.java#L20)*

Creates a new limited-size list.

**Parameter `maxSize`:** the maximum number of elements to retain

### `public boolean add(T element)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/LimitedSizeList.java#L26)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

### `public boolean addAll(Collection&lt;? extends T&gt; c)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/LimitedSizeList.java#L34)*

No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.

## Exposed fields and types

### `public class LimitedSizeList&lt;T&gt; extends ArrayDeque&lt;T&gt;`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/LimitedSizeList.java#L12)*

A fixed-capacity deque that automatically evicts the oldest element when full.
Useful for rolling windows of sensor readings or log history.

**Parameter `the`:** type of elements held in this list
