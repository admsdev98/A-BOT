import streamlit as st
import os

def load_css(css_file):
    """Load CSS file from the styles directory"""
    try:
        css_path = os.path.join(os.path.dirname(__file__), '..', 'styles', css_file)
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading CSS file: {e}")

def show_cookies_info():
    st.set_page_config(
        page_title="¿Que cookies usamos?",
        layout="wide"
    )

    load_css("cookies.css")

    st.markdown("""
    <script>
    // Prevenir múltiples clics en enlaces
    document.addEventListener('DOMContentLoaded', function() {
        const links = document.querySelectorAll('a[target="_blank"]');
        links.forEach(function(link) {
            link.addEventListener('click', function(e) {
                // Prevenir múltiples clics rápidos
                if (this.dataset.clicked === 'true') {
                    e.preventDefault();
                    return false;
                }
                
                this.dataset.clicked = 'true';
                
                // Reset después de 2 segundos
                setTimeout(() => {
                    this.dataset.clicked = 'false';
                }, 2000);
            });
        });
    });
    </script>
    
    <div class="cookies-container">
    <div class="content-wrapper fade-in">

    <h1>¿Que cookies usamos?</h1>

    <p>A-BOT utiliza cookies para proporcionar funcionalidad esencial de nuestros servicios, incluyendo autenticación y gestión de sesiones. Esta política describe qué cookies utilizamos y cómo puedes gestionarlas.</p>

    <h2>Tipos de Cookies</h2>

    <p>Utilizamos una cookie de sesión para que puedas usar nuestra aplicación de forma segura:</p>

    <div class="cookie-types">
    <div class="cookie-type-item">
    <h4>Cookie de Sesión</h4>
    <p>Te mantiene conectado mientras usas la aplicación y garantiza que tu sesión sea segura. Esta cookie es imprescindible para el funcionamiento de la aplicación.</p>
    </div>
    </div>

    <h2>Para qué las utilizamos</h2>

    <div class="usage-grid">
    <div class="usage-item">
    <h4>Autenticación</h4>
    <p>Mantener tu sesión autenticada a través de proveedores OAuth (Google, LinkedIn, GitHub)</p>
    </div>

    <div class="usage-item">
    <h4>Seguridad</h4>
    <p>Proteger contra ataques y validar la autenticidad de las peticiones</p>
    </div>

    <div class="usage-item">
    <h4>Funcionalidad</h4>
    <p>Gestionar el contador de mensajes de chat y preferencias de usuario</p>
    </div>
    </div>

    <h2>Cookies Utilizadas</h2>

    <div class="table-container">
    <table class="cookies-table">
    <thead>
    <tr>
    <th>Nombre de Cookie</th>
    <th>Propósito</th>
    <th>Duración</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>session_id</td>
    <td>Autenticación</td>
    <td>1 hora</td>
    </tr>
    </tbody>
    </table>
    </div>

    <h2>Configuración por navegador</h2>

    <div class="browser-links">
    <div class="browser-link">
    <h4>Chrome</h4>
    <p><a href="https://support.google.com/chrome/answer/95647" target="_blank" rel="noopener noreferrer">Configuración de cookies en Chrome</a></p>
    </div>

    <div class="browser-link">
    <h4>Firefox</h4>
    <p><a href="https://support.mozilla.org/es/kb/habilitar-y-deshabilitar-cookies-sitios-web-rastrear-preferencias" target="_blank" rel="noopener noreferrer">Configuración de cookies en Firefox</a></p>
    </div>

    <div class="browser-link">
    <h4>Safari</h4>
    <p><a href="https://support.apple.com/es-es/guide/safari/sfri11471/mac" target="_blank" rel="noopener noreferrer">Configuración de cookies en Safari</a></p>
    </div>

    <div class="browser-link">
    <h4>Edge</h4>
    <p><a href="https://support.microsoft.com/es-es/microsoft-edge/eliminar-cookies-en-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09" target="_blank" rel="noopener noreferrer">Configuración de cookies en Edge</a></p>
    </div>
    </div>

    </div>
    </div>
    """, unsafe_allow_html=True)

    st.stop()

def show_cookies_info_into_chat():
    load_css("cookies.css")
    
    return st.markdown(
    """
    <div class="cookie-link-bottom-right">
        <a href='?section=cookies'>¿Que cookies usamos?</a>
    </div>
    """,
    unsafe_allow_html=True,
)

