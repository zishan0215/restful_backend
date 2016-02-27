from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Api
from rest_framework import status
from django.utils import timezone
import time


@api_view(['GET'])
def server_status(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        processes = Api.objects.all()
        pro = {}
        for p in processes:
            now = timezone.now()
            diff = now - p.created
            time = divmod(diff.days * 86400 + diff.seconds, 60)
            pro[p.connid] = p.timeout - (time[0]*60 + time[1])
        return Response(pro)

@api_view(['GET'])
def process_request(request):
    connid = request.GET.get('connId')
    if connid is not None:
        connid = int(connid)
    timeout = request.GET.get('timeout')
    if timeout is not None:
        timeout = int(timeout)

    try:
        process = Api.objects.get(connid=connid)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Api.DoesNotExist:
        x = Api(connid=connid, timeout=timeout)
        x.save()

        while timeout:
            y = Api.objects.get(pk=x.pk)
            if y.timeout == 0:
                break
            time.sleep(1)
            timeout -= 1

        x.delete()
        print(connid, timeout)
        return Response({'status': 'ok'})

@api_view(['PUT'])
def kill(request):
    data = request.data
    connid = data.get('connId')
    try:
        process = Api.objects.get(connid=connid)
    except Api.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    process.timeout = 0
    process.save()

    return Response({'status': 'killed'})

