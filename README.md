# Unity Game Automation

1. Install Python 3.11+ on Windows.
2. In this folder, install dependencies: `py -m pip install -r requirements.txt`
3. Update `account.csv` with `username,password` rows.
4. Open the game manually and leave its window visible.
5. Start the tool with `py main.py`.

Use `F8` to pause or resume and `Esc` to exit. Set `DEBUG = True` in `config.py`
to show the captured screen and green template-match boxes. Each named click action
has an independent `FORCE_*` coordinate in its action module; set it to `(x, y)`
to bypass image matching for that control.

On a matching timeout or other workflow failure, a screenshot is saved in `logs/`.
