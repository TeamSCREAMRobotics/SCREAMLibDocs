# BLinePathSequence

`com.teamscreamrobotics.util.BLinePathSequence`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java) · **14 callables** · **1 exposed fields/types** · **1 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2026: Use `BLinePathSequence` in `Routines.java`

[`src/main/java/frc2026/tars/autonomous/Routines.java` lines 87–102](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/autonomous/Routines.java#L87-L102)

```java
"deployIntake", intakeWrist.applyGoalCommand(IntakeWristGoal.EXTENDED));
FollowPath.registerEventTrigger(
    "intakeFeed", new IntakeFeed(feeder, rollers, shooter.beam, shooter.beamOne));

Overbump_Outpost =
    new BLinePathSequence(
        pathBuilder, FieldSymmetry.kRotational, "Overbump_One", "Overbump_Two");

Overbump_Depot = Overbump_Outpost.mirror();

Middle =
    new BLinePathSequence(pathBuilder, FieldSymmetry.kRotational, "Middle_One", "Middle_Two");

routineChooser = new SendableChooser<>();
routineChooser.setDefaultOption("Do Nothing", Commands.none().withName("Do Nothing"));
routineChooser.addOption("Overbump Outpost", OverbumpOutpost().withName("Overbump Outpost"));
```

## Public and protected callables

### `public BLinePathSequence(FollowPath.Builder builder, FieldSymmetry fieldSymmetry, String... pathNames)`

[Source lines 44–56](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L44)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- It changes object/subclass state through `builder`, `fieldSymmetry`, `pathNames`.
- It has 1 conditional path: `pathNames.length == 0`.
- It iterates through 1 loop; work scales with the associated collection/range.
- It can explicitly throw `InvalidParameterException`.
- Key collaborators/calls: `InvalidParameterException()`, `entries.add()`, `PathEntry()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `builder` | `FollowPath.Builder` | `FollowPath.Builder` input consumed by the implementation shown below. |
| `fieldSymmetry` | `FieldSymmetry` | `FieldSymmetry` input consumed by the implementation shown below. |
| `pathNames` | `String...` | `String...` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `BLinePathSequence` instance.

??? example "Implementation (source lines 44–56)"

    ```java
    public BLinePathSequence(FollowPath.Builder builder, FieldSymmetry fieldSymmetry, String... pathNames){
        this.builder = builder;
        this.fieldSymmetry = fieldSymmetry;
        this.pathNames = pathNames;
    
        if (pathNames.length == 0) {
            throw new InvalidParameterException("Cannot create path sequence of length 0");
        }
    
        for (String pathName : pathNames){
            entries.add(new PathEntry(pathName, false));
        }
    }
    ```

### `public static boolean isRunningPath()`

[Source lines 91–93](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L91)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `isRunningPath`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 91–93)"

    ```java
    public static boolean isRunningPath(){
        return isRunningPath;
    }
    ```

### `public Pose2d getStartingPose()`

[Source lines 106–110](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L106)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `loadPath(entries.get(0)) .orElseThrow(() -> new RuntimeException("Failed to load path: " + entries.get(0).name)) .getStartPose()`.
- Key collaborators/calls: `loadPath()`, `entries.get()`, `orElseThrow()`, `RuntimeException()`, `getStartPose()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 106–110)"

    ```java
    public Pose2d getStartingPose(){
        return loadPath(entries.get(0))
            .orElseThrow(() -> new RuntimeException("Failed to load path: " + entries.get(0).name))
            .getStartPose();
    }
    ```

### `public Command getStart()`

[Source lines 113–118](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L113)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It has 1 conditional path: `index == -1`.
- Return path: `getPathCommand(entries.get(0))`.
- Key collaborators/calls: `getPathCommand()`, `entries.get()`.

**Inputs:** None.

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 113–118)"

    ```java
    public Command getStart(){
        if(index == -1){
            index = 0;
        }
        return getPathCommand(entries.get(0));
    }
    ```

### `public Command getEnd()`

