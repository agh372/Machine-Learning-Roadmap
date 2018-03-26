https://www.wolftech.ncsu.edu/gradwatch/students/login.php?logout=1https://www.wolftech.ncsu.edu/gradwatch/students/login.php?logout=1https:/https://www.wolftech.ncsu.edu/gradwatch/students/login.php?logout=1/www.wolftech.ncsu.edu/gradwatch/students/login.php?logout=1

Two fundamental objects are Points and Vectors.

Points - 

Point is a location. It is represented as a "dot".In a coordinate system, we can represent points by coordinates in its system.

In 2d space, the standard coordinate system is Cartesian coordinate system.

A Cartesian coordinate system is a coordinate system that specifies each point uniquely in a plane by a pair of numerical coordinates


Vectors

It represents change in position.In Euclidean space, it can be viewed as arrow connecting two points.
Properties
 Magnitude which is the length of the arrow
 Direction which direction towads where tip is pointing

Represented by column surrounded by square brackets.

Two vectors are equivalent if they have the same magnitude and direction.

The Zero vector is the one that has all its coordinates equal to 0. The Zero vector has no direction and no normalization.

A unit vector is any vector in which it's magnitude is 1.

The magnitude of the vector can be calculated using pythagorous formula adapted to as many dimensions as the vector has. e.g. 3 dimensions = square-root(x**2 + y**2 + z**2)

The process of finding a unit vector from a given vector is called normalization. There are 2 steps involved when normilizing a vector:

    A. Find magnitude.
    B. Multiply vector by 1/magnitude of vector.



Scalar multiplication

Scalar multiplication is represented in the same manners as algebraic multiplication. A scalar beside a vector (either or both of which may be in parentheses) implies scalar multiplication. The common operator, a dot , which operate on two vectors. The product of a scalar c with a vector v can be represented in any of the following fashions:

    c v
    c ⋅ v 

It scales the size of vector.



vector addition can be calculated by placing the initial points of the vectors together, completing a parallelogram, and finding the diagonal of the parallelogram.

vector subtraction can be calculated by placing the arrow which connects two arrow heads.



Parallel and orthogonal vectors

2 vectors are parallel if one is a scalar multiple of another one. e.g: v and 2v and 1/2v and Zero vector

2 vectors are orthogonal if v1 * v2 is = 0. There are 2 possibilities. A vector that is 90 deg with another vector or the Zero vector.

Zero vector is both parallel and orthogonal to all other vectors. Zero vector is the only one that is orthogonal to itself.

Orthogonality is a tool for decomposing objects into combinations of simpler objects in a structured way.



Proyecting a vector into another vector

Proyecting a vector into another vector:

v1 = v1-parallel (to base vector) + v1-orthogonal (to base vector)

v1-parallel is a cathetus, v2-orthogonal is the other cathetus and v1 is the hipotenuse.

(*) cos angle = magnitude(v1-parallel) / magnitude(v1) =>

magnitude(v1-parallel) = cos angle * magnitude(v1).

Being v2 the base vector:

(v1 * v2) / (magnitude(v1) * magnitude(v2)) = cos(v1-v2).

Substituting cos from (*):

magnitude(v1-parallel) = magnitude(v1) * (v1 * v2) / (magnitude(v1) * magnitude(v2)) =>

(eliminating magnitude(v1) in right equation) =>

magnitude(v1-parallel) = (v1 * v2) / magnitude(v2)) =>

magnitude(v1-parallel) = v1 * normalize(v2)

v1 parallel has the same direction as v2.

magnitude(v1-parallel) * normalize(v2) = v1-parallel =>

(v1 * normalize(v2)) * normalize(v2) = v1-parallel
Cross product

Cross product: It's only possible in 3-dimension vectors and it gives another vector.

Cross product of v and w is a vector that is orthogonal to both and its magintute = magnitude(v) * magnitude(w) * sin(angle v-w).

Cross product of 2 parallel vectors is the 0 vector. If v or w are the 0 vector the cross product will be the 0 vector. Cross product is anticommutative, which means that the order matters, in this case changing the order results on vectors having opposite directions.

cross product(v, w) = - cross product(v, w)

The area of the parallelogram created with v and w is the magnitude of the cross product of v and w.

The area of the triangle created by those 2 vectors v and w is half of the area of the parallelogram

For more information in cross products go here
Intersections

Flat objects such as lines and planes are defined by linear equations:

    Can add and subtract vars and constants
    Can multiply a var by a constant

x + 2y = 1 // y/2 - 2z = x => Linear equations

x**2 - 1 = y // y/x = 3 => Non linear equations

Finding intersections is solving systems of equations. We are basicaly converting a real world problems (linear equations) into a geometrical problem (n dimensional objects).
Lines and systems with 2 dimensional objects

The most basic problem is finding intersection between lines.

A line is defined with its basepoint (x0) and the direction of the vector(v).

x(t) = x0 + times_scalar(v, t) => x(t) = x0 + t * v (parametrization of line)

Parametrization of a line (dimensional object) is the act of conveting a system of equations into a set of one dimension equations that all take the same parameters in this case "t" (parameter).

Note that x0 is a point, but it's treated as a vector in order to computer other points (x(t))

A given line has infinetely many base points (basically each of its points).

