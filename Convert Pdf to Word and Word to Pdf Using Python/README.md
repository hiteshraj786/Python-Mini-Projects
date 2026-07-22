# Convert PDF to Word and Word to PDF Using Python 📄🔄📝

This mini-project demonstrates a two-way document conversion: converting a PDF document into a Word Document (`.docx`) and vice-versa, utilizing the `pdf2docx` and `docx2pdf` Python libraries.

## 🚀 Features
- **PDF to DOCX:** Extracts text, images, and layout from a PDF and recreates it in Microsoft Word format.
- **DOCX to PDF:** Takes a Word document and converts it seamlessly back into a standard PDF format.

## 🛠️ Prerequisites
You'll need two separate libraries depending on which conversion you are running.

1. **Install Python Libraries:**
   ```bash
   pip install pdf2docx
   pip install docx2pdf
   ```

*Note: For `docx2pdf` to work properly on Windows, you must have Microsoft Word installed on your system, as it interacts with Word via COM.*

## 💻 How to Run
The `main.py` file contains two distinct sections (one is usually commented out).

### 1. PDF to DOCX
1. Uncomment the "PDF To DOCX" section in `main.py`.
2. Ensure you have the source file (e.g., `ML.pdf`) in the same directory.
3. Run the script:
   ```bash
   python main.py
   ```
4. A new Word document (`new.docx`) will be generated.

### 2. DOCX to PDF
1. Comment out the PDF to DOCX section and uncomment the "DOCX To PDF" section.
2. Ensure you have a source Word document (`new.docx`).
3. Run the script:
   ```bash
   python main.py
   ```
4. A converted PDF (`new.pdf`) will be created in the directory.

## 📂 Code Overview
- **PDF to DOCX:** Utilizes `pdf2docx.Converter` to read the PDF and parse it into DOCX.
- **DOCX to PDF:** Uses the `convert` function from the `docx2pdf` module.
