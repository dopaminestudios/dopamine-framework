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

## [1.1.1](https://github.com/likerofturtles/dopamine-framework/compare/v1.1.0...v1.1.1) (2026-02-12)


### Bug Fixes

* sync callbacks now use the return statement so that errors can be shown (if any) instead of hard-coded success response. ([e85b752](https://github.com/likerofturtles/dopamine-framework/commit/e85b752643fe94ec0fedf3e194d57d4dfcf26814))
