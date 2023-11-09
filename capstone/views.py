# views.py

from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse 


def LogsListView(request):
    try:
        with connection.cursor() as cursor:
            strSql = "SELECT seq, event, create_date, hash, message FROM log"
            cursor.execute(strSql)
            logs = cursor.fetchall()

            # 데이터를 JSON 형식으로 변환하여 응답합니다.
            logs_data = []
            for log in logs:
                log_dict = {
                    'seq': log[0],
                    'event': log[1],
                    'create_date': log[2].strftime('%Y-%m-%d %H:%M:%S') if log[2] is not None else None,
                    'hash': log[3],
                    'message': log[4]
                }
                logs_data.append(log_dict)

            return render(request, 'logs_list.html', {'logs': logs_data})

    except Exception as e:
        print("Failed selecting in LogsListView:", str(e))
        return JsonResponse({'error': 'Failed to fetch data.'}, status=500)


def LogsList(request):
    try:
        with connection.cursor() as cursor:
            strSql = "SELECT seq, event, create_date, hash, message FROM log"
            cursor.execute(strSql)
            logs = cursor.fetchall()

            # 데이터를 JSON 형식으로 변환하여 응답합니다.
            logs_data = []
            for log in logs:
                log_dict = {
                    'seq': log[0],
                    'event': log[1],
                    'create_date': log[2].strftime('%Y-%m-%d %H:%M:%S') if log[2] is not None else None,
                    'hash': log[3],
                    'message': log[4]
                }
                logs_data.append(log_dict)

            return JsonResponse(logs_data, safe=False)

    except Exception as e:
        print("Failed selecting in LogsListView:", str(e))
        return JsonResponse({'error': 'Failed to fetch data.'}, status=500)

