---
PAS: 7
title: Hardware Specs
status: Open
author: Edu Clerici (@educlerici-zondax)
created: 23-02-2024
---

## Validators and Collators

These hardware specs takes as a reference the Polkadot hardware specs listed [here](https://wiki.polkadot.network/docs/maintain-guides-how-to-validate-polkadot#requirements). The initial group supporting Paseo Network decided to set the 1/2 of the resources needed for Polkadot (except the storage which much less than 1TB is needed).

### Hardware specs details:

- CPU
  - x86-64 compatible;
  - Intel Ice Lake, or newer (Xeon or Core series); AMD Zen3, or newer (EPYC or Ryzen);
  - **2 physical cores** @ 3.4GHz;
  - Simultaneous multithreading disabled (Hyper-Threading on Intel, SMT on AMD);
  - Prefer single-threaded performance over higher cores count. A comparison of single-threaded performance can be found [here](https://www.cpubenchmark.net/singleThread.html).
- Storage
  - An NVMe SSD of **200 GB** (As it should be reasonably sized to deal with blockchain growth). An estimation of current chain snapshot sizes can be found [here](https://stakeworld.io/docs/dbsize). In general, the latency is more important than the throughput.
- Memory
  - **16 GB** DDR4 ECC.
- System
  - Linux Kernel 5.16 or newer.
- Network
  - The minimum symmetric networking speed is set to 500 Mbit/s (= 62.5 MB/s). This is required to support a large number of parachains and allow for proper congestion control in busy network situations

