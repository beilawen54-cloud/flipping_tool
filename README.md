# flipping_tool

Tools for visualizing Balanced Yamanouchi Word (BYW) webs and flipping \(\lambda_i\) boundaries.

This repo is designed to be used with **Binder** so that others can run your code in the browser.

## Files

- `webs_toolkit.py` — core BYW + web drawing functions (your code).
- `demo.ipynb` — example notebook that:
  - checks if a word is a balanced Yamanouchi word,
  - computes the edges,
  - draws the web using `draw_web`.

## How to run on Binder

1. Make sure this repo is public on GitHub under your account, for example:

   `https://github.com/beilawen54-cloud/flipping_tool`

2. Go to <https://mybinder.org>.

3. In the "GitHub repository name or URL" box, enter:

   `beilawen54-cloud/flipping_tool`

4. (Optional but recommended) In "File to open", type:

   `demo.ipynb`

5. Click **Launch**. Binder will build the environment using `requirements.txt`, then open `demo.ipynb`.

You can also add this Binder badge to the top of this README once the repo is live:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/beilawen54-cloud/flipping_tool/HEAD?labpath=demo.ipynb)
