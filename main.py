import streamlit as st
import requests
from PIL import Image




left_co,centr ,cent_co,g,last_co = st.columns(5)
with centr:
    st.image("logo.png",width=360)
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Stability AI API key", type="password")


st.markdown("<h1 style='text-align: center; '>Sketch to image converter</h1>", unsafe_allow_html=True)



uploaded_file = st.file_uploader("Upload a sketch", type=["png", "jpg", "jpeg"])


if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Sketch", use_column_width=True)


st.write("## Select a Theme")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.markdown("<h3 style='text-align: center; '>Neon</h3>", unsafe_allow_html=True)
    png1 = Image.open("png1.png")
    st.image(png1, width=330)
    
with col2:
    st.markdown("<h3 style='text-align: center; '>Monument Valley</h3>", unsafe_allow_html=True) 
    png2 = Image.open("png2.png")
    st.image(png2, width=330)

with col3:
    st.markdown("<h3 style='text-align: center; '>Ori and the blind forest</h3>", unsafe_allow_html=True)
    png3 = Image.open("png3.png")
    st.image(png3, width=330)

with col4:
    st.markdown("<h3 style='text-align: center; '>illustration</h3>", unsafe_allow_html=True)  
    png4 = Image.open("png4.png")  
    st.image(png4, width=330)


theme = st.selectbox("Choose a theme", ["Neon", "Monument Valley Game", "Ori and the blind", "illustration"])
word=st.text_input("describe what are you trying to draw in 2 words or more ")

if theme == "Neon":

   
    PROMPT=word + "  in a neon 3D style. The asset should feature vibrant, glowing colors with a futuristic, cyberpunk aesthetic. Incorporate sleek, geometric shapes and dynamic lighting effects to give a sense of depth and energy, fitting seamlessly into a neon 3D game environment"
elif theme == "Monument Valley Game":
    PROMPT=word + "  that captures the whimsical and serene essence of Monument Valley, focusing on a green tone with pastel accents of pinks, purples, and blues. The asset should feature clean lines and simple, geometric shapes. Integrate subtle architectural elements such as arches or domes to give it an ancient yet timeless look. Add small natural accents like tiny waterfalls or vines to enhance the tranquility. Design the asset to appear interactable by small, stylized characters, adding narrative depth and scale. Use soft, ambient lighting to create a dreamy and ethereal atmosphere with smooth gradients"
elif theme == "Ori and the blind" :
    PROMPT=word+"  in The style of **Ori and the Blind Forest** is characterized by lush environments with dense, vibrant forests, ethereal lighting effects creating a magical atmosphere, fluid forms mimicking nature, a rich color palette featuring deep blues and vibrant hues, whimsical details adding life, contrasting shadows for depth, seamless integration of natural elements, and dynamic backgrounds for immersion."
elif theme == "illustration":
    PROMPT=word+"  digital illustration, featuring an object. in the center of the composition, surrounded by abstract shapes in pink,light blue, and pastel colors, a dreamy atmosphere, white background"




if st.button("Convert Sketch"):
    if not api_key:
        st.error("API key is required!")
    elif not uploaded_file:
        st.error("Please upload a sketch!")
    else:
        with st.spinner('Converting...'):
           

            url = "https://api.stability.ai/v2beta/stable-image/control/sketch"
            files = {"image": uploaded_file.getvalue()}
            data = {
                "prompt": PROMPT,
                "control_strength": 0.9,
                "output_format": "png"
            }
            headers = {
                "authorization": f"Bearer {api_key}",
                "accept": "image/*"
            }
            response = requests.post(url, headers=headers, files=files, data=data)
            
            if response.status_code == 200:
               

                st.image(response.content, caption="Generated Image", use_column_width=True)
            else:
                st.error("Failed to convert the sketch. Please check your API key and try again.")

