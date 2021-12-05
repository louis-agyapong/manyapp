from django.db import models
from django.db.models.fields import related
from django.utils.translation import ugettext_lazy as _


class Company(models.Model):
    name = models.CharField(_("Company"), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")


class Programmer(models.Model):
    """A company employee"""

    name = models.CharField(_("Name"), max_length=100)
    company = models.ForeignKey(
        Company,
        verbose_name=_("company"),
        on_delete=models.CASCADE,
        related_name="programmers",
    )

    def __str__(self):
        return f"{self.name} works at {self.company}"
