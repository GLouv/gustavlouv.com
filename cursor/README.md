# Cursor Prompt Architecture — Gustav Louv Site
All Cursor generations must load context from `/cursor/main_prompt.md`.
Sub-prompts are auto-loaded in this order: style → accessibility → provenance.
Never overwrite these files without review.
To regenerate context: `#context: cursor/main_prompt.md`

