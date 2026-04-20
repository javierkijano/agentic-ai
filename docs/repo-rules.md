# Repository Rules

To maintain the integrity and usability of this repository, all contributors must follow these rules:

## 1. Vendor is Read-Only
- Never modify files inside the `vendor/` directory manually.
- If a vendor resource needs modification, **derive** a new resource in `resources/` and reference the original in its `resource.yaml`.
- Updates to `vendor/` should only happen via import scripts or direct replacement of the upstream source.

## 2. Resources are the Truth
- The `resources/` directory contains the canonical, editable version of all agentic assets.
- Every resource must have a `resource.yaml` file defining its metadata.
- Structure within a resource should follow the established conventions (core, tests, platforms).

## 3. Contexts are Not Skills
- Files in `contexts/` define *how* an environment behaves, not *what* an agent can do.
- Keep operational logic (skills) separate from environment configuration (contexts).

## 4. Distribution is Generated
- Never commit manual changes to the `dist/` directory.
- `dist/` is for deployment-ready artifacts and should be reproducible from `resources/` and `contexts/` using build scripts.

## 5. Idempotency
- All scripts in `scripts/` must be idempotent. Running them multiple times should not corrupt the repository or create duplicate state.

## 6. Naming Conventions
- Use `kebab-case` for directory and file names.
- Keep IDs short, descriptive, and unique within their category.
