"""
Defining Opal PatientLists
"""
from opal import core
from opal.models import Episode

from wardtest import models


class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()


class WardTest(core.patient_lists.PatientList):
    display_name = "current"
    template_name = 'patient_lists/layouts/card_list.html'
    schema = [
        models.Demographics,
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()