from datetime import datetime
import pytz


def get_current_moscow_time() -> str:
    """Возвращает текущую дату и время в московском часовом поясе в формате YYYY-MM-DD HH:MM:SS."""
    moscow_tz = pytz.timezone("Europe/Moscow")  # Московский часовой пояс
    moscow_time = datetime.now(moscow_tz)  # Текущее время в Москве
    return moscow_time.strftime("%d-%m-%Y %H:%M")
