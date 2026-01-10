from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_mcqs_pdf(mcq_text, output_path="mcqs.pdf"):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    y = height - 40

    for line in mcq_text.split("\n"):
        if y < 40:
            c.showPage()
            y = height - 40
        c.drawString(40, y, line[:110])
        y -= 14

    c.save()
