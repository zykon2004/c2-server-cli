from pathlib import Path
from typing import Literal

PROTOCOL: Literal["http", "https"] = "http"
REMOTE_SERVER_HOST = "localhost"
REMOTE_SERVER_PORT = 8080
REMOTE_SERVER_BASE_URL = f"{PROTOCOL}://{REMOTE_SERVER_HOST}:{REMOTE_SERVER_PORT}"
# This should not be here
SECRET_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY5MTk1ODg2OCwiaWF0IjoxNjkxOTU4ODY4fQ.mi9ar0R_mHsq1JCvdbEvwHz40fGVgZXIARefYJ9f4iU"  # noqa: S105
REQUEST_TIMEOUT = 5
STATUS_REFRESH_INTERVAL = 5
DB_LOCATION = Path(__file__).parents[2] / "c2-server" / "resources" / "db.sqlite3"
DB_ENGINE = f"sqlite:///{DB_LOCATION}"
CLIENT_LIVELINESS_THRESHOLD_MINUTES = 60
