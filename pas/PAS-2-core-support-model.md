---
PAS: 2
title: Core Support Model
status: Open
author: Edu Clerici (@educlerici-zondax)
created: 23-02-2024
---

## Changelog

| Version | Description                      | Author    | Date       |
|---------|----------------------------------|-----------|------------|
| 1.0     | Initial version                  | Edu Clerici  | 23-02-2024 |
| 1.1     | ...                              |              |            |



## Summary
The purpose of operating and maintaining the Paseo testnet is to cater to the needs of various stakeholders in the ecosystem. These include:

- Parachains
- Wallets
- API Builders
- Validators
- Custodians
  
## Abstract
A short description of the proposed change, this should clearly describe the proposed change that will happen if this PAS is passed rather than why it should be done or the detail behind how to complete the changes. 


## Documentation

- **Internal Processes** : Documenting standard operating procedures, workflows, and best practices for the team.
- **Basic Tutorials** : Creating guides for new users and stakeholders to engage with Paseo Network.
- **Design Decision Documentation** : Recording rationales behind significant design decisions for transparency and future reference.
- **Parameter Change Documentation:** Keeping track of any changes made to the network's parameters, ensuring they're well-documented and justified.

## Coordination Meetings

- **Weekly Internal Report every Thursday** : A routine meeting to discuss progress, challenges, and plan for the upcoming week. The meeting must be documented in a Google Docs Shared where all the team can be aligned regarding the insights from the team.

## Community Management

- **Bridge Management** (_Platforms: Element, Discord - TBD_): Choosing and maintaining communication platforms for effective interaction with the community.
- **Paseo's GitHub Organization Maintenance** : Overseeing the GitHub repository, ensuring it's up-to-date and well-organised.
- **Element Channels** : Managing various channels with different topics, such as:
  - **Public** : Public channel to share every update and news to the complete community
  - **Tech** : Developer coordination channel and other Support channel for efficient communication and collaboration between them.
  - **Management Channels** : Specialised channels for internal and core team discussions.

## Social Media Management

- **X Account** : Engaging with the community, sharing updates, and announcements.
- Other Social Media Updates (_Weekly. Optional_): Regular updates across different platforms to keep the community informed.

## Monitoring

- Validator Monitoring (Service Level Agreements): Ensuring validators operate within agreed-upon standards and parameters.
- Bot Development:
  - Large Balance Monitoring: Keeping track of significant balance changes in the network.
  - OpenGov Monitoring: Monitoring governance activities and proposals.

## Runtime Management

- **Track, Add, Remove Pallets** : Managing the components of the runtime environment to ensure optimal performance.
- **Runtime Upgrades** : Establishing a timeline (TBD) and process for upgrading the network.
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

Support tasks that are **not** in the scope:
- Analyze parachain failed storage migrations.
- Check parachain configuration.
- Check parachain node logs.
- **XCM HRMP Channels Management for System Chains** : Handling cross-consensus message passing channels for any Paseo System chain.
- **XCM Debugging for Parachain Support** : Troubleshooting and supporting parachain-related issues.
- **Parachain Slot Assignment:** Managing the allocation of slots to parachains.
- **Benchmarking** : Recalculate weights for every Runtime upgrade, taking into account different hardware configurations from Polkadot.
- **Building Deterministic Runtime Artifacts** : Ensuring the runtime is predictable and repeatable.
**Coretime:** Lead migration from parachain slots into coretime sales. Also once we have more details about coretime, a proper process for handling core assigments will be put in place.

## Supported System Chains**
Ensuring these specific chains are supported and integrated within Paseo.

- Assethub
- Bridgehub
- People
- Coretime
- Collectives

## Service Level Agreement (Support)

The workflow to acknowledge and resolve support tickets within specified time frames will be the following.

- Support Ticket Handling
  - **Acknowledgment** : Within 24 hours.
  - **Resolution** : Mean time of 72 hours (_varies based on complexity and triage_)
 
Support tickets that are **not** in the scope for the SLA:
- every ticket that has the "Core" label on it.

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

## Coordination Meetings

- Weekly every Tuesday: Core Team Meeting
- Weekly every Thursdays: Internal Weekly Report
- Monthly TBD: Fellowship Coordination

## Reporting

Provide regular updates to stakeholders and the community in different formats.

- **Weekly Updates** : Written summary about what update was done during the week.
- **Monthly Reporting** :Written Blog Format summary about what happened during the current month.


## Copyright
Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
