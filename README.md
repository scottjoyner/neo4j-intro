# neo4j-intro — data collection exercises

Early Python scripts for collecting, preparing, and sorting external data in support of graph/data experiments. The name suggests a Neo4j introduction, but the inspected files are **data processing prototypes**, not a complete Neo4j server or verified Cypher tutorial.

## Files

- `dataCollection.py` — HTTP/data ingestion prototype importing `requests` and `python-decouple`, then performing JSON-to-CSV-oriented processing.
- `sortData.py` — short pandas/JSON processing experiment.
- `data2` — existing data artifact with an unspecified format; inspect provenance before reuse.
- `.gitignore` — project-level ignore rules.

There is no tracked Python lockfile, Docker/Neo4j deployment manifest, reliable entry-point documentation, or automated test suite.

## Safe reproduction

Review `dataCollection.py` before running it: it may contact a third-party data provider, rely on credentials configured outside source, and create/overwrite output data. Use synthetic fixtures, mocked HTTP responses, and an isolated working directory first. Do not commit real API tokens, contact records, or private graph extracts.

If evolving the project into a graph tutorial, add a disposable Neo4j test configuration, explicit Cypher schema and examples, and import/cleanup steps with a documented safety boundary.

**Status:** source inventory only. No APIs, database, or collection scripts were executed.
