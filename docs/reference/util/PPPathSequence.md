# PPPathSequence

`com.teamscreamrobotics.util.PPPathSequence`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java) · **12 callables** · **2 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public PPPathSequence(FlipType flipType, String... pathNames)`

[Source lines 53–66](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L53)

**Detailed behavior**

- The implementation executes 10 non-blank source lines.
- It changes object/subclass state through `flipType`, `pathNames`.
- It has 1 conditional path: `pathNames.length == 0`.
- It iterates through 1 loop; work scales with the associated collection/range.
- It can explicitly throw `InvalidParameterException`.
- Key collaborators/calls: `InvalidParameterException()`, `getPath()`, `orElseThrow()`, `RuntimeException()`, `list.add()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `flipType` | `FlipType` | `FlipType` input consumed by the implementation shown below. |
| `pathNames` | `String...` | `String...` input consumed by the implementation shown below. |

**Result:** Constructs and initializes a `PPPathSequence` instance.

??? example "Implementation (source lines 53–66)"

    ```java
    public PPPathSequence(FlipType flipType, String... pathNames){
        this.flipType = flipType;
        this.pathNames = pathNames;
    
        if (pathNames.length == 0) {
            throw new InvalidParameterException("Cannot create path sequence of length 0");
        }
    
        for (String pathName : pathNames){
            PathPlannerPath path = getPath(pathName)
                .orElseThrow(() -> new RuntimeException("Failed to load path: " + pathName));
            list.add(path);
        }
    }
    ```

### `public static boolean isRunningPath()`

[Source lines 80–82](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L80)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `isRunningPath`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 80–82)"

    ```java
    public static boolean isRunningPath(){
        return isRunningPath;
    }
    ```

### `public Pose2d getStartingPose()`

[Source lines 106–108](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L106)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getPathStartingPose(list.get(0))`.
- Key collaborators/calls: `getPathStartingPose()`, `list.get()`.

**Inputs:** None.

**Result:** Returns `Pose2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 106–108)"

    ```java
    public Pose2d getStartingPose(){
        return getPathStartingPose(list.get(0));
    }
    ```

### `public Command getStart()`

[Source lines 111–116](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L111)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It has 1 conditional path: `index == -1`.
- Return path: `getPathCommand(list.get(0))`.
- Key collaborators/calls: `getPathCommand()`, `list.get()`.

**Inputs:** None.

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 111–116)"

    ```java
    public Command getStart(){
        if(index == -1){
            index = 0;
        }
        return getPathCommand(list.get(0));
    }
    ```

### `public Command getEnd()`

[Source lines 119–121](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L119)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `getPathCommand(list.get(list.size() - 1))`.
- Key collaborators/calls: `getPathCommand()`, `list.get()`, `list.size()`.

**Inputs:** None.

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 119–121)"

    ```java
    public Command getEnd(){
        return getPathCommand(list.get(list.size() - 1));
    }
    ```

### `public int getSize()`

[Source lines 124–126](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L124)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `list.size()`.
- Key collaborators/calls: `list.size()`.

**Inputs:** None.

**Result:** Returns `int`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 124–126)"

    ```java
    public int getSize(){
        return list.size();
    }
    ```

### `public Command getNext()`

[Source lines 133–145](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L133)

**Detailed behavior**

- The implementation executes 10 non-blank source lines.
- It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.
- It has 1 conditional path: `index + 1 >= list.size(`.
- Return paths: `new InstantCommand()`; `getPathCommand(list.get(index))`.
- Key collaborators/calls: `list.size()`, `DriverStation.reportWarning()`, `InstantCommand()`, `getPathCommand()`, `list.get()`.

**Inputs:** None.

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 133–145)"

    ```java
    public Command getNext(){
        if (index + 1 >= list.size()) {
            DriverStation.reportWarning(
                "[Auto] No additional paths. Last supplied path: " +
                pathNames[pathNames.length - 1],
                true
            );
            return new InstantCommand();
        }
    
        index++;
        return getPathCommand(list.get(index));
    }
    ```

