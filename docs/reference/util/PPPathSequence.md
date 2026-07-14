# PPPathSequence

`com.teamscreamrobotics.util.PPPathSequence`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java) · **12 callables** · **2 exposed fields/types**

## Public and protected callables

### `public PPPathSequence(FlipType flipType, String... pathNames)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L53)*

Loads and prepares a sequence of PathPlanner paths for autonomous use.

**Parameter `flipType`:** how starting pose should be mirrored for the red alliance — see `FlipType`
**Parameter `pathNames`:** one or more path names to load, in order
**Throws `InvalidParameterException`:** if no path names are supplied
**Throws `RuntimeException`:** if any path fails to load

### `public static boolean isRunningPath()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L80)*

Returns `true` while any path command from this class is executing.

### `public Pose2d getStartingPose()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L106)*

Returns the starting pose of the first path — use this to reset odometry before auto.

### `public Command getStart()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L111)*

Returns a command that follows the first path in the sequence.

### `public Command getEnd()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L119)*

Returns a command that follows the last path in the sequence.

### `public int getSize()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L124)*

Returns the total number of paths in this sequence.

### `public Command getNext()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L133)*

Advances the internal cursor and returns a command for the next path.
Starts at index 1 on first call (use `#getStart()` for index 0).
Returns a no-op `InstantCommand` and logs a DS warning if already at the last path.

### `public Command getAll()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L148)*

Returns a `SequentialCommandGroup` that runs all paths in order.

### `public Command getIndex(int index)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L162)*

Returns a command for the path at `index`.
Returns a no-op `InstantCommand` and logs a DS warning if out of bounds.

**Parameter `index`:** zero-based path index

### `public Optional&lt;PathPlannerPath&gt; getPath(int index)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L180)*

Returns the raw `Path` at `index`, or `Optional#empty()` if out of bounds.
Use this when you need direct path access rather than a follow command.

**Parameter `index`:** zero-based path index

### `public PPPathSequence withAdditional(String... pathNames)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L199)*

Appends additional paths to the end of this sequence.
Paths that fail to load are skipped with a DS error (no exception thrown).

**Parameter `pathNames`:** one or more path names to append
**Returns:** `this`, for chaining

### `public PPPathSequence mirror()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L213)*

Returns a new `PPPathSequence` with all paths mirrored across the field
width centerline, regardless of alliance. Use this when reusing a path designed
for one half of the field on the other (e.g. top wall path -> bottom wall path).

**Returns:** a new `PPPathSequence` with mirrored paths

## Exposed fields and types

### `public class PPPathSequence`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L25)*

Ordered sequence of PathPlanner paths for autonomous routines.
Handles alliance-aware starting pose flipping and provides cursor-based path traversal.

### `public enum FlipType`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L40)*

Defines how a path should be transformed to produce its field-symmetric equivalent.


- `#RotatedField` - Use for rotationally symmetric fields (e.g. Rebuilt 2026).
Calls `AllianceFlipUtil#FlippedPose2d()` only, which rotates 180 degrees around the field center.
- `#SymmetricField` - Use for bilaterally symmetric fields where blue and red are
mirrored across the length midline (y axis). Calls `AllianceFlipUtil#MirroredPose2d()`, transforming both alliance side and field half.
