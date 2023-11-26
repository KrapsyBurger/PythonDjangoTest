from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .wikipedia_fetch import wikipedia_summary_fetch

@api_view(['POST'])
def testing(request):
	email_value = request.data.get('email', None)
	title_value = request.data.get('title', None)
	return Response(wikipedia_summary_fetch(title_value, email_value))


# Create your views here.
