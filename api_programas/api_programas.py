import reflex as rx
import requests


# ---------------- ESTADO ---------------- #

class State(rx.State):

    pregunta: str = ""
    respuesta: str = ""
    cargando: bool = False

    def set_pregunta(self, value: str):
        self.pregunta = value

    def consultar_ia(self):
        if not self.pregunta.strip():
            self.respuesta = " Escribe una pregunta primero."
            return
        self.cargando = True
        self.respuesta = " Consultando a Gemini..."
        yield
        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"pregunta": self.pregunta},
                timeout=30,
            )
            response.raise_for_status()
            data = response.json()
            self.respuesta = data.get("respuesta", "Sin respuesta del servidor.")
        except requests.exceptions.ConnectionError:
            self.respuesta = " Error: No se pudo conectar al servidor. ¿Está corriendo en http://127.0.0.1:8000?"
        except requests.exceptions.Timeout:
            self.respuesta = " Error: El servidor tardó demasiado en responder."
        except requests.exceptions.HTTPError as e:
            self.respuesta = f" Error HTTP: {e}"
        except Exception as e:
            self.respuesta = f" Error inesperado: {e}"
        finally:
            self.cargando = False

    def limpiar(self):
        self.pregunta = ""
        self.respuesta = ""
        self.cargando = False


# ---------------- SVG OVNI ---------------- #

def ufo_svg(color_body: str, color_dome: str, color_lights: str) -> rx.Component:
    return rx.html(f"""
    <svg width="52" height="36" viewBox="0 0 52 36" fill="none" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="26" cy="18" rx="22" ry="8" fill="{color_body}" opacity="0.85"/>
      <ellipse cx="26" cy="15" rx="12" ry="8" fill="{color_dome}"/>
      <ellipse cx="26" cy="14" rx="7" ry="5" fill="white" opacity="0.3"/>
      <ellipse cx="16" cy="22" rx="3" ry="2" fill="{color_lights}"/>
      <ellipse cx="26" cy="24" rx="3" ry="2" fill="{color_lights}"/>
      <ellipse cx="36" cy="22" rx="3" ry="2" fill="{color_lights}"/>
      <line x1="20" y1="26" x2="18" y2="36" stroke="{color_lights}" stroke-width="1" opacity="0.5"/>
      <line x1="26" y1="26" x2="26" y2="36" stroke="{color_lights}" stroke-width="1" opacity="0.5"/>
      <line x1="32" y1="26" x2="34" y2="36" stroke="{color_lights}" stroke-width="1" opacity="0.5"/>
    </svg>
    """)


UFOS = [
    {"color_body": "#4F46E5", "color_dome": "#818CF8", "color_lights": "#06B6D4", "dir": "up"},
    {"color_body": "#7C3AED", "color_dome": "#A78BFA", "color_lights": "#F472B6", "dir": "down"},
    {"color_body": "#0891B2", "color_dome": "#22D3EE", "color_lights": "#FCD34D", "dir": "up"},
    {"color_body": "#4F46E5", "color_dome": "#818CF8", "color_lights": "#34D399", "dir": "down"},
    {"color_body": "#BE185D", "color_dome": "#F472B6", "color_lights": "#06B6D4", "dir": "up"},
    {"color_body": "#065F46", "color_dome": "#10B981", "color_lights": "#FCD34D", "dir": "down"},
]

UFO_DELAYS = ["0s", "0.4s", "0.8s", "0.2s", "0.6s", "1.0s"]


def ufo_row() -> rx.Component:
    items = []
    for i, ufo in enumerate(UFOS):
        anim = "floatUp" if ufo["dir"] == "up" else "floatDown"
        delay = UFO_DELAYS[i]
        items.append(
            rx.box(
                ufo_svg(ufo["color_body"], ufo["color_dome"], ufo["color_lights"]),
                style={
                    "animation": f"{anim} 2.5s ease-in-out infinite",
                    "animation_delay": delay,
                    "display": "flex",
                }
            )
        )
    return rx.hstack(
        *items,
        width="100%",
        justify="between",
        padding_x="20px",
    )


# ---------------- ASTRONAUTAS ORBITANDO ---------------- #

ASTRONAUT_SVG = """
<svg width="38" height="48" viewBox="0 0 38 48" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="19" cy="30" rx="11" ry="13" fill="#CBD5E1"/>
  <circle cx="19" cy="14" r="11" fill="#E2E8F0"/>
  <circle cx="19" cy="14" r="8" fill="#0F172A" opacity="0.85"/>
  <ellipse cx="16" cy="11" rx="3" ry="2" fill="#38BDF8" opacity="0.6"/>
  <line x1="19" y1="3" x2="19" y2="0" stroke="#94A3B8" stroke-width="2"/>
  <circle cx="19" cy="0" r="2" fill="#F472B6"/>
  <ellipse cx="7" cy="28" rx="4" ry="7" fill="#94A3B8" transform="rotate(-15 7 28)"/>
  <ellipse cx="31" cy="28" rx="4" ry="7" fill="#94A3B8" transform="rotate(15 31 28)"/>
  <circle cx="5" cy="33" r="3" fill="#CBD5E1"/>
  <circle cx="33" cy="33" r="3" fill="#CBD5E1"/>
  <ellipse cx="14" cy="42" rx="4" ry="5" fill="#94A3B8"/>
  <ellipse cx="24" cy="42" rx="4" ry="5" fill="#94A3B8"/>
  <ellipse cx="14" cy="46" rx="5" ry="2.5" fill="#64748B"/>
  <ellipse cx="24" cy="46" rx="5" ry="2.5" fill="#64748B"/>
  <circle cx="19" cy="28" r="3" fill="#4F46E5" opacity="0.8"/>
  <circle cx="19" cy="28" r="1.5" fill="#818CF8"/>
</svg>
"""


