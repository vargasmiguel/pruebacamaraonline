import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_qrcode_scanner import qrcode_scanner 
from time import sleep

st.set_page_config(layout="wide",
                   page_title="Bodega", 
                   page_icon="🏭")

add_logo("logo.png",height=100)


st.image("logo-mexicargo.png", width=200)
st.markdown("### Pendiente por proponer") 

def resetli():
    st.session_state["scanned"]=df_s["Paquetes"]    

if "scanned" not in st.session_state:
    st.session_state["scanned"]=[]

st.header('Paquetes escaneados', divider='rainbow')
df_s=st.data_editor({"Paquetes": st.session_state["scanned"]}, num_rows="dynamic", on_change=resetli, key="dtosa")

if st.button("Confirmar paquetes", type="primary"):
    st.success(f"Has confirmado los siguientes paquetes: {df_s['Paquetes']}")

qr_code = qrcode_scanner(key="cam") 

if qr_code not in st.session_state["scanned"] and qr_code!=None:
    st.session_state["scanned"].append(qr_code)

st.write(st.session_state["scanned"])

st.camera_input("Hola")



hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
