import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from main import college_based, general_results, university_name, avg_gre
import time
import matplotlib.pyplot as plt
# import plotly.express as px
import plotly.graph_objects as px
data = [20, 16, 8, 9.8] 

# Plot

fig = plt.pie(data) 

# Display

plt.show() 
# st.pyplot(fig)

st.title('College admission prediction')

name = st.text_input('Enter your name')

university = st.selectbox('Pick one', university_name)

left, right = st.columns(2)
with left:
    gre_quants = st.number_input('Enter your GRE quants(out of 170)',min_value=0,max_value=170)

with right:
    gre_verbal = st.number_input('Enter your GRE verbal(out of 170)',min_value=0,max_value=170)

left, right = st.columns(2)
with left: 
    ug_cgpa = st.number_input('Enter your UG CGPA(from 0.0 to 4.0)',min_value=0.0,max_value=4.0)

with right:
    toefl = st.number_input('Enter your TOEFL(out of 120)',min_value=0,max_value=120)

left, right = st.columns(2)
with left: 
    no_of_papers = st.number_input('Enter number of papers published(min 0 to max 10)',min_value=0,max_value=10)

with right:
    work_experience = st.number_input('Enter your work experience(min 0 to max 10)',min_value=0,max_value=10)

arr = []
if st.button('Analyse'):
    if not name:
    
        with st.warning('Please fill out so required fields'):
            time.sleep(5)
        pass
    else:
        with st.spinner('Analysing your results...'):
            time.sleep(1)

        st.title('Hello, '+name)

        gre = gre_quants+gre_verbal

        st.text("Your scores:")

        values = [gre, 340-gre]

        fig = px.Figure(
        px.Pie(
        values = values,
        hole=.3,
        labels = ["Your score","Score missed"],
        ))

        fig.update_layout(height=200, margin=dict(l=0, r=0, t=0, b=0))

        st.text("GRE score:")
        st.plotly_chart(fig)

        values = [toefl, 120-toefl]

        fig = px.Figure(
        px.Pie(
        values = values,
        hole=.3,
        labels = ["Your score","Score missed"],
        ))

        fig.update_layout(height=200, margin=dict(l=0, r=0, t=0, b=0))

        st.text("TOEFL score:")
        st.plotly_chart(fig)

        st.text('You chose: '+university)
        
        df = [1,2,3,4,5,6]

        data = {'Your score':gre,'Average score':340-gre}
        courses = list(data.keys())
        values = list(data.values())
        
        fig = plt.figure(figsize = (12,5))
        
        # creating the bar plot
        plt.bar(courses, values, color ='blue',
                width = 0.4)
        
        plt.title("Compare your GRE scores")
        # plt.show()

        # st.write(fig)
        st.pyplot(fig)

        data = {'Your score':gre,'Average score':int(avg_gre[university])}
        courses = list(data.keys())
        values = list(data.values())
        st.write(data)
        
        fig = plt.figure(figsize = (12,5))
        
        # creating the bar plot
        plt.bar(courses, values, color ='blue',
                width = 0.4)
        
        plt.title("Compare your TOEFL scores")
        # plt.show()

        # st.write(fig)
        st.pyplot(fig)

        # fig = px.Figure([px.Bar(x=['1g','1gd','1hg'],
        #                 y=[80,70,60])])
 
        # st.pyplot(fig)

        if college_based(gre, gre_quants, gre_verbal, ug_cgpa, toefl, no_of_papers, work_experience, university):
            st.success("Yayy! We think with your scores you will definitely get the college as preferred.")
        else:
            st.error("Uh, oh. We think you will not be able to make it to this univ based on our prev records!")
        st.text('We also predict you are eligible for the following universities:') 
        for i in (general_results(gre, gre_quants, gre_verbal, ug_cgpa, toefl, no_of_papers, work_experience)):
            # st.success(i)
            arr.append(i)
        
        data = {
            'University list': arr
        }
        
        hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

        # Inject CSS with Markdown
        st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

        df = pd.DataFrame(data)
        st.table(df)
else:
    st.write('')