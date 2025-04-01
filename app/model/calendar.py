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

    def __str__(self):
        print(f"Reminder on {self.date_time} of type {type}")

@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time
    reminders: list[Remainder] = []

