# Task: L-System Fractal Architect

A Python-based L-System generator and visualizer using **Tkinter** and **Turtle Graphics**.

This project allows users to create fractal patterns using Lindenmayer Systems. It includes branching, colour gradients, and optimisation for rendering large strings.


# Example inputs

| Pattern             | Axiom     | Rules                        | Angle | Iterations |
| ------------------- | --------- | ---------------------------- | ----- | ---------- |
| Koch Snowflake      | `F--F--F` | `F:F+F--F+F`                 | `60`  | `3`        |
| Fractal Tree        | `F`       | `F:F[+F]F[-F]F`              | `25`  | `4`        |
| Dragon Curve        | `FX`      | `X:X+YF+, Y:-FX-Y`           | `90`  | `10`       |
| Sierpinski Triangle | `F-G-G`   | `F:F-G+F+G-F, G:GG`          | `120` | `5`        |
| Plant Fractal       | `X`       | `X:F-[[X]+X]+F[+FX]-X, F:FF` | `25`  | `6`        |

