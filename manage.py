import os
import sys
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


def main():
    """
    Entry point of the Django management script.
    Initializes the Sentry SDK, sets the Django settings module,
    and executes the command line arguments.
    """
    sentry_sdk.init(
        dsn="https://322da723973989b5a940d90e0779dcf3@o4506824189739008.ingest.us.sentry.io/4506892738953216",
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
