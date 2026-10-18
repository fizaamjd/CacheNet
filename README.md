# CacheNet: Agent-Based Distributed Cache Simulator

[![CI](https://github.com/fizaamjad897/ABM-Project/actions/workflows/ci.yml/badge.svg)](https://github.com/fizaamjad897/ABM-Project/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-16-000000.svg)](https://nextjs.org/)

A simulation platform for exploring distributed cache invalidation, consistency guarantees, and agent-based network behavior in a realistic event-driven environment.

## Demo video

https://github.com/user-attachments/assets/82fc32cb-b3fe-4a5f-9e2b-9362572e592f

[Open the interactive reel](https://cachenet-demo.netlify.app/).

## Why this project

CacheNet models distributed systems as autonomous agents that communicate through message passing, time-aware events, and configurable failure modes. It is useful for studying:

- Cache invalidation strategies
- Byzantine or adversarial node behavior
- Network delays and partitioning
- System resilience under chaos conditions
- End-to-end agent communication patterns

## Project architecture

```text
CacheNet/
├── backend/                # FastAPI API and simulation engine integration
│   ├── src/
│   │   ├── main.py
│   │   ├── simulation_manager.py
│   │   ├── ai_analyst.py
│   │   └── core/
│   └── requirements.txt
├── frontend/               # Next.js dashboard and visualization layer
│   ├── app/
│   ├── package.json
│   └── public/
├── motion-graphics/        # Presentation assets and reel content
├── project-guide-files/     # Project notes and architecture documentation
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── .github/
├── .gitignore
└── cache-net-demo.mp4
```

## Tech stack

- Backend: Python, FastAPI, Pydantic, asyncio
- Frontend: Next.js, React, Material UI
- Simulation: Discrete-event engine with agent-based orchestration
- Visualization: charts and dashboard components in the frontend app

## Quick start

### Prerequisites

- Python 3.11+
- Node.js 20+
- npm

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

The API will run at:

- http://localhost:8000

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The app will run at:

- http://localhost:3000

## Simulation capabilities

- Agent-driven simulation of cache nodes and clients
- Event queue orchestration and timing control
- Network latency and failure scenarios
- Metrics tracking for cache behavior and stale reads
- AI-assisted analysis endpoint for simulation interpretation

## Development workflow

```bash
# Backend tests
cd backend
pytest

# Frontend checks
cd frontend
npm run lint
npm run build
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## Security

If you discover a vulnerability, please follow the steps in [SECURITY.md](SECURITY.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This repository is designed to showcase an agent-based simulation of distributed cache systems for experimentation, research, and engineering exploration.