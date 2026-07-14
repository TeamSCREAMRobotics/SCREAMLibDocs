# Architecture

SCREAMLib is organized by responsibility. Most robot code starts with `drivers`, `pid`, `data`, and `util`; the remaining packages are focused helpers.

| Package | Use it for | Main extension points |
| --- | --- | --- |
| `config` | Applying and retrying device configuration | `DeviceConfig`, `ErrorChecker` |
| `dashboard` | NetworkTables values and Mechanism2d views | `DashboardBoolean`, `Mechanism`, `Ligament` |
| `data` | Unit-safe lengths and data flattening | `Length`, `DataConversions`, `LimitedSizeList` |
| `drivers` | Phoenix 6 motors, pigeon, swerve, orchestra | `TalonFXSubsystem`, `PigeonHelper` |
| `math` | Kinematics and interpolation helpers | `ScreamMath`, `Conversions`, `IKSolver` |
| `physics` | Projectile trajectory calculation | `Trajectory` |
| `pid` | Reusable WPILib/Phoenix PID values | `ScreamPIDConstants` |
| `sim` | Background simulation wrappers | `SimulationThread`, `SimWrapper`, `SimInterface` |
| `util` | Alliance flipping, geometry, paths, logging | `AllianceFlipUtil`, `GeomUtil`, `Logger` |
| `vision` | Limelight configuration and estimates | `LimelightVision`, `LimelightHelpers` |
| `zones` | Field containment tests | rectangular, circular, polygonal, and hexagonal areas |

## Core motor pattern

`TalonFXSubsystem` is the largest extension surface. A robot normally:

1. Creates a `TalonFXSubsystemConfiguration` in a constants class.
2. Supplies CAN devices, inversion, ratios, limits, PID slots, and simulation values.
3. Extends `TalonFXSubsystem` for the mechanism.
4. Implements goals with `TalonFXSubsystemGoal` and its `target()`, `controlType()`, and optional `feedForward()` methods.
5. Applies a goal through `applyGoal`, `applyGoalCommand`, or a mechanism-specific wrapper.

Read [TalonFXSubsystem](reference/drivers/TalonFXSubsystem.md) before changing periodic control or simulation behavior; its protected members are intentionally listed because subclasses use them.

## Units

`Length` stores meters and supplies factories and accessors for meters, inches, feet, centimeters, millimeters, and mechanism rotations. Prefer it at configuration boundaries, then convert only when a vendor API requires a scalar.

## Generated reference policy

The reference catalog is generated from Java declarations and implementations. It includes:

- every public and protected method or constructor;
- implicitly public interface methods and compiler-generated record constructors/accessors;
- public and protected fields, records, enums, interfaces, and nested classes;
- detailed behavior derived from each method body, including branches, state writes, return paths, external calls, and explicit failures;
- the complete implementation body in a collapsible source block;
- input/result descriptions derived from signatures and implementations rather than trusting potentially stale JavaDoc;
- exact GitHub source lines;
- embedded code examples from files in the 2025 and 2026 robots that use that class.

Private helpers are implementation details and are not API promises.
