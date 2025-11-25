"""
i_beam_capacity.py

Compute section properties and uniform load bending capacity for a symmetric I-beam
using the rectangular-flange + web approximation (fillets ignored).

Inputs are in the same units you gave (mm for geometry, MPa for fy, m for span L).

Outputs: I (mm^4), S (mm^3), Z (mm^3), My & Mp (kN·m), and uniform load w (kN/m)
for both elastic (first-yield) and plastic capacities for a simply supported beam.

Usage: python i_beam_capacity.py

"""

def uniform_load_capacity(h, b, tw, tf, L, fy):
    """
    Compute elastic and plastic uniform load capacity (kN/m) for a simply
    supported I‑beam using flange+web approximation.
    Inputs: geometry in mm, L in m, fy in MPa.
    Returns: (w_elastic, w_plastic).
    """
    from math import isfinite

    hw = h - 2.0 * tf
    if hw <= 0:
        raise ValueError("Invalid geometry: tf too large relative to h.")

    # Areas
    A_flange = b * tf
    d = (h/2.0) - (tf/2.0)

    # Inertia
    I_flange_centroid = (b * tf**3) / 12.0
    I_flange_total = I_flange_centroid + A_flange * d**2
    I_web = (tw * hw**3) / 12.0
    I = 2.0 * I_flange_total + I_web

    S = I / (h/2.0)
    Z = 2.0 * (A_flange * d) + (tw * hw**2) / 4.0

    My = fy * S * 1e-6
    Mp = fy * Z * 1e-6

    if L <= 0 or not isfinite(L):
        raise ValueError("Span L must be positive.")

    w_elastic = 8.0 * My / (L**2)
    w_plastic = 8.0 * Mp / (L**2)
    return w_elastic

