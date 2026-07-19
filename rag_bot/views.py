from django.shortcuts import render

from rest_framework.decorators import api_view
#to convert python directory to json format
from rest_framework.response import Response
#to access ask_queation fn from rag_engine file
from .rag_engine import ask_question

#it ensure user get responses after sender a request, not before
@api_view(['POST'])
def chat_with_bot(request):
    # 1. Catch the message sent by the HTML frontend
    user_message = request.data.get('message', '')
    
    if not user_message:
        return Response({"error": "Please provide a message."}, status=400)
    
    # 2. Hand the message to the AI Brain we built in the last step
    print(f"User asked: {user_message}")
    ai_response = ask_question(user_message)
    
    # 3. Send the AI's answer (and the source PDF info) back to the frontend
    return Response({
        "reply": ai_response["text"],
        "source": ai_response["source"]
    })