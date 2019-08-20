from django.urls import path

from .views.inicio.view import view as inicio_view

from .views.login.view import view as login_view
from .views.logout.view import view as logout_view
from .views.signup.view import view as signup_view

from .views.superuser.dashboard.view import view as superuser_dashboard_view
from .views.superuser.admins.create.view import view as superuser_dashboard_admin_create_view
from .views.superuser.admins.edit.view import view as superuser_dashboard_admin_edit_view

from .views.admins.dashboard.view import view as admins_dashboard_view
from .views.admins.edit.view import view as admins_edit_view
from .views.admins.historial.monitor.view import view as admins_historial_monitor_view
from .views.admins.historial.student.view import view as admins_historial_student_view
from .views.admins.students.view import view as admins_students_view

from .views.monitors.edit.view import view as monitors_edit_view
from .views.monitors.solicitudes.view import view as monitors_solicitudes_view
from .views.monitors.historial.view import view as monitors_historial_view
from .views.monitors.requested.view import view as monitors_requested_view
from .views.monitors.schedule.view import view as monitors_schedule_view

from .views.students.request.view import view as students_request_view
from .views.students.historial.view import view as students_historial_view
from .views.students.edit.view import view as students_edit_view
from .views.students.request_with_date.view import view as students_request_with_date_view

urlpatterns = [

    # inicio
    path('', inicio_view),
    
    # login
    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', signup_view),

    # Superusers
    path('dashboard/superuser/', superuser_dashboard_view),
    path('dashboard/superuser/admin/create/', superuser_dashboard_admin_create_view),
    path('dashboard/superuser/admin/edit/<int:id_admin>/', superuser_dashboard_admin_edit_view),

    # Administrators
    path('dashboard/admin/', admins_dashboard_view),
    path('dashboard/admin/profile/<int:id_admin>/', admins_edit_view),
    path('dashboard/admin/students/', admins_students_view),
    path('dashboard/admin/historial/monitors/', admins_historial_monitor_view),
    path('dashboard/admin/historial/students/', admins_historial_student_view),

    # Monitors
    path('dashboard/monitor/', monitors_requested_view),
    path('dashboard/monitor/profile/<int:id_monitor>/', monitors_edit_view),
    path('dashboard/monitor/solicitudes/', monitors_solicitudes_view),
    path('dashboard/monitor/historial/', monitors_historial_view),
    path('dashboard/monitor/accept/', monitors_requested_view),
    path('dashboard/monitor/schedule/', monitors_schedule_view),

    # Students
    path('dashboard/student/historial/', students_historial_view),
    path('dashboard/student/request/', students_request_view),
    path('dashboard/student/profile/<int:id_student>/', students_edit_view),
    path('dashboard/student/monitor/<int:id_subject>/<int:id_monitor>/', students_request_with_date_view),
]
