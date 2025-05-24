from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(40, 40, 40)
        self.cell(0, 10, "LexIA: Calidad, Innovación y Tecnología", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(30, 30, 120)
        self.cell(0, 10, title, ln=True, align="L")
        self.ln(3)

    def chapter_body(self, body):
        self.set_font("Helvetica", "", 11)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

pdf.chapter_title("Calidad que genera confianza")
pdf.chapter_body(
    "- Desarrollo bajo estándares profesionales, con control de versiones, validaciones exhaustivas y pruebas unitarias.\n"
    "- Consulta de datos directamente desde fuentes oficiales, asegurando exactitud, integridad y trazabilidad.\n"
    "- Experiencia de usuario (UX) pensada para ser clara, ágil y eficiente, entregando resultados útiles en segundos."
)

pdf.chapter_title("Innovación impulsada por IA")
pdf.chapter_body(
    "- Más que una simple plataforma de consulta: LexIA integra inteligencia artificial avanzada (GPT-4o) para análisis automatizado.\n"
    "- Identificación inteligente de casos urgentes a través de comprensión semántica.\n"
    "- Diseño modular preparado para:\n"
    "  - Alertas inteligentes ante nuevos eventos relevantes.\n"
    "  - Análisis profundo de documentos extensos o múltiples fuentes legales.\n"
    "  - Evolución continua sin romper la estabilidad del sistema."
)

pdf.chapter_title("Tecnología de vanguardia")
pdf.chapter_body(
    "- Backend robusto con FastAPI (Python), contenedorizado con Docker y desplegado en AWS: seguro, escalable y mantenible.\n"
    "- Frontend moderno desarrollado con React y Next.js, desplegado en Vercel para velocidad global y experiencia fluida.\n"
    "- Infraestructura con integración y despliegue continuo (CI/CD) gracias a Docker.\n"
    "- Integración directa con OpenAI GPT-4o, capaz de comprender y explicar contenido legal complejo con precisión."
)

pdf.chapter_title("LexIA no es el futuro: es el presente de la inteligencia legal")

pdf.output("LexIA_Calidad_Innovacion_Tecnologia.pdf")

