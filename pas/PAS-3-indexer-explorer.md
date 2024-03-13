---
PAS: 3
title: Indexer Explorer
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
This PAS proposes the adoption of TopMonks' Calamar, a robust indexer/explorer solution, for the paseo-network. The integration of this tool aims to enhance the network's transparency, accessibility, and user experience by providing an efficient way to query and visualize on-chain data.

## Abstract
An indexer/explorer is crucial for blockchain networks, offering users and developers a user-friendly interface to interact with the blockchain, search transactions, blocks, and addresses, and monitor network activity. The choice of an effective indexer/explorer is pivotal for ensuring network transparency and usability.

## Proposal
**Calamar Indexer/Explorer**
After evaluating several options, we propose the implementation of Calamar, developed by TopMonks. Key features and considerations include:


- Open Source: Calamar is an open-source project, allowing for customization and community contributions.
- Rich Feature Set: It offers comprehensive features for searching and visualizing blockchain data, including transactions, blocks, addresses, and various network metrics.
- Compatibility: Assessment of compatibility with paseo-network's blockchain architecture.
- Performance: Calamar's performance in terms of speed, reliability, and scalability.
- Community Support: Evaluate the level of ongoing support and development activity in the Calamar community.

## Implementation Plan
- Initial Setup: Configure and deploy Calamar in a test environment for paseo-network.
- Integration Testing: Rigorous testing to ensure compatibility and performance meet our network's requirements.
- Customization: Make necessary customizations to tailor Calamar to paseo-network's specific needs.
- Community Feedback: Engage with the paseo-network community for feedback and suggestions.
- Deployment: Once testing and customizations are complete, deploy Calamar as the official indexer/explorer for paseo-network.

### Detailed Calamar Setup
According to Calamar documentation, there are several data sources to feed the explorer. Some of them are mandatory, while others are optional. There are four possible data sources to use:

**FireSquid archive**
- Runtime spec metadata
- Extrinsic & event args
- Data about blocks, extrinsics, calls and events if GS explorer is not set up

**GiantSquid explorer**
- Data about blocks, extrinsics, calls and events except extrinsic & event args.
- Better optimized search
- Search by extrinsic/event name.
- Data about account's calls.

**GiantSquid main**
- Data about transfers
- Data about account identities if provided

**GiantSquid stats**
- Data about network's stats (in network detail page)
- Data about network's top holders
- Data about account's balances


For more information about them, the official documentation can be found [here](https://github.com/topmonks/calamar/wiki/Data-sources). We propose to implement all of them, in different phases:

**First phase**
- FireSquid archive (Required)

**Second phase**
- GiantSquid explorer (Optional, but highly recommended)


**Third phase**
- GiantSquid main (Optional)
- GiantSquid stats (Optional)

## Goals

- Enhanced User Experience: Providing a user-friendly interface for network interaction and data exploration.
- Increased Transparency: Making on-chain data easily accessible and understandable to users.
- Community Engagement: Encouraging community involvement in improving and maintaining the indexer/explorer.

## Copyright
Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
