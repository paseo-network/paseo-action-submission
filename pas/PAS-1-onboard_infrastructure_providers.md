---
PAS ID: 1
title: Onboard Infraestructure Provider
status: Draft
author: Alejandro Martinez (@al3mart)
created: 15-02-2024
---

## Changelog

| Version | Description                      | Author    | Date       |
|---------|----------------------------------|-----------|------------|
| 1.0     | Initial version                  | @al3mart  | 15-02-2024 |
| 1.1     | Adding System Parachains and new structure | @hbulgarini | 27-02-2024            |
| 1.2     | Misleading criteria                  | @al3mart  | 05-03-2024 |


## Summary

Paseo is a decentralised community testnet, we want to open the opportunity for infrastructure providers in the ecosystem to contribute to the success and scaling of the network.
This PAS (PAS) discusses about how different infrastructure providers can join and contribute to the Paseo network.

## Abstract

Many individuals and companies that provide infrastructure in the Polkadot ecosystem have expressed interest to participate in Paseo. A selection criteria is necessary to ensure high standards which avoid compromises or downtime to the network, while allowing as many parties as possible.


## Specification
### Proposal

Interested infrastructure providers (referred as _Contributor_ or _the contributor_ from here on) should open a PR in this repository and label it, `infra-onboarding` . If the contributor is submitting a validator also add the tag `new-validator` or in the case of system parachain collators, add the tag `new-system-collator`

## Validators

In the PR submission, contributors should create in the location specified below, the corresponding file starting from this template: (https://github.com/paseo-network/paseo-action-submission/blob/main/paseo-validators/active/example.yml):

```bash
paseo-rfcs
└── paseo-validators
     ├── active
          ├── existing-validators.yml
          └── <your-team-name>.yml
```

## System Parachain Collators

Same as validators, in the PR submission, contributors should create in the location specified below, the corresponding file starting from this template: (https://github.com/paseo-network/paseo-action-submission/blob/main/paseo-system-parachain/active/example.yml):

```bash
paseo-rfcs
└── paseo-system-parachain-collators
     ├── active
          ├── existing-collators.yml
          └── <your-team-name>.yml
```

This file should, at least, contain the identity of the contributor.

## Selection Criteria

The **selection criteria** is:

- Contributor is part of the [Polkadot 1KV Programme](https://wiki.polkadot.network/docs/thousand-validators).
- Contributor maintains an invulnerable collator for a system chain for a parachain connected to either, Kusama or Polkadot.
- They have introduced themselves in [Paseo's public Element channel](https://matrix.to/#/#paseo-testnet-support:parity.io) or at `#paseo-testnet` room in [Polkadot's offical Discord server](https://discord.gg/polkadot).

A proof of ownership of the onchain account is required in case the contributor is elegible because of its on-chain activity. This can be provided by signing the following text so it can be verified with your validator's on-chain public account:

```bash
PASEO
```

Using the same keypair might be a good idea in this scenario.


## Evaluation  period
Once approved the contributor will be able to run `1` system parachain collator.

Approved contributors will be elegible for compensation and the inclusion of more validators/system parachain collators after their services have been running for a month time period, during which the following metrics will be monitored:

- Uptime
- Performance
- Maintenance

The definition of said metrics as well as the minimum accepted values will be defined in a different PAS(PAS).
