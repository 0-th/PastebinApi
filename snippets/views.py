from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets or create a new snippet
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(instance=snippets, many=True)
        return JsonResponse(data=serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(stream=request)
        serializer = SnippetSerializer(instance=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete  a code snippet
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(instance=snippet)
        return JsonResponse(data=serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(instance=snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
