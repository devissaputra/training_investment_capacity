#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

INK = "#172033"
SOFT = "#475569"
GRAY = "#64748b"
GRID = "#e2e8f0"
NAVY = "#0f3d75"
ORANGE = "#ea580c"
BLUE = "#2563eb"
GREEN = "#16a34a"
PURPLE = "#7c3aed"
GOLD = "#f59e0b"
RED = "#dc2626"
CYAN = "#0891b2"


def esc(value):
    return html.escape(str(value))


def text(x, y, value, size=16, weight="400", anchor="start", fill=INK):
    return (
        f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
        f'fill="{fill}">{esc(value)}</text>'
    )


def line(x1, y1, x2, y2, stroke=GRID, width=1, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{stroke}" stroke-width="{width}"{extra}/>'
    )


def box(x, y, width, height, title, body, fill, stroke, title_fill=INK):
    output = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="15" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>',
        text(x + 18, y + 31, title, 16, "700", "start", title_fill),
    ]
    for index, item in enumerate(body):
        output.append(
            text(x + 18, y + 57 + index * 21, item, 12.5, "400", "start", SOFT)
        )
    return "".join(output)


def arrow(x1, y1, x2, y2, color=GRAY):
    return (
        line(x1, y1, x2 - 12, y2, color, 2)
        + f'<polygon points="{x2-12},{y2-6} {x2},{y2} {x2-12},{y2+6}" fill="{color}"/>'
    )


def read_csv(name):
    with (ROOT / "data/derived" / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def research_design():
    rows = read_csv("primary_results.csv")
    years = [int(row["year"]) for row in rows]
    spend = [float(row["per_employee_gbp_2024_prices"]) for row in rows]
    reach = [float(row["training_coverage_share"]) for row in rows]

    output = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<rect width="1200" height="92" fill="{NAVY}"/>',
        text(52, 43, "UK Employer Training Investment: Reach vs Real Intensity", 30, "700", "start", "#ffffff"),
        text(52, 72, "Comparable UK-wide ESS waves • expenditure in 2024 prices", 15, "400", "start", "#dbeafe"),
    ]

    left, right, top, bottom = 100, 820, 130, 585

    def sx(value):
        return left + (value - 2011) / (2024 - 2011) * (right - left)

    def sy_spend(value):
        return bottom - (value - 1600) / (2500 - 1600) * (bottom - top)

    def sy_reach(value):
        return bottom - (value - 0.52) / (0.66 - 0.52) * (bottom - top)

    output.append(
        f'<rect x="{sx(2022)-28}" y="{top}" width="{sx(2024)-sx(2022)+56}" '
        f'height="{bottom-top}" fill="#fff7ed" opacity="0.65"/>'
    )

    for value in (1600, 1800, 2000, 2200, 2400):
        y = sy_spend(value)
        output.extend(
            [
                line(left, y, right, y),
                text(left - 14, y + 5, f"£{value:,}", 12, "400", "end", ORANGE),
            ]
        )

    for value in (0.54, 0.58, 0.62, 0.66):
        output.append(
            text(right + 14, sy_reach(value) + 5, f"{round(value*100)}%", 12, "400", "start", BLUE)
        )

    for year in years:
        x = sx(year)
        output.extend(
            [
                line(x, top, x, bottom, "#f1f5f9"),
                text(x, bottom + 30, year, 12, "600", "middle", GRAY),
            ]
        )

    spend_points = " ".join(
        f"{sx(year)},{sy_spend(value)}" for year, value in zip(years, spend)
    )
    reach_points = " ".join(
        f"{sx(year)},{sy_reach(value)}" for year, value in zip(years, reach)
    )

    output.extend(
        [
            f'<polyline points="{spend_points}" fill="none" stroke="{ORANGE}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>',
            f'<polyline points="{reach_points}" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>',
        ]
    )

    for year, s, r in zip(years, spend, reach):
        output.extend(
            [
                f'<circle cx="{sx(year)}" cy="{sy_spend(s)}" r="6.5" fill="#fff" stroke="{ORANGE}" stroke-width="3"/>',
                f'<circle cx="{sx(year)}" cy="{sy_reach(r)}" r="6.5" fill="#fff" stroke="{BLUE}" stroke-width="3"/>',
            ]
        )

    output.extend(
        [
            line(left, bottom, right, bottom, "#334155", 1.7),
            line(left, top, left, bottom, "#334155", 1.7),
            line(right, top, right, bottom, "#334155", 1.7),
            text((left + right) / 2, 660, "Survey year", 14, "600", "middle"),
            f'<text x="28" y="{(top+bottom)/2}" transform="rotate(-90 28 {(top+bottom)/2})" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" '
            f'text-anchor="middle" fill="{ORANGE}">Real spend per employee</text>',
            f'<text x="866" y="{(top+bottom)/2}" transform="rotate(90 866 {(top+bottom)/2})" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" '
            f'text-anchor="middle" fill="{BLUE}">Derived training reach</text>',
            line(160, 110, 200, 110, ORANGE, 5),
            text(210, 115, "Real spend / employee", 12.5, "700"),
            line(390, 110, 430, 110, BLUE, 5),
            text(440, 115, "Trainees / employees", 12.5, "700"),
            '<rect x="900" y="128" width="250" height="208" rx="16" fill="#f8fafc" stroke="#cbd5e1"/>',
            text(925, 160, "Long-run investment", 16, "700"),
            text(925, 195, "2011", 12, "600", "start", GRAY),
            text(1125, 195, "£2,410", 17, "700", "end", ORANGE),
            text(925, 230, "2024", 12, "600", "start", GRAY),
            text(1125, 230, "£1,700", 17, "700", "end", ORANGE),
            text(925, 274, "Real change", 12, "600", "start", GRAY),
            text(1125, 274, "−29.46%", 22, "700", "end", RED),
            text(925, 310, "Lowest level in series", 12, "600", "start", "#7c2d12"),
            '<rect x="900" y="365" width="250" height="220" rx="16" fill="#eff6ff" stroke="#93c5fd"/>',
            text(925, 398, "2022 → 2024 divergence", 15, "700", "start", "#1d4ed8"),
            text(925, 435, "Spend / employee", 12, "600", "start", GRAY),
            text(925, 461, "£1,960 → £1,700", 18, "700", "start", ORANGE),
            text(925, 496, "Reach proxy", 12, "600", "start", GRAY),
            text(925, 522, "60.22% → 62.85%", 18, "700", "start", BLUE),
            text(925, 557, "Reach +2.63 pp", 12.5, "700", "start", BLUE),
            text(52, 704, "2019 is omitted from the comparable UK-wide series because Scotland did not participate. Reach is derived from published trainee and employee counts.", 12, "400", "start", GRAY),
            "</svg>",
        ]
    )
    return "".join(output)


