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
| 1.1     | Improvement                              | Portico Labs  | 03-09-2025 |


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
The official communication and coordination channel for Paseo providers is the Matrix room: [Paseo [Core & Infra] - Internal](https://matrix.to/#/#polkadot-community-testnet:parity.io). Providers are required to respond to any comments, questions, or requests when the room is tagged (`@room`) or when they are specifically mentioned (e.g., in weekly reports highlighting validators with below-expected performance) **within 72 hours once the communication was sent.**

### Node Versions
All nodes (validators, collators, and RPC nodes) **must run the latest node version, or at minimum, the previous version**. In the event of an emergency upgrade, providers must update their nodes **within 48 hours** of the request.

**Failure to meet this criterion will result in the complete loss of compensation for the affected node(s).**
