from fpdf import FPDF
import tkinter as tk
from tkinter import filedialog


pdf = FPDF()

root = tk.Tk()

def convertToPdf() -> None:

  filename = filedialog.askopenfilename()

  with open(filename, 'r', encoding='utf-8') as f:
      text = f.read()

  pdf.add_page()
  pdf.add_font('DejaVu','','DejaVuSans.ttf', uni=True)
  pdf.set_font('DejaVu','', size=12)

  pdf.write(5,text)

  despath = filedialog.asksaveasfile()
  print(despath)

  pdf.output(str(despath.name + '.pdf'))


  if __name__ == '__main__':
     convertToPdf()