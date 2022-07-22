import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st 

st.subheader('This is just a small test for learning how to use Stramlit :boom:')

st.title('Welcome To The First Penguin Dataset Exploration - as part of Spiced Academy')

st.write(":star: **Starting** the *build* of `penguins`:penguin: :mag: with first streamlit application :boom:")

st.write('Data taken from [here @ palmerpenguins](https://allisonhorst.github.io/palmerpenguins/)')

st.image('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png')

st.header('DataSet')

df_penguins = pd.read_csv('penguins_extra.csv') #just import the csv file from

st.write('Displaing the first 20 datapoints in the penguins dataset', df_penguins.head(20))
# can introduce more variations by adding a css command

species = st.selectbox('Select which species of Penguin you would like to check!', df_penguins.species.unique())
st.write(f'Display datapoint of {species} only', df_penguins[df_penguins['species']== species])

fig, ax = plt.subplots()
ax = sns.scatterplot(data=df_penguins, x = 'bill_length_mm', y= 'flipper_length_mm', hue ='species')
st.pyplot(fig)
# to display any matplot plot use st.

fig2 = px.scatter(data_frame = df_penguins, x = 'bill_length_mm', y= 'flipper_length_mm', color ='species', animation_frame='species', range_x = [0, 100], range_y = [170, 250])
#animation_group='species'
st.plotly_chart(fig2)

st.bar_chart(df_penguins.groupby('island')['species'].count())

st.map(df_penguins)
# inbuilt function in streamlit

st.write('For some really cool :cool: mapping references check out this links [degkgl](https://deckgl.readthedocs.io/en/latest/)')

#st.sidebar.selectbox('various types of input', ['yes', 'no'])

st.slider('test', min_value= 2, max_value=4)

slider_choice = st.sidebar.selectbox('various types of input', ['yes', 'no', 'other'])

if slider_choice == 'yes':
    st.write('yes selected - or output something here')
if slider_choice == 'no':
    st.write('answer no - try to add somethine else here')
if slider_choice == 'other':
    st.button('Try this now')

# for every sidebar i need to give a new variable name
img_variable = st.sidebar.file_uploader('Uploda some image', type=['.png', '.svg', '.jpg'])
from PIL import Image
if img_variable is not None:
    st.image(Image.open(img_variable))

csv_varibale = st.sidebar.file_uploader('upload a csv', type=['csv'])
if csv_varibale is not None:
    df = pd.read_csv(csv_varibale)
    st.write(df)

st.header('And here is the end of this Demo - Use to quickly prototype anyhting and lauch')

# to prevent the whole code from running again every time, on top of function that whould writn can add the decorator @st.chace command to save that and leave it untouche
