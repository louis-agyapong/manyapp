from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    name = models.CharField(_("name"), max_length=255)
    relatives = models.ManyToManyField(
        "self",
        verbose_name=_("relatives"),
        through="FamilyMember",
        through_fields=("member", "relative"),
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("member")
        verbose_name_plural = _("members")


class FamilyRelationship(models.Model):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("family relationship")
        verbose_name_plural = _("family relationships")


class FamilyMember(models.Model):
    member = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="family_members",
        verbose_name=_("member"),
    )
    relative = models.ForeignKey(
        Person,
        verbose_name=_("relative"),
        on_delete=models.CASCADE,
        related_name="family_relatives",
    )
    relation = models.ForeignKey(
        FamilyRelationship,
        on_delete=models.CASCADE,
        verbose_name=_("relation"),
        related_name="family_relations",
    )

    def __str__(self):
        return f"{self.member.name} - {self.relative.name}({self.relation.name})"

    class Meta:
        verbose_name = _("family member")
        verbose_name_plural = _("family members")
        app_label = "family_member"
