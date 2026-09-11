# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: ClientNotes
def _validate_idempotent_key(key: str, existing_ids: dict[str, bool]) -> None:
    """Ensure a proposed idempotent key is not already taken."""
    if key in existing_ids:
        raise ValueError(f"Idempotent key already in use: {key!r}")

def _apply_update(
    entity: dict,
    patch: dict,
    existing_ids: dict[str, bool],
    idempotent_keys: dict[str, bool],
) -> dict:
    """Apply a partial update and record the resulting idempotent key."""
    if "idempotent_key" in patch:
        _validate_idempotent_key(patch["idempotent_key"], idempotent_keys)
        patch["idempotent_key"] = patch["idempotent_key"].strip().lower()
    if "tags" in patch:
        patch["tags"] = sorted(set(patch["tags"]))
    if "status" in patch:
        allowed = {"todo", "done", "cancelled"}
        if patch["status"] not in allowed:
            raise ValueError(f"Invalid status: {patch['status']!r}")
    if patch:
        entity.update(patch)
    if "idempotent_key" not in patch:
        if "idempotent_key" not in entity and entity.get("_idempotent_key") is None:
            entity["_idempotent_key"] = f"key-{entity.get('id', entity.get('created_at', ''))}"
            existing_ids[entity["_idempotent_key"]] = True
    return entity
