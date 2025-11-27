# Docs-as-Code Demo Project (Using Sphinx)

This repository is an example implementation of a full Docs-as-Code workflow using:

- Sphinx for documentation.
- Autodoc for API extraction.
- Doctest for testing documentation examples.
- Doxygen + Breathe for cross-language code documentation.
- sphinx-needs for requirements & traceability.
- A realistic but minimal example project: QuadLED Controller.

The goal is to demonstrate how documentation can become:

- Versioned.
- Testable.
- Reviewable.
- Automated.
- Integrated directly with code.

This repository is used together with the presentation:

- **Docs-as-Code-with-Sphinx.pdf** (included in the repo).

## 🔧 Repository Structure

```
.
├── LICENSE
├── Makefile                         # Full Sphinx build pipeline
├── README.md
├── ubproject.toml                   # Example build/project metadata
│
├── docs/                            # All documentation sources
│   ├── 01_overview.rst              # Intro & problem statement
│   ├── 02_requirements.rst          # Requirements (with sphinx-needs)
│   ├── 03_specifications.rst        # System & component specs
│   ├── 04_architecture.rst          # Architecture diagrams & views
│   ├── 05_implementation.rst        # Implementation explanation
│   ├── 06_testing.rst               # Test strategy + doctest integration
│   ├── 07_reports.rst               # Generated reports
│   │
│   ├── _doxygen/                    # Doxygen templates (for C/C++/firmware docs)
│   ├── _sphinx/                     # Dynamic configuration templates
│   ├── _static/                     # Images, diagrams, and CSS
│   ├── conf.py                      # Sphinx configuration
│   └── index.rst                    # Documentation entry point
│
├── software/                        # Example code to document
│   ├── api/
│   │   └── openapi.yaml             # Used in OpenAPI → Sphinx integration
│   └── quadled/
│       └── controller.py            # Demonstrates autodoc + type hints
│
├── firmware/                        # Placeholder demonstrating multi-domain docs
│   └── README.md
│
├── hardware/                        # Additional domain placeholder
│   └── README.md
│
└── tests/                           # Tests + doctest integration
    └── test_controller.py

```

## 📌 Why This Repository Exists

This repository exists **not to showcase the QuadLED device**, but to demonstrate a **complete Docs-as-Code pipeline**, including:

### Sphinx Documentation

Organized by engineering lifecycle:

- Overview.
- Requirements.
- Specifications.
- Architecture.
- Implementation.
- Testing.
- Reports.

### Autodoc

Python code inside `software/quadled/` contains docstrings that are automatically extracted into the documentation.

### Doctest

Executable code examples inside .rst files are automatically validated during documentation builds.
This ensures that:

- Examples remain correct and in sync with the codebase.
- Documentation fails to build if example code is broken.
- Standard test runners (e.g., pytest) and doctest checks work together to maintain accuracy.

Doctest provides an additional safety layer, preventing outdated or incorrect examples from being merged.

### Doxygen + Breathe

Firmware components can be documented using Doxygen and included in Sphinx.

### sphinx-needs

All specifications, requirements, risks, and system architecture are maintained in the `docs/` folder using [Sphinx](https://www.sphinx-doc.org/) and [`sphinx-needs`](https://sphinx-needs.readthedocs.io/)

### CI-Friendly Makefile

The `Makefile` includes:

- `make all` → clean + doctest + JSON + HTML
- `make latexpdf` → PDF output
- `make json` → machine-readable documentation
- `make git-hours` → estimate work time from Git

## Build Documentation

### Build Everything (Doctests + JSON + HTML)

```
make all
```

### Build Only HTML

```
make html
```

### Build PDF

```
make latexpdf
```

### Clean Everything

```
make clean
make clean-gitignore
```

### Estimate Development Hours (Docs + Code)

```
make git-hours
```
This runs [git-hours](https://pypi.org/project/git-hours/) using default settings.

## Example Use Case

The QuadLED Controller is included only as a sample multi-domain project, demonstrating how Sphinx accommodates:

- Hardware documentation.
- Firmware.
- Desktop software.
- API specs.
- Python modules.
- Tests.
- Architecture diagrams.

This structure helps teams adopt Docs-as-Code for real engineering projects.

## 🛡️ License

This project is licensed under the MIT License – see the LICENSE file for detail.