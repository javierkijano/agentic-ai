# Resource Lifecycle

This document describes the common workflows for managing resources in this repository.

## 1. Importing a Third-Party Resource

1. Use a script (or manual download) to place the resource in `vendor/<type>/<id>/`.
2. Add a `vendor.yaml` or similar metadata to track the origin and version.
3. **DO NOT** edit the files inside this folder.

## 2. Deriving from a Vendor Resource

If you need to customize a vendor resource:
1. Create a new folder in `resources/<type>/<custom-id>/`.
2. Copy relevant parts from `vendor/` or reference them.
3. In `resource.yaml`, set `derived_from: <vendor-id>`.
4. Implement your changes in the new folder.

## 3. Creating a New Resource

1. Run `python scripts/create_resource.py --type <type> --id <id>`.
2. Fill in the `resource.yaml` metadata.
3. Add logic in `core/` and tests in `tests/`.
4. Document the resource in `README.md`.

## 4. Adding Platform Overlays

To make a resource compatible with Hermes:
1. Create `resources/<type>/<id>/platforms/hermes/`.
2. Add required files like `SKILL.md` or platform-specific prompts.
3. Update `resource.yaml` to include `hermes` in the `platforms` list.

## 5. Building and Deploying

1. Run `python scripts/build_platform.py --platform hermes`.
2. This will aggregate resources and contexts into `dist/hermes/`.
3. Run `python scripts/install_hermes.py` to sync the generated artifacts to your active Hermes environment.
