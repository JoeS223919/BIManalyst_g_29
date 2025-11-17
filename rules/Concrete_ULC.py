def concrete_uniform_load_capacity(h, b, L, d, As, fck, fyk):
    """
    Compute uniform load capacity (kN/m) for a simply supported
    singly reinforced rectangular concrete beam governed by bending.
    
    Inputs:
        h   : total height (mm)
        b   : width (mm)
        L   : span (mm)
        d   : effective depth (mm)
        As  : steel area (mm^2)
        fck : concrete strength (MPa = N/mm^2)
        fyk : steel yield strength (MPa = N/mm^2)

    Returns:
        w   : uniform load capacity (kN/m)
    """

    from math import isfinite

    if L <= 0 or not isfinite(L):
        raise ValueError("Span L must be positive.")

    # --- Material design limits (no partial factors unless user asks) ---
    fcd = 0.85 * fck     # concrete design compressive block stress (N/mm^2)
    fyd = fyk            # steel yield (no safety factors here)

    # --- Neutral axis depth (a) and lever arm z ---
    # Whitney rectangular stress block: a = As * fyd / (0.85 fck * b)
    a = As * fyd / (fcd * b)          # mm
    z = d - a / 2.0                   # mm

    # --- Bending moment capacity ---
    M_Nmm = As * fyd * z              # N·mm

    # Convert to kN·m
    M_kNm = M_Nmm * 1e-6

    # --- Uniform load capacity ---
    # For a simply supported beam:
    #     M = w * L^2 / 8   →   w = 8M / L^2
    # L is in mm   → convert to meters where needed
    L_m = L / 1000.0
    w = (8.0 * M_kNm) / (L_m**2)      # kN/m

    return w
