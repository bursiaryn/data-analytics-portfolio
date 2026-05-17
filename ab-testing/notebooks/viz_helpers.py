"""Reusable visualization helpers for portfolio dashboards.

Three primitives used across all dashboard notebooks:
- kpi_card           : rounded box with bold value + subdued label
- annotate_top_n     : value labels on every bar in a bar/barh plot
- add_benchmark_line : threshold/baseline reference line with optional text label
"""
from typing import Optional, Sequence

import matplotlib.patches as mpatches
from matplotlib.axes import Axes


PALETTE = {
    'BLUE':    '#2563EB',
    'LIGHT':   '#93C5FD',
    'LIGHTER': '#DBEAFE',
    'RED':     '#DC2626',
    'AMBER':   '#F59E0B',
    'GREEN':   '#059669',
    'GRAY':    '#6B7280',
    'BG':      '#F8FAFC',
    'CARD_BG': '#FFFFFF',
}


def add_benchmark_line(
    ax: Axes,
    value: float,
    *,
    orientation: str = 'h',
    label: Optional[str] = None,
    color: str = '#6B7280',
    linestyle: str = '--',
    linewidth: float = 1.2,
    alpha: float = 0.7,
    fontsize: int = 8,
) -> None:
    """Draw a reference/threshold line at ``value`` with optional inline label.

    Parameters
    ----------
    orientation : 'h' for axhline, 'v' for axvline
    label       : if given, text is placed at the line's endpoint
    """
    if orientation == 'h':
        ax.axhline(value, color=color, linestyle=linestyle,
                   linewidth=linewidth, alpha=alpha)
        if label:
            xlim = ax.get_xlim()
            ax.text(xlim[1], value, f' {label}', color=color,
                    fontsize=fontsize, ha='right', va='bottom')
    elif orientation == 'v':
        ax.axvline(value, color=color, linestyle=linestyle,
                   linewidth=linewidth, alpha=alpha)
        if label:
            ylim = ax.get_ylim()
            ax.text(value, ylim[1], f' {label}', color=color,
                    fontsize=fontsize, ha='left', va='top', rotation=90)
    else:
        raise ValueError("orientation must be 'h' or 'v'")


def annotate_top_n(
    ax: Axes,
    values: Sequence[float],
    *,
    orientation: str = 'h',
    fmt: str = '{:,.0f}',
    offset_frac: float = 0.01,
    fontsize: int = 8,
    fontweight: str = 'normal',
    color: str = '#1E293B',
) -> None:
    """Annotate each bar in a bar/barh plot with its value.

    Parameters
    ----------
    orientation : 'h' (barh, label at right) or 'v' (bar, label on top)
    fmt         : Python format string, e.g. '{:.1%}', 'R${:,.0f}'
    offset_frac : fraction of axis range to offset label from bar end
    """
    if orientation == 'h':
        xr = ax.get_xlim()[1] - ax.get_xlim()[0]
        dx = xr * offset_frac
        for i, v in enumerate(values):
            ax.text(v + dx, i, fmt.format(v), va='center',
                    fontsize=fontsize, fontweight=fontweight, color=color)
    elif orientation == 'v':
        yr = ax.get_ylim()[1] - ax.get_ylim()[0]
        dy = yr * offset_frac
        for i, v in enumerate(values):
            ax.text(i, v + dy, fmt.format(v), ha='center',
                    fontsize=fontsize, fontweight=fontweight, color=color)
    else:
        raise ValueError("orientation must be 'h' or 'v'")


def kpi_card(
    ax: Axes,
    label: str,
    value: str,
    *,
    color: str = '#2563EB',
    label_color: str = '#6B7280',
    edge_color: str = '#DBEAFE',
    fontsize_value: int = 18,
    fontsize_label: int = 10,
) -> None:
    """Render a KPI card (rounded box + bold value + subdued label) on ``ax``.

    The Axes is cleaned (no spines, no ticks). Use one Axes per card from a
    GridSpec row. Long values auto-shrink so they don't overflow the box.
    """
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    for spine in ax.spines.values():
        spine.set_visible(False)
    rect = mpatches.FancyBboxPatch(
        (0, 0), 1, 1,
        boxstyle='round,pad=0.05',
        facecolor='#FFFFFF',
        edgecolor=edge_color,
        linewidth=1.5,
        transform=ax.transAxes,
        clip_on=False,
    )
    ax.add_patch(rect)
    fs = max(12, fontsize_value - 4) if len(value) > 14 else fontsize_value
    ax.text(0.5, 0.60, value, ha='center', va='center',
            fontsize=fs, fontweight='bold', color=color,
            transform=ax.transAxes)
    ax.text(0.5, 0.22, label, ha='center', va='center',
            fontsize=fontsize_label, color=label_color,
            transform=ax.transAxes)
