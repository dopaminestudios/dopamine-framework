# Dopamine Framework

Dopamine Framework is a framework for discord.py which allows you to initialize a production-ready Discord bot in just 4 lines of code. In technical terms, this is a **Flexible Boilerplate Framework** (not to be confused with **opinionated** boilerplate framework). It is designed to streamline the development of scalable Discord applications by automating the process of registering commands, diagnosing the bot, and various other utilities such as a paginator helper and "Private View" helpers which let only the user who initiated the interaction to interact with the components like buttons.

Made by likerofturtles.

---
## Installing

**Use Python 3.12 or higher:**

```Linux/MacOS
# Linux/MacOS
python3 -m pip install -U dopamine-framework
```
```Windows
# Windows
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

No need for terminal access/SSH. This simple to use and feature-rich dashboard for bot owners allows you to unload/reload cogs on the fly, restart the bot, or check logs, accessed using `/od`. This allows bot owner(s) to manage, diagnose the bot right within Discord itself. This dashboard allows the bot to run idefinitely without restarts:

* **Cog Management:** Dynamic loading, unloading, and reloading of cogs.
* **Power State:** Remote shutdown and process-level restarts.
* **Logs:** Real-time retrieval of log files via the Discord UI.
* **Manual Command Syncs:** Sync commands manually globally or within only the current guild.

### 4. Built-in Logging Backend

* A robust Logging Manager utilizing `aiosqlite` that can be plugged into any feature of your bot to implement a logging system, such as for mod logs, action logs, etc.

---

### Comparison (with Sapphire Framework and bare-bones discord.py)

| Feature                                   |      Dopamine Framework       |      Sapphire (js/ts)       |           discord.py            |
|:------------------------------------------|:-----------------------------:|:---------------------------:|:-------------------------------:|
| **Easy Setup**                            |  **✅ (minimal boilerplate)**  | **❌** (Lots of boilerplate) |              **❌**              |
| **No tantrums over different structure**  |             **✅**             |            **❌**            |              **✅**              |
| **Python's ease of use**                  |             **✅**             |            **❌**            |              **✅**              |
| **Smart Commands Sync**                   |       **✅ (Built-in)**        |   **✅** (Through plugins)   |  **❌** (not included/standard)  |
| **In-Discord Dashboard**                  |       **✅ (Built-in)**        |            **❌**            |              **❌**              |
| **Latency Graphs**                        |       **✅ (Built-in)**        |            **❌**            |              **❌**              |
| **Scalability***                          |             **✅**             |            **✅**            |              **✅**              |
| **Fast Iteration**                        |             **✅**             |            **❌**            |              **❌**              |
| **Strict TypeScript Rules**               |             **❌**             |            **✅**            |              **❌**              |
| **Built-in Resource Monitoring**          |             **✅**             |            **❌**            |              **❌**              |
| **Is it JS, tho?**                        |             **❌**             |            **✅**            |              **❌**              |
| **Wins Imaginary Benchmarks**             |             **❌**             |            **✅**            |              **❌**              |
| **Gives you that Dopamine rush?**         |       **✅ (Built-in)**        |            **❌**            |              **❌**              |

<sup>*Scalability refers to ability to run without problems when the bot is in tens of thousands of servers or more. While it's a common myth that "Python is bloated", that's not true in the context of Discord bots. The real bottleneck in popular Discord bots always comes down to network, not code execution time or memory usage.</sup>


---

## Implementation Example

To initialize a bot using the Dopamine Framework, follow the following example:

```python
import discord
from dopamineframework import Bot

bot = Bot(command_prefix="?", cogs_path="your cogs/modules folder path here*", logging_path="path to .sqlite, .db, or .db3 file; only define if you want to use this logging backend.", default_diagnostics=True, intents=discord.Intents.default()) # If no cogs folder is defined, it will default to "cogs". If no logging path, logging will be disabled.

bot.run("YOUR_BOT_TOKEN_HERE")
```
<sub>*Note: All .py files will be attempted to be loaded in the folder. It's recommended to only use the defined path for cogs/extensions/modules.</sub>

---

## Requirements

* `discord.py`
* `aiosqlite`
* `psutil`
* `Pillow`
* `geocoder`

---

## License & Attribution

Dopamine Framework is licensed under the **Apache License 2.0**.

### How to Credit
While you are free to use this framework for private or commercial bots, I require explicit credit. Please include a link to this repository or a mention of "Dopamine Framework" in:
1. Your project's **README** or documentation.
2. Your bot's **info/credits command** (for example `/about` or `/help`).

*Example: "Built with [__Dopamine Framework__](https://github.com/smite-codes/dopamine-framework)"*
