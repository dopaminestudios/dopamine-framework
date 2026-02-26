## [v1.4.22](https://github.com/dopaminestudios/dopamine-framework/compare/vv1.4.21...vv1.4.22) (2026-02-26)
### Bug Fixes

* Finally fixed command sync always being triggered even with no changes by comparing local last synced hash with local now hash. No need for API calls now ([6bab338](https://github.com/dopaminestudios/dopamine-framework/commit/6bab33887488f493e4de73f5e86d5508af45fab6))

## [v1.4.21](https://github.com/dopaminestudios/dopamine-framework/compare/vv1.4.20...vv1.4.21) (2026-02-26)
### Bug Fixes

* Finally fixed command sync always being triggered even with no changes ([b2bbc39](https://github.com/dopaminestudios/dopamine-framework/commit/b2bbc39caf52d040fc366701f8a48b24f8770e5d))

## [v1.4.20](https://github.com/dopaminestudios/dopamine-framework/compare/vv1.4.19...vv1.4.20) (2026-02-26)
### Bug Fixes

* Hotfix: Fixed: `ERROR: Failed to start the bot: Object of type locale_str is not JSON serializable` ([496d853](https://github.com/dopaminestudios/dopamine-framework/commit/496d853577e66c11dac9fb8d8b717e2f1faba2fa))

## [v1.4.19](https://github.com/dopaminestudios/dopamine-framework/compare/vv1.4.18...vv1.4.19) (2026-02-26)
### Bug Fixes

* Hotfix: Fixed error `Failed to start the bot: 'Command' object has no attribute 'type'` ([3f7b2eb](https://github.com/dopaminestudios/dopamine-framework/commit/3f7b2eb0d363cc292eec63649b1bbac1e6a7f5ee))

## [v1.4.18](https://github.com/dopaminestudios/dopamine-framework/compare/vv1.4.17...vv1.4.18) (2026-02-26)
### Bug Fixes

* Switched to hashing to fix command sync always being triggered ([6ab4149](https://github.com/dopaminestudios/dopamine-framework/commit/6ab41496217d9a8cda9e9c57e3a0b2ec591d801c))

## [v1.4.17](https://github.com/dopaminestudios/dopamine-framework/compare/vv1.4.16...vv1.4.17) (2026-02-26)
### Bug Fixes

* Finally fixed command sync always being triggered ([ce9fdf1](https://github.com/dopaminestudios/dopamine-framework/commit/ce9fdf1ee5510649a1f77291f5029c9bdd0b0f4e))

## [v1.4.16](https://github.com/dopaminestudios/dopamine-framework/compare/vv1.4.15...vv1.4.16) (2026-02-26)
### Bug Fixes

* Fixed command sync always being triggered ([0adf0f7](https://github.com/dopaminestudios/dopamine-framework/commit/0adf0f7b76b57de9f9eae1aa471ae57c2efe2fab))

## [v1.4.15](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.14...vv1.4.15) (2026-02-19)
### Bug Fixes

* Fixed sync buttons in owner dashboard. ([2856a58](https://github.com/likerofturtles/dopamine-framework/commit/2856a58afd0d58bbf0e86351f5972542b483d5b5))

## [v1.4.14](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.13...vv1.4.14) (2026-02-18)
### Bug Fixes

* Fixed API latency cache freezing and never recovering due to waiting forever for response. (Waiting forever for a response from someone who won't ever respond, instead of moving on? Sounds a lot like my life and she- uhm sorry, where were we?) ([b865b47](https://github.com/likerofturtles/dopamine-framework/commit/b865b471599e22dceae9176d8ce9dd0d80f9a581))

## [v1.4.13](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.12...vv1.4.13) (2026-02-14)
### Bug Fixes

* Hotfix: Fixed the error: Failed to start the bot: 'Command' object has no attribute 'type' ([cf09a04](https://github.com/likerofturtles/dopamine-framework/commit/cf09a0436b0fa3a7d3a9e01db9d359eb810aad2c))

## [v1.4.12](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.11...vv1.4.12) (2026-02-14)
### Bug Fixes

* Fixed and added ability to handle message commands. ([67eff45](https://github.com/likerofturtles/dopamine-framework/commit/67eff4523c8248f069813779202f390df0831e83))

## [v1.4.11](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.10...vv1.4.11) (2026-02-14)
### Bug Fixes

* Hotfix: Updated log file button to use trailing approach because trying to send the whole file to discord just isn't working. ([9004f75](https://github.com/likerofturtles/dopamine-framework/commit/9004f75f4513305e92bcf647a2481bfc575c7f14))

## [v1.4.10](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.9...vv1.4.10) (2026-02-14)
### Bug Fixes

* Hotfix: Changed error message to followup because interaction was already responded to. ([452c6d2](https://github.com/likerofturtles/dopamine-framework/commit/452c6d25b14a14272940c3e04cd74ec4f58f61e2))

## [v1.4.9](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.8...vv1.4.9) (2026-02-14)
### Bug Fixes

* Added interaction defer for log button. ([d6a1fcf](https://github.com/likerofturtles/dopamine-framework/commit/d6a1fcf1e097571ec0768d9a63d8190130811145))

## [v1.4.8](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.7...vv1.4.8) (2026-02-14)
### Bug Fixes

* Hotfix: Fixed the error: Dopamine Framework: ERROR: Failed to read log: seek of closed file. ([0e91423](https://github.com/likerofturtles/dopamine-framework/commit/0e91423bc5b74d91db1e9b31fc57542cf541a4bf))

## [v1.4.7](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.6...vv1.4.7) (2026-02-14)
### Bug Fixes

* Fixed "show log" button only showing the first 50-60 lines of the log. ([2eb0a07](https://github.com/likerofturtles/dopamine-framework/commit/2eb0a07c59912a1083e0c73df3e12b6d8cd55018))

## [v1.4.6](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.5...vv1.4.6) (2026-02-14)
### Bug Fixes

* Fixed "error" unloading in main unloading of extensions because the extension is already manually unloaded. ([93bfdf9](https://github.com/likerofturtles/dopamine-framework/commit/93bfdf9266e82f7c19f3f9c388d9dd6c40fa3b07))
* Hotfix: Updated status and activity updater code to use new variables (bug caused by old fix) ([be6f0a8](https://github.com/likerofturtles/dopamine-framework/commit/be6f0a814400a10df7ea2e283e588d2cda029de2))

## [v1.4.5](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.4...vv1.4.5) (2026-02-14)
### Bug Fixes

* Added separate unloading for internal cogs so they don't show up mixed with user's cogs during shutdown. ([cf16529](https://github.com/likerofturtles/dopamine-framework/commit/cf16529b00300cacbc13c926b38db784665124a1))

## [v1.4.4](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.3...vv1.4.4) (2026-02-14)
### Bug Fixes

* Hotfix: Fixed shutdown and restart buttons not working in owner's dashboard. ([1ce4af9](https://github.com/likerofturtles/dopamine-framework/commit/1ce4af9aaa574ceefcdd38b1afcd34267aa600c6))

## [v1.4.3](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.2...vv1.4.3) (2026-02-14)
### Bug Fixes

* Hotfix: Fixed conflict with commands.Bot internal "status" object ([1e3f616](https://github.com/likerofturtles/dopamine-framework/commit/1e3f61619f7802221b672ac7bc49ae19d6dc2af3))

## [v1.4.2](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.1...vv1.4.2) (2026-02-13)
### Bug Fixes

* Hotfix: Added line to load the pic.py (i forgot it :sob:) ([347378b](https://github.com/likerofturtles/dopamine-framework/commit/347378b4e054c0d1d3c394017d7f3a0271ebb208))

## [v1.4.1](https://github.com/likerofturtles/dopamine-framework/compare/vv1.4.0...vv1.4.1) (2026-02-13)
### Bug Fixes

* Hotfix: Added return statements to views that got lost (shorthand for: i accidentally removed it on purpose) while porting from Dopamine. ([5866e83](https://github.com/likerofturtles/dopamine-framework/commit/5866e83f0d6902a8864d5a1450bf7eba40d874c4))

### Documentation Changes

* Centered the ticks and crosses and stuff column in the comparison table. ([2cf2f95](https://github.com/likerofturtles/dopamine-framework/commit/2cf2f956c4ce70cda50212c4680fab61ee7f101d))
* New DOCUMENTATION folder that contains documentation for devs for how to use each feature or utility. ([e358662](https://github.com/likerofturtles/dopamine-framework/commit/e358662b7cf51a411ce2df1883676892e4decb49))
* Removed redundant logging documentation from readme. ([061a342](https://github.com/likerofturtles/dopamine-framework/commit/061a3426bab9b65ecda6ddefdee6b88ea8633328))

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
