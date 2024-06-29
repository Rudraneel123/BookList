from django.forms import ValidationError
from .models import Bookbuy
from .serializers import BookListSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class BookListAPIView(APIView):
    
    def post(self,request,format=None):
        serializer=BookListSerializers(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        except ValidationError as e:
                return Response(e.detail,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                return Response({"error in posting data":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    def get(self,request,format=None):
        try:
            books=Bookbuy.objects.all()
            serializer=BookListSerializers(books,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error in retrieving data":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
    def put(self, request, format=None):
        try:
            # Extract the book ID from the request data
            book_id = request.data.get('id')
            if not book_id:
                return Response({"error": "ID is required for updating"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Fetch the book object using the ID from the request data
            book = Bookbuy.objects.get(pk=book_id)
            serializer = BookListSerializers(book, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Bookbuy.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error in updating data": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, format=None):
        try:
            book_id=request.data.get('id')
            if not book_id:
                return Response({"error": "ID is required for deleting"}, status=status.HTTP_400_BAD_REQUEST)
            
            book=Bookbuy.objects.get(pk=book_id)
            book.delete()
            return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Bookbuy.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error in deleting data": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    