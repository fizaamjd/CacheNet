# Contributing to CacheNet

Thanks for your interest in improving the project.

## How to contribute

1. Fork the repository.
2. Create a feature branch from `main`:
   ```bash
   git checkout -b feat/your-change-name
   ```
3. Make focused changes with clear commit messages.
4. Run the relevant checks before opening a pull request.
5. Submit a pull request with a clear summary and related issue references.

## Development workflow

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

### Frontend

```bash
cd frontend
npm install
npm run lint
npm run build
```

## Pull request expectations

- Keep PRs focused on a single concern.
- Include tests or validation when changing behavior.
- Update documentation when user-facing behavior changes.
- Reference any related GitHub issues.

## Code of conduct

Please review [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.
