# BLinePathSequence

`com.teamscreamrobotics.util.BLinePathSequence`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java) · **14 callables** · **1 exposed fields/types**

## Competition usage

**2026:** [`Routines.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/autonomous/Routines.java#L3)

## Public and protected callables

### `public BLinePathSequence(FollowPath.Builder builder, FieldSymmetry fieldSymmetry, String... pathNames)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L44)*

Loads and prepares a sequence of BLine paths for autonomous use.
Alliance flipping is deferred to retrieval time so the correct alliance
is used even if the object is constructed before the DS reports alliance.

**Parameter `builder`:** the `FollowPath.Builder` used to build each path-following command
**Parameter `flipType`:** how paths should be mirrored for the red alliance — see `FlipType`
**Parameter `pathNames`:** one or more BLine path names to load, in order
**Throws `InvalidParameterException`:** if no path names are supplied

### `public static boolean isRunningPath()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L91)*

Returns `true` while any path command from this class is executing.

### `public Pose2d getStartingPose()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L106)*

Returns the starting pose of the first path — use this to reset odometry before auto.

### `public Command getStart()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L113)*

Returns a command that follows the first path in the sequence.

### `public Command getEnd()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L121)*

Returns a command that follows the last path in the sequence.

### `public int getSize()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L126)*

Returns the total number of paths in this sequence.

### `public Command getNext()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L135)*

Advances the internal cursor and returns a command for the next path.
Starts at index 1 on first call (use `#getStart()` for index 0).
Returns a no-op `InstantCommand` and logs a DS warning if already at the last path.

### `public Command getAll()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L150)*

Returns a `SequentialCommandGroup` that runs all paths in order.

### `public Command getIndex(int index)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L164)*

Returns a command for the path at `index`.
Returns a no-op `InstantCommand` and logs a DS warning if out of bounds.

**Parameter `index`:** zero-based path index

### `public Optional&lt;Path&gt; getPath(int index)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L183)*

Returns the raw `Path` at `index`, or `Optional#empty()` if out of bounds.
The path is flipped according to the current alliance at call time.
Use this when you need direct path access rather than a follow command.

**Parameter `index`:** zero-based path index

### `public BLinePathSequence withAdditional(String... pathNames)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L201)*

Appends additional paths to the end of this sequence.

**Parameter `pathNames`:** one or more BLine path names to append
**Returns:** `this`, for chaining

### `public BLinePathSequence mirror()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L216)*

Returns a new `BLinePathSequence` with all paths mirrored across the field
width centerline (`y -> fieldSizeY - y`), regardless of alliance.
Use this when reusing a path designed for one half of the field on the other
(e.g. top wall path -> bottom wall path).

**Returns:** a new `BLinePathSequence` with mirrored paths

### `public BLinePathSequence withName(String name)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L226)*

Sets the name of this path sequence.

**Parameter `name`:** the name to assign to this sequence
**Returns:** `this`, for chaining

### `public String getName()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L236)*

Returns the name of this path sequence.

**Returns:** the sequence name, or `null` if no name has been set

## Exposed fields and types

### `public class BLinePathSequence`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L16)*