def astronaut_overlay() -> rx.Component:
    css = rx.html("""
    <style>
    @keyframes orbitTop {
      0%   { left: 0%;   top: 4px;  transform: rotate(0deg); }
      100% { left: 96%;  top: 4px;  transform: rotate(0deg); }
    }
    @keyframes orbitRight {
      0%   { left: calc(100% - 42px); top: 0%;   transform: rotate(90deg); }
      100% { left: calc(100% - 42px); top: 96%;  transform: rotate(90deg); }
    }
    @keyframes orbitBottom {
      0%   { left: 96%;  top: calc(100% - 52px); transform: rotate(180deg); }
      100% { left: 0%;   top: calc(100% - 52px); transform: rotate(180deg); }
    }
    @keyframes orbitLeft {
      0%   { left: 4px;  top: 96%;  transform: rotate(270deg); }
      100% { left: 4px;  top: 0%;   transform: rotate(270deg); }
    }
    .astronaut-orbit {
      position: absolute;
      width: 38px;
      height: 48px;
      animation-duration: 8s;
      animation-timing-function: linear;
      animation-iteration-count: infinite;
    }
    .a0 { animation-name: orbitTop;    animation-delay: 0s; }
    .a1 { animation-name: orbitRight;  animation-delay: 2s; }
    .a2 { animation-name: orbitBottom; animation-delay: 4s; }
    .a3 { animation-name: orbitLeft;   animation-delay: 6s; }
    </style>
    """)

    astronauts = rx.html(f"""
    <div class="astronaut-orbit a0">{ASTRONAUT_SVG}</div>
    <div class="astronaut-orbit a1">{ASTRONAUT_SVG}</div>
    <div class="astronaut-orbit a2">{ASTRONAUT_SVG}</div>
    <div class="astronaut-orbit a3">{ASTRONAUT_SVG}</div>
    """)

    return rx.fragment(css, astronauts)


# ---------------- DISEÑO ---------------- #

def index() -> rx.Component:

    animations_css = rx.html("""
    <style>
    @keyframes floatUp {
      0%, 100% { transform: translateY(0px); }
      50%       { transform: translateY(-28px); }
    }
    @keyframes floatDown {
      0%, 100% { transform: translateY(0px); }
      50%       { transform: translateY(28px); }
    }
    </style>
    """)

    return rx.box(

        astronaut_overlay(),

        rx.center(
            rx.vstack(

                animations_css,

                rx.heading(
                    "Arpía IA",
                    size="9",
                    color="white",
                ),

                rx.text(
                    "Consulta cualquier cosa usando Gemini IA",
                    color="#94A3B8",
                    size="4",
                ),

                ufo_row(),

                rx.text_area(
                    placeholder="Escribe tu pregunta...",
                    value=State.pregunta,
                    on_change=State.set_pregunta,
                    width="100%",
                    height="120px",
                    background_color="#1E1E1E",
                    color="white",
                    border="2px solid #4F46E5",
                    border_radius="15px",
                    disabled=State.cargando,
                ),

                rx.hstack(
                    rx.button(
                        rx.cond(
                            State.cargando,
                            "⏳ Consultando...",
                            "🚀 Consultar",
                        ),
                        on_click=State.consultar_ia,
                        background_color="#4F46E5",
                        color="white",
                        size="3",
                        border_radius="12px",
                        disabled=State.cargando,
                        cursor="pointer",
                    ),
                    rx.button(
                        "🧹 Limpiar",
                        on_click=State.limpiar,
                        background_color="#E11D48",
                        color="white",
                        size="3",
                        border_radius="12px",
                        disabled=State.cargando,
                        cursor="pointer",
                    ),
                    spacing="3",
                ),

                rx.box(
                    rx.cond(
                        State.respuesta != "",
                        rx.text(
                            State.respuesta,
                            color="white",
                            size="4",
                            white_space="pre-wrap",
                        ),
                        rx.text(
                            "La respuesta de Gemini aparecerá aquí...",
                            color="#475569",
                            size="4",
                            font_style="italic",
                        ),
                    ),
                    width="100%",
                    min_height="200px",
                    background_color="#111827",
                    border="2px solid #06B6D4",
                    border_radius="15px",
                    padding="20px",
                ),

                spacing="6",
                width="700px",
            ),

            width="100%",
            min_height="100vh",
        ),

        position="relative",
        width="100%",
        min_height="100vh",
        background_color="#0F172A",
        overflow="hidden",
    )


app = rx.App()
app.add_page(index)