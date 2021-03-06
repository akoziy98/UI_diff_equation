# UI_diff_equation
This is repository with two versions of UI for differential equation solving, provided by streamlit and Voila packages.

Here was solved the equation of oscillator:

Equation: 

![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2%20y%7D%7Bdt%5E2%7D%20%3D%20-%20%5Comega%5E2%20y%28t%29%20-%20%5Cbeta%20y%5E3%28t%29)

Conditions:

![equation](https://latex.codecogs.com/gif.latex?y%280%29%3Dq%24%2C%20%24%5Cfrac%7Bdy%280%29%7D%7Bdt%7D%20%3D%20r)

## Voila

to run UI with Voila you need to open your console and run the next command:

```
voila .\UI_diff_eq_voila.ipynb
```

## Streamlit

to run UI with streamlit you need to open your console and run the next command:

```
streamlit run .\UI_diff_eq_streamlit.py
```

## Functionality

Two proposed UI have similar functions to work with differential equation.

We have four parameters of equation to variate: omega, beta, q, r. Also, we have parameter of solve representation: Integrating steps. Due to equation solving with scipy odeint function, parameter of integrating steps didn't influence on solution convergence. Animation speed changes the speed of animation of phase portrait. We add possibility to save the solution. It saves file pandas dataframe with 3 colemns: time, y, y` in csv format.

## Work example


it can be run with bad parameters of integrating steps. And it leads to beautiful animations. You can see the example below.

![](https://github.com/akoziy98/UI_diff_equation/blob/main/example_animation_bad_parameters.gif)
