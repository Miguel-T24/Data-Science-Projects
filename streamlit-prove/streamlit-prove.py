#imports
import streamlit as st
import pandas as pd
import seaborn as sns

#1. Title and subheader
st.title("Data Analysis")
st.subheader("Data Analysis using python and Streamlit")

#2. Upload data set
upload = st.file_uploader("Upload your dataset (in CSV format)")
if upload is not None:
    data = pd.read_csv(upload)

#3. Show dataset
if st.checkbox("Preview Dataset"):
    if upload is not None:
        if st.button("Head"):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail())

#4. Check Datatyoe of Each Column
if upload is not None:
    if st.checkbox("Datatype of Each Column"):
        st.text('DataTypes')
        st.write(data.dtypes)

#5. Find shape of our dataset (number of rows and number of columns)
if upload is not None:
    data_shape = st.radio("What dimension do you want to check?", ('Rows' , "Columns"))

    if data_shape == 'Rows':
        st.text("Number of rows: ")
        st.write(data.shape[0])
    if data_shape == "Columns":
        st.text("Number of Columns: ")
        st.write(data.shape[1])

#6. Find null values in the dataset
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox("Null Values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations!!, no Missing Values")

#7. find duplicate Values in the dataset
if upload is not None:
    text = data.duplicated().any()  
    if test == True:
        st.warning("this Datasset Contains some duplicate values")
        dup = st.selectbox("Do you want o remove dulicate values?" , ("Select one", "Yes" , "No"))
        if dup == "Yes":
            data.drop_duplicates()
            st.text("Duplicate values are removed")
        elif dup =='No':
            st.text("Ok, No Problem")
    else:
        st.succes("Congratulations, this dataset not content duplicte values")

#8. Get overall Statistics
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe(include = "all"))


#9. about section
if st.button("About app"):
    st.text("Built with streamlit")
    st.text("Thanks to streamlit")

#10. by
if st.checkbox("By"):
    st.success("Miguel Tamayo")