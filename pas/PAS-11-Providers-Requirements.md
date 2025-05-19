---
PAS: 11
title: Paseo Node Providers Requirements
status: Open
author: Portico Labs
created: 19-05-2025
---
## Changelog

| Version | Description                      | Author    | Date       |
|---------|----------------------------------|-----------|------------|
| 1.0     | Initial version                  | Portico Labs  | 19-05-2025 |
| 1.1     | ...                              |              |            |


## Summary
This PAS proposes defines the new requirements for the Paseo node providers, meaning validators and system chain collators, as well as RPC infrastructure. 

## Requirements

### Grafana and Telemetry Connection
100% of nodes are connected to Grafana and telemetry, providing all the logs and metrics to the following sites:

Telemetry: https://telemetry.polkadot.io/#list/0x77afd6190f1554ad45fd0d31aee62aacc33c6db0ea801129acb813f913e0764f
Grafana: http://grafana.paseo.site/

### Validator Performance Requirement
The validators should reach at least 80% of score (B grade) of validating performance for the whole quarter according to the metrics provided by the Turboflake portal:

https://apps.turboflakes.io/?chain=paseo#/insights

**Exception Policy for Outages**:In case any provider suffers an outage or any service disruption, the exception could be applied if the issue is communicated proactively by the provider and they maintain active communication with the core group.

### Communication Response Time
To ensure timely coordination and smooth progress on technical matters, the provider is expected to respond to a direct message or a tag in the Core & Infra channel within 72 hours of being contacted```

### Node Versions
Nodes must be upgraded to the latest stable release within one week of its official availability.
