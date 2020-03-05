from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Transaction
from django.http import HttpResponse, HttpResponseRedirect
#from sterling.transfer import Transfer #importing the sterling transfer module


class Pay(View):
	def post(self, request, receiver):
		transaction = Transaction.object.create(receiver=receiver, sender=request.user)
		if transaction.transaction_id:
			return HttpResponse(f"the payment id is : {transaction.transaction_id}")
		else:
			return HttpResponse("the server responded with an error")

	def get(self, request, receiver):
		return render(request, 'payment_processor/pay.html', {})

# Create your views here.
