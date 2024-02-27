### Introduction

Paseo is a decentralized community testnet, we want to open the opportunity for infrastructure providers in the ecosystem to contribute to the success and scaling of the network.

This PAS (PAS) discusses about how different infrastructure providers can join and contribute to the Paseo network.

### Background

Many individuals and companies that provide infrastructure in the Polkadot ecosystem have expressed interest to participate in Paseo. A selection criteria is necessary to ensure high standards which avoid compromises or downtime to the network, while allowing as many parties as possible.


### Proposal

Interested infrastructure providers (referred as _Contributor_ or _the contributor_ from here on) should open a PR in this repository and label it, `collator-onboarding`.

In this PR, the contributor should create a file as described in [#20](https://github.com/paseo-network/paseo-action-submission/blob/main/paseo-system-parachain/example.yml):

```bash
paseo-rfcs
└── paseo-system-parachain
     ├── active
        ├── existing-collators.yml
        └── <your-team-name>.yml
```
This file should, at least, contain the identity of the contributor.

The **selection criteria** is:

- Contributor is part of the [Polkadot 1KV Programme](https://wiki.polkadot.network/docs/thousand-validators).
- Contributor maintains an invulnerable collator for a system chain for a parachain connected to either, Kusama or Polkadot.

> At least one of the above statements needs to be true.

A proof of ownership of the onchain account is required in case the contributor is elegible because of its on-chain activity. This can be provided by signing the following text so it can be verified with your validator's on-chain public account:

```bash
PASEO
```

Using the same keypair might be a good idea in this scenario.

Once approved the contributor will be able to run `1` system parachain collator.

Approved contributors will be elegible for compensation and the inclusion of more system parachain collators after their services have been running for a month time period, during which the following metrics will be monitored:

- Uptime
- Performance
- Maintenance

The definition of said metrics as well as the minimum accepted values will be defined in a different PAS(PAS).