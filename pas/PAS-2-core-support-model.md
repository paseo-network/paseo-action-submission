---
PAS: 2
title: Core Support Model
status: Open
author: paseo-team
created: 23-02-2024
---

## Changelog

| Version | Description                      | Author    | Date       |
|---------|----------------------------------|-----------|------------|
| 1.0     | Initial version                  | Edu Clerici  | 23-02-2024 |
| 1.1     | Coretime update                  |  @al3mart   | 24-10-2024  |
| 1.2     | Restructuring update: stakeholders, abstract, community/monitoring, system chains, region-based assignment, SLO alignment, removed obsolete sections | paseo-team | 20-07-2026 |



## Summary
The purpose of operating and maintaining the Paseo testnet is to cater to the needs of various stakeholders in the ecosystem. These include:

- Parachains
- Ecosystem product teams
- Wallets
- API Builders
- Validators

## Abstract
This document defines the operational support model for the Paseo testnet. It describes the responsibilities, processes, and communication channels through which the Paseo Core Team keeps the network running and supports the teams building on it.


## Documentation

- **Internal Processes** : Documenting standard operating procedures, workflows, and best practices for the team.
- **Basic Tutorials** : Creating guides for new users and stakeholders to engage with Paseo Network.
- **Design Decision Documentation** : Recording rationales behind significant design decisions for transparency and future reference.
- **Parameter Change Documentation:** Keeping track of any changes made to the network's parameters, ensuring they're well-documented and justified.

## Community Management

- **Bridge Management** (_Platforms: Element/Matrix and the official Polkadot forum: https://forum.polkadot.network/_): Choosing and maintaining communication platforms for effective interaction with the community.
- **Paseo's GitHub Organization Maintenance** : Overseeing the GitHub repository, ensuring it's up-to-date and well-organised.
- **Element Channels** : Managing various channels with different topics, such as:
  - **Public** : Public channel to share every update and news to the complete community
  - **Tech** : Developer coordination channel and other Support channel for efficient communication and collaboration between them.
  - **Management Channels** : Specialised channels for internal and core team discussions.

## Monitoring

- Staking and validator data is sourced from the Turboflakes Paseo portal.
- Additional monitoring processes are being developed in the Paseo Dashboard, maintained by R0GUE: https://polkadot-testnet.r0gue.io/network

## Runtime Management

- **Track, Add, Remove Pallets** : Managing the components of the runtime environment to ensure optimal performance.
- **Runtime Upgrades** : The runtime upgrade and integration process is defined in PAS-3 (Runtime Upgrade). Paseo tracks the development branches to surface new features and products early, rather than following tagged releases.
- **Pallet Configuration Analysis** : Assessing whether new or existing pallet configurations align with Paseo's requirements.

## Runtime Upgrade Testing and Coordination

- **Local Dry-Runs with Live State** : Testing upgrades in a controlled environment to ensure stability.
- **Backporting** : Applying new features or fixes from the mainnet to the testnet.
- **Bricked Parachains Resolution** : In case of malfunctioning parachains the team will provide the corresponding support from the relay chain perspective. Below there are more details about support tasks scope:

Support tasks that are within the scope:
- Force Storage Items for parachains (including runtime storage item)
- Remove parachain locks
- Dmp queues that usually come from forcing wasm changes force the parachains
- Force lifecycle upgrades
- Top up balances for sovereign accounts
- XCM HRMP Channels Management for System Chains: Handling cross-consensus message passing channels for any Paseo System chain.
- XCM Debugging for Parachain Support: Troubleshooting and supporting parachain-related issues from the relay chain or system chain perspective.
- Region and Task Assignment: Tasks (parachains) are assigned to regions based on demand. At present, a region is backed by a single core and holds a maximum of 6 tasks.
- Benchmarking : Recalculate weights for every Runtime upgrade, taking into account different hardware configurations from Polkadot.
- Building Deterministic Runtime Artifacts: Ensuring the runtime is predictable and repeatable.
- Core and Region Administration: Assign tasks to regions and cores as needed to maintain the finalization of the chains connected to Paseo. Core allocation is managed directly by administrators with sudo access rather than through market-based Coretime sales.

Support tasks that are **not** in the scope:
- Analyze parachain failed storage migrations.
- Check parachain configuration.
- Check parachain node logs.

## Supported System Chains**
Ensuring these specific chains are supported and integrated within Paseo.

- Assethub
- People
- Bulletin

## Support Response

General support response is governed by the Service Level Objectives (SLOs) approved in the latest Paseo governance proposal, which define the coverage windows and the acknowledgment and mitigation targets. Refer to the current proposal for the applicable SLO definitions.

Tickets labeled "Core" fall outside the general support flow and are handled through the runtime and core administration processes.

## High-Level Process Description

- Documentation Management:
  - Wiki
  - Processes
  - Mini-Tutorials ([https://github.com/paseo-network/support](https://github.com/paseo-network/support))

- Documentation Pull Requests
  - **Review changes to documentation** : Regularly reviewing changes made to documentation ensures that updates align with current processes and standards, maintaining the integrity of the knowledge base.
  - **Update Technical documentation** : Team members are responsible for keeping technical documentation up-to-date, reflecting the latest features, configurations, and troubleshooting steps.

- Issue Management
  - **Daily Support Triage** : Daily updates englobe communicating key information, achievements, or notable events to the public. This includes marketing efforts and maintaining effective communication over element, discord, X, etc.

  - **Weekly Escalation Process:** Monthly reporting involves summarizing significant events, blog posts, or achievements. It provides a holistic view of the team's activities and contributions to Paseo.

## Reporting

Provide updates to stakeholders and the community in different formats, without fixed time commitments.

- **Written Updates** : Summaries of the work done, shared periodically.
- **Blog / Forum Reporting** : Longer-form summaries published on the Polkadot forum as relevant.


## Copyright
Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
