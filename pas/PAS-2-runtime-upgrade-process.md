---
PAS ID: 2
title: Runtime Upgradte
status: Open
author: Author (@educlerici_zondax)
created: 20-02-2024
---

## Changelog

| Version | Description                      | Author    | Date       |
|---------|----------------------------------|-----------|------------|
| 1.0     | Initial version                  | Edu Clerici  | 20-02-2024 |
| 1.1     | Update to PAS Repository         | Edu Clerici  |            |


## Summary
This document outlines the standardized procedure for conducting a runtime upgrade on the Paseo Testnet. It aims to ensure that upgrades are executed smoothly, securely, and with minimal network disruption.

## Abstract
This process covers all steps from the initial planning and scheduling of a runtime upgrade to its final deployment and post-deployment monitoring on the Paseo Testnet.

## Specification
## Prerequisites
- Access to the Paseo Testnet repository with necessary permissions.
- A tested and reviewed runtime upgrade proposal.
- Approval from the Paseo governance body or a consensus among the core development team, as per the governance model.
## Process Overview
### Preparation
1.1 Proposal Review: Ensure the runtime upgrade has been thoroughly reviewed and tested. This includes peer review of the code changes and testing in a controlled environment.
1.2 Communication Plan: Prepare a communication plan to inform validators, developers, and users about the upcoming upgrade, including timelines and expected actions.

### Scheduling
2.1 Determine Upgrade Window: Choose a time for the upgrade that minimizes impact on network users. Consider different time zones and network activity patterns.
2.2 Notify Stakeholders: Use the communication plan to notify all stakeholders of the scheduled upgrade time. Provide detailed instructions for validators and users, if any actions on their part are required.
### Execution
3.1 Final Checks: Perform last-minute checks and ensure all stakeholders are prepared for the upgrade.
3.2 Deploy Upgrade: Execute the runtime upgrade using the agreed-upon method (e.g., Sudo, Democracy proposal, or other governance mechanisms).
3.3 Monitor Deployment: Closely monitor the network for any unexpected behavior as the upgrade takes effect.
### Validation
4.1 Verify Upgrade Success: Confirm that the new runtime is operating as expected. Check block production, transaction processing, and other critical network functions.
4.2 Stakeholder Feedback: Gather feedback from validators, developers, and users to ensure the upgrade has not introduced any unforeseen issues.
### Post-Deployment
5.1 Update Documentation: Ensure all relevant documentation is updated to reflect the new runtime features or changes.
5.2 Communicate Completion: Inform all stakeholders that the upgrade has been successfully completed and the network is stable.
5.3 Review Process: Conduct a post-upgrade review to identify any issues or improvements for future upgrades.
## Roles and Responsibilities
- Core Developers: Prepare the runtime upgrade, perform testing, and assist in troubleshooting post-upgrade issues.
- Validators: Update their nodes as required and monitor the network's stability.
- Communication Team: Inform the community about the upgrade schedule, requirements, and status updates.
## Troubleshooting
Include common issues that might arise during the upgrade process and their solutions. Provide contact information for real-time assistance.

## Appendix
- A.1 Upgrade Proposal Template: Outline the structure for upgrade proposals.
- A.2 Communication Template: Sample messages for informing the community about the upgrade phases.
- A.3 Checklist for Validators: Pre and post-upgrade checklist for validators.

## Copyright
Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
