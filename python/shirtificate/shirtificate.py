from fpdf import FPDF

def main():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(60, 10, 'CS50 Shirtificate', align='C')

if __name__ == "__main__":
    main()