from fpdf import FPDF

def create_pdf(child_name: str, story_text: str) -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.multi_cell(0, 10, txt=f"قصة {child_name}\n\n{story_text}", align='R')
    filename = f"{child_name}_story.pdf"
    pdf.output(filename)
    return f"/static/{filename}"  # Adjust path as needed
