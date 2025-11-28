# src/memory/session_service.py

from typing import Any, Dict


class SessionMemory:
    """
    Simple in-memory session store for the current run.
    In a real system, this could be backed by a database
    or a dedicated memory service.
    """

    def __init__(self) -> None:
        self._store: Dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        self._store[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._store.get(key, default)

    def get_all(self) -> Dict[str, Any]:
        return dict(self._store)

