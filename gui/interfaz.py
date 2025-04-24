import streamlit as st
from database.conexion import iniciar_firebase
from firebase_admin import auth

# Inicializar Firebase
iniciar_firebase()

# --- FUNCIÓN DE LOGIN ---
def login_usuario():
    st.markdown("## 🔐 Iniciar Sesión")
    correo = st.text_input("Correo electrónico")
    contrasena = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if correo == "" or contrasena == "":
            st.warning("Completa todos los campos.")
        else:
            try:
                user = auth.get_user_by_email(correo)
                st.success(f"Bienvenido, {user.display_name or user.email}")
                st.session_state["autenticado"] = True
                st.session_state["usuario"] = user.email
                st.rerun()
            except:
                st.error("Credenciales incorrectas o usuario no registrado.")

# --- FUNCIÓN DE INTERFAZ PRINCIPAL ---
def mostrar_interfaz():
    st.markdown("## 👤 Panel Principal")
    st.write("Bienvenido al simulador de entrevistas con IA.")

    if st.button("Cerrar sesión"):
        st.session_state.clear()
        st.rerun()
