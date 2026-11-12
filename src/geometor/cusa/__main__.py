"""Module execution entry point for ``python -m geometor.cusa``."""

from __future__ import annotations

import sys

from geometor.cusa.cli import main

if __name__ == "__main__":
    sys.exit(main())
