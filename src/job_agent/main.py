"""Ponto de entrada do agente: `python -m job_agent.main`."""

from __future__ import annotations

import argparse
import logging
import os
from collections.abc import Sequence
from enum import StrEnum

from job_agent import __version__

logger = logging.getLogger("job_agent")


class ExecutionMode(StrEnum):
    """Modos de execução. Só `dry_run` existe até a fase 3."""

    DRY_RUN = "dry_run"


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="job_agent", description=__doc__)
    parser.add_argument(
        "--mode",
        choices=[m.value for m in ExecutionMode],
        default=os.environ.get("EXECUTION_MODE", ExecutionMode.DRY_RUN.value),
        help="Modo de execução (padrão: variável EXECUTION_MODE ou dry_run).",
    )
    return parser.parse_args(argv)


def run(mode: ExecutionMode) -> int:
    """Executa um ciclo do agente. Por enquanto só registra o início."""
    logger.info("job_agent %s iniciado em modo %s", __version__, mode.value)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    args = parse_args(argv)
    return run(ExecutionMode(args.mode))


if __name__ == "__main__":
    raise SystemExit(main())
