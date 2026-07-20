---
PAS ID: 3
title: Runtime Integration & Upgrade Process
status: Draft
author: Author (@educlerici_zondax)
created: 20-02-2024
---

## Changelog

| Version | Description                      | Author    | Date       |
|---------|----------------------------------|-----------|------------|
| 1.0     | Initial version                  | Edu Clerici  | 20-02-2024 |
| 1.1     | Update to PAS Repository         | Edu Clerici  |            |
| 1.2     | Include pre-approval caveats         | @al3mart  | 12-03-2024 |
| 2.0     | Pivot to integration-first model: track development branches instead of following Polkadot stable releases; Fellowship release flow retained as fallback | @paseo-team  | 20-07-2026 |


## Summary
This document outlines the standardized procedure for conducting runtime upgrades on the Paseo Testnet under Paseo's integration-first model. Rather than trailing tagged Polkadot stable releases, Paseo keeps its runtime close to the branches under active development, so that new protocol changes and the new Polkadot product suite can be exercised on the testnet as early as possible. The aim is to provide a complete integration environment while still executing upgrades smoothly, securely, and with minimal disruption.

## Abstract
This process covers all steps from the continuous integration of upstream changes, through the planning and scheduling of a runtime upgrade, to its final deployment and post-deployment monitoring on the Paseo Testnet. It reflects Paseo's role as an early integration environment that runs ahead of production release cycles.

## Motivation
Historically Paseo followed the Polkadot Fellowship stable releases and, in practice, upgraded after Kusama, using Kusama as a stability signal before enacting changes. That posture made sense while Paseo's priority was mirroring production as closely and safely as possible.

The ecosystem has since shifted from a focus on shared infrastructure toward shipping products that onboard end users. Teams increasingly need to test their integrations against upcoming protocol changes, and against the new Polkadot products, before those land in a tagged release. To serve this need, Paseo now tracks the development branches directly instead of waiting for the Fellowship to cut a release. This lets the testnet surface new features and products earlier and act as a full integration environment for the ecosystem.

The trade-off is deliberate: by running ahead of production, Paseo no longer inherits Kusama's prior validation as a safety net. Consequently, the testing performed on Paseo itself, described below, becomes the primary guarantee of runtime safety, and Paseo is expected to be more bleeding-edge and occasionally less stable than a release-following testnet would be.

## Specification

### Integration Model
- **Primary (integration-first):** the Paseo Core Team integrates changes from the relevant development branches on a rolling basis (the Polkadot SDK and Fellowship runtimes development branches, plus product branches as they are open sourced), rather than waiting for a tagged release. The objective is to make new features and products testable on Paseo as soon as they are stable enough to run.
- **Fallback (release-following):** the previous flow of deploying tagged Fellowship releases within the agreed SLO window (see PAS-12) is retained for cases where a formal release-candidate validation and status report is explicitly requested by the Fellowship. No runtime upgrades are enacted on Fridays.
- **Consequence:** because Paseo may run ahead of Kusama and Polkadot, upstream production networks can no longer be relied on as a prior validation signal. The validation steps in this document are therefore mandatory before any enactment.

## Prerequisites
- Access to the Paseo Testnet repository with necessary permissions.
- A tested and reviewed change set, whether integrated from a development branch or from a tagged release.
- Approval from the Paseo governance body or a consensus among the core development team, as per the governance model.
## Process Overview
### Preparation
1.1 Proposal Review: Ensure the runtime upgrade has been thoroughly reviewed and tested. This includes peer review of the code changes and testing in a controlled environment.

1.1.1 Leverage ecosystem tools such as [chopsticks](https://github.com/AcalaNetwork/chopsticks) and [try-runtime-cli](https://github.com/paritytech/try-runtime-cli) to get as many warranties as possible before the approval of the changes. Ideally the reviewer will use try-runtime-cli to verify the correctness of the migrations, if applicable, either pulling the state of the live network or from a local fork.
If migrations testing seems healthy the runtime upgrade should then be enacted in a local fork that should outlive the upgrade to see the following happening without problems:

- an epoch change
- an era change
- any other even affected due to a migration or the removal or inclusion of new logic.

> Even though this should be enough to warranty the safety of the runtime, this process does not assure changes requiring action from validators on their infrastructure, as in a local environment these are not present. Different measures should be taken to check these scenarios. Note that, under the integration-first model, Paseo may run ahead of Kusama and Polkadot, so upstream networks can no longer be assumed to have validated these changes beforehand. When available, a dedicated Paseo test instance (TOT, Testnet of a Testnet) should be used to validate an upgrade before it is applied to the main Paseo network.

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
- Core Team (R0GUE): Integrate upstream changes from the development branches, prepare and test the runtime upgrade, deploy it, and assist in troubleshooting post-upgrade issues.
- Validators and Providers: Update their nodes as required within the windows defined in PAS-11, and monitor the network's stability.
- Communication: Inform the community about the upgrade schedule, requirements, and status updates, using the templates in PAS-3.
## Troubleshooting
Include common issues that might arise during the upgrade process and their solutions. Provide contact information for real-time assistance.

## Appendix
- A.1 Upgrade Proposal Template: Outline the structure for upgrade proposals.
- A.2 Communication Template: Sample messages for informing the community about the upgrade phases.
- A.3 Checklist for Validators: Pre and post-upgrade checklist for validators.

## Relationship to other PAS
- **PAS-12 (Paseo as QA Environment):** PAS-12 describes the release-following QA role, where Paseo validates tagged Fellowship releases before Kusama and Polkadot. Under the integration-first model that role becomes the fallback path described above rather than the default. PAS-12 currently lists this document as replaced; that relationship needs to be reconciled so both documents describe a single, consistent release posture.
- **PAS-7 (Hardware Specs):** Reference hardware used when recalculating weights for an upgrade.
- **PAS-11 (Provider Requirements):** Node update requirements and the emergency upgrade window for providers.

## Copyright
Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
