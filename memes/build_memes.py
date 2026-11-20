#!/usr/bin/env python3
"""
build_memes.py — assemble the three gta6-meme-x-01 candidate memes.

Pipeline (all in-session, reproducible):
  1. Base scenes in raw/ were generated with the session's image tool
     (parody illustration, no GTA artwork, no text baked in — AI text
     misspells, and the judge shrinks the picture to 480px, so every
     caption is typeset here in code where spelling is exact).
  2. This script draws the make.fun ghost mascot from scratch as vector
     shapes (white ghost, thick black outline, two black four-point
     sparkle eyes, one round little hand, holding a magenta coin with a
     white star) and places it INSIDE each scene as a character:
       A: the ghost is the HR approver floating over the PTO stack.
       B: the ghost is the AI agent handing the broke gamer a coin.
       C: the ghost is the gamer's partner in crime by the pink car.
  3. Captions are set in DejaVu Sans Bold with a heavy stroke so they
     stay readable when the judge's view shrinks the image to 480px.

Run:  python3 memes/build_memes.py
Out:  memes/candidate-a-pto.png, candidate-b-wallet.png,
      memes/candidate-c-duo.png  (1600x1600 PNG each)
"""

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
MAGENTA = (230, 0, 150)


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD, size)


def star_points(cx, cy, r_out, r_in, n=5, rot=-90):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def sparkle_points(cx, cy, s):
    """Four-pointed sparkle (the ghost's eyes)."""
    k = 0.22
    return [
        (cx, cy - s), (cx + s * k, cy - s * k), (cx + s, cy),
        (cx + s * k, cy + s * k), (cx, cy + s), (cx - s * k, cy + s * k),
        (cx - s, cy), (cx - s * k, cy - s * k),
    ]


