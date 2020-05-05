from reportlab.pdfgen import canvas
from django.http import HttpResponse


def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="BigData.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Oblique", 55)
    p.drawString(100, 700, "Hi, Sunny.")
    p.showPage()
    p.save()
    return response
