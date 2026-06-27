import reflex as rx
import requests


class State(rx.State):
    pregunta: str = ""
    respuesta: str = ""
    cargando: bool = False

    def set_pregunta(self, valor: str):
        self.pregunta = valor

    def limpiar(self):
        self.pregunta = ""
        self.respuesta = ""

    async def enviar_pregunta(self):
        if not self.pregunta.strip():
            self.respuesta = "Escribe una pregunta primero."
            return

        self.cargando = True
        self.respuesta = "Consultando la base de datos..."
        yield

        try:
            response = requests.post(
                "http://fastapi_veterinaria:8000/preguntar",
                json={"pregunta": self.pregunta},
                timeout=60,
            )
            if response.status_code == 200:
                data = response.json()
                self.respuesta = data.get("respuesta", "No se recibió respuesta.")
            else:
                self.respuesta = f"Error del servidor: {response.status_code}"
        except Exception as e:
            self.respuesta = f"Error de conexión: {str(e)}"

        self.cargando = False


def neon_icons() -> rx.Component:
    return rx.html(
        """
        <div class="neon-icons">
            <div class="paw paw-big"><span></span><span></span><span></span><span></span><i></i></div>
            <div class="heart heart-1"></div>
            <div class="paw paw-small"><span></span><span></span><span></span><span></span><i></i></div>
            <div class="heart heart-2"></div>
        </div>
        """
    )


