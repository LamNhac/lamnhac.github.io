import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "ARH-d6f0pp9PK06LlLSLe43YA4i0Q5tYqHjzdJbLZ1zLJttNMKe4dzATk6eOfuBkIcFzzuRg2IfLtxFq"
        self.client_secret = "ELX_OOdaXodx-bmSaNCzT1deU3M29JouGd9XpkBOz4HjMk2sm5SoY2ot4l4S3-GZFVmTiFc7aI9TQy27"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