def draw_ghost(base: Image.Image, cx: int, cy: int, w: int) -> None:
    """Draw the make.fun ghost centred at (cx, cy), body width w.

    Drawn on an overlay so the thick black outline is one silhouette
    pass behind the white body pass — same shape, slightly larger.
    """
    h = int(w * 1.18)
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x0, y0 = cx - w // 2, cy - h // 2
    x1, y1 = cx + w // 2, cy + h // 2

    def body(draw, pad, fill):
        # Rounded dome + straight sides + three-bump wavy hem.
        draw.pieslice([x0 - pad, y0 - pad, x1 + pad, y0 - pad + w], 180, 360, fill=fill)
        draw.rectangle([x0 - pad, y0 + w // 2, x1 + pad, y1 - int(w * 0.16) + pad], fill=fill)
        bumps = 3
        bw = (x1 - x0) / bumps
        for i in range(bumps):
            bx0 = x0 - pad + i * bw
            draw.ellipse([bx0, y1 - int(w * 0.30) - pad, bx0 + bw + 2 * pad, y1 + pad], fill=fill)

    # Soft contact shadow, then outline pass, then white pass.
    d.ellipse([x0 + 8, y1 + 6, x1 - 8, y1 + int(w * 0.14)], fill=(0, 0, 0, 70))
    body(d, max(7, w // 22), (0, 0, 0, 255))
    body(d, 0, (255, 255, 255, 255))

    # Sparkle eyes.
    eye_y = y0 + int(h * 0.34)
    eye_dx = int(w * 0.19)
    eye_s = int(w * 0.115)
    d.polygon(sparkle_points(cx - eye_dx, eye_y, eye_s), fill=(0, 0, 0, 255))
    d.polygon(sparkle_points(cx + eye_dx, eye_y, eye_s), fill=(0, 0, 0, 255))

    # Magenta coin with white star, held low on the right side.
    coin_r = int(w * 0.30)
    coin_cx, coin_cy = x1 - int(w * 0.02), y0 + int(h * 0.72)
    d.ellipse([coin_cx - coin_r, coin_cy - coin_r, coin_cx + coin_r, coin_cy + coin_r],
              fill=MAGENTA + (255,), outline=(0, 0, 0, 255), width=max(5, w // 40))
    d.polygon(star_points(coin_cx, coin_cy, coin_r * 0.58, coin_r * 0.24),
              fill=(255, 255, 255, 255))

    # One round little hand, on the left, overlapping the body edge.
    hand_r = int(w * 0.13)
    hand_cx, hand_cy = x0 + int(w * 0.02), y0 + int(h * 0.62)
    d.ellipse([hand_cx - hand_r, hand_cy - hand_r, hand_cx + hand_r, hand_cy + hand_r],
              fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=max(5, w // 40))

    base.alpha_composite(layer)


def caption(draw, cx, cy, text, size, fill=WHITE, stroke=BLACK, stroke_w=None,
            anchor="mm"):
    f = font(size)
    draw.text((cx, cy), text, font=f, fill=fill, anchor=anchor,
              stroke_width=stroke_w if stroke_w is not None else max(4, size // 9),
              stroke_fill=stroke)


def build_a() -> Path:
    img = Image.open(RAW / "raw-a-office.png").convert("RGBA")
    d = ImageDraw.Draw(img)
    # Ghost = a fellow launch-week escapee, floating outside the office
    # window on the Leonida side (v1 put it at y=300, where it covered
    # the top caption — moved into the empty window area instead).
    draw_ghost(img, 1320, 500, 240)
    d = ImageDraw.Draw(img)
    caption(d, 800, 105, "ME: *SUBMITS 47 SICK DAYS", 74, fill=BLACK, stroke=WHITE, stroke_w=3)
    caption(d, 800, 195, "FOR GTA 6 LAUNCH WEEK*", 74, fill=BLACK, stroke=WHITE, stroke_w=3)
    caption(d, 800, 1395, "MY BOSS: “APPROVED.”", 76)
    caption(d, 800, 1490, "“I'M CALLING IN DEAD TOO.”", 76)
    out = HERE / "candidate-a-pto.png"
    img.convert("RGB").save(out, "PNG")
    return out


def build_b() -> Path:
    img = Image.open(RAW / "raw-b-wallet.png").convert("RGBA")
    # Ghost = the AI agent beside the gamer, coin out (v1 centred it on
    # the wallet and hid the joke's key prop — moved right, wallet visible).
    draw_ghost(img, 1235, 960, 255)
    d = ImageDraw.Draw(img)
    caption(d, 800, 120, "GTA 6 WANTS $80 + 150 GB", 78, fill=BLACK, stroke=WHITE, stroke_w=3)
    caption(d, 800, 215, "MY WALLET:", 78, fill=BLACK, stroke=WHITE, stroke_w=3)
    caption(d, 800, 1330, "MY AI AGENT ON make.fun:", 72)
    caption(d, 800, 1425, "“RELAX. I WIN MONEY", 76)
    caption(d, 800, 1520, "WHILE YOU WAIT.”", 76)
    out = HERE / "candidate-b-wallet.png"
    img.convert("RGB").save(out, "PNG")
    return out


def build_c() -> Path:
    img = Image.open(RAW / "raw-c-duo.png").convert("RGBA")
    # Ghost = partner in crime, standing on the road by the pink car.
    draw_ghost(img, 430, 1090, 330)
    d = ImageDraw.Draw(img)
    caption(d, 800, 92, "ROCKSTAR GAVE JASON", 80)
    caption(d, 800, 185, "A PARTNER: LUCIA", 80)
    caption(d, 800, 1400, "make.fun GAVE ME ONE TOO.", 78)
    caption(d, 800, 1498, "MINE PAYS ME.", 88, fill=(255, 210, 63))
    out = HERE / "candidate-c-duo.png"
    img.convert("RGB").save(out, "PNG")
    return out


if __name__ == "__main__":
    for build in (build_a, build_b, build_c):
        p = build()
        print(f"built {p.name}")
