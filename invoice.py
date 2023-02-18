from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas 
invoice_number = input("Enter invoice number: ")
customer_name = input("Enter customer name: ")
num_items = int(input("Enter number of items: "))
items = []
for i in range(num_items):
    item_name = input(f"Enter name of item {i+1}: ")
    item_price = float(input(f"Enter price of item {i+1}: "))
    items.append((item_name, item_price))
pdf = canvas.Canvas("invoice.pdf", pagesize=letter)
pdf.setFont("Helvetica-Bold", 24)
pdf.drawString(1 * inch, 10 * inch, "Invoice")
pdf.setFont("Helvetica", 12)
pdf.drawString(1 * inch, 9.5 * inch, f"Invoice number: {invoice_number}")
pdf.drawString(1 * inch, 9.25 * inch, f"Customer name: {customer_name}")
pdf.setFont("Helvetica", 12)
pdf.drawString(1 * inch, 8 * inch, "Items")
pdf.drawString(4 * inch, 8 * inch, "Price")
row_height = 0.25 * inch
y = 7.75 * inch
for item, price in items:
    pdf.drawString(1 * inch, y, item)
    pdf.drawString(4 * inch, y, f"Rs.{price:.2f}")
    y -= row_height
total = sum([price for item, price in items])
pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(1 * inch, 7 * inch, f"Total amount due: Rs.{total:.2f}")
pdf.save()
