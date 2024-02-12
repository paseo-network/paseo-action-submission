### Introduction

It seems reasonable that being Paseo a community testnet not a single party has to make all the efforts of maintaining this platform. At the same time, moving away from a single operator should not compromise the availablity of the network.

This RFC talks about how different infrastructure providers can support Paseo network.

### Background

Different members of the Polkadot ecosystem have expressed interest to participate in this initiative. A selection criteria is necessary to don't compromise the network while allowing as many parties as possible. 

Infrastructure providers can run validators following the information detailed in [#20](https://github.com/paseo-network/paseo-rfcs/issues/20).

### Proposal

Interested infrastructure providers (referred as _Contributor_ or _the contributor_ from here on) should open a PR in this repository and label is as `infra onboarding`.

In this PR they should create a file as described in [#20](https://github.com/paseo-network/paseo-rfcs/issues/20):

```bash
paseo-rfcs
└── paseo-validators
     ├── existing-infra-prov.yml
     └── <your-team-name>.yml
```
This file should, at least, contain the identity of the contributor.

The **election criteria** is:

- Contributor is part of [Polkadot 1KV Programme](https://wiki.polkadot.network/docs/thousand-validators).
- Contributor maintains an invulnerable collator for a system chain for a parachain connected to either, Kusama or Polkadot.

> At least one of the above statements needs to be true.

A proof of ownership of the onchain account is required in case the contributor is elegible because of its on-chain activity. This can be provided by signing the following text so it can be verified with your validator's on-chain public account:

```bash
PASEO
```

Using the same keypair might be a good idea in this scenario.

Once approved the contributor will be able to run `1` validator.

Approved contributors will be elegible for compensation and the inclusion of more validators after their services have been running for a month time period, during which the following metrics will be monitored:

- Uptime
- Performance
- Maintenance