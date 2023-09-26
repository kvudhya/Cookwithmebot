import streamlit as st 
import Chat_GPT as  cg
import model 

from PIL import Image

st.title(":blue[AI Cook app]")

st.header("Upload an image of your refrigedgator here")


uploaded_file = st.file_uploader("Choose your file")

if uploaded_file is not None:
    name_file = uploaded_file.name
    
    recipe=cg.recipe_bot(name_file)

    st.success(str(recipe))

else:
    st.write('Please upload an Image')


