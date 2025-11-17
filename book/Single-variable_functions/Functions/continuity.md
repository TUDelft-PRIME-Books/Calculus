(Section:Continuity)=

# Continuity

Almost all functions we have encountered so far have the nice property that it is possible to sketch their graph without lifting your pen, except possibly for skipping over a vertical asymptote. Indeed, all of polynomials, powers of $x$, rational functions, (inverse) trigonometric functions, exponential functions and logarithms have this property. A function with this property is called **continuous**. Stated differently, a function is continuous whenever small changes in the input give rise to small changes in the function values. 

In science and engineering, most variables depend on each other in a continuous way. However, that does not need to be the case. Consider, for instance, a simple electrical circuit, where a DC voltage source is connected to a resistor. Initially, the voltage source is turned off, but at $t=0$, we turn on the voltage source. Instantly, the currenct through the resistor will jump from $0$ to a non-zero value, so a small change in time will give rise to a large change in current. As such, the current is not continuous at the moment in time the voltage source is turned on (it is continuous at other points in time).


Hier plaatje van het circuit beschreven in de tekst hierboven. Voor mijn vak bij EE heeft een TA ooit mooie plaatjes gemaakt, maar ik weet niet hoe. Ik heb wel voorbeelden van hoe dat er typisch uitziet. Ook een grafiek van de stroom, wat dus een Heaviside functie is. Omdat we geen getallen gegeven hebben wil je misschien geen maatvoering op de assen?

(Subsec:ContProp)=

## Definition and properties

In this section we cover

- Definition (limit definition), standard continuous functions and basic rules of calculation (including left- and right-continuity)
- "Taking a limit inside a continuous function"
- Intermediate value theorem