# uaap-ledger-invariant-checker

**Ledger Invariant Checker** (deterministic bot, no model): Checks the ledger balances; reports only.

This bot runs on the UAAP kernel, [qavril-labs/uaap](https://github.com/qavril-labs/uaap). Installing this
package registers it with the kernel through the `uaap.bots` entry point, so the kernel's service, CLI and
MCP server pick it up.

```
pip install "uaap-ledger-invariant-checker @ git+https://github.com/qavril-labs/uaap-ledger-invariant-checker.git"
python -m uaap.bots describe ledger-invariant-checker
```

In code:

```python
from uaap.bots import BotHost
host = BotHost(tools=register_my_tools)
bot = host.build("ledger-invariant-checker")
```

Develop: `pip install -e ".[dev]"`, then `ruff check .` and `pytest`.
The test doubles come from the kernel (`uaap.testing`). The agent standard is in the kernel's docs;
`tests/test_conformance.py` checks this bot against it.
