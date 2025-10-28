.PHONY: sync
sync:
	conda run -n purple_team uv sync

.PHONY: probe
probe: sync
	conda run -n purple_team uv run python3 probe.py

.PHONY: help
help:
	conda run -n purple_team \
	uv run garak --help

.PHONY: list
list: sync
	conda run -n purple_team uv run garak --list_probes

.PHONY: debug-chain
debug-chain: sync
	conda run -n purple_team uv run python3 chain.py