def method():
    output = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<rect width="1200" height="92" fill="#312e81"/>',
        text(52, 43, "Employer Training Investment — Reproducible Analysis", 30, "700", "start", "#ffffff"),
        text(52, 72, "Official ESS data → comparable waves → reach/intensity separation → sector evidence", 15, "400", "start", "#e0e7ff"),
        box(45, 135, 205, 125, "1 • Official data", ["7,848 ESS rows", "National + sector data", "Pinned SHA-256"], "#eff6ff", "#3b82f6", "#1d4ed8"),
        box(290, 135, 205, 125, "2 • Comparable UK", ["2011 / 13 / 15 / 17", "2022 / 2024", "2019 excluded"], "#f5f3ff", "#8b5cf6", "#6d28d9"),
        box(535, 135, 205, 125, "3 • Real intensity", ["2024-price fields", "Spend / employee", "Spend / trainee"], "#fff7ed", "#f59e0b", "#92400e"),
        box(780, 135, 205, 125, "4 • Reach proxy", ["Trainees / employees", "Approx. aggregate ratio", "Keep derivation visible"], "#eff6ff", "#3b82f6", "#1d4ed8"),
        arrow(250, 198, 290, 198),
        arrow(495, 198, 535, 198),
        arrow(740, 198, 780, 198),
        box(780, 335, 205, 135, "5 • Longitudinal", ["Six-wave trajectory", "Endpoint changes", "2022–24 divergence"], "#fef2f2", "#ef4444", "#991b1b"),
        arrow(882, 260, 882, 335, RED),
        box(505, 335, 225, 135, "6 • Sector evidence", ["13 sectors in 2024", "Range / ratio / median", "Unweighted CV"], "#f0fdf4", "#22c55e", "#15803d"),
        arrow(780, 402, 730, 402, GREEN),
        box(230, 335, 225, 135, "7 • Triangulate", ["Total expenditure", "Per-person intensity", "Reach"], "#ecfeff", "#06b6d4", "#0e7490"),
        arrow(505, 402, 455, 402, CYAN),
        box(230, 540, 755, 105, "8 • Bounded L&D interpretation", ["Separate reach, resource intensity, and sector context before judging training capacity", "Do not infer quality, transfer, skill gain, or causal ROI from expenditure alone"], "#f8fafc", "#94a3b8", "#334155"),
        arrow(342, 470, 342, 540, CYAN),
        arrow(618, 470, 618, 540, GREEN),
        arrow(882, 470, 882, 540, RED),
        text(52, 700, "Scientific safeguard: official estimates, repository-derived ratios, and interpretation remain explicitly separated.", 13, "700", "start", "#334155"),
        "</svg>",
    ]
    return "".join(output)


