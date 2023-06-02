# detahard Firmware documentation

_This documentation can also be found at [docs.detahard.io](https://docs.detahard.io) where it is available in a HTML-built version compiled using [mdBook](https://github.com/rust-lang/mdBook)._

Welcome to the detahard Firmware repository. This repository is so called _monorepo_, it contains several different yet very related projects that together form the detahard Firmware ecosystem.

## Repository Structure

* **[`ci`](https://github.com/detahard/detahard-firmware/tree/master/ci/)**: [Gitlab CI](https://gitlab.com/satoshilabs/detahard/detahard-firmware) configuration files
* **[`common/defs`](https://github.com/detahard/detahard-firmware/tree/master/common/defs/)**: JSON coin definitions and support tables
* **[`common/protob`](https://github.com/detahard/detahard-firmware/tree/master/common/protob/)**: Common protobuf definitions for the detahard protocol
* **[`common/tools`](https://github.com/detahard/detahard-firmware/tree/master/common/tools/)**: Tools for managing coin definitions and related data
* **[`core`](https://github.com/detahard/detahard-firmware/tree/master/core/)**: detahard Core, firmware implementation for detahard T
* **[`crypto`](https://github.com/detahard/detahard-firmware/tree/master/crypto/)**: Stand-alone cryptography library used by both detahard Core and the detahard One firmware
* **[`docs`](https://github.com/detahard/detahard-firmware/tree/master/docs/)**: Assorted documentation
* **[`legacy`](https://github.com/detahard/detahard-firmware/tree/master/legacy/)**: detahard One firmware implementation
* **[`python`](https://github.com/detahard/detahard-firmware/tree/master/python/)**: Python [client library](https://pypi.org/project/detahard) and the `detahardctl` command
* **[`storage`](https://github.com/detahard/detahard-firmware/tree/master/storage/)**: NORCOW storage implementation used by both detahard Core and the detahard One firmware
* **[`tests`](https://github.com/detahard/detahard-firmware/tree/master/tests/)**: Firmware unit test suite
* **[`tools`](https://github.com/detahard/detahard-firmware/tree/master/tools/)**: Miscellaneous build and helper scripts
* **[`vendor`](https://github.com/detahard/detahard-firmware/tree/master/vendor/)**: Submodules for external dependencies


## Contribute

See [CONTRIBUTING.md](https://github.com/detahard/detahard-firmware/tree/master/CONTRIBUTING.md).

Also please have a look at the docs, either in the `docs` folder or at  [docs.detahard.io](https://docs.detahard.io) before contributing. The [misc](misc/index.md) chapter should be read in particular because it contains some useful assorted knowledge.

## Security vulnerability disclosure

Please report suspected security vulnerabilities in private to [security@satoshilabs.com](mailto:security@satoshilabs.com), also see [the disclosure section on the detahard.io website](https://detahard.io/security/). Please do NOT create publicly viewable issues for suspected security vulnerabilities.

## Note on terminology

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).
