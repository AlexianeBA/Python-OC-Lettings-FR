# Generated by Django 3.0 on 2024-03-06 17:32

from django.db import migrations


def copy_adress_data(apps, schema_editor):
    OldModel = apps.get_model("oc_lettings_site", "Address")
    NewModel = apps.get_model("lettings", "Address")

    NewModel.objects.bulk_create(
        NewModel(
            number=old_object.number,
            street=old_object.street,
            city=old_object.city,
            state=old_object.state,
            zip_code=old_object.zip_code,
            country_iso_code=old_object.country_iso_code,
        )
        for old_object in OldModel.objects.all()
    )


def copy_letting_data(apps, schema_editor):
    """Copies the letting data from the old app to the new app."""
    try:
        OldModel = apps.get_model("oc_lettings_site", "Letting")
    except LookupError:
        return

    NewModel = apps.get_model("lettings", "Letting")
    AddressModel = apps.get_model("lettings", "Address")

    NewModel.objects.bulk_create(
        NewModel(
            title=old_object.title,
            address=AddressModel.objects.get(id=old_object.address.id),
        )
        for old_object in OldModel.objects.all()
    )


class Migration(migrations.Migration):

    dependencies = [("lettings", "0001_initial"), ("oc_lettings_site", "0001_initial")]

    operations = [
        migrations.RunPython(copy_adress_data, migrations.RunPython.noop),
        migrations.RunPython(copy_letting_data, migrations.RunPython.noop),
    ]
