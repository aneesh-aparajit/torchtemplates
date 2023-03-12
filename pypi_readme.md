# Torch Templates


- The file structure is vastly inspired from [madewithml.com](https://madewithml.com/) and many Kaggle Kernels from top kagglers.

- Till now, this would create a package for you with the `setup.py` and the `requirements.txt`.
- TODO:
    - Add TODO for hyperparameter tuning.

## File structure
```
- src
    - config
        - config.py
    - project_name
        - main.py
        - dataset.py
        - model.py
        - train.py
        - utils.py
        - hyparam.py (need to add...)
    - README.md
    - requirements.txt
```

## How to use?

### Install
```bash
pip install torchtemplates
```

### Commands
```bash
torchtemplates --help
```

### `init`
```bash
torchtemplates init
```

### `new-pipeline`
```bash
torchtemplates new-pipeline image testing
```
