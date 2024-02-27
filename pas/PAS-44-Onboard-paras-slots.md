---
PAS: 0044
title: Onboarding Parachains - Slots
status: Proposed
author: Alejandro (@al3mart)
created: 27-02-2024
---

Please use this template when creating a new PAS. Note that a PAS number will need to be manually assigned by the author. 
When creating a PR for your PAS, please use an abbreviated title in the filename, PAS-draft_title_abbrev.md. The title should be 44 characters or less.

## Summary
Means to onboard a parachain to Paseo via **leases and slot assingment**.
This PAS is to be deprecated once parachain scheduling via coretime is deployed in Paseo.

## Abstract
In this document users can find the steps to follow to register their parachain in Paseo.
- Maintainers of a live parachain in Polkadot or Kusama will be granted a slot in Paseo with no expiration date.
- Maintainers of parachains in development, or those that have not yet secured a slot in Kusama or Polkadot, will be assigned a lease for a shorter period of time.

## Motivation
At the moment of writing there is no way a user without access to root origin can get their parachain's block finalised by Paseo.

## Specification
### Overview

Users can do a regular registration via dispatching the extrinsics `registrar.reserve` to reserve a `ParaId` and `registrar.register` to submit their code and state. 
To obtain a slot for your parachain, aka upgrading your parathread to a parachain, users can log an issue in [Paseo's support repository](https://github.com/paseo-network/support) for what they can use the custom issue tempalte in https://github.com/paseo-network/support/issues/new/choose.
This might be handy in case the root action is needed in the relay chain, for instance.
Users can always open an issue in case their desired `ParaId` is < `4000`.
Resources will be assigned as long as the network is not at capacity. This depends on the number of validators supporting the network.
For this test environment we work with the assumtion that there should always be at least 2 validators per parachain running in the network.

_If you are willing to support the network, please see [PAS#1](https://github.com/paseo-network/paseo-action-submission/blob/main/pas/PAS_ID1_onboard_infrastructure_providers.md).

### Rationale

The onboarding process is bounded by the resources available in the network. Meaning that we will prioritize parachains that are already live and need a testbed for their users, while trying to
maintain a healthy ratio of teams that just need sporadic resources from Paseo.
Teams having secured a slot in either Kusama or Polkadot will receive leases for the duration of **1 year**.
Teams that have not yet secured a slot in the above mentioned relay chains, will receive leases for at most **two continued weeks** at a time.

## Copyright
Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
