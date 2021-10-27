import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
from scipy.integrate import odeint
import time
import html
import csv

st.title('UI for differential equation solving')
st.write('Equation: ' + r'$\frac{d^2 y}{dt^2} = - \omega^2 y(t) - \beta y^3(t)$')
st.write('Conditions: ' + r'$y(0)=q$, $\frac{dy(0)}{dt} = r$')

#Add left slidebar boxes
st.sidebar.subheader('Equation parameters')
omega_input = st.sidebar.text_input(html.unescape('&omega;'), 1)
beta_input = st.sidebar.text_input(html.unescape('&beta;'), 1)
q_input = st.sidebar.text_input('q', 1)
r_input = st.sidebar.text_input('r', 1)
N_input = st.sidebar.slider('Integrating steps', 10, 1000, 100, 10)
animation_speed = st.sidebar.slider('Animation speed', 1, 100, 5, 1)
st.sidebar.write('***')

#Add saving
st.sidebar.subheader('Saving solution')
save_filename = st.sidebar.text_input('Filename:', 'solution_0000')
save_button = st.sidebar.button('Save')

def saving_file():
    if save_button:
        df_solution.to_csv(save_filename + '.csv')

#Solve equation
#N = 100
N = int(N_input)
tmin, tmax = 0, 10
tlist = np.linspace(tmin, tmax, N)
om = float(omega_input)
beta = float(beta_input)
q = float(q_input)
r = float(r_input)
var0 = [q, r]
y_list_odeint, y_dir_list_odeint = [], []

def equation(var, t):
    y, phi = var
    dvardt = [phi, - om ** 2 * y - beta * y ** 3]
    return dvardt

sol = odeint(equation, var0, tlist)
y_list_odeint = sol[:, 0]
y_dir_list_odeint = sol[:, 1]

df_solution = pd.DataFrame({'tlist' : tlist, 'y' : y_list_odeint, 'ydir' : y_dir_list_odeint})
saving_file()

#Plot graphics
#st.write(df_solution)
st.subheader('y(t) function')

solution_plot_y = alt.Chart(df_solution).mark_line(interpolate= 'basis').encode(
    alt.X('tlist', title = r't, s'),
    alt.Y('y', title = r'y'),
).properties(title = 'y(t) function')
st.altair_chart(solution_plot_y)

st.subheader('y`(t) function')

solution_plot_ydir = alt.Chart(df_solution).mark_line(interpolate= 'basis').encode(
    alt.X('tlist', title = r't, s'),
    alt.Y('ydir', title = r'y`'),
).properties(title = 'y`(t) function')
st.altair_chart(solution_plot_ydir)

st.subheader('Phase plotting')

st.write('This is animation')
st.button("Re-run")

phase_plot = alt.Chart(df_solution.loc[:1]).mark_line(interpolate= 'basis').encode(
    alt.X('y', title = r'y'),
    alt.Y('ydir', title = r'y`'),
    order = 'tlist'
).properties(title = 'Phase portret y(y`)')
alt_phase_plot = st.altair_chart(phase_plot)

for i in range(2, df_solution.shape[0]):
    phase_plot = alt.Chart(df_solution.loc[:i]).mark_line(interpolate='basis').encode(
        alt.X('y', title=r'y'),
        alt.Y('ydir', title=r'y`'),
        order = 'tlist'
    ).properties(title='Phase portret y`(y)')
    alt_phase_plot.altair_chart(phase_plot)
    time.sleep(float(animation_speed) / 1000)







