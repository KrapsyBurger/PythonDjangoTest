from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .wikipedia_fetch import wikipedia_summary_fetch
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

@api_view(['POST'])
def testing(request):
	email_value = request.data.get('email', None)
	try:
		validate_email(email_value)
	except ValidationError as e:
		return Response(e)
	title_value = request.data.get('title', None)
	return Response(wikipedia_summary_fetch(title_value, email_value))
