# detahard Firmware


## Repository Structure

* **[`ci`](ci/)**: [Gitlab CI](https://gitlab.com/satoshilabs/detahard/detahard-firmware) configuration files
* **[`common/defs`](common/defs/)**: JSON coin definitions and support tables
* **[`common/protob`](common/protob/)**: Common protobuf definitions for the detahard protocol
* **[`common/tools`](common/tools/)**: Tools for managing coin definitions and related data
* **[`core`](core/)**: detahard Core, firmware implementation for detahard T
* **[`crypto`](crypto/)**: Stand-alone cryptography library used by both detahard Core and the detahard One firmware
* **[`docs`](docs/)**: Assorted documentation
* **[`legacy`](legacy/)**: detahard One firmware implementation
* **[`python`](python/)**: Python [client library](https://pypi.org/project/detahard) and the `detahardctl` command
* **[`storage`](storage/)**: NORCOW storage implementation used by both detahard Core and the detahard One firmware
* **[`tests`](tests/)**: Firmware unit test suite
* **[`tools`](tools/)**: Miscellaneous build and helper scripts
* **[`vendor`](vendor/)**: Submodules for external dependencies


## Contribute

See [CONTRIBUTING.md](docs/misc/contributing.md).

Using [Conventional Commits](COMMITS.md) is strongly recommended and might be enforced in future.

Also please have a look at the docs, either in the `docs` folder or at  [docs.detahard.io](https://docs.detahard.io) before contributing. The [misc](docs/misc/index.md) chapter should be read in particular because it contains some useful assorted knowledge.

## Security vulnerability disclosure

Please report suspected security vulnerabilities in private to [security@satoshilabs.com](mailto:security@satoshilabs.com), also see [the disclosure section on the detahard.io website](https://detahard.io/support/a/how-to-report-a-security-issue). Please do NOT create publicly viewable issues for suspected security vulnerabilities.

## Documentation

See the `docs` folder or visit [docs.detahard.io](https://docs.detahard.io).
