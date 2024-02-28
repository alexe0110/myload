init:
	python3.11 -m venv .venv
	.venv/bin/python3.11 -m pip install --upgrade pip
	.venv/bin/pip install -r requirements

