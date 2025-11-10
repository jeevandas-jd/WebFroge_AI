from django.shortcuts import render
import os
from google import genai
def  getGemini(request):
	client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
	response=client.models.generate_content(model="gemini-2.5-flash",contents="what is 2+2")
	print(response.text)
	return HttpResponse("done with the gemini")
# Create your views here.
