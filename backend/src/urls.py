from django.urls import path
from . import views
from .views.attendance_tools.attendance_tool_view import AttendanceToolView

urlpatterns = [
    path("attendance_tool/", AttendanceToolView.as_view(), name="index"),
]
