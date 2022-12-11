from django.utils.timezone import utc
import datetime


def get_time_diff(self):
    if self.created_at:
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        difference = now - self.created_at
        second = difference.total_seconds()
        minute = int(second / 60)
        hour = int(minute / 60)
        return second, minute, hour
