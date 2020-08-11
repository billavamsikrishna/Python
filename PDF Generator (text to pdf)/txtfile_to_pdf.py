from fpdf import FPDF
f = open('text.txt','r') #exp.txt is a text file here.
content = ''
for i in f:
    content =i
#print(d)
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial',size=18)
pdf.cell(100,10,txt=content,align='C')
pdf.output("txtfile_to_pdf.pdf")
