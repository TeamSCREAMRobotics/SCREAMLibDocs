# Ligament

`com.teamscreamrobotics.dashboard.Ligament`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java) · **15 callables** · **4 exposed fields/types** · **1 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2026: Use `Ligament` in `IntakeWrist.java`

[`src/main/java/frc2026/tars/subsystems/intake/IntakeWrist.java` lines 21–36](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/intake/IntakeWrist.java#L21-L36)

```java
import lombok.Getter;

public class IntakeWrist extends TalonFXSubsystem {

  private final Ligament intakeOne =
      new Ligament()
          .withStaticLength(Length.fromInches(9.58))
          .withDynamicAngle(() -> getAngle(), () -> Rotation2d.fromRotations(getSetpoint()));
  private final Ligament intakeTwo =
      new Ligament()
          .withStaticLength(Length.fromInches(8.5))
          .withDynamicAngle(
              () -> getAngle().unaryMinus().minus(Rotation2d.fromDegrees(90)),
              () ->
                  Rotation2d.fromRotations(getSetpoint())
                      .unaryMinus()
```

## Public and protected callables

### `public Ligament()`

[Source lines 30–30](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L30)

**Detailed behavior**

- This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself.

**Inputs:** None.

**Result:** Constructs and initializes a `Ligament` instance.

??? example "Implementation (source lines 30)"

    ```java
    public Ligament(){}
    ```

### `protected void initialize(int index, MechanismRoot2d measured, MechanismRoot2d setpoint)`

[Source lines 32–37](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L32)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It changes object/subclass state through `measuredLig`, `setpointLig`.
- Key collaborators/calls: `measured.append()`, `MechanismLigament2d()`, `Color8Bit()`, `setpoint.append()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `index` | `int` | `int` input consumed by the implementation shown below. |
| `measured` | `MechanismRoot2d` | `MechanismRoot2d` input consumed by the implementation shown below. |
| `setpoint` | `MechanismRoot2d` | `MechanismRoot2d` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 32–37)"

    ```java
    protected void initialize(int index, MechanismRoot2d measured, MechanismRoot2d setpoint){
      measuredLig = measured.append(
          new MechanismLigament2d("Joint " + (index + 1),  0.0, 0.0, 6, new Color8Bit(Color.kRed)));
      setpointLig = setpoint.append(
          new MechanismLigament2d("Joint " + (index + 1), 0.0, 0.0, 6, new Color8Bit(Color.kGreen)));
    }
    ```

### `protected void initialize(int index, MechanismLigament2d previousMeasured, MechanismLigament2d previousSetpoint)`

[Source lines 39–44](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L39)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It changes object/subclass state through `measuredLig`, `setpointLig`.
- Key collaborators/calls: `previousMeasured.append()`, `MechanismLigament2d()`, `Color8Bit()`, `previousSetpoint.append()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `index` | `int` | `int` input consumed by the implementation shown below. |
| `previousMeasured` | `MechanismLigament2d` | `MechanismLigament2d` input consumed by the implementation shown below. |
| `previousSetpoint` | `MechanismLigament2d` | `MechanismLigament2d` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 39–44)"

    ```java
    protected void initialize(int index, MechanismLigament2d previousMeasured, MechanismLigament2d previousSetpoint){
      measuredLig = previousMeasured.append(
          new MechanismLigament2d("Joint " + (index + 1), 0.0, 0.0, 6, new Color8Bit(Color.kRed)));
      setpointLig = previousSetpoint.append(
          new MechanismLigament2d("Joint " + (index + 1), 0.0, 0.0, 6, new Color8Bit(Color.kGreen)));
    }
    ```

### `public Ligament withOverrideAppend(boolean override)`

[Source lines 50–53](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L50)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `overrideAppend`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `override` | `boolean` | `boolean` input consumed by the implementation shown below. |

**Result:** Returns `Ligament`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 50–53)"

    ```java
    public Ligament withOverrideAppend(boolean override){
      overrideAppend = override;
      return this;
    }
    ```

### `public Ligament withStaticAngle(Rotation2d angle)`

[Source lines 60–64](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L60)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `measuredAngle`, `setpointAngle`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `angle` | `Rotation2d` | `Rotation2d` input consumed by the implementation shown below. |

**Result:** Returns `Ligament`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 60–64)"

    ```java
    public Ligament withStaticAngle(Rotation2d angle) {
      this.measuredAngle = () -> angle;
      this.setpointAngle = () -> angle;
      return this;
    }
    ```

### `public Ligament withDynamicAngle(Supplier&lt;Rotation2d&gt; measured, Supplier&lt;Rotation2d&gt; setpoint)`

[Source lines 72–76](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L72)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `measuredAngle`, `setpointAngle`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `measured` | `Supplier&lt;Rotation2d&gt;` | Callback evaluated at use time rather than construction time. |
| `setpoint` | `Supplier&lt;Rotation2d&gt;` | Callback evaluated at use time rather than construction time. |

**Result:** Returns `Ligament`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 72–76)"

    ```java
    public Ligament withDynamicAngle(Supplier<Rotation2d> measured, Supplier<Rotation2d> setpoint) {
      this.measuredAngle = measured;
      this.setpointAngle = setpoint;
      return this;
    }
    ```

