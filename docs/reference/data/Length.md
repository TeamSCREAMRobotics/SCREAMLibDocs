# Length

`com.teamscreamrobotics.data.Length`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java) · **27 callables** · **3 exposed fields/types** · **2 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.

### 2025: Keep field dimensions and zone sizes unit-safe (legacy package names)

[`src/main/java/frc2025/constants/FieldConstants.java` lines 51–93](https://github.com/TeamSCREAMRobotics/4522_2025Competition/blob/38f0984ae704c4e3da266547f38d9efcdccebe9b/src/main/java/frc2025/constants/FieldConstants.java#L51-L93)

```java
public static final Length CORAL_DIAMETER = Length.fromInches(4.5);

public static final Length BRANCH_TO_REEF_EDGE = Length.fromInches(2.111249);

public static final double STATION_X_OFFSET = -0.1; // -0.1
public static final double STATION_Y_OFFSET = -0.1; // -0.1

public static final Pose2d BLUE_PROCESSOR_FEEDER_ALIGN =
    new Pose2d(1.544 - STATION_X_OFFSET, 0.734 - STATION_Y_OFFSET, Rotation2d.fromDegrees(54.0));
public static final Pose2d RED_PROCESSOR_FEEDER_ALIGN =
    new Pose2d(
        FIELD_DIMENSIONS.getX() - 1.544 + STATION_X_OFFSET,
        FIELD_DIMENSIONS.getY() - 0.734 + STATION_Y_OFFSET,
        Rotation2d.fromDegrees(54.0 + 180.0));

public static final Pose2d BLUE_NONPROCESSOR_FEEDER_ALIGN =
    new Pose2d(1.544 - STATION_X_OFFSET, 7.293 + STATION_Y_OFFSET, Rotation2d.fromDegrees(-54.0));
public static final Pose2d RED_NONPROCESSOR_FEEDER_ALIGN =
    new Pose2d(
        FIELD_DIMENSIONS.getX() - 1.544 + STATION_X_OFFSET,
        0.734 - STATION_Y_OFFSET,
        Rotation2d.fromDegrees(-54.0 + 180.0));

public static final Pose2d BLUE_BARGE_ALIGN =
    new Pose2d(/* 7.7 */ 7.5, FIELD_DIMENSIONS.getY() * /* 0.75 */ 0.65, Rotation2d.kZero);
public static final Pose2d RED_BARGE_ALIGN =
    new Pose2d(
        FIELD_DIMENSIONS.getX() - /* 7.7 */ 7.5,
        FIELD_DIMENSIONS.getY() * /* 0.25 */ 0.35,
        Rotation2d.k180deg);
public static final Pose2d BLUE_BARGE_ALIGN_FLIPPED =
    new Pose2d(/* 7.7 */ 10.25, FIELD_DIMENSIONS.getY() * /* 0.75 */ 0.65, Rotation2d.k180deg);
public static final Pose2d RED_BARGE_ALIGN_FLIPPED =
    new Pose2d(FIELD_DIMENSIONS.getX() - 10.25, FIELD_DIMENSIONS.getY() * 0.35, Rotation2d.kZero);

public static final Translation2d BLUE_REEF_CENTER =
    new Translation2d(Units.inchesToMeters(176.746), FIELD_DIMENSIONS.getY() / 2.0);
public static final Translation2d RED_REEF_CENTER = FIELD_DIMENSIONS.minus(BLUE_REEF_CENTER);

public static final HexagonalPoseArea BLUE_REEF =
    new HexagonalPoseArea(BLUE_REEF_CENTER, Length.fromMeters(10), Rotation2d.fromDegrees(-30));
public static final HexagonalPoseArea RED_REEF =
    new HexagonalPoseArea(RED_REEF_CENTER, Length.fromMeters(10), Rotation2d.fromDegrees(-30));
```

### 2026: Represent wheel dimensions and derived circumference

[`src/main/java/frc2026/tars/subsystems/shooter/flywheel/FlywheelConstants.java` lines 12–21](https://github.com/TeamSCREAMRobotics/4522_2026Competition/blob/e9d3ad1471c68ffa779655b75c4d56b9b7730325/src/main/java/frc2026/tars/subsystems/shooter/flywheel/FlywheelConstants.java#L12-L21)

```java
public class FlywheelConstants {
  public static final double FLYWHEEL_REDUCTION = 1.0;

  public static final Length FLYWHEEL_CIRCUMFERENCE = Length.fromInches(4.0 * Math.PI);

  public static final Length FLYWHEEL_DIAMETER = Length.fromInches(4.0);
  public static final Length FLYWHEEL_RADIUS = Length.fromInches(FLYWHEEL_DIAMETER.getInches() / 2);

  public static final TalonFXSubsystemConfiguration FLYWHEEL_CONFIG =
      new TalonFXSubsystemConfiguration();
```

## Public and protected callables

### `public Length()`

[Source lines 16–18](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L16)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It delegates initialization to another constructor in the same type with `0`.

**Inputs:** None.

**Result:** Constructs and initializes a `Length` instance.

??? example "Implementation (source lines 16–18)"

    ```java
    public Length() {
      this(0);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a zero-length value.

### `public Length(double inches)`

[Source lines 25–27](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L25)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `inches`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `inches` | `double` | the distance in inches |

**Result:** Constructs and initializes a `Length` instance.

??? example "Implementation (source lines 25–27)"

    ```java
    public Length(double inches) {
      this.inches = inches;
    }
    ```

??? note "Author note from JavaDoc"

    Creates a length from a raw inch value.
    
    **Parameter `inches`:** the distance in inches

### `public static Length fromInches(double inches)`

[Source lines 30–32](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L30)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Length(inches)`.
- Key collaborators/calls: `Length()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `inches` | `double` | Linear value in inches. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 30–32)"

    ```java
    public static Length fromInches(double inches) {
      return new Length(inches);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a `Length` from a value in inches.

### `public static Length fromFeet(double feet)`

[Source lines 35–37](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L35)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `from(feet, 12.0)`.
- Key collaborators/calls: `from()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `feet` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 35–37)"

    ```java
    public static Length fromFeet(double feet) {
      return from(feet, 12.0);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a `Length` from a value in feet.

### `public static Length fromCentimeters(double centimeters)`

[Source lines 40–42](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L40)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `from(centimeters, 1.0 / 2.54)`.
- Key collaborators/calls: `from()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `centimeters` | `double` | Linear value in meters. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 40–42)"

    ```java
    public static Length fromCentimeters(double centimeters) {
      return from(centimeters, 1.0 / 2.54);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a `Length` from a value in centimeters.

### `public static Length fromMeters(double meters)`

[Source lines 45–47](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L45)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `from(meters, 39.37)`.
- Key collaborators/calls: `from()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `meters` | `double` | Linear value in meters. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 45–47)"

    ```java
    public static Length fromMeters(double meters) {
      return from(meters, 39.37);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a `Length` from a value in meters.

### `public static Length fromRotations(double rotations, Length circumference)`

[Source lines 55–57](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L55)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Length(rotations * circumference.inches)`.
- Key collaborators/calls: `Length()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `rotations` | `double` | number of full rotations **Parameter `circumference`:** the circumference per rotation |
| `circumference` | `Length` | the circumference per rotation |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 55–57)"

    ```java
    public static Length fromRotations(double rotations, Length circumference) {
      return new Length(rotations * circumference.inches);
    }
    ```

??? note "Author note from JavaDoc"

    Converts a rotational distance to a linear distance given a wheel/spool circumference.
    
    **Parameter `rotations`:** number of full rotations
    **Parameter `circumference`:** the circumference per rotation

### `public static Length from(double value, double inchConversionFactor)`

[Source lines 65–67](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L65)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Length(value * inchConversionFactor)`.
- Key collaborators/calls: `Length()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | `double` | the measurement in the source unit **Parameter `inchConversionFactor`:** inches per source unit (e.g. `39.37` for meters) |
| `inchConversionFactor` | `double` | inches per source unit (e.g. `39.37` for meters) |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 65–67)"

    ```java
    public static Length from(double value, double inchConversionFactor) {
      return new Length(value * inchConversionFactor);
    }
    ```

??? note "Author note from JavaDoc"

    Creates a `Length` from an arbitrary unit by supplying the inches-per-unit factor.
    
    **Parameter `value`:** the measurement in the source unit
    **Parameter `inchConversionFactor`:** inches per source unit (e.g. `39.37` for meters)

### `public Length plus(Length other)`

[Source lines 70–72](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L70)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Return path: `new Length(this.inches + other.getInches())`.
- Key collaborators/calls: `Length()`, `other.getInches()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `other` | `Length` | `Length` input consumed by the implementation shown below. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 70–72)"

    ```java
    public Length plus(Length other) {
      return new Length(this.inches + other.getInches());
    }
    ```

??? note "Author note from JavaDoc"

    Returns a new `Length` equal to `this + other`.

### `public Length minus(Length other)`

[Source lines 75–77](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L75)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Return path: `new Length(this.inches - other.getInches())`.
- Key collaborators/calls: `Length()`, `other.getInches()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `other` | `Length` | `Length` input consumed by the implementation shown below. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 75–77)"

    ```java
    public Length minus(Length other) {
      return new Length(this.inches - other.getInches());
    }
    ```

??? note "Author note from JavaDoc"

    Returns a new `Length` equal to `this - other`.

### `public Length times(double scalar)`

[Source lines 80–82](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L80)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Length(this.inches * scalar)`.
- Key collaborators/calls: `Length()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `scalar` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 80–82)"

    ```java
    public Length times(double scalar) {
      return new Length(this.inches * scalar);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a new `Length` scaled by `scalar`.

### `public Length div(double scalar)`

[Source lines 85–87](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L85)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Length(this.inches / scalar)`.
- Key collaborators/calls: `Length()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `scalar` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 85–87)"

    ```java
    public Length div(double scalar) {
      return new Length(this.inches / scalar);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a new `Length` divided by `scalar`.

### `public Length times(Length scalar)`

[Source lines 90–92](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L90)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Length(this.inches * scalar.inches)`.
- Key collaborators/calls: `Length()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `scalar` | `Length` | `Length` input consumed by the implementation shown below. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 90–92)"

    ```java
    public Length times(Length scalar) {
      return new Length(this.inches * scalar.inches);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a new `Length` whose inch value is the product of the two inch values.

### `public Length div(Length scalar)`

[Source lines 95–97](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L95)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Length(this.inches / scalar.inches)`.
- Key collaborators/calls: `Length()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `scalar` | `Length` | `Length` input consumed by the implementation shown below. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 95–97)"

    ```java
    public Length div(Length scalar) {
      return new Length(this.inches / scalar.inches);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a new `Length` whose inch value is `this.inches / scalar.inches`.

### `public Length squared()`

[Source lines 100–102](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L100)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Length(this.inches * this.inches)`.
- Key collaborators/calls: `Length()`.

**Inputs:** None.

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 100–102)"

    ```java
    public Length squared(){
      return new Length(this.inches * this.inches);
    }
    ```

??? note "Author note from JavaDoc"

    Returns a new `Length` whose inch value is `inches²`.

### `public double getInches()`

[Source lines 105–107](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L105)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `inches`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 105–107)"

    ```java
    public double getInches() {
      return inches;
    }
    ```

??? note "Author note from JavaDoc"

    Returns the length in inches.

### `public double getFeet()`

[Source lines 110–112](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L110)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `inches / 12.0`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 110–112)"

    ```java
    public double getFeet() {
      return inches / 12.0;
    }
    ```

??? note "Author note from JavaDoc"

    Returns the length in feet.

### `public double getCentimeters()`

[Source lines 115–117](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L115)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `inches * 2.54`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 115–117)"

    ```java
    public double getCentimeters() {
      return inches * 2.54;
    }
    ```

??? note "Author note from JavaDoc"

    Returns the length in centimeters.

### `public double getMeters()`

[Source lines 120–122](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L120)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `inches / 39.37`.

**Inputs:** None.

**Result:** Returns `double`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 120–122)"

    ```java
    public double getMeters() {
      return inches / 39.37;
    }
    ```

??? note "Author note from JavaDoc"

    Returns the length in meters.

### `public boolean equals(Object obj)`

[Source lines 125–127](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L125)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- It changes object/subclass state through `inches`.
- Return path: `this.inches == ((Length)obj).inches`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `obj` | `Object` | `Object` input consumed by the implementation shown below. |

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 125–127)"

    ```java
    public boolean equals(Object obj) {
        return this.inches == ((Length)obj).inches;
    }
    ```

### `public Class&lt;Length&gt; getTypeClass()`

[Source lines 134–136](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L134)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `Length.class`.

**Inputs:** None.

**Result:** Returns `Class&lt;Length&gt;`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 134–136)"

    ```java
    public Class<Length> getTypeClass() {
      return Length.class;
    }
    ```

### `public String getTypeName()`

[Source lines 139–141](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L139)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `"Length"`.

**Inputs:** None.

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 139–141)"

    ```java
    public String getTypeName() {
      return "Length";
    }
    ```

### `public int getSize()`

[Source lines 144–146](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L144)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `kSizeDouble * 4`.

**Inputs:** None.

**Result:** Returns `int`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 144–146)"

    ```java
    public int getSize() {
      return kSizeDouble * 4;
    }
    ```

### `public String getSchema()`

[Source lines 149–151](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L149)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `"double inches`.

**Inputs:** None.

**Result:** Returns `String`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 149–151)"

    ```java
    public String getSchema() {
      return "double inches;double feet;double centimeters;double meters";
    }
    ```

### `public Length unpack(ByteBuffer bb)`

[Source lines 154–157](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L154)

**Detailed behavior**

- The implementation executes 2 non-blank source lines.
- Return path: `new Length(inches)`.
- Key collaborators/calls: `bb.getDouble()`, `Length()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `bb` | `ByteBuffer` | `ByteBuffer` input consumed by the implementation shown below. |

**Result:** Returns `Length`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 154–157)"

    ```java
    public Length unpack(ByteBuffer bb) {
      double inches = bb.getDouble();
      return new Length(inches);
    }
    ```

### `public void pack(ByteBuffer bb, Length value)`

[Source lines 160–165](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L160)

**Detailed behavior**

- The implementation executes 4 non-blank source lines.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Key collaborators/calls: `bb.putDouble()`, `value.getInches()`, `value.getFeet()`, `value.getCentimeters()`, `value.getMeters()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `bb` | `ByteBuffer` | `ByteBuffer` input consumed by the implementation shown below. |
| `value` | `Length` | `Length` input consumed by the implementation shown below. |

**Result:** No return value; observable behavior comes from the state changes and calls listed above.

??? example "Implementation (source lines 160–165)"

    ```java
    public void pack(ByteBuffer bb, Length value) {
      bb.putDouble(value.getInches());
      bb.putDouble(value.getFeet());
      bb.putDouble(value.getCentimeters());
      bb.putDouble(value.getMeters());
    }
    ```

### `public boolean isImmutable()`

[Source lines 168–170](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L168)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `true`.

**Inputs:** None.

**Result:** Returns `boolean`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 168–170)"

    ```java
    public boolean isImmutable() {
      return true;
    }
    ```

## Exposed fields and types

### `public class Length implements StructSerializable`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L8)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    An immutable, unit-safe linear distance value. Stored internally in inches.

### `public static final Length kZero = new Length()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L11)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 1 time, so changing it can affect every control path that reads `kZero`.

??? note "Author note from JavaDoc"

    A zero-length constant.

### `public static final LengthStruct struct = new LengthStruct()`

*Exposed field · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/Length.java#L129)*

This is a **static final public** field with an initializer. It is not reassigned after initialization. The declaring source references it 3 times, so changing it can affect every control path that reads `struct`.
