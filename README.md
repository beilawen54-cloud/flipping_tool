# flipping_tool

Tools for visualizing Balanced Yamanouchi Word (BYW) webs and flipping boundaries.

This repo is designed to be used with **Binder** so that others can run the *full* `webs_toolkit.py` script exactly like on your local machine (Spyder / terminal), using a Binder terminal.

## Files

- `webs_toolkit.py` — core BYW + web drawing + interactive CLI (`interactive_flips()`).
- `requirements.txt` — Python dependencies needed for Binder (`numpy`, `matplotlib`).

## How to run the FULL tool on Binder (Option 3: Terminal, like Spyder)

1. Make sure this repo is public on GitHub under your account, for example:

   `https://github.com/beilawen54-cloud/flipping_tool`

2. Go to <https://mybinder.org>.

3. In the **"GitHub repository name or URL"** box, enter:

   `beilawen54-cloud/flipping_tool`

4. Leave everything else at the default (you don't have to specify a file).

5. Click **Launch**. Binder will:
   - build an environment using `requirements.txt`
   - open **JupyterLab** in your browser.

6. In JupyterLab, do:

   - Click the **"+" Launcher** tab (or "File → New Launcher").
   - Under **Other**, click **Terminal** to open a terminal.

7. In the terminal, type:

   ```bash
   python webs_toolkit.py
   ```

   and press **Enter**.

   This will:
   - run the entire `webs_toolkit.py` file
   - start the `interactive_flips()` prompt
   - show plots in the JupyterLab window (just like figures in Spyder).

You and other users can now interact with the tool exactly as if running the script locally.

## Optional: Add a Binder badge

After the repo is public, you can add this badge near the top of the README to give people a one-click launch button:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/beilawen54-cloud/flipping_tool/HEAD)

Clicking the badge will open Binder on this repo. From there, follow steps **6–7** above to open a terminal and run:

```bash
python webs_toolkit.py
```
