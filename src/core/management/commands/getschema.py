"""Command to generate an openapi schema."""

import os
from io import StringIO

import yaml
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    """Command to generate an openapi schema."""

    help = "Generate a schema file and add relevant metadata."

    def handle(self, *args, **options):
        """Read the API document from generateschema and reformat it."""
        file = StringIO()
        call_command("generateschema", stdout=file)
        file.seek(0)
        document = yaml.load(file, Loader=yaml.FullLoader)
        document.update(
            {
                "externalDocs": {
                    "description": "Check us out on GitHub",
                    "url": "https://github.com/ractf",
                },
                "info": {
                    "title": "RACTF Core",
                    "version": os.popen("git rev-parse HEAD").read().strip()[:8],
                    "description": "The API for RACTF.",
                    "contact": {
                        "name": "Support",
                        "email": "support@ractf.co.uk",
                        "url": "https://reallyawesome.atlassian.net/servicedesk/customer/portals",
                    },
                    "x-logo": {
                        "url": "https://www.ractf.co.uk/brand_assets/combined/wordmark_white.svg",
                        "altText": "RACTF Logo",
                    },
                },
            }
        )
        print(yaml.dump(document))
