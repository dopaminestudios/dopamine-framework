# Dopamine Framework

Dopamine Framework is the best framework for `discord.py` bots. Dopamine Framework allows you to initialyze a production-ready Discord bot in just 5 lines of code. It is designed to streamline the development of scalable Discord applications by automating the process of registering commands, diagnosing the bot, and various other utilities such as a paginator helper and "Private View" helpers which let only the user who initiated the interaction to interact with the components like buttons.

Made by smite-codes.

---
## Installing

**Use Python 3.12 or higher:**

```Linux/MacOS
python3 -m pip install -U dopamine-framework
```
```Windows
py -3 -m pip install -U dopamine-framework
```
## Features

### 1. Smart Command Syncs

The framework includes a Command Registry that compares local command states with remote Discord API states. This ensures that global and guild-specific slash commands are only synced when changes are detected, preventing unnecessary API overhead and rate-limit triggers.

### 2. Diagnostics

The built-in `Diagnostics` "cog" (module) provides real-time monitoring of the bot's health, including:

* **Latency:** High precision API, Heartbeat, and Round-trip latency monitoring.
* **Resource Utilization:** CPU and RAM usage tracking via `psutil`.
* **Graphs:** Generate graphs for the bot's latency for visual performance auditing.
* **Host Device Metrics:** Integration with system sensors to report host location and battery status, if available.

### 3. In-Discord Owner Dashboard

Never have to need terminal access/SSH using this simple to use and feature-rich dashboard for bot owners, accessed using `/od`. This allows bot owner(s) to manage, diagnose the bot right within Discord itself. This dashboard allows the bot to run idefinitely without restarts:

* **Cog Management:** Dynamic loading, unloading, and reloading of cogs.
* **Power State:** Remote shutdown and process-level restarts.
* **Logs:** Real-time retrieval of local log files via the Discord UI.
* **Manual Command Syncs:** Sync commands manually globally or within only the current guild.

### 4. Built-in Logging Backend

* A robust Logging Manager utilizing `aiosqlite` that can be plugged into any feature of your bot to implement a logging system, such as for mod logs, action logs, etc.

---

## Implementation Example

To initialize a bot using the Dopamine Framework, follow the following example:

```python
import discord
from dopamine_framework import Bot

intents = discord.Intents.default()
bot = Bot(command_prefix="?", cogs_path="modules", logging_path="logging.db", default_diagnostics=True, intents=intents) # If no cogs folder is defined, it will default to "cogs". If no logging path, logging will be disabled.

bot.run("YOUR_BOT_TOKEN_HERE")
```

---

## Requirements

* `discord.py`
* `aiosqlite`
* `psutil`
* `Pillow`
* `geocoder`

---

## Logging Manager Documentation

The LoggingManager is an asynchronous backend designed to facilitate per-guild Discord channel logging for things such as mod logs, action logs, and more.

* **`self.logger.get(guild.id)`:** Get the logging channel, where guild.id the guild whose logging channel's ID you want to get.
* **`self.logger.set(guild.id, channel_id)`:** Set the logging channel, where guild.id the guild and channel_id is the ID of the channel to be set for logging.
* **`self.logger.delete(guild.id)`:** Delete the logging channel, where guild.id the guild whose logging channel you want to delete.

### Example:

```python
import discord
from dopamine_framework import Bot

intents = discord.Intents.default()
bot = Bot(command_prefix="?", cogs_path="modules", logging_path="logging.db", default_diagnostics=True, intents=intents) # Define logging path to enable logging. If no logging path, logging will be disabled.

bot.run("YOUR_BOT_TOKEN_HERE")
```

## License & Attribution

Dopamine Framework is licensed under the **Apache License 2.0**.

### How to Credit
While you are free to use this framework for private or commercial bots, I require explicit credit. Please include a link to this repository or a mention of "Dopamine Framework" in:
1. Your project's **README** or documentation.
2. Your bot's **info/credits command** (for example `/about` or `/help`).

*Example: "Built with [__Dopamine Framework__](https://github.com/smite-codes/dopamine-framework)"*
