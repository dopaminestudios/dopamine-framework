import warnings
from src.dopamineframework import bot, now_plus_seconds_unix, duration_to_seconds, PrivateLayoutView, PrivateView, ViewPaginator, LayoutViewPaginator, mod_check, prefix_mod_check

warnings.warn(
    "dopamine_framework will be deprecated in the next major release. Use dopamineframework instead.",
    DeprecationWarning,
    stacklevel=2
)