from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import logging

class AttendanceToolView(View):
    def get(self, request):
        context = {
            'count': 1
        }
        return render(request, 'pages/attendance_tool.html', context)

