from django.conf.urls import include, url
# from django.views.generic import TemplateView
from rest_framework import routers
# from django.contrib import admin
# from UIS.api.views.student import StudentViewSet
# from UIS.api.views.user import UserViewSet
# from UIS.api.views.course import CourseViewSet
# from UIS.api.views.student_result import StudentResultViewSet
# from UIS.api.views.student_registration import StudentRegistrationViewSet
# from UIS.api.views.student_enrolment import SectionEnrolmentViewSet
# from UIS.api.views.period_degree import PeriodDegreeViewSet
# from UIS.api.views.section import SectionViewSet
# from UIS import views

from rest_framework_jwt.views import obtain_jwt_token

from pX.administration.courses.views import PeriodCourseViewSet
from pX.administration.periods.views import PeriodViewSet
from pX.users.views import PersonViewSet
from pX.forms.views import advisors_list_as_pdf

router = routers.DefaultRouter(trailing_slash=False)
#router.register(r'users', UserViewSet)
# router.register(r'students',
#                 StudentViewSet,
#                 base_name='student')
# router.register(r'users',
#                 UserViewSet)
# router.register(r'courses',
#                 CourseViewSet)
# router.register(r'student-enrolments',
#                 SectionEnrolmentViewSet,
#                 base_name='studentenrolment')
# router.register(r'student-registrations',
#                 StudentRegistrationViewSet)
# router.register(r'period-degrees',
#                 PeriodDegreeViewSet)
# router.register(r'results',
#                 StudentResultViewSet,
#                 base_name='result')
router.register(r'period-courses',
                PeriodCourseViewSet,
                base_name='period_courses')
router.register(r'periods',
                PeriodViewSet,
                base_name='periods')
router.register(r'people',
                PersonViewSet,
                base_name='people')

urlpatterns = [

    url(r'^api/v1/', include(router.urls)),

    url(r'^api/v1/auth/login/', obtain_jwt_token),

#     url(
#         r'^docs/', include('rest_framework_swagger.urls')
#     ),
#     url(
#         r'^student-allowed-enrolments/(?P<registration_number>\d+)/$',
#         views.student_enrolment_as_pdf,
#         name='student_enrolment_pdf'
#     ),
#     url(
#         r'^student-grades/(?P<registration_number>\d+)/$',
#         views.student_grade_as_pdf,
#         name='student_grade__pdf'
#     ),
     url(
         r'^advisor-lists/$',
         advisors_list_as_pdf,
         name='advisors_list_as_pdf'
     ),
     ]
#     # url(r'^o/', include('oauth2_provider.urls',
# namespace='oauth2_provider')),

#     # url('', include('social.apps.django_app.urls', namespace='social')),
#     # url('', include('django.contrib.auth.urls', namespace='auth')),
#     url(r'^$', 'pX.views.home', name='home'),
#     url('', include('django.contrib.auth.urls')),

#     # url(
#     #     r'^$', 'pX.views.main'
#     # ),

#     url(
#          r'^admin/', include(admin.site.urls)
#     ),
#     # url(
#     #     r'^user/', include('UIS.urls', namespace='UIS')
#     # )
#            ]
