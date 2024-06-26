# Generated by Django 4.2.11 on 2024-04-10 13:57

from enum import IntEnum

from django.db import migrations


def _paypal_recurringuserplan_renewal_triggered_by_task_to_other(apps, schema_editor):
    RecurringUserPlan = apps.get_model("plans", "RecurringUserPlan")
    paypal_recurringuserplans_changed = (
        RecurringUserPlan.objects.select_for_update().filter(
            payment_provider="paypal-recurring",
            renewal_triggered_by=_RenewalTriggeredByEnum.TASK,
        )
    )
    for paypal_recurringuserplan_changed in paypal_recurringuserplans_changed:
        print(
            "RecurringUserPlan's renewal_triggered_by will be overwritten:",
            paypal_recurringuserplan_changed.pk,
        )
    paypal_recurringuserplans_changed.update(
        renewal_triggered_by=_RenewalTriggeredByEnum.OTHER
    )


def _paypal_recurringuserplan_renewal_triggered_by_other_to_task(apps, schema_editor):
    RecurringUserPlan = apps.get_model("plans", "RecurringUserPlan")
    paypal_recurringuserplans_changed = (
        RecurringUserPlan.objects.select_for_update().filter(
            payment_provider="paypal-recurring",
            renewal_triggered_by=_RenewalTriggeredByEnum.OTHER,
        )
    )
    for paypal_recurringuserplan_changed in paypal_recurringuserplans_changed:
        print(
            "RecurringUserPlan's renewal_triggered_by will be overwritten:",
            paypal_recurringuserplan_changed.pk,
        )
    paypal_recurringuserplans_changed.update(
        renewal_triggered_by=_RenewalTriggeredByEnum.TASK
    )


class _RenewalTriggeredByEnum(IntEnum):
    OTHER = 1
    USER = 2
    TASK = 3


class Migration(migrations.Migration):

    dependencies = [
        ("plans_paypal", "0002_auto_20211130_1117"),
        (
            "plans",
            "0014_recurringuserplan_has_automatic_renewal_backup_deprecated_to_renewal_triggered_by",
        ),
    ]

    operations = [
        migrations.RunPython(
            _paypal_recurringuserplan_renewal_triggered_by_task_to_other,
            reverse_code=_paypal_recurringuserplan_renewal_triggered_by_other_to_task,
        )
    ]
