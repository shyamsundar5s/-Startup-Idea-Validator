from fpdf import FPDF

class ReportPDF(FPDF):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.add_page()
        self.set_font("Arial", size=12)
        self._add_title()
        self._add_content()

    def _add_title(self):
        self.set_font("Arial", style="B", size=16)
        self.cell(0, 10, "Startup Idea Validation Report", ln=True, align="C")
        self.ln(10)

    def _add_content(self):
        self.set_font("Arial", size=12)
        self.cell(0, 10, f"Idea: {self.data['idea']}", ln=True)
        self.cell(0, 10, f"Industry: {self.data.get('industry', 'General')}", ln=True)
        self.ln(5)

        self.cell(0, 10, "Competitors:", ln=True)
        for competitor in self.data['competitors']:
            self.cell(0, 10, f"- {competitor}", ln=True)

        self.ln(5)
        self.cell(0, 10, "Suggested Improvements:", ln=True)
        self.multi_cell(0, 10, self.data['improvements'])

        self.ln(5)
        self.cell(0, 10, "Market Demand Analysis:", ln=True)
        self.multi_cell(0, 10, self.data['market_demand'])

def generate_pdf_report(data, output_file):
    pdf = ReportPDF(data)
    pdf.output(output_file)
