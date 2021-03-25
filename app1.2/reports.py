import webbrowser
from fpdf import FPDF
import os

class PdfReport:
    """
    Creates a PDF file that contains data about the flatmates such as their names, their due amounts and the periods
    of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        # Instanciating the FPDF class using the pdf= . The pdf is the object instance.
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add house icon
        pdf.image("C:\\Users\\sdevk\\OneDrive\\Desktop\\Ardit\\app1.2\\files\\house.png", w=30, h=30)

        #Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)    
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=str(flatmate1.name), border=0)    
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of second flatmate
        pdf.cell(w=100, h=25, txt=str(flatmate2.name), border=0)    
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)
        
        # This code below was the original method but ended up using the OS library and the chdir method. 
        # # self.filename becasue filename is local variable inside the __init_method and not generate method. 
        # pdf.output(f"C:\\Users\\sdevk\\OneDrive\\Desktop\\Ardit\\app1.2\\files\\{self.filename}")  

        # # To open the generated pdf automatically on a webbrowser. But doesnt seems to work (3/23/21)
        # webbrowser.open(self.filename) 

        # The code below is an alternate way to do things with the "OS" library with chdir.
        os.chdir("C:\\Users\\sdevk\\OneDrive\\Desktop\\Ardit\\app1.2\\files")

        # self.filename becasue filename is local variable inside the __init_method and not generate method. 
        pdf.output(self.filename)  

        # To open the generated pdf automatically on a webbrowser. But doesnt seems to work (3/23/21)
        webbrowser.open(self.filename) 