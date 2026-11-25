"""Draw the original front page for 25 November 2026 (build-time only).

This script is NOT the graded program: it runs once here, with Pillow
and local fonts, to produce entry.png. The graded program (main.py)
only copies that PNG with the standard library. Every shape and word
below is drawn from scratch in this session; no photo or artwork is
copied in. Layout: 1024x1024, one masthead, one lead story, five
supporting stories, one footer line.
"""

import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 227)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (14, 42, 74)
SKY = (16, 52, 96)
GOLD = (201, 162, 39)
GREY = (90, 88, 82)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def centred(draw, y, text, fnt, fill=INK):
    draw.text((W / 2, y), text, font=fnt, fill=fill, anchor="ma")


def stars(draw, seed=7):
    rng = random.Random(seed)
    for _ in range(70):
        x = rng.randint(40, 545)
        y = rng.randint(205, 420)
        r = rng.choice([1, 1, 2, 2, 3])
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255))


def rocket_scene(draw):
    # Sky panel, left half of the lead story.
    draw.rectangle([28, 196, 560, 560], fill=SKY)
    stars(draw)
    # Earth arc, kept wholly inside the sky panel (panel ends at y=560).
    draw.ellipse([-120, 430, 340, 560], fill=(38, 110, 180))
    draw.arc([-120, 430, 340, 560], 180, 360, fill=(255, 255, 255), width=3)
    for cx, cy, rx, ry in [(40, 505, 60, 24), (180, 525, 50, 20), (285, 510, 40, 18)]:
        draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(74, 160, 90))
    for cx, cy, rx, ry in [(90, 470, 52, 10), (225, 478, 46, 9)]:
        draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(255, 255, 255))
    # Space station, top right of the panel.
    draw.rectangle([412, 232, 492, 252], fill=(120, 170, 220), outline=INK, width=2)
    for px in (352, 492):
        draw.rectangle([px, 236, px + 56, 248], fill=(50, 110, 190), outline=INK, width=2)
        for gx in range(px + 14, px + 56, 14):
            draw.line([gx, 236, gx, 248], fill=INK, width=1)
    draw.rectangle([446, 246, 458, 262], fill=(220, 220, 220), outline=INK, width=2)
    # Rocket, climbing diagonally. Body, nose, fins, window, flame.
    body = [(300, 470), (340, 400), (360, 330), (330, 300), (300, 330), (280, 400)]
    draw.polygon(body, fill=(245, 245, 245), outline=INK, width=3)
    draw.polygon([(330, 300), (360, 330), (330, 335)], fill=RED, outline=INK, width=2)
    draw.polygon([(300, 470), (280, 400), (262, 452)], fill=RED, outline=INK, width=2)
    draw.polygon([(300, 470), (340, 400), (362, 448)], fill=RED, outline=INK, width=2)
    draw.ellipse([306, 352, 336, 382], fill=(140, 200, 235), outline=INK, width=2)
    draw.polygon([(296, 470), (312, 520), (322, 470)], fill=(255, 140, 0), outline=INK, width=2)
    draw.polygon([(304, 470), (312, 498), (320, 470)], fill=(255, 220, 60))
    draw.text((44, 536), "SHENZHOU-24  •  LONG MARCH-2F", font=font(SANS_B, 16), fill=(255, 255, 255))


def vignette_bank(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(232, 226, 205))
    cx = x + w // 2
    draw.polygon([(cx - 52, y + 14), (cx + 52, y + 14), (cx, y - 2 + 14)], fill=NAVY)
    for i in (-36, 0, 36):
        draw.rectangle([cx + i - 7, y + 20, cx + i + 7, y + 44], fill=(255, 255, 255), outline=INK, width=2)
    draw.rectangle([cx - 52, y + 46, cx + 52, y + 50], fill=NAVY)


def vignette_chart(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(232, 226, 205))
    base = y + h - 10
    for i, bh in enumerate((18, 28, 40)):
        bx = x + 52 + i * 34
        draw.rectangle([bx, base - bh, bx + 20, base], fill=NAVY)
    draw.line([x + 36, base, x + w - 36, base], fill=INK, width=3)
    draw.ellipse([x + w - 92, y + 10, x + w - 52, y + 50], outline=RED, width=4)
    draw.line([x + w - 72, y + 30, x + w - 72, y + 16], fill=RED, width=4)
    draw.line([x + w - 72, y + 30, x + w - 60, y + 34], fill=RED, width=4)


def vignette_line(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(232, 226, 205))
    draw.ellipse([x + 30, y + 10, x + 62, y + 42], fill=GOLD, outline=INK, width=2)
    pts = [(x + 40, y + 44), (x + 100, y + 38), (x + 160, y + 26), (x + 230, y + 12)]
    draw.line(pts, fill=RED, width=4, joint="curve")
    draw.polygon([(x + 230, y + 12), (x + 212, y + 12), (x + 228, y + 24)], fill=RED)


def vignette_house(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(232, 226, 205))
    cx = x + w // 2
    draw.polygon([(cx - 46, y + 28), (cx, y + 6), (cx + 46, y + 28)], fill=RED, outline=INK, width=2)
    draw.rectangle([cx - 34, y + 28, cx + 34, y + 52], fill=(255, 255, 255), outline=INK, width=2)
    draw.polygon([(cx + 6, y + 30), (cx - 6, y + 40), (cx + 4, y + 40), (cx - 6, y + 52)], fill=GOLD, outline=INK, width=1)


