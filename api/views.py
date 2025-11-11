from django.shortcuts import render
import os
from django.http import HttpResponse
from google import genai
def  getGemini(request):
	if request.method=="GET":
		print(f"api key = {os.getenv("")}")
		client=genai.Client(api_key=os.getenv("GEMNI_API_KEY"))
		response=client.models.generate_content(model="gemini-2.5-flash-lite",contents="write a html code for a simple portfolio website,well you are a software engineer agent who only give html response for prototyping dont give any other explanations,just executable code as response")
		print(response.text)
		return HttpResponse(response.text)
# Create your views here.
