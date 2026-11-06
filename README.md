# rrx-poc-api

Run locally with `docker compose up --build`.

`curl http://localhost:8000/api/health`

`curl -X POST http://localhost:8000/api/echo -H "Content-Type: application/json" -d '{"text":"hello"}'`

Release from a clean main that matches origin/main: `.\release.ps1 -Bump patch -RemoteImage "<dockerhub-user>/poc-api"`
