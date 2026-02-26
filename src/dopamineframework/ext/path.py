from pathlib import Path
import importlib.resources

BASE_PATH = Path(__file__).parent

try:
    with importlib.resources.path("dopamineframework.ext", "Bold.ttf") as p:
        BOLDFONT_PATH = str(p)
except Exception:
    BOLDFONT_PATH = "Bold.ttf"

framework_version = "1.4.22"