[Source lines 121–123](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L121)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getPathCommand(entries.get(entries.size() - 1))`.
- Key collaborators/calls: `getPathCommand()`, `entries.get()`, `entries.size()`.

**Inputs:** None.

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 121–123)"

    ```java
    public Command getEnd(){
        return getPathCommand(entries.get(entries.size() - 1));
    }
    ```

### `public int getSize()`

[Source lines 126–128](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L126)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `entries.size()`.
- Key collaborators/calls: `entries.size()`.

**Inputs:** None.

**Result:** Returns `int`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 126–128)"

    ```java
    public int getSize(){
        return entries.size();
    }
    ```

### `public Command getNext()`

[Source lines 135–147](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L135)

**Detailed behavior**

- The implementation executes 10 non-blank source lines.
- It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.
- It has 1 conditional path: `index + 1 >= entries.size(`.
- Return paths: `new InstantCommand()`; `getPathCommand(entries.get(index))`.
- Key collaborators/calls: `entries.size()`, `DriverStation.reportWarning()`, `InstantCommand()`, `getPathCommand()`, `entries.get()`.

**Inputs:** None.

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 135–147)"

    ```java
    public Command getNext(){
        if (index + 1 >= entries.size()) {
            DriverStation.reportWarning(
                "[Auto] No additional paths. Last supplied path: " +
                pathNames[pathNames.length - 1],
                true
            );
            return new InstantCommand();
        }
    
        index++;
        return getPathCommand(entries.get(index));
    }
    ```

### `public Command getAll()`

[Source lines 150–156](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L150)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `new SequentialCommandGroup(commands)`.
- Key collaborators/calls: `entries.size()`, `getPathCommand()`, `entries.get()`, `SequentialCommandGroup()`.

**Inputs:** None.

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 150–156)"

    ```java
    public Command getAll(){
        Command[] commands = new Command[entries.size()];
        for (int i = 0; i < entries.size(); i++){
            commands[i] = getPathCommand(entries.get(i));
        }
        return new SequentialCommandGroup(commands);
    }
    ```

### `public Command getIndex(int index)`

[Source lines 164–174](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L164)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.
- It has 1 conditional path: `index < 0 || index >= entries.size(`.
- Return paths: `new InstantCommand()`; `getPathCommand(entries.get(index))`.
- Key collaborators/calls: `entries.size()`, `DriverStation.reportWarning()`, `InstantCommand()`, `getPathCommand()`, `entries.get()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `index` | `int` | `int` input consumed by the implementation shown below. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 164–174)"

    ```java
    public Command getIndex(int index){
        if (index < 0 || index >= entries.size()) {
            DriverStation.reportWarning(
                "[Auto] No path at specified index " + index +
                ". Last supplied path: " + pathNames[pathNames.length - 1],
                true
            );
            return new InstantCommand();
        }
        return getPathCommand(entries.get(index));
    }
    ```

### `public Optional&lt;Path&gt; getPath(int index)`

[Source lines 183–193](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L183)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.
- It has 1 conditional path: `index < 0 || index >= entries.size(`.
- Return paths: `Optional.empty()`; `loadPath(entries.get(index))`.
- Key collaborators/calls: `entries.size()`, `DriverStation.reportWarning()`, `Optional.empty()`, `loadPath()`, `entries.get()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `index` | `int` | `int` input consumed by the implementation shown below. |

**Result:** Returns `Optional&lt;Path&gt;`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 183–193)"

    ```java
    public Optional<Path> getPath(int index){
        if (index < 0 || index >= entries.size()) {
            DriverStation.reportWarning(
                "[Auto] No path at specified index " + index +
                ". Last supplied path: " + pathNames[pathNames.length - 1],
                true
            );
            return Optional.empty();
        }
        return loadPath(entries.get(index));
    }
    ```

### `public BLinePathSequence withAdditional(String... pathNames)`

[Source lines 201–206](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L201)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `this`.
- Key collaborators/calls: `entries.add()`, `PathEntry()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pathNames` | `String...` | `String...` input consumed by the implementation shown below. |

**Result:** Returns `BLinePathSequence`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 201–206)"

    ```java
    public BLinePathSequence withAdditional(String... pathNames){
        for (String pathName : pathNames){
            entries.add(new PathEntry(pathName, false));
        }
        return this;
    }
    ```

### `public BLinePathSequence mirror()`

[Source lines 216–218](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L216)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new BLinePathSequence(this, true)`.
- Key collaborators/calls: `BLinePathSequence()`.

**Inputs:** None.

**Result:** Returns `BLinePathSequence`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 216–218)"

    ```java
    public BLinePathSequence mirror() {
        return new BLinePathSequence(this, true);
    }
    ```

### `public BLinePathSequence withName(String name)`

[Source lines 226–229](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L226)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `name`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | `String` | `String` input consumed by the implementation shown below. |

**Result:** Returns `BLinePathSequence`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 226–229)"

    ```java
    public BLinePathSequence withName(String name) {
        this.name = name;
        return this;
    }
    ```

### `public String getName()`

[Source lines 236–238](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L236)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `name`.

**Inputs:** None.

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 236–238)"

    ```java
    public String getName() {
        return name;
    }
    ```

## Exposed fields and types

### `public class BLinePathSequence`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/BLinePathSequence.java#L16)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
