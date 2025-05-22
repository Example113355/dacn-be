from background_task import background
import requests
from django.conf import settings


@background(schedule=10)
def stop_pump(token):
    """
    Stop the pump after 10s.
    """
    requests.post(
        settings.PUMP_URL,
        headers={"X-Authorization": f"Bearer {token}"},
        json={"method": "setBumpStatus", "params": 0},
    )
