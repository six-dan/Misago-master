# Generated by Django 1.11.15 on 2018-08-15 20:58
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("misago_legal", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Agreement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("terms_of_service", "Terms of service"),
                            ("privacy_policy", "Privacy policy"),
                        ],
                        db_index=True,
                        default="terms_of_service",
                        max_length=20,
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("link", models.URLField(blank=True, max_length=255, null=True)),
                ("text", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "created_by_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("last_modified_on", models.DateTimeField(blank=True, null=True)),
                (
                    "last_modified_by_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "last_modified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserAgreement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "accepted_on",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "agreement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accepted_by",
                        to="misago_legal.Agreement",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-pk"]},
        ),
    ]
