# Answer Citation Checker

Check source markers in a recorded answer against the supplied document catalog.

Uses Python 3.10+ and its standard library only. No package installation, virtual
environment, external service, or network access is required.

## Run

```console
python -m citations_tool --help
python -m citations_tool examples/sample.json
python -m citations_tool --check-fixtures fixtures/cases.jsonl
python generate_fixtures.py --count 20
python -m unittest discover -s tests -v
```

Run from this directory. The optional path defaults to `-`, which reads JSON from
stdin. Output is JSON or a fixture-check summary. Exit codes are 0 success,
1 file failure, and 2 invalid input. Examples and fixtures contain generated data.

Requires answer text and unique marker-safe source IDs, plus optional boolean require_citation (default true). Simple [source_id] markers are compared with the supplied catalog; repeated markers count as occurrences. This checks marker membership only, not factual truth, quotation fidelity, semantic grounding, URLs, or source contents.

## Learning focus

User-directed personal AI/LLM/agent exploration. This is an independent concept exercise based on the modeled
roadmap. It makes no claim to be employer-owned or period-authentic production code.

## Structure

- `citations_tool/core.py`: validated parsing, storage, or state transitions.
- `citations_tool/cli.py`: JSON command interface.
- `citations_tool/generate_fixtures.py`: original deterministic validation cases.
- `citations_tool/fixture_check.py`: expected-output/error checks.
- `fixtures/cases.jsonl`: 294 generated cases, with explicit descriptions.
- `tests/`: independently selected boundaries and the complete corpus check.

Branches `feature/core`, `feature/cli`, `data/fixtures`, and `docs/usage` retain
snapshots; `main` contains the complete tool. Dates and provenance are also recorded
in TIMELINE.json. Many data cases share a scenario; they are not separate features.

Keep changes focused, use actual dates for new work, and add a regression test
for changed behavior. Licensed under [MIT](LICENSE).

[History and provenance](HISTORY.md).
