"""
Component that will help guide the user taking its first steps.

For more details about this component, please refer to the documentation at
https://home-assistant.io/components/introduction/
"""
import logging

DOMAIN = 'introduction'


def setup(hass, config=None):
    """Setup the introduction component."""
    log = logging.getLogger(__name__)
    log.info("""

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Hello, and welcome to Home Assistant!

        We'll hope that we can make all your dreams come true.

        Here are some resources to get started:

         - Configuring Home Assistant:
           https://home-assistant.io/getting-started/configuration/

         - Available components:
           https://home-assistant.io/components/

         - Troubleshooting your configuration:
           https://home-assistant.io/getting-started/troubleshooting-configuration/

         - Getting help:
           https://home-assistant.io/help/

        This message is generated by the introduction component. You can
        disable it in configuration.yaml.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

    return True
