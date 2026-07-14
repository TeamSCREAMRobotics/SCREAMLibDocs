# IKSolver

`com.teamscreamrobotics.math.IKSolver`

[View source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/IKSolver.java) · **2 callables** · **1 exposed fields/types** · **0 embedded competition examples**

[Jump to examples](#competition-examples){ .md-button .md-button--primary }

## Competition examples

No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.

## Public and protected callables

### `public IKSolver(Length joint1Length, Length joint2Length)`

[Source lines 21–25](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/IKSolver.java#L21)

**Detailed behavior**

- The implementation executes 3 non-blank source lines.
- It changes object/subclass state through `jointLengths`, `maxDistance`, `minDistance`.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- Key collaborators/calls: `Math.abs()`, `joint1Length.minus()`, `getMeters()`, `joint1Length.plus()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `joint1Length` | `Length` | length of the first link (shoulder to elbow) **Parameter `joint2Length`:** length of the second link (elbow to end-effector) |
| `joint2Length` | `Length` | length of the second link (elbow to end-effector) |

**Result:** Constructs and initializes a `IKSolver` instance.

??? example "Implementation (source lines 21–25)"

    ```java
    public IKSolver(Length joint1Length, Length joint2Length) {
        this.jointLengths = new Length[] { joint1Length, joint2Length };
        this.minDistance = Math.abs(joint1Length.minus(joint2Length).getMeters());
        this.maxDistance = joint1Length.plus(joint2Length).getMeters();
    }
    ```

??? note "Author note from JavaDoc"

    Creates an IK solver for a two-link arm.
    
    **Parameter `joint1Length`:** length of the first link (shoulder to elbow)
    **Parameter `joint2Length`:** length of the second link (elbow to end-effector)

### `public Rotation2d[] solve(Translation2d target, boolean elbowDown)`

[Source lines 35–63](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/IKSolver.java#L35)

**Detailed behavior**

- The implementation executes 22 non-blank source lines.
- It bounds at least one intermediate or output value before use.
- It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.
- It has 1 conditional path: `distance != target.getNorm(`.
- Return path: `new Rotation2d[] { Rotation2d.fromRadians(theta1), Rotation2d.fromRadians(theta2) }`.
- Key collaborators/calls: `target.getX()`, `target.getY()`, `Math.sqrt()`, `getMeters()`, `MathUtil.clamp()`, `target.getNorm()`, `Math.acos()`, `Math.cos()`, `Math.sin()`, `Math.atan2()`.

**Inputs**

| Parameter | Type | Meaning |
| --- | --- | --- |
| `target` | `Translation2d` | the desired end-effector position (meters) relative to the shoulder **Parameter `elbowDown`:** `true` for the elbow-down configuration, `false` for elbow-up **Returns:** `[theta1, theta2]` — shoulder and elbow joint ang… |
| `elbowDown` | `boolean` | `true` for the elbow-down configuration, `false` for elbow-up **Returns:** `[theta1, theta2]` — shoulder and elbow joint angles |

**Result:** Returns `Rotation2d[]`. Exact return expressions are listed in the behavior section.

??? example "Implementation (source lines 35–63)"

    ```java
    public Rotation2d[] solve(Translation2d target, boolean elbowDown) {
        double x = target.getX();
        double y = target.getY();
        double distanceSquared = x * x + y * y;
        double distance = Math.sqrt(distanceSquared);
    
        double length1 = jointLengths[0].getMeters();
        double length2 = jointLengths[1].getMeters();
    
        distance = MathUtil.clamp(distance, minDistance, maxDistance);
        if (distance != target.getNorm()) {
            double scale = distance / target.getNorm();
            x *= scale;
            y *= scale;
        }
    
        double cosTheta2 = (distanceSquared - length1 * length1 - length2 * length2) / (2 * length1 * length2);
        cosTheta2 = MathUtil.clamp(cosTheta2, -1.0, 1.0);
        double theta2 = elbowDown ? -Math.acos(cosTheta2) : Math.acos(cosTheta2);
    
        double k1 = length1 + length2 * Math.cos(theta2);
        double k2 = length2 * Math.sin(theta2);
        double theta1 = Math.atan2(y, x) - Math.atan2(k2, k1);
    
        return new Rotation2d[] {
            Rotation2d.fromRadians(theta1),
            Rotation2d.fromRadians(theta2)
        };
    }
    ```

??? note "Author note from JavaDoc"

    Solves for the joint angles needed to reach `target`.
    If the target is outside the arm's reachable range it is clamped to the nearest reachable point.
    
    **Parameter `target`:** the desired end-effector position (meters) relative to the shoulder
    **Parameter `elbowDown`:** `true` for the elbow-down configuration, `false` for elbow-up
    **Returns:** `[theta1, theta2]` — shoulder and elbow joint angles

## Exposed fields and types

### `public class IKSolver`

*Nested/API type · [source](https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/e3d20643f43b7f35da63011d6083caccac8b062c/src/main/java/com/teamscreamrobotics/math/IKSolver.java#L9)*

This exposed `class` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.

??? note "Author note from JavaDoc"

    Two-joint 2D inverse kinematics solver using the law of cosines.
