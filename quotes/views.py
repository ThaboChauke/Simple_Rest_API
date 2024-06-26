from .models import Quotes
from .serializers import QuotesSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def quotes_list(request,format=None):

    if request.method == 'GET':
        quotes = Quotes.objects.all()
        serializer = QuotesSerializers(quotes,many=True)

        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET','PUT','DELETE'])
def quote_detail(request,id,format=None):

    try:
        quote = Quotes.objects.get(pk=id)
    except Quotes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = QuotesSerializers(quote)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = QuotesSerializers(quote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
