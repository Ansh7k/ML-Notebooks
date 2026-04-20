# Contributing & Commit Conventions

This repository follows a consistent commit message format to keep the history clean and readable.

## Commit Message Format

```
Add [topic] [vid/week number] [short description]
```

### Examples

```
Add Normalization vid25 - MinMaxScaler and StandardScaler comparison
Add EDA Bivariate vid21 - correlation heatmaps and pairplots
Add End-to-End Project vid13 - placement prediction pipeline
```

## File Naming Convention

Notebooks are named by topic and video number:

```
topic_name_vidXX.ipynb
```

## What NOT to commit

- `__pycache__/` or `.pyc` files
- `.ipynb_checkpoints/`
- Large model files (`.h5`, `.pkl`, `.pt`)
- Raw data files (`.csv`, `.xlsx`) — use links or download scripts instead
- Hardcoded API keys or tokens
