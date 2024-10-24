---
PAS ID: 10
title: Onboarding Parachains - Coretime
status: Proposed
author: Alejandro (@al3mart)
created: 24-10-2024
---

## Changelog

| Version | Description                      | Author    | Date       |
|---------|----------------------------------|-----------|------------|
| 1.0     | Initial version                  | Alejandro/Hector  | 24-10-2024 |


## Summary
Means to onboard a parachain to Paseo via **coretime** assignment.

[- Overview section details how to obtain coretime](#overview)

[- Rationale section details the expected onboarding flow](#rationale)

[- Fast forward an onboarding as detailed in the support section](#support)

## Abstract
In this document users can find the steps to follow to register their parachain in Paseo.

## Motivation
Allocation of resources that imply a cost and can be accessed by obtaining tokens that are freely available to everyone and have no intrinsic value.

## Specification
### Overview
While the registration process stays the same. A combination of `registrar.reserve` and `registrar.register` calls.
Agile Coretime introduces new methods for users to have the relay chain finalize blocks produced by connected chains.

- On demand Coretime: Allows users to place a bid to have the next produced block finalized, and only one block.
- Bulk Coretime: Allows users to acquire a fixed duration of continuous relay chain coretime.

Users can place a bid to obtain on demand coretime directly in the relay chain.
While for obtaining bulk coretime users will need to interface with the broker, hosted in the coretime chain. The broker will offer a certain number of cores available for sale periodically. Which users can obtain and assign to their chains if they so choose, if now assigned these are also transferable.

The following resources contain details on how to interact with these features:
- Polkadot Wiki: https://wiki.polkadot.network/docs/learn-agile-coretime-index
- W3F Educhain: https://web3educhain.xyz/

Ecosystem applications featuring coretime management:
- RegionX: https://app.regionx.tech/?network=paseo


### Rationale
The onboarding process is bounded by the resources available in the network. Meaning that parachains that are already live and need a testbed for their users will be the priority, while trying to
maintain a healthy ratio of teams that just need sporadic resources from Paseo.

The expected flow for teams to onboard is the following:

- Open a parachain onboarding issue in the Paseo support repository:
https://github.com/paseo-network/support/issues/new?assignees=al3mart%2Chbulgarini%2Ceduclerici-zondax&labels=onboard-para&projects=&template=onboard-parachain.yaml&title=%5BParachain+Onboarding+%7C+Slot+Request%5D+ParaId%3A+%3Cyour_paraId%3E

- Once the core team has proceed with the parachain registration and enough balance was transfer to the parachain manager account, a core could be acquired following this documentation: https://wiki.polkadot.network/docs/learn-guides-coretime-parachains


Note: If a chain is being migrated from a different testing environment or it is running in production and needs to use Paseo, contact the team, who can help you with the registration process.

### Support

- If there are no cores available or any other issue is faced, please escalate the issue on the same parachain onboarding, please contact the team at:

- https://matrix.to/#/#paseo-testnet-support:parity.io

## Copyright
Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
