"""Original bounded concept exercise with supplied synthetic data only."""


def fields(value, required, optional=()):
    if not isinstance(value, dict) or not set(required) <= value.keys() or not value.keys() <= set(required) | set(optional):
        raise ValueError("Unexpected or missing object fields")


def integer(value, low=0, high=10**12):
    if type(value) is not int or not low <= value <= high:
        raise ValueError("Integer outside the supported range")
    return value


def label(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 80 or any(ord(c) < 32 for c in value):
        raise ValueError("Expected a nonblank label of at most 80 characters")
    return value.strip()


def sequence(value, maximum):
    if not isinstance(value, list) or len(value) > maximum:
        raise ValueError("Expected a bounded list")
    return value


def day(value):
    from datetime import date
    import re
    if not isinstance(value,str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}",value):
        raise ValueError("Use YYYY-MM-DD")
    return date.fromisoformat(value)


def text(value,maximum=10000):
    if not isinstance(value,str) or len(value)>maximum:
        raise ValueError("Expected bounded text")
    return value

def evaluate(data):
    import re
    fields(data,("answer","sources"),("require_citation",))
    answer=text(data["answer"],20000)
    sources=[label(item) for item in sequence(data["sources"],200)]
    if len(set(sources))!=len(sources) or any(not re.fullmatch(r"[A-Za-z0-9_-]+",item) for item in sources):
        raise ValueError("Sources need unique marker-safe IDs")
    required=data.get("require_citation",True)
    if type(required) is not bool:
        raise ValueError("require_citation must be boolean")
    markers=re.findall(r"\[([A-Za-z0-9_-]{1,80})\]",answer)
    used=set(markers);unknown=sorted(used-set(sources))
    return {"valid":not unknown and (bool(markers) or not required),"used":sorted(used),"unknown":unknown,
        "unused_sources":sorted(set(sources)-used),"occurrences":len(markers)}