def architecture():
    rows = read_csv("secondary_results.csv")
    output = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="760" viewBox="0 0 1200 760">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<rect width="1200" height="92" fill="#064e3b"/>',
        text(52, 43, "2024 Sector Training Investment Intensity", 30, "700", "start", "#ffffff"),
        text(52, 72, "Real spend per employee • all 13 published UK sectors", 15, "400", "start", "#d1fae5"),
    ]

    left, right, top, row_gap, max_value = 315, 1080, 125, 43, 2800

    for value in (0, 500, 1000, 1500, 2000, 2500):
        x = left + value / max_value * (right - left)
        output.extend(
            [
                line(x, top - 10, x, 690),
                text(x, 715, f"£{value:,}", 11.5, "400", "middle", GRAY),
            ]
        )

    for index, row in enumerate(rows):
        value = float(row["per_employee_gbp"])
        y = top + index * row_gap
        width = value / max_value * (right - left)
        fill = ORANGE if index == 0 else RED if index == len(rows) - 1 else GREEN
        output.extend(
            [
                text(left - 18, y + 18, row["sector"], 12.5, "600", "end", "#334155"),
                f'<rect x="{left}" y="{y}" width="{width}" height="24" rx="6" fill="{fill}" fill-opacity="0.82"/>',
                text(left + width + 10, y + 18, f"£{int(value):,}", 11.5, "700", "start", fill),
            ]
        )

    output.extend(
        [
            '<rect x="835" y="625" width="300" height="85" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>',
            text(858, 655, "Observed max / min", 12, "600", "start", GRAY),
            text(1110, 655, "2.86×", 18, "700", "end", PURPLE),
            text(858, 685, "Unweighted median", 12, "600", "start", GRAY),
            text(1110, 685, "£1,570", 18, "700", "end", GREEN),
            text(52, 744, "Sector differences are descriptive resource-intensity differences, not rankings of training quality or effectiveness.", 12, "400", "start", GRAY),
            "</svg>",
        ]
    )
    return "".join(output)


def evaluation():
    output = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="660" viewBox="0 0 1200 660">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<rect width="1200" height="92" fill="#7c2d12"/>',
        text(52, 43, "Evidence Boundary for Employer Training Investment", 30, "700", "start", "#ffffff"),
        text(52, 72, "What the official aggregate data support — and what they do not", 15, "400", "start", "#ffedd5"),
        box(55, 115, 1090, 96, "Long-run real intensity", ["Spend per employee: £2,410 → £1,700 (−29.46%); spend per trainee: −38.69%; total real expenditure: −18.53%."], "#fff7ed", "#f59e0b", "#92400e"),
        box(55, 235, 1090, 96, "Reach-intensity divergence", ["2022→2024 derived reach: 60.22% → 62.85%, while spend per employee fell £1,960 → £1,700."], "#eff6ff", "#3b82f6", "#1d4ed8"),
        box(55, 355, 1090, 96, "Sector heterogeneity", ["2024 spend per employee ranges £920–£2,630; national averages do not describe every sector's resource environment."], "#f0fdf4", "#22c55e", "#15803d"),
        box(55, 475, 1090, 96, "Claim boundary", ["Expenditure and reach do not directly measure training quality, learning transfer, skill gain, causal ROI, or latent organizational capability."], "#fef2f2", "#ef4444", "#991b1b"),
        text(52, 635, "L&D use: treat reach, resource intensity, and outcome evidence as separate layers when diagnosing training capacity.", 13, "700", "start", "#334155"),
        "</svg>",
    ]
    return "".join(output)


def render(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    figures = {
        "research_design.svg": research_design(),
        "method.svg": method(),
        "architecture.svg": architecture(),
        "evaluation.svg": evaluation(),
    }
    for name, content in figures.items():
        ET.fromstring(content)
        (out_dir / name).write_text(content, encoding="utf-8")
    return figures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=str(ROOT / "assets"))
    args = parser.parse_args()
    figures = render(Path(args.out_dir))
    print("generated_figures:", len(figures))


if __name__ == "__main__":
    main()
