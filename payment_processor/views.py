from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Transaction
from accounts.models import Profile
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
#from sterling.transfer import Transfer #importing the sterling transfer module


class Pay(View):
	def post(self, request, receiver):
		transaction = Transaction.objects.create(receiver=receiver, sender=request.user)
		if transaction.transaction_id:
			return HttpResponse(f"the payment id is : {transaction.transaction_id}")
		else:
			return HttpResponse("the server responded with an error")

	def get(self, request, receiver):
		return render(request, 'payment_processor/pay.html', {})


def create_payment_token(request, sender, amount):
	if request.method == "POST":
		user_id = request.cleaned_data.get('sender_id')
		try:
			sender = Profile.objects.get(reference_id=user_id)
			if sender.account_balance < amount:
				return HttpResponse("Insufficient fund")
			else:
				instance = Transaction.objects.create(receiver=request.user, sender=sender)
				return JsonResponse({'message':'transaction token has been sent', 'error':False})
		except:
			return HttpResponse("No such user")
	else:
		return HttpResponse("Only post methods are allowed")

def verify_transaction_token(request, token):
	if request.method == "POST":
		try:
			instance = Transaction.objects.get(transaction_id=token)
			receiver = instance.receiver
			sender = instance.sender
			if instance.sender.user == request.user:
				receiver.profile.account_balance = receiver.profile.account_balance + instance.amount
				sender.account_balance = sender.account_balance - instance.amount
				instance.verified = True
				instance.save()
			else:
				return HttpResponse("unauthorized operation")
		except:
			return HttpResponse("No such transaction to validate")
	else:
		return HttpResponse("only post method is allowed")
# Create your views here.
