from __future__ import annotations

from typing import Any, Dict


def diff_config(old: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
    old_keys = set(old)
    new_keys = set(new)

    added_keys = new_keys - old_keys
    removed_keys = old_keys - new_keys
    common_keys = old_keys & new_keys

    added = {k: new[k] for k in added_keys}
    removed = {k: old[k] for k in removed_keys}
    changed = {k: {"before": old[k], "after": new[k]} for k in common_keys if old[k] != new[k]}

    return {
        "added": added,
        "removed": removed,
        "changed": changed,
    }
