from tools.models import Tool
from tools.serializers import ToolSerializer
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tools(request):
    if request.method == 'GET':
        # invoke serializer and return to client
        data = Tool.objects.all()
        serializer = ToolSerializer(data, many=True)
        return JsonResponse({'tools' : serializer.data})
        
    elif request.method == 'POST':
        serializer = ToolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'tool': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def tool(request, id):
    # invoke serializer and return to client
    try:
        data = Tool.objects.get(pk=id)
    except Tool.DoesNotExist:
        raise Http404('Tool does not exist')
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if(request.method == 'GET'):
        serializer = ToolSerializer(data)
        return Response({'tool': serializer.data}, status=status.HTTP_200_OK)
    elif (request.method == 'DELETE'):
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif (request.method == 'POST'):
        serializer = ToolSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'tool': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return Response(tokens, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
