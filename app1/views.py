from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app1.models import Customer
from app1.serializers import CustomerSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


import json
from django.http import HttpResponse
import jwt


# @login_required
def index(request):
    return render(request, "app1/index.html", 
    {'title': 'App here'})

def jwtToken(self):
    
    response_data = {}
    response_data['status'] = True
    response_data['message'] = 'Token found'
    # enccode
    response_data['token'] = jwt.encode({'user_id': 'abc', 'user_email': 'abc@gmail.com'}, "SECRET", algorithm="HS256").decode('utf-8')
    # decode
    print(type(response_data['token']))
    response_data['decode_token'] = jwt.decode( response_data['token'], "SECRET", algorithm="HS256" )    
    return HttpResponse(json.dumps(response_data), content_type="application/json")



class CustomerList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        # print(request.data)
        snippets = Customer.objects.all()
        serializer = CustomerSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        print(pk, " :- get_object ")
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print(" get request", pk)
        snippet = self.get_object(pk)
        serializer = CustomerSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
