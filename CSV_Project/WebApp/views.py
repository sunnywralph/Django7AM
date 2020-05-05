from django.http import HttpResponse
import csv


def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="BigData.csv"'
    writer = csv.writer(response)
    writer.writerow(['1001', 'Subba', 'Raju', 'S/W'])
    writer.writerow(['1002', 'Sara', 'Thomson', 'Networking', 'Testing'])
    writer.writerow(['1003', 'Sunny', 'William', 'Django Developer'])
    return response
