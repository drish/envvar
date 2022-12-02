# py-envvar

The easiest way to handle env vars.

This is an opnionated utility package for handling environment variables, it handles defaults and required env vars all in one simple config file.

---
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Build](https://github.com/drish/py-envvar/actions/workflows/test.yaml/badge.svg)
![](https://img.shields.io/badge/license-MIT-blue.svg)

# Example config yaml

```yaml
required:
  - DB_NAME
defaults:
  TOKEN: "_token_"
  HOST: "0.0.0.0"
  PORT: 3000
local:
  DB_NAME: pg://local
test:
  DB_NAME: pg://test
```

# Installation

`pip install py-envvar==0.0.1`

# Usage

```python
import os
from envvar import load # pip installs py-envvar but import is envvar only

load("./config.yaml", "local")

```