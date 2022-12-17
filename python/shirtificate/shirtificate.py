from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.output("shirtificate.pdf")


class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 10, 65, 190, 190)
        self.set_font("helvetica", "B", 45)
        self.cell(45, 45, "CS50 Shirtificate", align='C')

    def footer(self):
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255,255,255)
        self.cell(72, 140, name + " took CS50", align='C')


if __name__ == "__main__":
    main()