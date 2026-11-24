"""Ledger Invariant Checker: a UAAP bot, packaged on its own. Installing it registers it with the UAAP kernel."""

from uaap.bots.catalog import BotSpec

SPEC = BotSpec(
    id="ledger-invariant-checker",
    name="Ledger Invariant Checker",
    version="0.1.0",
    kind="deterministic",
    module="uaap_bot_ledger_invariant_checker.agent",
    class_name="LedgerInvariantChecker",
    needs_model=False,
    needs_inbox=False,
    summary="Checks the ledger balances; reports only.",
)