def vignette_chess(draw, x, y, w, h):
    # A single checker strip with one white king piece: fits a short band.
    draw.rectangle([x, y, x + w, y + h], fill=(232, 226, 205))
    sq, by = 26, y + 12
    bx = x + w // 2 - 4 * sq
    for c in range(8):
        fill = INK if c % 2 == 0 else (255, 255, 255)
        draw.rectangle([bx + c * sq, by, bx + (c + 1) * sq, by + sq], fill=fill, outline=INK, width=1)
    draw.ellipse([bx + 3 * sq + 3, by - 8, bx + 4 * sq - 3, by + 18], fill=(255, 255, 255), outline=INK, width=2)
    draw.text((bx + 3 * sq + 13, by + 5), "K", font=font(SANS_B, 16), fill=INK, anchor="mm")


def story_box(draw, x, y, w, h, kicker, headline, sub, vignette):
    draw.rectangle([x, y, x + w, y + h], fill=(255, 253, 247), outline=INK, width=2)
    vignette(draw, x + 2, y + 2, w - 4, 52)
    draw.text((x + 14, y + 60), kicker, font=font(SANS_B, 16), fill=RED)
    lines = wrap(draw, headline, font(SANS_B, 24), w - 28)
    ty = y + 82
    for line in lines[:3]:
        draw.text((x + 14, ty), line, font=font(SANS_B, 24), fill=INK)
        ty += 28
    sub_lines = wrap(draw, sub, font(SANS, 17), w - 28)
    for line in sub_lines[:1]:
        draw.text((x + 14, ty + 4), line, font=font(SANS, 17), fill=GREY)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    draw.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)

    centred(draw, 22, "THE WORLD TODAY", font(SERIF, 76))
    draw.line([28, 116, 996, 116], fill=INK, width=2)
    draw.line([28, 122, 996, 122], fill=INK, width=5)
    centred(draw, 132, "WEDNESDAY,  25  NOVEMBER  2026", font(SANS_B, 31))
    centred(draw, 168, "EARLY EDITION  •  FROM REPORTS AVAILABLE EARLY IN THE DAY (UTC)", font(SANS, 17), fill=GREY)

    # Lead story: drawn scene left, words right. Panel is 196..560.
    rocket_scene(draw)
    draw.rectangle([560, 196, 996, 560], outline=INK, width=3)
    lx = 584
    draw.text((lx, 212), "SPACE  •  CHINA / PAKISTAN", font=font(SANS_B, 18), fill=RED)
    lead = wrap(draw, "FIRST PAKISTANI IN ORBIT", font(SERIF, 40), 996 - lx - 20)
    ty = 240
    for line in lead:
        draw.text((lx, ty), line, font=font(SERIF, 40), fill=INK)
        ty += 48
    draw.line([lx, ty + 8, 972, ty + 8], fill=GOLD, width=3)
    ty += 22
    body = wrap(draw, "Shenzhou-24 lifts off with Zeeshan Ali aboard, the first foreign visitor to China's Tiangong station.",
                font(SANS, 22), 996 - lx - 20)
    for line in body:
        draw.text((lx, ty), line, font=font(SANS, 22), fill=INK)
        ty += 30
    ty += 8
    for line in wrap(draw, "Short stay, running experiments.", font(SANS, 22), 996 - lx - 20):
        draw.text((lx, ty), line, font=font(SANS, 22), fill=INK)
        ty += 30
    draw.text((lx, 526), "Reuters, 25 November", font=font(SANS, 16), fill=GREY)

    draw.line([28, 574, 996, 574], fill=INK, width=3)

    boxes_top = [
        ("BANKS  •  VENEZUELA", "CITI WEIGHS A RETURN TO VENEZUELA",
         "Five years after its exit.", vignette_bank),
        ("ECONOMY  •  UNITED STATES", "US GDP AND INFLATION FIGURES DUE TODAY",
         "Due 8:30 a.m. ET.", vignette_chart),
        ("MARKETS  •  JAPAN", "NIKKEI SEEN RISING, SHORT OF RECORD",
         "Poll: 67,500 by end-2027.", vignette_line),
    ]
    xs = [28, 356, 684]
    for (kicker, head, sub, vig), x in zip(boxes_top, xs):
        story_box(draw, x, 588, 312, 192, kicker, head, sub, vig)

    boxes_bottom = [
        ("ENERGY  •  UNITED KINGDOM", "UK ENERGY PRICE CAP TO BE ANNOUNCED",
         "Households braced for higher bills in January.", vignette_house),
        ("SPORT  •  CHESS", "WORLD CHESS: GAME 2 TODAY",
         "Title match resumes in Geneva.", vignette_chess),
    ]
    for (kicker, head, sub, vig), x in zip(boxes_bottom, [28, 524]):
        story_box(draw, x, 794, 472, 164, kicker, head, sub, vig)

    centred(draw, 970, "Later developments are not shown: figures due today are shown as due, not as results.",
            font(SANS, 15), fill=GREY)

    out = Path(__file__).resolve().parent / "entry.png"
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} {out.stat().st_size} bytes")


if __name__ == "__main__":
    main()
