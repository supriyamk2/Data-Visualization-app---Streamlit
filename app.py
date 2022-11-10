
import streamlit as st

import pandas as pd
import numpy as np
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import altair as alt





def main():
    st.title("Data Visualization")
    df = pd.read_csv("data/StudentsPerformance.csv")
    df2 = pd.read_csv("data/lang_data.csv")
    df3 = pd.read_csv("data/prog_languages_data.csv")

    st.dataframe(df.head())

    #df['species'].value_counts().plot(kind="bar")
    #st.pyplot()

    #Bar chart
    #using St.bar_chart

    #st.bar_chart(df[['sepal_length','petal_length']])

    #lang_list = df2.columns.tolist()

    #lang_choices = st.multiselect("Choose Language", lang_list, default="Python")
    #new_df = df2[lang_choices]
    #st.line_chart(new_df)

    #Area chart

    # st.area_chart(new_df)


    fig = px.pie(df,'gender', title="Pie chart of gender")
    st.plotly_chart(fig)

    count = Counter(df['race/ethnicity'])
    data = pd.DataFrame({'Ethnicity group':count.keys(), 'Number of students':count.values()})
    fig = px.bar(data, 'Ethnicity group', 'Number of students', title="Race/Ethnicity")
    st.plotly_chart(fig)


    fig = px.scatter(df, 'math score', 'reading score',color="gender", title="Math and Reading score")
    st.plotly_chart(fig)



    clist = ["reading score", "math score","writing score"]

    parents = st.multiselect("Select education", clist, default="math score")
    data = df[parents]
    st.line_chart(data)


    



    





    
    

    




    #fig = plt.figure()
    #df['species'].value_counts().plot(kind="bar")
    #st.pyplot(fig)

    #method 2
    #fig,ax = plt.subplots()
    #df['species'].value_counts().plot(kind="bar")
    #st.pyplot(fig)
    
    




if __name__ == '__main__':
    main()