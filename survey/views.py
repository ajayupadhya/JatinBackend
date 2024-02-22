from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
# Create your views here.





class SurveyListView(APIView):
    permission_classes = (AllowAny,)
    # def get_queryset(self):
    #     return HttpResponse("Hello there")
    
    
    def post(self,request):
        
        
      
    
        return HttpResponse("Created" , request)