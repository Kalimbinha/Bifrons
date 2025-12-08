# Bifrons

[![PyPI version](https://img.shields.io/pypi/v/bifrons)](https://pypi.org/project/bifrons/)
[![Python versions](https://img.shields.io/pypi/pyversions/bifrons)](https://pypi.org/project/bifrons/)
[![License](https://img.shields.io/github/license/Kalimbinha/Bifrons)](https://github.com/Kalimbinha/Bifrons/blob/main/LICENSE)

CLI tool for automating SemVer versioning based on PR/commit titles.

**Repository**: [https://github.com/Kalimbinha/Bifrons](https://github.com/Kalimbinha/Bifrons)

**PyPI**: [https://pypi.org/project/bifrons/](https://pypi.org/project/bifrons/)

## Description

Bifrons analyzes the title of a PR or commit and automatically increments the version following [Semantic Versioning (SemVer)](https://semver.org/) rules. It classifies the title into:

- **patch** (fixes): titles starting with "fix"
- **minor** (new features): titles starting with "feat" or "feature"
- **major** (breaking changes): titles starting with "breaking", "major", or containing "breaking change"

The current version is read from and written to the [`version.txt`](version.txt) file in the current directory.

## Installation

Ensure you have Python 3.8+ installed.

```bash
pip install bifrons
```

## Usage

Run the command with the PR/commit title:

```bash
bifrons --title "fix: bug correction"
```

### Examples

- **Patch (fix)**:

  ```bash
  bifrons --title "fix: resolve memory leak"
  ```

  Output:

  ```text
  [bifrons] previous version: 1.0.0
  [bifrons] new version: 1.0.1
  ```

- **Minor (new feature)**:

  ```bash
  bifrons --title "feat: add dark mode"
  ```

  Output:

  ```text
  [bifrons] previous version: 1.0.1
  [bifrons] new version: 1.1.0
  ```

- **Major (breaking change)**:

  ```bash
  bifrons --title "breaking: remove deprecated API"
  ```

  Output:

  ```text
  [bifrons] previous version: 1.1.0
  [bifrons] new version: 2.0.0
  ```

- **Invalid title**:

  ```bash
  bifrons --title "random title"
  ```

  Output:

  ```text
  Error: Invalid title! Use fix/feat/major
  ```

### Version File

- The [`version.txt`](version.txt) file is created automatically if it does not exist (starts with `0.0.0`).
- It contains only the current version (e.g., `1.2.3`).
- Run the command in the directory where you want to manage the version.

## Development

- **Project Structure**:

  ```text
  Bifrons/
  ├── bifrons/
  │   ├── __init__.py
  │   ├── cli.py       # Command-line interface
  │   └── core.py      # Core logic
  ├── pyproject.toml   # Project configuration
  ├── README.md        # This file
  └── version.txt      # Version file (generated)
  ```

- **Testing**: Run `pytest` to execute tests in `tests/`.
- **Linting**: Use `black bifrons/` to format the code.

## Author

Fernando Barreto

## License

MIT License. See the LICENSE file for details.
