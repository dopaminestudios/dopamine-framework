from pathlib import Path
import importlib.resources

BASE_PATH = Path(__file__).parent

try:
    with importlib.resources.path("dopamine_framework.ext", "Bold.ttf") as p:
        BOLDFONT_PATH = str(p)
except Exception:
    BOLDFONT_PATH = "Bold.ttf"

framework_version = "v1.1.0"