def index() -> rx.Component:
    return rx.fragment(
        rx.html(
            """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap');

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; min-height: 100vh; font-family: 'Montserrat', sans-serif; }

.main-bg {
    min-height: 100vh;
    width: 100%;
    position: relative;
    overflow: hidden;
    color: white;
    background:
        radial-gradient(circle at 18% 57%, rgba(0, 92, 255, .72) 0%, rgba(0, 63, 190, .45) 15%, rgba(0,0,0,0) 34%),
        radial-gradient(circle at 75% 88%, rgba(0, 72, 255, .56) 0%, rgba(0, 46, 150, .35) 20%, rgba(0,0,0,0) 42%),
        radial-gradient(circle at 58% 35%, rgba(0, 18, 75, .85) 0%, rgba(0,0,0,0) 36%),
        linear-gradient(135deg, #00020b 0%, #020414 42%, #001646 100%);
}

.main-bg::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(135deg, rgba(0,0,0,.92) 0%, rgba(0,0,0,.25) 24%, rgba(0,0,0,0) 42%),
        linear-gradient(25deg, rgba(0,0,0,.95) 0%, rgba(0,0,0,0) 38%);
    pointer-events: none;
}

.main-bg::after {
    content: "";
    position: absolute;
    width: 1100px;
    height: 420px;
    left: 12%;
    bottom: 0;
    background: radial-gradient(ellipse at center, rgba(0, 78, 255, .50), rgba(0,0,0,0) 68%);
    transform: rotate(-8deg);
    filter: blur(10px);
    pointer-events: none;
}

.navbar {
    position: relative;
    z-index: 5;
    height: 92px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 9vw;
}

.brand, .nav-links, .nav-actions { display: flex; align-items: center; }
.brand { gap: 12px; font-weight: 700; letter-spacing: 1px; font-size: 18px; }
.brand-circle { width: 24px; height: 24px; border: 3px solid white; border-radius: 50%; }
.nav-links { gap: 72px; font-size: 14px; font-weight: 700; }
.nav-actions { gap: 42px; font-weight: 700; }
.search-icon { font-size: 28px; line-height: 1; }
.sign-btn { border: 1px solid white; border-radius: 18px; padding: 8px 30px; font-size: 14px; }

.animals-img {
    position: absolute;
    z-index: 3;
    left: 0;
    bottom: 0;
    width: min(31vw, 430px);
    max-height: 90vh;
    object-fit: contain;
    object-position: left bottom;
    filter: drop-shadow(0 0 28px rgba(0, 102, 255, .42));
}

.center-content {
    position: relative;
    z-index: 4;
    width: min(560px, 92vw);
    margin: 5vh auto 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 18px;
}

.title-box { text-align: center; margin-bottom: 4px; }
.title-box h1 {
    margin: 0;
    font-size: clamp(34px, 4vw, 58px);
    line-height: 1;
    font-weight: 800;
    letter-spacing: 1px;
    text-shadow: 0 0 26px rgba(0, 132, 255, .6);
}
.title-box h1 span { color: #35a9ff; }
.title-box p { margin: 10px 0 0; color: rgba(224, 243, 255, .72); font-weight: 600; letter-spacing: 5px; font-size: 12px; }

.search-card, .response-card {
    width: 100%;
    border: 1px solid rgba(88, 178, 255, .45);
    background: rgba(2, 10, 28, .58);
    backdrop-filter: blur(16px);
    border-radius: 24px;
    box-shadow: 0 0 38px rgba(0, 104, 255, .24), inset 0 0 28px rgba(0, 90, 255, .08);
}
.search-card { padding: 24px; }
.response-card { padding: 20px 24px; min-height: 150px; }

textarea {
    width: 100%;
    min-height: 112px;
    resize: vertical;
    border: 1px solid rgba(82, 170, 255, .38);
    border-radius: 17px;
    outline: none;
    color: #eaf7ff;
    background: rgba(0, 7, 22, .68);
    padding: 16px 18px;
    font-size: 15px;
    line-height: 1.6;
    font-family: 'Montserrat', sans-serif;
}
textarea:focus { border-color: #4db8ff; box-shadow: 0 0 22px rgba(45, 158, 255, .32); }
textarea::placeholder { color: rgba(197, 229, 255, .42); }

.btn-row { display: flex; gap: 14px; margin-top: 16px; }
button { font-family: 'Montserrat', sans-serif; font-weight: 800; cursor: pointer; transition: .2s ease; }
.btn-search {
    flex: 1;
    border: 0;
    color: white;
    padding: 14px 18px;
    border-radius: 16px;
    background: linear-gradient(135deg, #0099ff, #004fd7);
    box-shadow: 0 0 26px rgba(0, 130, 255, .42);
    letter-spacing: 1px;
}
.btn-search:hover { transform: translateY(-2px); box-shadow: 0 0 34px rgba(0, 154, 255, .64); }
.btn-clear {
    width: 126px;
    color: #cfeeff;
    border: 1px solid rgba(100, 190, 255, .56);
    background: rgba(255,255,255,.04);
    padding: 14px 18px;
    border-radius: 16px;
}
.btn-clear:hover { background: rgba(0, 130, 255, .12); transform: translateY(-2px); }

.response-label { color: #72c8ff; font-size: 12px; font-weight: 800; letter-spacing: 4px; margin-bottom: 10px; }
.response-text { white-space: pre-wrap; word-break: break-word; line-height: 1.75; color: #e9f7ff; font-size: 15px; }

.neon-icons { position: absolute; z-index: 2; right: 5vw; top: 105px; width: 300px; height: 330px; }
.paw, .heart { position: absolute; filter: drop-shadow(0 0 16px rgba(50, 165, 255, .95)); opacity: .94; animation: float 3.4s ease-in-out infinite; }
.paw span, .paw i { position: absolute; display: block; background: #45b7ff; box-shadow: 0 0 18px #45b7ff; }
.paw i { width: 62px; height: 46px; border-radius: 48% 48% 42% 42%; left: 34px; top: 58px; }
.paw span { width: 26px; height: 36px; border-radius: 50%; }
.paw span:nth-child(1) { left: 0; top: 32px; transform: rotate(-18deg); }
.paw span:nth-child(2) { left: 36px; top: 5px; }
.paw span:nth-child(3) { left: 76px; top: 8px; transform: rotate(15deg); }
.paw span:nth-child(4) { left: 112px; top: 38px; transform: rotate(22deg); }
.paw-big { right: 0; top: 0; transform: scale(.92); }
.paw-small { right: 72px; top: 155px; transform: scale(.63); opacity: .78; }
.heart { width: 72px; height: 72px; border: 3px solid #3aaeff; border-top: 0; border-left: 0; transform: rotate(45deg); }
.heart::before, .heart::after { content: ""; position: absolute; border: 3px solid #3aaeff; border-radius: 50%; }
.heart::before { width: 72px; height: 72px; left: -38px; top: 0; border-right: 0; }
.heart::after { width: 72px; height: 72px; left: 0; top: -38px; border-bottom: 0; }
.heart-1 { right: 20px; top: 145px; animation-delay: .8s; }
.heart-2 { right: 135px; top: 62px; transform: rotate(45deg) scale(.42); opacity: .45; animation-delay: 1.3s; }

@keyframes float { 0%,100% { margin-top: 0; } 50% { margin-top: -14px; } }

@media (max-width: 900px) {
    .navbar { padding: 0 24px; }
    .nav-links { display: none; }
    .animals-img { opacity: .32; width: 360px; }
    .neon-icons { opacity: .35; right: -50px; }
    .center-content { margin-top: 4vh; }
}
</style>
"""
        ),
        rx.el.main(
            rx.el.header(
                rx.el.div(rx.el.div(class_name="brand-circle"), rx.el.span("COMPANY"), class_name="brand"),
                rx.el.nav(
                    rx.el.span("-"),
                    rx.el.span("-"),
                    rx.el.span("-"),
                    class_name="nav-links",
                ),
                rx.el.div(rx.el.span("⌕", class_name="search-icon"), rx.el.div("B-vet", class_name="sign-btn"), class_name="nav-actions"),
                class_name="navbar",
            ),
            rx.image(src="/sin2.png", class_name="animals-img"),
            neon_icons(),
            rx.el.section(
                rx.el.div(
                    rx.el.h1(rx.el.span("Bi"), "Vet"),
                    rx.el.p("SISTEMA VETERINARIO IA"),
                    class_name="title-box",
                ),
                rx.el.div(
                    rx.el.textarea(
                        placeholder="Escribe tu pregunta sobre propietarios, mascotas o consultas veterinarias...",
                        value=State.pregunta,
                        on_change=State.set_pregunta,
                    ),
                    rx.el.div(
                        rx.el.button("BUSCAR", on_click=State.enviar_pregunta, disabled=State.cargando, class_name="btn-search"),
                        rx.el.button("LIMPIAR", on_click=State.limpiar, class_name="btn-clear"),
                        class_name="btn-row",
                    ),
                    class_name="search-card",
                ),
                rx.el.div(
                    rx.el.div("RESPUESTA", class_name="response-label"),
                    rx.el.div(
                        rx.cond(State.cargando, "Consultando la base de datos...", State.respuesta),
                        class_name="response-text",
                    ),
                    class_name="response-card",
                ),
                class_name="center-content",
            ),
            class_name="main-bg",
        ),
    )


app = rx.App()
app.add_page(index, route="/")
