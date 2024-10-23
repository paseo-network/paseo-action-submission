---
PAS: 9
title: Onboarding Parachains - Slots
status: Proposed
author: Alejandro (@al3mart)
created: 27-02-2024
---

## Changelog

| Version | Description                      | Author    | Date       |
|---------|----------------------------------|-----------|------------|
| 1.0     | Initial version                  | @al3mart  | 12-03-2024 |
| 2.0     | Coretime                  | @hbulgarini  | 12-03-2024 |

## Summary
Means to onboard a parachain to Paseo via **coretime**.

## Abstract
In this document users can find the steps to follow to register their parachain in Paseo.
- Maintainers of a live parachain in Polkadot or Kusama will be granted enough funds to renew their core in Paseo for 1 year long.
- Maintainers of parachains in development, or those that have not yet secured a slot in Kusama or Polkadot will receive funds to buy a core only for a shorter period of time: 2 weeks long. If the demand allows it (and is our the Paseo core team expectations), these teams will have the chance to renew their core for longer period.
- If there are no cores available for sell, the parachains can use the available on-demand core.

## Motivation
At the moment of writing there is no way a user without access to root origin can get their parachain's block finalised by Paseo.

## Specification
### Overview

Users can do a regular registration via dispatching the extrinsics `registrar.reserve` to reserve a `ParaId` and `registrar.register` to submit their code and state. 
To obtain a enough funds for buying the core for your parachain, users can log an issue in [Paseo's support repository](https://github.com/paseo-network/support) for that, they can use the custom issue template in https://github.com/paseo-network/support/issues/new/choose.
This might be handy in case the root action is needed in the relay chain, for instance.
Users can always open an issue in case their desired `ParaId` is < `4000`.
Resources will be assigned as long as the network is not at capacity. This depends on the number of validators supporting the network.
For this test environment we work with the assumption that there should always be at least 3 validators per parachain running in the network.

_If you are willing to support the network, please see [PAS#1](https://github.com/paseo-network/paseo-action-submission/blob/main/pas/PAS_ID1_onboard_infrastructure_providers.md).

### Rationale

The onboarding process is bounded by the resources available in the network. Meaning that we will prioritize parachains that are already live and need a testbed for their users, while trying to
maintain a healthy ratio of teams that just need sporadic resources from Paseo.

## Copyright
Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
