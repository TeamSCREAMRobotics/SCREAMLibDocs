# IKSolver

`com.teamscreamrobotics.math.IKSolver`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/IKSolver.java) · **2 callables** · **1 exposed fields/types**

## Public and protected callables

### `public IKSolver(Length joint1Length, Length joint2Length)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/IKSolver.java#L21)*

Creates an IK solver for a two-link arm.

**Parameter `joint1Length`:** length of the first link (shoulder to elbow)
**Parameter `joint2Length`:** length of the second link (elbow to end-effector)

### `public Rotation2d[] solve(Translation2d target, boolean elbowDown)`

*Callable · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/IKSolver.java#L35)*

Solves for the joint angles needed to reach `target`.
If the target is outside the arm's reachable range it is clamped to the nearest reachable point.

**Parameter `target`:** the desired end-effector position (meters) relative to the shoulder
**Parameter `elbowDown`:** `true` for the elbow-down configuration, `false` for elbow-up
**Returns:** `[theta1, theta2]` — shoulder and elbow joint angles

## Exposed fields and types

### `public class IKSolver`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/IKSolver.java#L9)*

Two-joint 2D inverse kinematics solver using the law of cosines.
