# Simplex-method

Simplex method (based on Dantzig's selection method) written in Python 3

---

## Preliminary 

This program requires modules below:

- numpy


> TASK: **to solve linear programming optimization problem using Simplex method**


## Python file

| File name             | Class                     | Explanation               |
| --                    | --                        | --                        |
| `simplex.py`          | Configuration, Simplex    | to run Simplex method     |

## Output folders and files

None

---

## Example

Objective function and constraint functions should be prepared in canonical form

- All variables should be ***non-negative***
- Make the problem ***Maximize one***
- All formulas should be ***equality***, not inequality, and the right side should be non-negative


A problem below

```math
{\rm Maximize} \; 4x_1 + 5x_2 + 4 \\
5x_1 - 2x_2 \leq 11 \\
4x_1 + 2x_2 \leq 28 \\
-3x_1 + 3x_2 \leq 6 \\
x_1, x_2 \geq 0
```

can be explained in canonical form using slack variables ($x_3, x_4, x_5$) like this:


```math
5x_1 - 2x_2 + x_3 = 11 \\
4x_1 + 2x_2 + x_4 = 28 \\
-3x_1 + 3x_2 + x_5 = 6 \\
-4x_1 - 5x_2 + z = 4 \\
x_1, x_2, x_3, x_4, x_5 \geq 0.
```

Then, you can define the problem in Configuration class:

```python

    self.constraint = [
        # [coefficient_1, coefficient_2, ... , constant_value]
        [ 5,    -2,     11],
        [ 4,     2,     28],
        [-3,     3,      6]
    ]
    self.object = [-4, -5, 4]   # [coefficient_1, coefficient_2, ... , constant_value]

```

After running the program, you can get the log of process and the final result on console. 

```python

                [ Simplex Method ]

Initial Dictionary:
[[ 5 -2  1  0  0  0 11]
 [ 4  2  0  1  0  0 28]
 [-3  3  0  0  1  0  6]
 [-4 -5  0  0  0  1  4]]

<Operation 1>
 Dictionary:
[[ 3  0  1  0  0  0 15]
 [ 6  0  0  1  0  0 24]
 [-1  1  0  0  0  0  2]
 [-9  0  0  0  1  1 14]]

<Operation 2>
 Dictionary:
[[ 0  0  1  0  0  0  3]
 [ 1  0  0  0  0  0  4]
 [ 0  1  0  0  0  0  6]
 [ 0  0  0  1  1  1 50]]

 <Final result>
 Objective value = 50

```

---

## Notification

This program assumes a problem where all variables have 0 in the feasible area, otherwise it needs to be reworked into a program such as the two-step method or the fine method.