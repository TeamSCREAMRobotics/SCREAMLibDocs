# DataConversions

`com.teamscreamrobotics.data.DataConversions`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java) · **10 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public static double[] pose2dToArray(Pose2d pose)`

[Source lines 18–20](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L18)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new double[] {pose.getX(), pose.getY(), pose.getRotation().getDegrees()}`.
- Key collaborators/calls: `pose.getX()`, `pose.getY()`, `pose.getRotation()`, `getDegrees()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `pose` | `Pose2d` | `Pose2d` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 18–20)"

    ```java
    public static double[] pose2dToArray(Pose2d pose) {
      return new double[] {pose.getX(), pose.getY(), pose.getRotation().getDegrees()};
    }
    ```

### `public static double[] translation3dToArray(Translation3d translation)`

[Source lines 28–30](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L28)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new double[] {translation.getX(), translation.getY(), translation.getZ(), 0, 0, 0, 0}`.
- Key collaborators/calls: `translation.getX()`, `translation.getY()`, `translation.getZ()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation3d` | `Translation3d` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 28–30)"

    ```java
    public static double[] translation3dToArray(Translation3d translation) {
      return new double[] {translation.getX(), translation.getY(), translation.getZ(), 0, 0, 0, 0};
    }
    ```

### `public static double[] translation3dToArray(Translation3d translation, Rotation3d rot)`

[Source lines 39–50](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L39)

**Detailed behavior**

- The implementation executes 10 non-blank source lines.
- Return path: `new double[] { translation.getX(), translation.getY(), translation.getZ(), quat.getX(), quat.getY(), quat.getZ(), quat.getW() }`.
- Key collaborators/calls: `rot.getQuaternion()`, `translation.getX()`, `translation.getY()`, `translation.getZ()`, `quat.getX()`, `quat.getY()`, `quat.getZ()`, `quat.getW()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation3d` | `Translation3d` input consumed by the implementation shown below. |
| `rot` | `Rotation3d` | `Rotation3d` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 39–50)"

    ```java
    public static double[] translation3dToArray(Translation3d translation, Rotation3d rot) {
      Quaternion quat = rot.getQuaternion();
      return new double[] {
        translation.getX(),
        translation.getY(),
        translation.getZ(),
        quat.getX(),
        quat.getY(),
        quat.getZ(),
        quat.getW()
      };
    }
    ```

### `public static Translation3d pose3dArrayToTranslation3d(double[] array)`

[Source lines 57–59](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L57)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Translation3d(array[0], array[1], array[2])`.
- Key collaborators/calls: `Translation3d()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `array` | `double[]` | `double[]` input consumed by the implementation shown below. |

**Result:** Returns `Translation3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 57–59)"

    ```java
    public static Translation3d pose3dArrayToTranslation3d(double[] array) {
      return new Translation3d(array[0], array[1], array[2]);
    }
    ```

### `public static double[] translation3dArrayToNumArray(Translation3d[] translations)`

[Source lines 67–85](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L67)

**Detailed behavior**

- The implementation executes 12 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `combinedArr`.
- Key collaborators/calls: `translation.getX()`, `translation.getY()`, `translation.getZ()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translations` | `Translation3d[]` | `Translation3d[]` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 67–85)"

    ```java
    public static double[] translation3dArrayToNumArray(Translation3d[] translations) {
      double[] combinedArr = new double[translations.length * 7];
      int index = 0;
    
      for (Translation3d translation : translations) {
        combinedArr[index] = translation.getX();
        combinedArr[index + 1] = translation.getY();
        combinedArr[index + 2] = translation.getZ();
    
        index += 7;
        /* double[] arr = translation3dToArray(translation);
    
        System.arraycopy(arr, 0, combinedArr, index, arr.length);
    
        index += arr.length; */
      }
    
      return combinedArr;
    }
    ```

### `public static double[] translation2dArrayToNumArray(Translation2d[] translations)`

[Source lines 93–105](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L93)

**Detailed behavior**

- The implementation executes 8 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `combinedArr`.
- Key collaborators/calls: `translation.getX()`, `translation.getY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translations` | `Translation2d[]` | `Translation2d[]` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 93–105)"

    ```java
    public static double[] translation2dArrayToNumArray(Translation2d[] translations) {
      double[] combinedArr = new double[translations.length * 7];
      int index = 0;
    
      for (Translation2d translation : translations) {
        combinedArr[index] = translation.getX();
        combinedArr[index + 1] = translation.getY();
    
        index += 7;
      }
    
      return combinedArr;
    }
    ```

### `public static double[] translation2dArrayToNumArray(Translation2d[] translations, double z)`

[Source lines 114–127](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L114)

**Detailed behavior**

- The implementation executes 9 non-blank source lines.
- It iterates through 1 loop; work scales with the associated collection/range.
- Return path: `combinedArr`.
- Key collaborators/calls: `translation.getX()`, `translation.getY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translations` | `Translation2d[]` | `Translation2d[]` input consumed by the implementation shown below. |
| `z` | `double` | `double` input consumed by the implementation shown below. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 114–127)"

    ```java
    public static double[] translation2dArrayToNumArray(Translation2d[] translations, double z) {
      double[] combinedArr = new double[translations.length * 7];
      int index = 0;
    
      for (Translation2d translation : translations) {
        combinedArr[index] = translation.getX();
        combinedArr[index + 1] = translation.getY();
        combinedArr[index + 2] = z;
    
        index += 7;
      }
    
      return combinedArr;
    }
    ```

### `public static double[] chassisSpeedsToArray(ChassisSpeeds speeds)`

[Source lines 134–138](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L134)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- Return path: `new double[] { speeds.vxMetersPerSecond, speeds.vyMetersPerSecond, speeds.omegaRadiansPerSecond }`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `speeds` | `ChassisSpeeds` | Velocity/speed in the units required by this API and configuration. |

**Result:** Returns `double[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 134–138)"

    ```java
    public static double[] chassisSpeedsToArray(ChassisSpeeds speeds) {
      return new double[] {
        speeds.vxMetersPerSecond, speeds.vyMetersPerSecond, speeds.omegaRadiansPerSecond
      };
    }
    ```

### `public static Translation2d projectTo2d(Translation3d translation)`

[Source lines 145–147](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L145)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Translation2d(translation.getX(), translation.getZ())`.
- Key collaborators/calls: `Translation2d()`, `translation.getX()`, `translation.getZ()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation3d` | `Translation3d` input consumed by the implementation shown below. |

**Result:** Returns `Translation2d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 145–147)"

    ```java
    public static Translation2d projectTo2d(Translation3d translation) {
      return new Translation2d(translation.getX(), translation.getZ());
    }
    ```

### `public static Translation3d projectTo3d(Translation2d translation)`

[Source lines 154–156](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L154)

**Detailed behavior**

- The implementation executes 1 non-blank source line.
- Return path: `new Translation3d(translation.getX(), 0, translation.getY())`.
- Key collaborators/calls: `Translation3d()`, `translation.getX()`, `translation.getY()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `translation` | `Translation2d` | `Translation2d` input consumed by the implementation shown below. |

**Result:** Returns `Translation3d`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 154–156)"

    ```java
    public static Translation3d projectTo3d(Translation2d translation){
      return new Translation3d(translation.getX(), 0, translation.getY());
    }
    ```

## Exposed fields and types

### `public class DataConversions`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/data/DataConversions.java#L11)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.
