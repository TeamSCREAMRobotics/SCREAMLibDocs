# Getting started

SCREAMLib 26.3.7 targets **Java 17**, **WPILib 2026.2.1**, and the 2026 FRC toolchain.

## Install through WPILib

In VS Code, open the Command Palette and run **WPILib: Manage Vendor Libraries** → **Install new libraries (online)**. Paste:

```text
https://teamscreamrobotics.github.io/SCREAMLib/SCREAMLib.json
```

The vendordep resolves this Maven artifact:

```gradle
implementation "com.github.TeamSCREAMRobotics:SCREAMLib:26.3.7"
```

If SCREAMLib is already installed, use **WPILib: Manage Vendor Libraries** → **Check for updates**.

## Required dependencies

SCREAMLib directly uses these libraries. Keep compatible vendordeps in the robot project:

- CTRE Phoenix 6
- PathPlannerLib
- DogLog
- WPILib New Commands
- BLine-Lib (for the `BLine*` path helpers)

The exact versions used to publish 26.3.7 are visible in the [library build file](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/build.gradle).

## Confirm the install

```java
import com.teamscreamrobotics.data.Length;
import com.teamscreamrobotics.util.ScreamUtil;

Length bumperDepth = Length.fromInches(3.25);
boolean onTarget = ScreamUtil.epsilonEquals(errorMeters, 0.0, 0.01);
```

Run the normal robot build:

```powershell
./gradlew build
```

## 2025 import warning

The 2025 competition repository embedded an earlier SCREAMLib layout and imports packages such as `data.Length`, `drivers.TalonFXSubsystem`, and `util.AllianceFlipUtil`. With 26.3.7, add the `com.teamscreamrobotics` prefix:

```java
import com.teamscreamrobotics.data.Length;
import com.teamscreamrobotics.drivers.TalonFXSubsystem;
import com.teamscreamrobotics.util.AllianceFlipUtil;
```

