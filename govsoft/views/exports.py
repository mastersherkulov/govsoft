import csv
from django.http import HttpResponse
from govsoft.models import Organizations, Systems


def export_organizations_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=organizations.csv"

    writer = csv.writer(response)
    writer.writerow([
        "id",
        "org_code",
        "org_name",
        "is_active",
        "created_at",
        "updated_at",
    ])

    for org in Organizations.objects.all().order_by("id"):
        writer.writerow([
            org.id,
            org.org_code,
            org.org_name,
            org.is_active,
            org.created_at.isoformat() if org.created_at else "",
            org.updated_at.isoformat() if org.updated_at else "",
        ])

    return response


def export_systems_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=systems.csv"

    writer = csv.writer(response)
    writer.writerow([
        "id",
        "org_id",
        "org_name",
        "system_type",
        "system_name",
        "status",
        "created_at",
        "updated_at",
    ])

    for system in Systems.objects.select_related("org_id").all().order_by("id"):
        writer.writerow([
            system.id,
            system.org_id_id,
            system.org_id.org_name if system.org_id_id else "",
            system.get_system_type_display(),
            system.system_name,
            system.status,
            system.created_at.isoformat() if system.created_at else "",
            system.updated_at.isoformat() if system.updated_at else "",
        ])

    return response

