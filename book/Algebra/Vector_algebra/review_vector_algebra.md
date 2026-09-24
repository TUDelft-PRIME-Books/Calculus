{.unnumbered}
# Review: Vector algebra

In {numref}`Sec:Vectors` we introduced vectors as mathematical objects that make it possible to describe both magnitude and direction in a single entity. Beginning with arrows in the plane, we developed the geometric intuition behind vector addition and scalar multiplication before formalising vectors as elements of $\mathbb{R}^n$. We then define the basic operations on vectors and presents the fundamental algebraic properties that govern them. Through an application to chemical reactions, it demonstrates that vectors in higher dimensions arise naturally in real-world situations. Finally, we established the correspondence between points and vectors by introducing coordinates relative to a fixed origin, thereby providing a framework for describing geometric objects and their relationships using vector notation.

:::{fetch} {numref}`Fig:Vectors:3DAddition`
:::

In {numref}`Sec:DotProduct` we introduced the dot product as a tool for expressing geometric properties of vectors algebraically. Beginning with the concepts of length and perpendicularity in the plane and in three-dimensional space, we developed the dot product and used it to characterise orthogonality. We then generalised these ideas to vectors in $\mathbb{R}^n$, establishing the fundamental properties of the dot product and showing how it gives rise to the notions of norm and distance. The chapter also introduced orthogonal projection and unit vectors, which provide useful ways to describe the direction and components of vectors. Finally, we derived several fundamental results, including Pythagoras' theorem in $\mathbb{R}^n$, the Cauchy-Schwarz inequality, the triangle inequality, and the formula relating the dot product to the angle between two vectors, thereby extending familiar geometric concepts to arbitrary dimensions.

:::{fetch} {numref}`Fig:InnerProduct:TriangleInequality`
:::

In {numref}`Sec:CrossProduct` we introduced the cross product as an operation on vectors in $\mathbb{R}^3$ that produces a vector orthogonal to two given vectors. After defining the cross product algebraically, we established its fundamental geometric properties, showing that its direction is determined by the right-hand rule and that its length is given by the product of the lengths of the original vectors and the sine of the angle between them. We then used these results to characterise parallel vectors and to relate the norm of the cross product to the area of a parallelogram spanned by two vectors, which in turn provides a method for computing the area of a triangle in three-dimensional space. Finally, we derived the main algebraic properties of the cross product, highlighted its non-commutativity, and showed how its components can be expressed conveniently using determinants.

:::{fetch} {numref}`Fig:CrossProduct:RightHandRule`
:::

In {numref}`Sec:LinesAndPlanes` we studied how lines and planes can be described using equations and vectors. Beginning with Cartesian equations of lines in $\mathbb{R}^2$, we examined the possible ways in which lines can intersect and introduced directional vectors to obtain parametric vector equations. We then developed the concept of normal vectors and used them to derive normal equations and Cartesian equations of lines. Next, we extended these ideas to planes in $\mathbb{R}^3$, showing how Cartesian, normal, and parametric vector equations each provide a different description of the same geometric object. Using directional vectors and the cross product, we learned how to construct equations of planes from geometric information. Finally, we investigated the possible intersections of lines and planes in two and three dimensions, thereby establishing a vector-based framework for describing and analysing geometric objects in Euclidean space.

:::{fetch} {numref}`Fig:LinesAndPlanes:PlanesPointIntersection`
:::

In {numref}`Sec:DetGeometric` we introduced determinants through their geometric interpretation as signed areas and volumes. Beginning with two vectors in $\mathbb{R}^2$, we showed that the determinant of a $2\times2$-matrix measures the signed area of the parallelogram spanned by these vectors and encodes their orientation. We then established the fundamental algebraic properties of determinants and interpreted these properties geometrically. Next, we extended these ideas to three dimensions, where determinants of $3\times3$-matrices describe the signed volume of a parallelepiped spanned by three vectors. By relating determinants to the cross product and scalar triple product, we derived a formula for computing $3\times3$-determinants and investigated their key properties. Finally, we showed how determinants are connected to orientation, linear independence, and invertibility, thereby providing both a geometric and an algebraic perspective on this important concept.

:::{fetch} {numref}`Fig:DetGeometric:Paraped`
:::