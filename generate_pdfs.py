from fpdf import FPDF
import random
import os

# 1. Create a folder to hold the 100 PDFs
folder_name = "dummy_pdfs"
os.makedirs(folder_name, exist_ok=True)

# 2. Some realistic college sentences for the AI to read
subjects = ["Computer Science", "Psychology", "History", "Mathematics", "Biology"]
sentences = [
    "The grading policy requires a minimum of 75% attendance to pass.",
    "The final exam is worth 40% of your total grade.",
    "Late assignments will receive a 10% penalty per day.",
    "Office hours are held every Tuesday and Thursday at 3 PM.",
    "Plagiarism will result in an automatic zero for the project.",
    "Please read chapters 4 through 7 before the midterm."
]

print("Generating 100 PDFs... Please wait.")

# 3. Loop 100 times to create 100 PDFs
for i in range(1, 101):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Pick a random subject for the title
    subject = random.choice(subjects)
    pdf.cell(200, 10, txt=f"Course Syllabus: {subject} 10{i}", ln=True, align='C')
    pdf.cell(200, 10, txt="", ln=True) # Blank line
    
    # Add 4 random rules to the PDF
    for _ in range(4):
        random_rule = random.choice(sentences)
        pdf.cell(200, 10, txt=random_rule, ln=True)
        
    # Save the file
    file_path = f"{folder_name}/syllabus_{i}.pdf"
    pdf.output(file_path)

print(f"✅ Success! 100 PDFs have been saved in the '{folder_name}' folder.")