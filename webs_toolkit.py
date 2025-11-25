from typing import List, Tuple, Optional, Dict
import numpy as np
import matplotlib.pyplot as plt

Edge = Tuple[int, int, int]  # (start_idx, end_idx, level) with level = high digit (2..n)

# ---------- Checks ----------

def is_yamanouchi(word: str) -> Tuple[bool, Optional[int]]:
    if not word or not all(ch.isdigit() for ch in word) or '0' in word:
        return False, 0
    n = max(int(ch) for ch in word)
    counts = [0]*(n+1)
    for idx, ch in enumerate(word, start=1):
        c = int(ch)
        counts[c] += 1
        for i in range(1, n):
            if counts[i] < counts[i+1]:
                return False, idx
    return True, None

def check_balanced_yamanouchi(word: str) -> Tuple[bool, Optional[str], Optional[int]]:
    ok, _ = is_yamanouchi(word)
    if not ok:
        return False, "Prefix (Yamanouchi) violation in the initial word.", None
    n = max(int(ch) for ch in word)
    counts = [0]*(n+1)
    for ch in word:
        counts[int(ch)] += 1
    if counts[1] == 0 or len(set(counts[1:])) != 1:
        return False, "Not balanced: counts of 1..n must be equal and nonzero.", None
    return True, None, n

# ---------- Pairings ----------

def pair_non_crossing(byw: str, n: int) -> List[Edge]:
    stacks: Dict[int, List[int]] = {lvl: [] for lvl in range(1, n)}
    edges: List[Edge] = []
    for idx, ch in enumerate(byw):
        c = int(ch)
        if c >= 2 and stacks[c - 1]:
            start = stacks[c - 1].pop()
            edges.append((start, idx, c))
        if c <= n - 1:
            stacks[c].append(idx)
    return edges

def pair_perfect_zip(byw: str, n: int) -> List[Edge]:
    edges: List[Edge] = []
    for k in range(2, n+1):
        low = [i for i, ch in enumerate(byw) if ch == str(k-1)]
        high = [i for i, ch in enumerate(byw) if ch == str(k)]
        m = min(len(low), len(high))
        for a, b in zip(low[:m], high[:m]):
            edges.append((a, b, k))
    return edges

def pair_byw_or_perfect(byw: str, n: int) -> List[Edge]:
    ok, _ = is_yamanouchi(byw)
    return pair_non_crossing(byw, n) if ok else pair_perfect_zip(byw, n)

# ---------- Flip relabel ----------

def swap_digits_in_word(word: str, lam: int) -> str:
    a, b = str(lam), str(lam + 1)
    trans = str.maketrans({a: '#', b: a})
    w = word.translate(trans)
    return w.replace('#', b)

# ---------- Plot helpers ----------

def _parabola_points(x1, x2, h, m=200):
    mid = 0.5*(x1+x2)
    d = (x2-x1)
    if d == 0: return np.array([x1, x2]), np.array([0,0])
    a = -4*h/(d*d)
    X = np.linspace(x1, x2, m)
    Y = a*(X-mid)**2 + h
    return X, Y

def _tangent_segment(x1, x2, h, frac=0.5, step_frac=0.02):
    mid = 0.5*(x1+x2)
    d = (x2-x1)
    if d == 0: return x2-0.01, 0, x2, 0
    a = -4*h/(d*d)
    t = float(np.clip(frac,0,1))
    xc = x1 + t*d
    eps = step_frac*d
    xp, xn = xc-eps, xc+eps
    yp = a*(xp-mid)**2 + h
    yn = a*(xn-mid)**2 + h
    return xp, yp, xn, yn

def _plot_arc_mid_arrow(ax, x1, x2, h, color="C0", lw=2.0, ms=14.0):
    X, Y = _parabola_points(x1, x2, h)
    ax.plot(X, Y, color=color, lw=lw, zorder=2)
    xp, yp, xn, yn = _tangent_segment(x1, x2, h)
    ax.annotate("", xy=(xn, yn), xytext=(xp, yp),
                arrowprops=dict(arrowstyle="-|>", lw=lw, mutation_scale=ms, color=color),
                zorder=3)

def draw_web(word: str, edges: List[Edge], height_scale=0.3, title_suffix=""):
    L = len(word)
    xs = list(range(L))
    fig, ax = plt.subplots(figsize=(max(8,L*0.6),4))
    for i, label in enumerate(word):
        ax.plot(xs[i], 0, 'ko', ms=4, zorder=4)
        ax.text(xs[i], -0.3, label, ha='center', va='top', fontsize=12)
    colors = plt.rcParams['axes.prop_cycle'].by_key().get('color', ['C0','C1','C2','C3','C4','C5'])
    for s, e, lev in edges:
        color = colors[(lev-2)%len(colors)]
        x1, x2 = xs[s], xs[e]
        span = abs(x2-x1)
        h = span*height_scale
        _plot_arc_mid_arrow(ax, x1, x2, h, color=color)
    ax.axis('off')
    ax.set_title(f"Web for BYW: {word}  {title_suffix}", fontsize=14)
    plt.show()

# ---------- Interactive ----------

def interactive_flips():
    print("BYW Web — λ_i flips with guaranteed n↔n+1 connections (with heading)")
    print("After each flip λ_i, boundary digits i↔i+1 swap; edges recompute.")
    print("Arrowheads always point n→n+1.\n")

    while True:
        w0 = input("BYW> ").strip()
        if w0.lower() == "quit":
            return
        ok, msg, n = check_balanced_yamanouchi(w0)
        if not ok:
            print(f"❌ {msg}\n"); continue

        word_init = w0
        word = w0
        edges = pair_byw_or_perfect(word, n)
        draw_web(word, edges, title_suffix=f"(n={n}, start)")

        flips = 0
        while True:
            s = input(f"Flip which λ_i? (1..{n-1}) — 'none', 'done', or 'quit'> ").strip().lower()
            if s in ("done","d"): print(""); break
            if s == "quit": return
            if s in ("none","n",""):
                draw_web(word, edges, title_suffix=f"(n={n}, unchanged)"); continue
            try: i = int(s)
            except: print("⚠️ integer 1..n-1.\n"); continue
            if not (1 <= i <= n-1):
                print(f"⚠️ λ_i must satisfy 1 ≤ i ≤ {n-1}.\n"); continue

            word = swap_digits_in_word(word, i)
            edges = pair_byw_or_perfect(word, n)
            flips += 1
            if word == word_init:
                draw_web(word, edges, title_suffix=f"(n={n}, BACK TO INITIAL after {flips})")
                print(f"🔁 Back to the initial configuration after {flips} flips.\n")
                break
            else:
                draw_web(word, edges, title_suffix=f"(n={n}, flipped λ_{i} → boundary {i}↔{i+1})")

if __name__ == "__main__":
    interactive_flips()
