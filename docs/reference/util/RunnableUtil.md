# RunnableUtil

`com.teamscreamrobotics.util.RunnableUtil`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java) · **10 callables** · **3 exposed fields/types** · **1 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

!!! note "2025 package names"
    The 2025 robot used SCREAMLib's earlier short packages such as `data`, `drivers`, and `util`. With SCREAMLib 26.3.7, prefix those imports with `com.teamscreamrobotics.`; the implementation pattern remains applicable.

### 2025: Reload an autonomous command only when the dashboard selection changes

[`src/main/java/frc2025/Robot.java` lines 25–77](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/Robot.java#L25-L77)

```java
public class Robot extends TimedRobot {
  private Command autonomousCommand;

  private List<Command> allCommands = new ArrayList<>();

  private RunOnce autoCommandReloader = new RunOnce();

  private boolean hasScheduledAutoInit = false;

  private final RobotContainer robotContainer;

  public Robot() {
    // super(0.0225);
    robotContainer = new RobotContainer();

    Logger.setOptions(
        new DogLogOptions()
            .withCaptureDs(true)
            .withCaptureNt(true)
            .withLogExtras(true)
            .withNtPublish(true)
            .withLogEntryQueueCapacity(2000));
    Logger.setEnabled(true);

    SignalLogger.enableAutoLogging(true);

    CommandScheduler.getInstance().onCommandInitialize((command) -> allCommands.add(command));
    CommandScheduler.getInstance().onCommandFinish((command) -> allCommands.remove(command));
    CommandScheduler.getInstance().onCommandInterrupt((command) -> allCommands.remove(command));

    FollowPathCommand.warmupCommand().schedule();
    DriveToPose.warmup(robotContainer.getSubsystems());

    Threads.setCurrentThreadPriority(true, 10);
  }

  @Override
  public void robotPeriodic() {
    CommandScheduler.getInstance().run();
    robotContainer.logTelemetry();
    Dashboard.periodic();
    RobotContainer.getVisionManager().periodic();

    Logger.log(
        "AllCommands",
        allCommands.stream().map((command) -> command.getName()).toArray(String[]::new));

    autoCommandReloader.runOnceWhenChanged(
        () -> {
          autonomousCommand = robotContainer.getAutonomousCommand();
        },
        robotContainer.getAutoSelector().getSelected());
  }
```

## Public and protected callables

### `public void runOnce(Runnable runnable)`

[Source lines 20–24](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L20)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `hasRun.compareAndSet(false, true`.
- Key collaborators/calls: `hasRun.compareAndSet()`, `runnable.run()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `runnable` | `Runnable` | `Runnable` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 20–24)"

    ```java
    public void runOnce(Runnable runnable) {
      if (hasRun.compareAndSet(false, true)) {
        runnable.run();
      }
    }
    ```

### `public void runOnceWhen(Runnable runnable, boolean condition)`

[Source lines 27–31](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L27)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It has 1 conditional path: `!hasRun.get(`.
- Key collaborators/calls: `hasRun.get()`, `hasRun.compareAndSet()`, `runnable.run()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `runnable` | `Runnable` | `Runnable` input consumed by the implementation shown below. |
| `condition` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 27–31)"

    ```java
    public void runOnceWhen(Runnable runnable, boolean condition) {
      if (!hasRun.get() && condition && hasRun.compareAndSet(false, true)) {
        runnable.run();
      }
    }
    ```

### `public &lt;T&gt; void runOnceWhenChanged(Runnable runnable, T newValue)`

[Source lines 40–47](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L40)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- It has 2 conditional paths: `isInitialized.get(`; `!isInitialized.getAndSet(true`.
- Key collaborators/calls: `isInitialized.get()`, `newValue.equals()`, `lastValue.get()`, `lastValue.set()`, `runnable.run()`, `isInitialized.getAndSet()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `runnable` | `Runnable` | `Runnable` input consumed by the implementation shown below. |
| `newValue` | `T` | `T` input consumed by the implementation shown below. |

**Result:** Returns `&lt;T&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 40–47)"

    ```java
    public <T> void runOnceWhenChanged(Runnable runnable, T newValue) {
      if (isInitialized.get() && !newValue.equals(lastValue.get())) {
        lastValue.set(newValue);
        runnable.run();
      } else if (!isInitialized.getAndSet(true)) {
        lastValue.set(newValue);
      }
    }
    ```

