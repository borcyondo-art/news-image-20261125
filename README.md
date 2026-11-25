# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/borcyondo-art/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/borcyondo-art/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page newspaper front page summing up Wednesday 25 November 2026,
built from reports available early in the day (about 01:20 UTC). The
page is labelled an early edition on its face, and anything due later
in the day is shown as due — never as a result.

## What the page shows

- **Lead — "First Pakistani in orbit."** China's Shenzhou-24 lifted off
  on a Long March-2F rocket from Jiuquan at 08:18 local time on
  25 November, carrying Zeeshan Ali of Pakistan, the first Pakistani in
  orbit and the first foreign visitor to the Tiangong space station,
  for a short stay running experiments.
- **Citi weighs a return to Venezuela** — five years after its exit.
- **US GDP and inflation figures due today** — the PCE price index and
  the second reading of Q3 GDP, due 8:30 a.m. ET.
- **Nikkei seen rising, short of record** — a Reuters poll of
  strategists puts the index at 67,500 by the end of 2027.
- **UK energy price cap to be announced** — households braced for
  higher bills in January.
- **World chess: Game 2 today** — the Gukesh–Sindarov title match
  resumes in Geneva.

All drawings (rocket, Earth, station, bank, chart, house, chess strip)
are original shapes drawn in `render_frontpage.py`. No photograph or
artwork was copied in.

## Sources (one per story)

1. Shenzhou-24 — Reuters, "China's Shenzhou-24 space flight takes off
   with Pakistani national as first foreign astronaut", 25 Nov 2026.
2. Citi / Venezuela — Reuters, "Citi weighs return to Venezuela five
   years after exit, Bloomberg News reports", 25 Nov 2026 (reporting a
   Bloomberg News report).
3. US GDP / PCE due — Reuters Trading Day, 24 Nov 2026 ("two huge US
   economic data releases on the docket on Wednesday — PCE inflation
   for October, and the second reading of Q3 GDP"); schedule confirmed
   by Morningstar / Dow Jones Newswires, 24 Nov 2026.
4. Nikkei poll — Reuters, "Japan's Nikkei to rise next year but fall
   short of record as investors reassess AI trade", 25 Nov 2026.
5. UK energy price cap — BBC, 25 Nov 2026: "Households braced for
   soaring energy bills with new price cap to be announced."
6. Chess Game 2 — The Guardian's World Chess Championship 2026
   schedule: Game 2, Gukesh–Sindarov, Wednesday 25 Nov, Geneva.

## How to run

```sh
python3 main.py
# writes entry.png to $MAKEFUN_OUTPUT_DIR, or /output by default
```

`main.py` uses only the Python standard library, makes no network
calls, and copies the shipped `entry.png` byte for byte. The image
itself was produced during this build by `render_frontpage.py`
(Pillow + local DejaVu fonts, build-time only; not part of the graded
run).

## Verification (this build, 25 Nov 2026 ~01:30 UTC)

- Two runs from clean output directories: sha256 identical —
  `770877112e6ddb47251cfc69cee968a67475314bed8ed1259a0868c09374d50b`
  for the shipped asset and both outputs.
- Format: PNG magic bytes `89 50 4e 47 0d 0a 1a 0a`; dimensions
  1024×1024; size 108,676 bytes (≤ 1,048,576).
- Runtime: ~0.04 s per run (limit 60 s).
- Viewed at full size: every headline inside its box, no overlap, no
  garbled text, date unmistakable. Viewed at 300×300: masthead, date,
  lead headline and all five story headlines remain readable; the
  rocket scene still reads as a launch.

## Honest gaps

- Built at ~01:20–01:30 UTC, most of 25 November had not happened yet
  in the Americas/Europe. Later developments on 25 November are not
  shown, by design; the page says so.
- Stories announced on 24 November were deliberately left out even
  though they dominated 25 November morning coverage: the reported
  CIA/ODNI hack (CNN, 24 Nov), the WHO evacuation from the Akwe
  hospital in DR Congo (announced 24 Nov), the Senegal/CAS Africa Cup
  ruling (24 Nov), the Nvidia share fall (US trading, 24 Nov),
  Sooryavanshi's 204 off 53 balls (match played 24 Nov in Doha), and
  the NATO AWACS deployment to Poland (authorised 23–24 Nov). None is
  presented as 25 November news.
- The UK price-cap and chess items are "due / scheduled today" items,
  not results; the US figures had not been released at build time.
- The Nikkei 67,500 figure is a poll median forecast, labelled as a
  poll on the page.
