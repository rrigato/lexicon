Anki add-on to create flash cards

### getting-started
```
pyenv install 3.9
pyenv virtualenv 3.9 lexicon
pyenv activate lexicon
pip install requirements/requirements-dev.txt
```


### anki-debugging

#### add-python-debug-breakpoint
```python
from aqt.qt import debug; debug()
```

#### anki-debug-in-terminal
Run the following from a terminal
```bash
/Applications/Anki.app/Contents/MacOS/anki
```


### run-a-terminal-inside-anki
- inside anki
```shell
cmd+shift+;
```
[debug-documentation](https://docs.ankiweb.net/misc.html#debug-console)


