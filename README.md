# Job Application Agent

Agente em Python que busca vagas em fontes permitidas, pontua a compatibilidade com o perfil do candidato e prepara candidaturas para revisão humana. Nada é enviado sem aprovação, e o LinkedIn nunca é acessado de forma automatizada.

## Estrutura

```text
src/job_agent/
├── main.py          # ponto de entrada: python -m job_agent.main
├── collectors/      # adaptadores de coleta (ATS, agregadores, alertas por e-mail)
├── matching/        # pontuação com LLM
├── rules/           # elegibilidade, limites e deduplicação
├── applications/    # preparação e envio de candidaturas
├── persistence/     # Neon Postgres
├── reports/         # relatório diário
└── profile/         # perfil, currículo e respostas confirmadas
config/              # regras e fontes (YAML)
migrations/          # migrations Alembic
tests/               # unit, integration, e2e
```

## Desenvolvimento

Requer [uv](https://docs.astral.sh/uv/) e Python 3.12+.

```bash
uv sync                      # instala dependências travadas em uv.lock
uv run pytest                # testes
uv run ruff check .          # lint
uv run ruff format .         # formatação
uv run python -m job_agent.main --mode dry_run
```

Segredos ficam em `.env` (veja `.env.example`) localmente e em GitHub Actions Secrets na nuvem. Currículo, perfil e chaves nunca são versionados.
