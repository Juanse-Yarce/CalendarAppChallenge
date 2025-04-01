from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error

EMAIL = "email"
SYSTEM = "system"

@dataclass
class Remainder:

    date_time: datetime
    type: str = EMAIL

    