### `public Command getAll()`

[Source lines 148–154](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L148)

**Detailed behavior**

- The implementation executes 5 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `new SequentialCommandGroup(commands)`.
- Key collaborators/calls: `list.size()`, `getPathCommand()`, `list.get()`, `SequentialCommandGroup()`.

**Inputs:** None.

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 148–154)"

    ```java
    public Command getAll(){
        Command[] commands = new Command[list.size()];
        for (int i = 0; i < list.size(); i++){
            commands[i] = getPathCommand(list.get(i));
        }
        return new SequentialCommandGroup(commands);
    }
    ```

### `public Command getIndex(int index)`

[Source lines 162–172](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L162)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.
- It has 1 conditional path: `index < 0 || index >= list.size(`.
- Return paths: `new InstantCommand()`; `getPathCommand(list.get(index))`.
- Key collaborators/calls: `list.size()`, `DriverStation.reportWarning()`, `InstantCommand()`, `getPathCommand()`, `list.get()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `index` | `int` | `int` input consumed by the implementation shown below. |

**Result:** Returns `Command`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 162–172)"

    ```java
    public Command getIndex(int index){
        if (index < 0 || index >= list.size()) {
            DriverStation.reportWarning(
                "[Auto] No path at specified index " + index +
                ". Last supplied path: " + pathNames[pathNames.length - 1],
                true
            );
            return new InstantCommand();
        }
        return getPathCommand(list.get(index));
    }
    ```

### `public Optional&lt;PathPlannerPath&gt; getPath(int index)`

[Source lines 180–190](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L180)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.
- It has 1 conditional path: `index < 0 || index >= list.size(`.
- Return paths: `Optional.empty()`; `Optional.of(list.get(index))`.
- Key collaborators/calls: `list.size()`, `DriverStation.reportWarning()`, `Optional.empty()`, `Optional.of()`, `list.get()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `index` | `int` | `int` input consumed by the implementation shown below. |

**Result:** Returns `Optional&lt;PathPlannerPath&gt;`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 180–190)"

    ```java
    public Optional<PathPlannerPath> getPath(int index){
        if (index < 0 || index >= list.size()) {
            DriverStation.reportWarning(
                "[Auto] No path at specified index " + index +
                ". Last supplied path: " + pathNames[pathNames.length - 1],
                true
            );
            return Optional.empty();
        }
        return Optional.of(list.get(index));
    }
    ```

### `public PPPathSequence withAdditional(String... pathNames)`

[Source lines 199–204](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L199)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `this`.
- Key collaborators/calls: `getPath()`, `ifPresent()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pathNames` | `String...` | `String...` input consumed by the implementation shown below. |

**Result:** Returns `PPPathSequence`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 199–204)"

    ```java
    public PPPathSequence withAdditional(String... pathNames){
        for (String pathName : pathNames){
            getPath(pathName).ifPresent(list::add);
        }
        return this;
    }
    ```

### `public PPPathSequence mirror()`

[Source lines 213–220](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L213)

**Detailed behavior**

- The implementation executes 6 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `mirrored`.
- Key collaborators/calls: `PPPathSequence()`, `mirrored.list.clear()`, `mirrored.list.add()`, `path.mirrorPath()`.

**Inputs:** None.

**Result:** Returns `PPPathSequence`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 213–220)"

    ```java
    public PPPathSequence mirror() {
        PPPathSequence mirrored = new PPPathSequence(flipType, pathNames);
        mirrored.list.clear();
        for (PathPlannerPath path : list) {
            mirrored.list.add(path.mirrorPath());
        }
        return mirrored;
    }
    ```

## Exposed fields and types

### `public class PPPathSequence`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L25)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `public enum FlipType`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/util/PPPathSequence.java#L40)*

This exposed `enum` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
