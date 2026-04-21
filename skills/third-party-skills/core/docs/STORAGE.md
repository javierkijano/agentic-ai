# Storage Contract: third-party-skills

## Runtime Data
- **Location**: `runtime/{{agent_id}}/{{env}}/third-party-skills/{{session_id}}/`
- **Format**: CLI output captures and installation logs.

## External State
- This skill manages external state via the `npx skills` CLI. 
- Installed skills are typically stored in the user's global `node_modules` or local project directory as per `npx skills` behavior.
