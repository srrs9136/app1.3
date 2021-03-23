from fpdf import FPDF
import webbrowser

class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill
    """
    def __init__ (self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays the share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay
      


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
        pdf.image("C:\\Users\\sdevk\\OneDrive\\Desktop\\Ardit\\app1.2\\house.png", w=30, h=30)

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
        
        # self.filename becasue filename is local variable inside the __init_method and not generate method. 
        pdf.output('C:\\Users\\sdevk\\OneDrive\\Desktop\\Ardit\\app1.2\\Report1.pdf', 'F')  

        # To open the generated pdf automatically on a webbrowser. But doesnt seems to work (3/23/21)
        webbrowser.open(self.filename)   

the_bill = Bill(amount=120, period="April 2021")
john = Flatmate(name="John", days_in_house=20)
mary = Flatmate(name="Mary", days_in_house=25)

print("John pays: ", john.pays(bill=the_bill, flatmate2=mary))
print("Mary pays: ", mary.pays(bill=the_bill, flatmate2=john))

# Calling the generate method
pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)