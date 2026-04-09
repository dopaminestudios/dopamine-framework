from discord import app_commands
from functools import wraps
from .preconditions import global_cooldown as g_cooldown, permissions_preset as preset, cooldown as local_cooldown


def command(
        name: str = None,
        description: str = None,
        global_cooldown: bool = True,
        permissions_preset: str = None,
        cooldown: tuple[int, float] = None,
        **kwargs
):
    """Build a slash-command decorator that applies framework defaults and checks.

    Args:
        name: Slash-command name override.
        description: Slash-command description override.
        global_cooldown: Whether the framework-level cooldown should be attached.
        permissions_preset: Optional preset name that adds permission checks.
        cooldown: Optional per-command cooldown as a `(rate, per)` tuple.
        **kwargs: Additional keyword arguments forwarded to the underlying API.

    Returns:
        Any: Result produced by this function.
    """
    def decorator(func):
        """Transform a coroutine into an app command with configured checks.

        Args:
            func: Function that will be wrapped by this decorator.

        Returns:
            Any: Result produced by this function.
        """
        cmd = app_commands.command(
            name=name or func.__name__,
            description=description or (func.__doc__ or "No description provided"),
            **kwargs
        )(func)

        if permissions_preset:
            cmd = preset(permissions_preset)(cmd)

        if cooldown:
            rate, per = cooldown
            cmd = local_cooldown(rate, per)(cmd)
        elif global_cooldown:
            cmd = g_cooldown()(cmd)

        return cmd

    return decorator


class Group(app_commands.Group):
    """Custom app-command group that inherits Dopamine defaults.

    """
    def __init__(
            self,
            name: str = None,
            description: str = None,
            global_cooldown: bool = True,
            permissions_preset: str = None,
            cooldown: tuple[int, float] = None,
            **kwargs
    ):
        """Initialize a command group with optional preset and cooldown checks.

        Args:
            name: Slash-command name override.
            description: Slash-command description override.
            global_cooldown: Whether the framework-level cooldown should be attached.
            permissions_preset: Optional preset name that adds permission checks.
            cooldown: Optional per-command cooldown as a `(rate, per)` tuple.
            **kwargs: Additional keyword arguments forwarded to the underlying API.
        """
        super().__init__(
            name=name or self.__class__.__name__.lower(),
            description=description or (self.__doc__ or "No description provided"),
            **kwargs
        )
        if permissions_preset:
            preset(permissions_preset)(self)

        if cooldown:
            rate, per = cooldown
            local_cooldown(rate, per)(self)
        elif global_cooldown:
            g_cooldown()(self)