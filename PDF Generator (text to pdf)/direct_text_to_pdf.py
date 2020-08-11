from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial',size=18)
pdf.cell(200,100,txt='Hello, Hi, This is vamsi here ', align='C')
pdf.output("txt_pdf.pdf")
