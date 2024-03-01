init:
	python3.11 -m venv .venv
	.venv/bin/python3.11 -m pip install --upgrade pip
	.venv/bin/pip install -r requirements

run-service:
	uvicorn service.app:app --log-level=debug --reload