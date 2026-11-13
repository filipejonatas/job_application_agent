import logging

import pytest

from job_agent.main import ExecutionMode, main, parse_args


def test_modo_padrao_e_dry_run(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("EXECUTION_MODE", raising=False)
    assert parse_args([]).mode == ExecutionMode.DRY_RUN


def test_modo_vem_da_variavel_de_ambiente(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("EXECUTION_MODE", "dry_run")
    assert parse_args([]).mode == "dry_run"


def test_modo_invalido_e_recusado() -> None:
    with pytest.raises(SystemExit):
        parse_args(["--mode", "automatic"])


def test_main_retorna_zero_em_dry_run(caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.INFO, logger="job_agent")
    assert main(["--mode", "dry_run"]) == 0
    assert "dry_run" in caplog.text
