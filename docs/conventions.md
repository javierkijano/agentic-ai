# Conventions

Standardizing the structure and metadata of resources ensures they are portable and easy to manage.

## Resource Pack Structure

Each resource in `resources/<type>/<id>/` should follow this general layout:

```
<id>/
  resource.yaml    # Mandatory metadata
  README.md        # Documentation for the resource
  core/            # Main logic, prompts, or data
  tests/           # Validation tests for the resource
  platforms/       # Platform-specific overlays (e.g., platforms/hermes/SKILL.md)
```

## `resource.yaml` Schema

Every resource must include a `resource.yaml` with at least the following fields:

- `id`: Unique identifier (e.g., `git-helper`)
- `kind`: Type of resource (e.g., `skill`, `agent`, `workflow`)
- `status`: Lifecycle state (e.g., `draft`, `active`, `deprecated`)
- `source`: URL or path to original source (if applicable)
- `derived_from`: ID of the resource this was branched from (if applicable)
- `tags`: List of descriptive tags
- `platforms`: List of supported platforms (e.g., `[hermes, albert]`)
- `depends_on`: List of other resource IDs required

## Naming Standards

- **Folders**: `kebab-case` (e.g., `memory-packs`, `advanced-coder`)
- **Files**: `kebab-case` or `snake_case` depending on the language, but consistency is key.
- **IDs**: Must match the folder name in `resources/`.

## Platform Overlays

If a resource needs specific behavior for a platform like Hermes, place it in `platforms/hermes/`.
Example:
- `resources/skills/web-search/platforms/hermes/SKILL.md`
- `resources/memory-packs/coding-standards/platforms/hermes/`
