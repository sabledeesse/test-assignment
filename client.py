from requests import Session

_client = Session | None


def get_client() -> Session:
    global _client
    if not _client:
        _client = Session()
    return _client