### `public &lt;T&gt; void runOnceWhenTrueThenWhenChanged( Runnable runnable, boolean condition, T newValue)`

[Source lines 57–69](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L57)

**Detailed behavior**

- The implementation executes 10 non-blank source lines.
- It has 3 conditional paths: `!conditionMet.get(`; `condition && conditionMet.compareAndSet(false, true`; `isInitialized.get(`.
- Key collaborators/calls: `conditionMet.get()`, `conditionMet.compareAndSet()`, `runnable.run()`, `lastValue.set()`, `isInitialized.set()`, `isInitialized.get()`, `newValue.equals()`, `lastValue.get()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `runnable` | `Runnable` | `Runnable` input consumed by the implementation shown below. |
| `condition` | `boolean` | `boolean` input consumed by the implementation shown below. |
| `newValue` | `T` | `T` input consumed by the implementation shown below. |

**Result:** Returns `&lt;T&gt; void`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 57–69)"

    ```java
    public <T> void runOnceWhenTrueThenWhenChanged(
        Runnable runnable, boolean condition, T newValue) {
      if (!conditionMet.get()) {
        if (condition && conditionMet.compareAndSet(false, true)) {
          runnable.run();
          lastValue.set(newValue);
          isInitialized.set(true);
        }
      } else if (isInitialized.get() && !newValue.equals(lastValue.get())) {
        lastValue.set(newValue);
        runnable.run();
      }
    }
    ```

### `public void reset()`

[Source lines 72–74](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L72)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `hasRun.set()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 72–74)"

    ```java
    public void reset() {
      hasRun.set(false);
    }
    ```

### `public void runUntil(Runnable runnable, boolean stopCondition)`

[Source lines 90–95](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L90)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It has 1 conditional path: `!shouldStop.get(`.
- Key collaborators/calls: `shouldStop.get()`, `runnable.run()`, `shouldStop.compareAndSet()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `runnable` | `Runnable` | `Runnable` input consumed by the implementation shown below. |
| `stopCondition` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 90–95)"

    ```java
    public void runUntil(Runnable runnable, boolean stopCondition) {
      if (!shouldStop.get() && stopCondition) {
        runnable.run();
        shouldStop.compareAndSet(false, true);
      }
    }
    ```

### `public void tryUntil(Runnable runnable, boolean stopCondition)`

[Source lines 104–113](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L104)

**Detailed behavior**

- The implementation executes 8 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `shouldStop.get()`, `runnable.run()`, `shouldStop.compareAndSet()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `runnable` | `Runnable` | `Runnable` input consumed by the implementation shown below. |
| `stopCondition` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 104–113)"

    ```java
    public void tryUntil(Runnable runnable, boolean stopCondition) {
      while (!shouldStop.get() && stopCondition) {
        try {
          runnable.run();
          break;
        } catch (Exception e) {
        }
      }
      shouldStop.compareAndSet(false, true);
    }
    ```

### `public void tryUntil(Runnable runnable)`

[Source lines 121–130](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L121)

**Detailed behavior**

- The implementation executes 8 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Key collaborators/calls: `shouldStop.get()`, `runnable.run()`, `shouldStop.compareAndSet()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `runnable` | `Runnable` | `Runnable` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 121–130)"

    ```java
    public void tryUntil(Runnable runnable) {
      while (!shouldStop.get()) {
        try {
          runnable.run();
          break;
        } catch (Exception e) {
        }
      }
      shouldStop.compareAndSet(false, true);
    }
    ```

### `public void reset()`

[Source lines 133–135](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L133)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Key collaborators/calls: `shouldStop.set()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 133–135)"

    ```java
    public void reset() {
      shouldStop.set(false);
    }
    ```

### `public boolean hasStopped()`

[Source lines 138–140](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L138)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `shouldStop.get()`.
- Key collaborators/calls: `shouldStop.get()`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 138–140)"

    ```java
    public boolean hasStopped() {
      return shouldStop.get();
    }
    ```

## Exposed fields and types

### `public class RunnableUtil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L7)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static class RunOnce`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L13)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public static class RunUntil`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/RunnableUtil.java#L80)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
