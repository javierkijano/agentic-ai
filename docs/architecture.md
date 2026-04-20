# Repository Architecture

This repository is designed to be a robust, flexible, and simple hub for "agentic resources". It follows a clear separation of concerns to ensure scalability and maintainability.

## Core Concepts

The repository is organized into five main pillars:

### 1. Vendor (`vendor/`)
- **Purpose**: Contains resources imported from third-party sources.
- **Rules**: Treated as read-only. No manual edits should be performed here.
- **Content**: Skills, agents, prompts, and knowledge packs from external contributors or platforms.

### 2. Resources (`resources/`)
- **Purpose**: The canonical source of truth for own and editable resources.
- **Rules**: This is where active development happens.
- **Content**:
    - **Skills**: Functional capabilities.
    - **Agents**: Agent definitions and personas.
    - **Workflows**: Multi-step processes.
    - **Packs**: Grouped prompts, memory, or knowledge assets.

### 3. Contexts (`contexts/`)
- **Purpose**: Platform or project-specific operational contexts.
- **Rules**: These are not "skills" but environment-defining files.
- **Content**: Project templates, home profiles, and subtree-specific configurations (e.g., `.hermes.md`, `AGENTS.md`, `SOUL.md`).

### 4. Shared (`shared/`)
- **Purpose**: Cross-cutting reusable pieces.
- **Content**: Schemas, libraries, snippets, fixtures, and assets used by multiple resources.

### 5. Distribution (`dist/`)
- **Purpose**: Generated outputs prepared for deployment to specific platforms (Hermes, Albert, OpenClaw).
- **Rules**: Never edit files in `dist/` manually; they are products of the build process.

## Flow of Information

### 6. Meta-Skills
- **Purpose**: Skills that allow agents to manage the repository itself.
- **Example**: `resources/skills/repository-manager/` contains the logic to validate, create, and build resources.
- **Access**: Available as CLI scripts in `scripts/` or as a skill for agents.
