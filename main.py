import streamlit as st
from gui.interfaz import login_usuario, mostrar_interfaz

def main():
    st.set_page_config(
        page_title="Simulador de Entrevistas con IA",
        layout="centered"
    )

    if "autenticado" in st.session_state and st.session_state["autenticado"]:
        mostrar_interfaz()
    else:
        login_usuario()

if __name__ == "__main__":
    main()
