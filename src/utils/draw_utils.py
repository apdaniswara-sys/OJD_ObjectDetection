# draw_utils.py - helper functions to draw a modern side panel
import cv2
import numpy as np
import random

# simple deterministic color palette to make reproducible colors
COLOR_PALETTE = [
    (52, 152, 219),   # blue
    (46, 204, 113),   # green
    (231, 76, 60),    # red
    (155, 89, 182),   # purple
    (241, 196, 15),   # yellow
    (26, 188, 156),   # turquoise
    (149, 165, 166),  # gray
]

def _get_color_for_label(label):
    # deterministic color choice
    idx = abs(hash(label)) % len(COLOR_PALETTE)
    return COLOR_PALETTE[idx]

def draw_side_panel(frame, counts, panel_width=320):
    """Return a combined image where the right side is a modern panel showing counts."""
    h, w = frame.shape[:2]
    panel = np.zeros((h, panel_width, 3), dtype=np.uint8)
    # semi-transparent background
    panel[:] = (30, 30, 30)
    overlay = panel.copy()
    alpha = 0.85
    cv2.addWeighted(overlay, alpha, panel, 1 - alpha, 0, panel)

    # Title
    title = "Object Count"
    cv2.putText(panel, title, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 2, cv2.LINE_AA)
    y = 90
    # draw each count as a colored badge
    for label, cnt in counts.items():
        color = _get_color_for_label(label)
        # draw badge rectangle
        cv2.rectangle(panel, (18, y-28), (panel_width-18, y+6), color, -1)
        # text label on badge (white)
        text = f" {label}: {cnt} "
        cv2.putText(panel, text, (30, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2, cv2.LINE_AA)
        y += 50

    # total
    total = sum(counts.values())
    cv2.putText(panel, f"Total: {total}", (20, h-40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (200,200,200), 2, cv2.LINE_AA)

    # combine
    combined = np.hstack((frame, panel))
    return combined
