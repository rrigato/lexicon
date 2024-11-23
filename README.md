Anki add-on to create flash cards

### getting-started
```
pyenv install 3.9
pyenv virtualenv 3.9 lexicon
pyenv activate lexicon
pip install requirements/requirements-dev.txt
```


### anki-debugging


#### anki-debug-console
Run the following from a terminal
```bash
/Applications/Anki.app/Contents/MacOS/anki
```

#### run-anki-from-terminal
- inside anki
```shell
cmd+shift+;
```
[debug-documentation](https://docs.ankiweb.net/misc.html#debug-console)

#### python-debug-breakpoint
```python
from aqt.qt import debug; debug()
```

