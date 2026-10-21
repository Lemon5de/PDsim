# Changelog

All notable changes to **PDSim** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2026-10-04

### Changed
- Refactored physical correction logic to improve differential drive response accuracy.
- Removed arbitrary/faulty physics calculations in favor of scaled PWM differential offsets.

## [1.1.0] - 2026-09-26

### Changed
- Adjusted simulation measurement units for line offset tracking.

## [1.0.0] - 2026-09-19

### Added
- Initial release of the PD loop line-follower robot simulator.
- Interactive CLI prompt for $K_p$, $K_d$, base PWM speed, initial offset, and simulation duration.
- Real-time tabular logging for simulation time, robot position, error, correction force, and individual wheel PWM outputs.