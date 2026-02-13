## [v1.4.0](https://github.com/likerofturtles/dopamine-framework/compare/vv1.3.3...vv1.4.0) (2026-02-13)
### Features & Minor Updates and Changes

* Added ability to set status and activity when calling Bot. ([456eafa](https://github.com/likerofturtles/dopamine-framework/commit/456eafa29d464fc987bacddaed77022e9b3c951c))

## [v1.3.3](https://github.com/likerofturtles/dopamine-framework/compare/vv1.3.2...vv1.3.3) (2026-02-13)
### Bug Fixes

* Moved owner dashboard command to a new pic.py (PIC = Permanent Internal Cog) so that owner dashboard doesn't get disabled if the user disables the diagnostics feature. ([efdc633](https://github.com/likerofturtles/dopamine-framework/commit/efdc6332c43311fd028588e7a2632ef622026c62))

### Documentation Changes

* Added "No tantrums over different structure" as a feature in readme comparison table. ([ff1dafb](https://github.com/likerofturtles/dopamine-framework/commit/ff1dafbdc218742189412a51f651402bd69a632a))

## [v1.3.2](https://github.com/likerofturtles/dopamine-framework/compare/vv1.3.1...vv1.3.2) (2026-02-12)
### Bug Fixes

* Hotfix: Fixed commands registry crashing and failing to load the bot while trying to handle command groups. ([dd8bfb0](https://github.com/likerofturtles/dopamine-framework/commit/dd8bfb0280cf9aea43f7997f1e27529b8f2e2f5c))

## [v1.3.1](https://github.com/likerofturtles/dopamine-framework/compare/vv1.3.0...vv1.3.1) (2026-02-12)
### Bug Fixes

* Added relative import fix in dashboard.py to fix this error that occurs when attempting to load internal cog: ERROR: Failed to start the bot: Extension 'dopamineframework.ext.diagnostics' raised an error: ModuleNotFoundError: No module named 'src' ([3cbc6d9](https://github.com/likerofturtles/dopamine-framework/commit/3cbc6d94dcca6e155473a18c5521aa95ce1e2bcf))

## [v1.3.0](https://github.com/likerofturtles/dopamine-framework/compare/vv1.2.4...vv1.3.0) (2026-02-12)
### Features & Minor Updates and Changes

* Added ephemeral option to /od command that shows the owners dashboard. The dashboard is now sent as non-ephemeral by default, but you can choose to make it ephemeral using the option. ([defa142](https://github.com/likerofturtles/dopamine-framework/commit/defa142f3f6eef6c7d6853b21ff998317ca96e54))

### Bug Fixes

* Added relative import to fix this error that occurs when attempting to load internal cog: ERROR: Failed to start the bot: Extension 'dopamineframework.ext.diagnostics' raised an error: ModuleNotFoundError: No module named 'src' ([0f29ed1](https://github.com/likerofturtles/dopamine-framework/commit/0f29ed13332724e4a6f1ebfa968a6ae2a072030e))

### Styling, UI, Code Cleanup, and Linting Fixes

* Added "Dopamine Framework: " prefix to all strings and to owner dashboard header. Because, branding is always nice! ([83a6e29](https://github.com/likerofturtles/dopamine-framework/commit/83a6e299a082fa46d6b687cb50f11880fd3cda5d))

### Documentation Changes

* Updated README. ([c2b080b](https://github.com/likerofturtles/dopamine-framework/commit/c2b080b46e1aa8188962adf813fe9df440a59416))

## [v1.2.4](https://github.com/likerofturtles/dopamine-framework/compare/vv1.2.3...vv1.2.4) (2026-02-12)
### Bug Fixes

* Fixed capitalization of Bot in legacy support import statement. Legacy support now works perfectly. ([1651b9f](https://github.com/likerofturtles/dopamine-framework/commit/1651b9f9bb4602916051bfb07e53f3f85692c0e0))

## [v1.2.3](https://github.com/likerofturtles/dopamine-framework/compare/vv1.2.2...vv1.2.3) (2026-02-12)
### Bug Fixes

* Fixed legacy support. Before: dopamine_framework.py in root folder. This wasn't being included in the package when it was being built. Now: dopamine_framework directory with __init__.py with the same code. Legacy support now works. ([2fa0ee5](https://github.com/likerofturtles/dopamine-framework/commit/2fa0ee54cab7020ecef623d9c02769c40b45c991))

### Documentation Changes

* Expanded intro in readme: "In technical terms, this is a **Flexible Boilerplate Framework**." ([0ad11b7](https://github.com/likerofturtles/dopamine-framework/commit/0ad11b7c570690d1c6e5082cd7c19566245ef4ab))

## [v1.2.2](https://github.com/likerofturtles/dopamine-framework/compare/vv1.2.1...vv1.2.2) (2026-02-12)
### Bug Fixes

* Added "v" prefix to internal cog framework version. ([a477468](https://github.com/likerofturtles/dopamine-framework/commit/a4774686798a0766ef37162d74235c29dc5c36dc))
* Added "v" prefix to print and log statements in bot.py. ([ee8ad77](https://github.com/likerofturtles/dopamine-framework/commit/ee8ad7709871d52b7756b2079824763f7c71b257))

## [v1.2.1](https://github.com/likerofturtles/dopamine-framework/compare/vv1.2.0...vv1.2.1) (2026-02-12)
### Bug Fixes

* Fixed internal cog's version not updating on version bump. ([5683fe1](https://github.com/likerofturtles/dopamine-framework/commit/5683fe1203f7bacdcb3c9ff6677bad8d9174430f))

## [v1.2.0](https://github.com/likerofturtles/dopamine-framework/compare/vv1.1.1...vv1.2.0) (2026-02-12)
### Features

* Renamed folder from dopamine_framework to dopamineframework. Now, use "from dopamineframework import ..." for imports instead of dopamine_framework. (Note: This isn't a breaking change, because you can still use dopamine_framework and it will automatically import from "dopamineframework". However, this legacy support will be dropped in the next major release, so it's highly recommended to use "dopamineframework" in your code. ([0559afe](https://github.com/likerofturtles/dopamine-framework/commit/0559afee7a7ec77fc8ab1f04d4038f7f17fef41e))

### Styling, UI, Code Cleanup, and Linting Fixes

* Updated colours for in-built cog's graph and embed. ([72b9e3b](https://github.com/likerofturtles/dopamine-framework/commit/72b9e3be45a0c366a84dd4bbfbc72912603e75f8))

### Documentation Changes

* Updated code snippets in readme to use the new "dopamineframework" name in imports. ([8503cae](https://github.com/likerofturtles/dopamine-framework/commit/8503cae20cafa4ec1c54e37f22bca889d450660f))
* updated readme. ([cc28971](https://github.com/likerofturtles/dopamine-framework/commit/cc289715b118731a0721443456d7cdd7ea5626fc))

## [v1.1.1](https://github.com/likerofturtles/dopamine-framework/compare/v1.1.0...v1.1.1) (2026-02-12)


### Bug Fixes

* sync callbacks now use the return statement so that errors can be shown (if any) instead of hard-coded success response. ([e85b752](https://github.com/likerofturtles/dopamine-framework/commit/e85b752643fe94ec0fedf3e194d57d4dfcf26814))
