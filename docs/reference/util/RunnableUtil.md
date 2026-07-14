# RunnableUtil

`com.teamscreamrobotics.util.RunnableUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java) · **10 callables** · **3 exposed fields/types**

## Competition usage

**2025:** [`Robot.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/Robot.java#L23), [`Drivetrain.java`](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/subsystems/drivetrain/Drivetrain.java#L34)

**2026:** [`Drivetrain.java`](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/drivetrain/Drivetrain.java#L14)

## Public and protected callables

### `public void runOnce(Runnable runnable)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L20)*

Runs `runnable` the first time this method is called; subsequent calls are no-ops.

### `public void runOnceWhen(Runnable runnable, boolean condition)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L27)*

Runs `runnable` the first time `condition` is `true`; no-op thereafter.

### `public &lt;T&gt; void runOnceWhenChanged(Runnable runnable, T newValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L40)*

Runs `runnable` each time `newValue` differs from the previous call's value.
Does not fire on the first call (initialization).

**Parameter `runnable`:** the action to execute on change
**Parameter `newValue`:** the value to compare against the previous call

### `public &lt;T&gt; void runOnceWhenTrueThenWhenChanged( Runnable runnable, boolean condition, T newValue)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L57)*

Fires `runnable` the first time `condition` becomes `true`, then again
on every subsequent change to `newValue`.

**Parameter `runnable`:** the action to execute
**Parameter `condition`:** the trigger condition
**Parameter `newValue`:** the value to monitor for changes after the condition is met

### `public void reset()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L72)*

Resets the run state so the next call to any `run*` method fires again.

### `public void runUntil(Runnable runnable, boolean stopCondition)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L90)*

Runs `runnable` once if `stopCondition` is `true` and has not already stopped.
Marks as stopped after running.

**Parameter `runnable`:** the action to execute
**Parameter `stopCondition`:** when `true`, executes and then stops future calls

### `public void tryUntil(Runnable runnable, boolean stopCondition)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L104)*

Retries `runnable` in a loop while `stopCondition` is `true` and
not yet stopped, silently swallowing exceptions until it succeeds.

**Parameter `runnable`:** the action to attempt
**Parameter `stopCondition`:** loop continues while this is `true` and not stopped

### `public void tryUntil(Runnable runnable)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L121)*

Retries `runnable` until it succeeds without throwing, silently swallowing exceptions.
Marks as stopped on first success.

**Parameter `runnable`:** the action to attempt repeatedly

### `public void reset()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L133)*

Resets the stopped state so future calls to `runUntil`/`tryUntil` can fire again.

### `public boolean hasStopped()`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L138)*

Returns `true` if this instance has reached its stop condition.

## Exposed fields and types

### `public class RunnableUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L7)*

Thread-safe utility classes for executing runnables conditionally or exactly once.

### `public static class RunOnce`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L13)*

Executes a `Runnable` at most once (or once per triggering condition).
All state is thread-safe via atomics.

### `public static class RunUntil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L80)*

Executes a `Runnable` until a stop condition is met, with optional retry-on-exception.
