Anki add-on to create flash cards

### getting-started

1) Download the Anki app for [your platform here](https://apps.ankiweb.net/)
2)
```sh
pyenv install 3.9

# Make sure DYLIB_PATH and VENV_PATH arguements
# Match your local setup
make install

```


### anki-debugging

#### add-python-debug-breakpoint
```python
import pdb; pdb.set_trace();

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


### addon-directory-overview
- [config.json](addon/config.json) = configuration that users can set within the anki user interface
- [manifest.json](addon/manifest.json) = for distributing anki addons outside of anki web


### viewing-anki-versions
- The version of the aqt library used in the anki application can be found by clicking on Anki -> About Anki

![images/anki_python_version.png](images/anki_python_version.png)
- Version should correspond to the `aqt` version in [requirements/requirements-dev.in](requirements/requirements-dev.in)
- Check the pyqt version locally from an interpreter
```python
from aqt import PYQT_VERSION_STR, qVersion
print(PYQT_VERSION_STR) #PyQt version
print(qVersion()) #qt version
```
- The latest dependencies that aqt uses can be found [here](https://github.com/ankitects/anki/tree/main/python)

# missing libankihelper.dylib file
**libankihelper No longer used**

If you received the following error, this means that the `libankihelper.dylib` dynamic library calling some of the C++ code for Qt was not included in the make install:

![images/anki_missing_dylib.jpg](images/anki_missing_dylib.jpg)


1) The libankihelper.dylib file should be available from here, if you installed the .dmg to `/Applications`
```
/Applications/Anki.app/Contents/MacOS/libankihelper.dylib
```
2) When calling make install pass the appropriate path to the dylib and virtualenv install location
```sh
make install \
DYLIB_PATH=/Applications/Anki.app/Contents/MacOS/libankihelper.dylib \
VENV_PATH=~/.pyenv/versions/lexicon3.13/lib/python3.13/site-packages/_aqt/data/lib/
```