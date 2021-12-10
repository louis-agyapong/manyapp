from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import FamilyMember, FamilyRelationship, Person


admin.site.register(Person)
admin.site.register(FamilyMember)
admin.site.register(FamilyRelationship)