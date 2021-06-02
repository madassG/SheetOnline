import csv
import json
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from sheet import settings
from sheetCheck.forms import SheetForm
from . import script


def index(request):
    form = SheetForm()
    error = None
    if request.method == 'POST':
        form = SheetForm(request.POST, request.FILES)
        if not request.POST.get('columns').replace(',', '').isdigit() or ',,' in request.POST.get('columns'):
            form.errors['columns'] = ['Формат ввода столбцов неверный']
        if form.is_valid():
            sheet = form.save()
            url = os.path.join(os.path.join(settings.MEDIA_ROOT, 'sheets'), request.FILES['file'].name)
            script_json = script.get_dict(url, sheet.sheet_format.code, sheet.columns)
            script_output = str(script_json)
            if script_output == '1':
                error = 'Формат документа не совпадает с данным вами'
            elif script_output == '2':
                error = 'Проверьте ввод колонок'
            elif script_output == '3':
                error = 'Ошибка в программе'
            else:
                sheet.response = script_output
                sheet.save()
                response = HttpResponse(
                    content_type='text/csv',
                    headers={'Content-Disposition': 'attachment; filename="students.csv"'},
                )
                writer = csv.writer(response)
                for student in script_json:
                    arr = []
                    if student.get('id', 0) != 0:
                        arr.append(student['id'])
                    if student.get('ticket', 0) != 0:
                        arr.append(student['ticket'])
                    if student.get('FIO', 0) != 0:
                        arr.append(student['FIO'])
                    if student.get('mark', 0) != 0:
                        arr.append(student['mark'])
                    writer.writerow(arr)
                return response

    return render(request, 'index.html', {
        'error': error,
        'form': form,
    })


# @csrf_exempt
def apiSheet(request):
    if request.method == 'POST':
        response_data = {
            'status': 'success',
            'error': None,
            'result': None,
        }
        if not request.POST.get('columns').replace(',', '').isdigit() or ',,' in request.POST.get('columns'):
            response_data['status'] = 'error'
            response_data['error'] = 'Invalid columns input'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        form = SheetForm(request.POST, request.FILES)
        if form.is_valid():
            sheet = form.save()
            url = os.path.join(os.path.join(settings.MEDIA_ROOT, 'sheets'), request.FILES['file'].name)
            script_json = script.get_dict(url, sheet.sheet_format.code, sheet.columns)
            script_output = str(script_json)
            if script_output == '1':
                response_data['status'] = 'error'
                response_data['error'] = 'Invalid document format'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            elif script_output == '2':
                response_data['status'] = 'error'
                response_data['error'] = 'Columns error'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            elif script_output == '3':
                response_data['status'] = 'error'
                response_data['error'] = 'Unknown error'
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                sheet.response = script_output
                sheet.save()
                response_data['result'] = script_json
                return HttpResponse(json.dumps(response_data), content_type="application/json", charset='utf-8')
    return redirect('index')
