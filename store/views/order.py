from django.shortcuts import render, redirect
from django.views import View
from store.models import Customer
from store.models import Order
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
from datetime import timedelta  # Added this line

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from store.models import Customer, Order
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from datetime import timedelta
from django.contrib import messages

class OrderView(View):
    def get(self, request, order_id=None):
        if order_id:
            return self.get_bill_pdf(request, order_id)
        else:
            customer_id = request.session.get('customer')
            orders = Order.objects.filter(customer=customer_id).order_by("-date", "-id")
            return render(request, 'order.html', {"orders": orders})

    def get_bill_pdf(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Order_{order_id}_Bill.pdf"'

        doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
        elements = []

        # Invoice header
        elements.append(Spacer(1, 20))
        elements.append(Table(
            [[
                "RIOT STORE",  # Company Name
                ""
            ]],
            colWidths=[150*mm, 70*mm],
            hAlign='LEFT'
        ))

        elements.append(Table(
            [[
                "RIOT STORE Building ",  # Company Address
                ""
            ]],
            colWidths=[150*mm, 70*mm],
            hAlign='LEFT'
        ))

        elements.append(Spacer(1, 40))

        # Client Information and Invoice details
        client_info_table = Table(
            [
                ["BILL TO", "Invoice No.:", order.id],
                [order.customer.name, "Issue date:", order.date.strftime('%d/%m/%Y')],
                [order.address, "Due date:", (order.date + timedelta(days=14)).strftime('%d/%m/%Y')],
                
            ],
            colWidths=[90*mm, 30*mm, 50*mm]
        )
        elements.append(client_info_table)

        elements.append(Spacer(1, 40))

        # Invoice items
        items_data = [
            ["PRODUCT NAME", "QUANTITY", "UNIT PRICE (£)", "AMOUNT (£)"],
            [order.product.name, order.quantity, f"{order.price:.2f}", f"{order.quantity * order.price:.2f}"],
        ]
        items_table = Table(items_data, colWidths=[90*mm, 30*mm, 30*mm, 30*mm])
        items_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
        ]))
        elements.append(items_table)

        elements.append(Spacer(1, 20))

        # Total amount
        total_table = Table(
            [["", "", "TOTAL (GBP):", f"{order.quantity * order.price:.2f}"]],
            colWidths=[90*mm, 30*mm, 30*mm, 30*mm]
        )
        total_table.setStyle(TableStyle([
            ('BACKGROUND', (2, 0), (-1, 0), colors.lightgrey),
            ('ALIGN', (2, 0), (-1, 0), 'CENTER'),
        ]))
        elements.append(total_table)

        elements.append(Spacer(1, 60))

        # Signature
        elements.append(Table(
            [["Issued by, signature:", "", "RIOT STORE shop owner"]],
            colWidths=[50*mm, 90*mm, 50*mm]
        ))

        doc.build(elements)
        return response
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.status != 'Delivered':
        order.status = 'Cancelled'
        order.save()
        messages.success(request, 'Order has been cancelled successfully.')
    else:
        messages.error(request, 'Delivered orders cannot be cancelled.')
    return redirect('order') 