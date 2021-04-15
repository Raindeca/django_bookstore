from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from datetime import date
from io import BytesIO
from xhtml2pdf import pisa
from book.models import Book
from .models import Invoice



# class IndexView(generic.ListView):
#     template_name = "invoice/buy.html"
#     context_object_name = 'invoices'

#     def get_queryset(self):
#         return Book.objects.filter(id=self.book.id)

#     def get(self, *args, **kwargs):
#         if bool(self.request.user and self.request.user.is_authenticated):
#             return super().get(*args, **kwargs)
#         else:
#             return redirect('account:login_user')

# class DetailView(generic.DetailView):
#     model = Invoice
    

def buy(request, book_id):
    if bool(request.user and request.user.is_authenticated):
        if request.method == "POST":
            payment_method = request.POST['payment_method']
            Invoice.user = request.user
            Invoice.invoice_date = date.today
            Invoice.item = Book.objects.filter(id=book_id).values('book_title')
            Invoice.payment_method = payment_method
            invoice.total = Book.objects.filter(id=book_id).values('unit_price')
            Invoice.save()

            return redirect('invoice:buy')
        
        else:
            return redirect('account:login_user')
    else:
        return redirect('account:login_user')


def invoice(request):
    return redirect('invoice:invoice')


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        data = Invoice.objects.filter(id=request.user)
        pdf = render_to_pdf('invoice/pdf_template.html', {'data' : data})
        return HttpResponse(pdf, content_type='application.pdf')

class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        data = Invoice.objects.filter(id=request.user)
        pdf = render_to_pdf('invoice/pdf.template.html', {'data' : data})

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %(date.today)
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response