A given line has infinetely many directions (we can multiply the direction vector by any postive scalar and it will give the same direction)

x(t) = [1, -2] + t*[3, 1]

for t = 0 => x = [1, -2] => Base point

for t = 1 => x = [1, -2] + [3, 1] = [3, -1] => Another point on the line

A generic way of representing a line: Ax + By = k (A, B not both 0)

k => constant term

Base point => (0, k/B) and (k/A, 0)

if k = 0 =>

[A, B] (dot product) [x, y] = 0 => [x, y] is orthogonal to [A, B] =>

[B, -A] is orthogonal to [A, B] (that's how we figure out the direction vector)

Direction vector => [B, -A]

Ax + By = k => Gives us an implicit representation of the line such that for a set of points (x, y):

[A, B] (dot product) [x, y] = k

A line is defined by its normal vector [A, B] and its constant term k. An orthogonal or normal vector to the line is the one represented by [A, B].

2 lines are parallel if their normal vectors are parallel.

If 2 lines are not parallel they'll have an intersection in a single point.

If 2 lines are parallel there are 2 options:

    They never cross
    They are the same line, which means that they are conincidental and intersect in infinite points

So 2 lines could have:

    1 point of intersection
    0 points of intersection
    infinite points of intersection

To solve the system:

    First check if 2 lines are parallel by checking if their normal vecotrs are parallel.

    If normal vectors are parallel, then check if they are the same vector.

    Make a line connecting a point of line 1 and line 2 and if that third line is orthogonal to either normal vectors for line 1 and 2 => line 1 and 2 are coincident or the same.

    If we have 2 lines that are not parallel, to know how they intersect:

    Ax + By = k1

    Cx + Dy = k2

Either A or C need to not be 0, b/c if not the lines would both be horizontal and these lines intersect with each other.

if A = 0 => swap A by C, B by D and k1 by k2 => A will never be 0

(AD - BC) is never 0 b/c that would mean that both lines are parallel

y = (-Ck1 + Ak2) / (AD - BC)

x = (Dk1 - Bk2) / (AD - BC)

If there are no intersections in a system => the system is "Inconsistent"
Planes and systems with 3 dimensional objects

Three dimensional spaces are defined by linear equations of 3 variables Ax + By + Cz = k => [A B C] (dot product) [x y z] = k

[A B C] => Normal vector (similiar with lines)

Changing k shifts the plane but it doesn't change the direction of the plane

Same rules as with lines apply here.

    Planes that are not parallel intersect on a line not a point.

With 2 planes (a system of 2, 3-dimenstion equations) could have:

    No intersections (parallel planes)
    Intesect in a line
    Intersect in a whole plane

With 3 planes (a system of 3, 3-dimenstion equations), the planes could intersect:

    In a line
    No solution
    A plane
    A single point

The coefficients of a linear equation are the coordinates of a normal vector to the object the equation defines

In order to solve a system wtih 3 linear equations and 3 variables we need a set of "tools" to manipulate its data (they need to be reversible):

    Swap equations
    Multiply each of the sides of the planes that is not 0
    Add a multiple of one equation to another equation

Gaussanian elimination:

    Clear a variable in successive equations until there is only one equation with one variable.
    At that point 3 eq with 3 variables have been converted to a system of 3 equations, one with 3 variables, one with 2 variables and another one with one variable (triangular form)

The triangular form doesn't represent the same set of planes as the original system, but it represents the same result.

If when we are resolving the system and at any point we get the one of the sides of an equation is 0 and the side is not 0 => Inconsistent system, the system has no solution.

If the system gets to a point in which we have 0 = 0, that means that the last equation that we were soloving was redundant and gives no additional information.

The system in this case has been converted from a 3 plane system to a 2 plane system, and now we are not looking for a single point of intersection but for a line of intersection

When the solution is not a point we need to parametrize the solution set. We need to identify the pivot variables (lead variables), which are variables in the leading term, when the system is in a triangular form. The other variables are called the free variable.

This free variables will become a parameter in the parametrization. So in order to find the values of the pivotal variables for any given point in the line we'll use the free variable (parameter) to compute it.

Then we have to make the coefficient of pivot variable to be 1

Then we clear the pivot variable of the second equation in the first equation leaving the system:

x + Az = B

y + Cz = D

The leading variables have coefficient one and they only appear on one equation each. The system is simplified as much as possible giving us the "reduced row-echelon form" or rref.

With the rref we are able to get a basepoint and a direction vector that define the parametrization of the soluton for the system.

[x y z] = [(B - AZ) (D - Cz) z ]=> [B D 0] + z* [-A -C 1]

Base point [B D 0]

Direction vector [-A -C 1]

In order for a system to intersect in only one point it needs at least 3 equations, 3 planes.

A system is inconsistent if we find 0 = k during Gaussian elimination

A consistent solution has a unique solution and each variable is a pivotal or lead variable.

Number of free variables is equal to the dimension of the solution set.

Hyperplane in n dimensions is defined as a single linear equation with n variables.

A hyperplane in n dimensions is an (n-1) dimensional object. // I don't understand this concept yet.

Gaussian elimination and parametrization through the rref works the same way with planes as with hyperplanes.

A 2 dimenstional plane in 3 dimensions. Single linear equation with 3 dimensions