### `public Ligament withDynamicAngle(Supplier&lt;Rotation2d&gt; angle)`

[Source lines 83–87](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L83)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `measuredAngle`, `setpointAngle`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `angle` | `Supplier&lt;Rotation2d&gt;` | Callback evaluated at use time rather than construction time. |

**Result:** Returns `Ligament`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 83–87)"

    ```java
    public Ligament withDynamicAngle(Supplier<Rotation2d> angle) {
      this.measuredAngle = angle;
      this.setpointAngle = angle;
      return this;
    }
    ```

### `public Ligament withStaticLength(Length length)`

[Source lines 94–98](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L94)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `measuredLength`, `setpointLength`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `length` | `Length` | `Length` input consumed by the implementation shown below. |

**Result:** Returns `Ligament`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 94–98)"

    ```java
    public Ligament withStaticLength(Length length) {
      this.measuredLength = () -> length;
      this.setpointLength = () -> length;
      return this;
    }
    ```

### `public Ligament withDynamicLength(Supplier&lt;Length&gt; measured, Supplier&lt;Length&gt; setpoint)`

[Source lines 106–110](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L106)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `measuredLength`, `setpointLength`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `measured` | `Supplier&lt;Length&gt;` | Callback evaluated at use time rather than construction time. |
| `setpoint` | `Supplier&lt;Length&gt;` | Callback evaluated at use time rather than construction time. |

**Result:** Returns `Ligament`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 106–110)"

    ```java
    public Ligament withDynamicLength(Supplier<Length> measured, Supplier<Length> setpoint) {
      this.measuredLength = measured;
      this.setpointLength = setpoint;
      return this;
    }
    ```

### `public Ligament withDynamicLength(Supplier&lt;Length&gt; length)`

[Source lines 117–121](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L117)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `measuredLength`, `setpointLength`.
- Return path: `this`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `length` | `Supplier&lt;Length&gt;` | Callback evaluated at use time rather than construction time. |

**Result:** Returns `Ligament`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 117–121)"

    ```java
    public Ligament withDynamicLength(Supplier<Length> length) {
      this.measuredLength = length;
      this.setpointLength = length;
      return this;
    }
    ```

### `public void setAngle(Rotation2d angle)`

[Source lines 128–131](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L128)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `measuredAngle`, `setpointAngle`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `angle` | `Rotation2d` | `Rotation2d` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 128–131)"

    ```java
    public void setAngle(Rotation2d angle) {
      this.measuredAngle = () -> angle;
      this.setpointAngle = () -> angle;
    }
    ```

### `public void setAngle(Rotation2d measured, Rotation2d setpoint)`

[Source lines 139–142](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L139)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `measuredAngle`, `setpointAngle`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `measured` | `Rotation2d` | `Rotation2d` input consumed by the implementation shown below. |
| `setpoint` | `Rotation2d` | `Rotation2d` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 139–142)"

    ```java
    public void setAngle(Rotation2d measured, Rotation2d setpoint) {
      this.measuredAngle = () -> measured;
      this.setpointAngle = () -> setpoint;
    }
    ```

### `public void setLength(Length length)`

[Source lines 149–152](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L149)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `measuredLength`, `setpointLength`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `length` | `Length` | `Length` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 149–152)"

    ```java
    public void setLength(Length length) {
      this.measuredLength = () -> length;
      this.setpointLength = () -> length;
    }
    ```

### `public void setLength(Length measured, Length setpoint)`

[Source lines 160–163](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L160)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- It changes object/subclass state through `measuredLength`, `setpointLength`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `measured` | `Length` | `Length` input consumed by the implementation shown below. |
| `setpoint` | `Length` | `Length` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 160–163)"

    ```java
    public void setLength(Length measured, Length setpoint) {
      this.measuredLength = () -> measured;
      this.setpointLength = () -> setpoint;
    }
    ```

### `protected void update()`

[Source lines 165–170](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L165)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Key collaborators/calls: `this.setpointLig.setLength()`, `setpointLength.get()`, `getMeters()`, `this.setpointLig.setAngle()`, `setpointAngle.get()`, `getDegrees()`, `this.measuredLig.setLength()`, `measuredLength.get()`, `this.measuredLig.setAngle()`, `measuredAngle.get()`.

**Inputs:** None.

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 165–170)"

    ```java
    protected void update(){
      this.setpointLig.setLength(setpointLength.get().getMeters());
      this.setpointLig.setAngle(setpointAngle.get().getDegrees());
      this.measuredLig.setLength(measuredLength.get().getMeters());
      this.measuredLig.setAngle(measuredAngle.get().getDegrees());
    }
    ```

## Exposed fields and types

### `public class Ligament`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L17)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

### `protected MechanismLigament2d measuredLig`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L19)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 5 times, so changing it can affect every control path that reads `measuredLig`.

### `protected MechanismLigament2d setpointLig`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L20)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 5 times, so changing it can affect every control path that reads `setpointLig`.

### `protected boolean overrideAppend`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/dashboard/Ligament.java#L27)*

This is a **protected** field without an inline initializer. It is mutable by callers/subclasses. The declaring source references it 2 times, so changing it can affect every control path that reads `overrideAppend`.
