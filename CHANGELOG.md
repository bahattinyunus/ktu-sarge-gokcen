# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2025-12-15

### Added
- **CI/CD**: Added `pylint`, `flake8`, and `black` checks to GitHub Actions workflow.
- **Documentation**:
    - Converted internal text notes to Markdown in `docs/internal/`.
    - Added `calculations_rationale.md` and `variable_nomenclature.md`.
- **Infrastructure**:
    - Added `requirements-dev.txt` for development dependencies.
    - Added `lint` target to `Makefile`.
    - Added `__init__.py` to source packages for better module resolution.

### Changed
- **Organization**:
    - Moved raw asset images to `assets/raw/`.
    - Moved miscellaneous `.docx` files to `docs/internal/`.
- **Cleanup**:
    - Removed clutter ("Yeni Metin Belgesi" files) from the root directory.
