def uniform_load_capacity(h, b, L, d, As, fck, fyk,
                                          alpha_cc=0.85, gamma_c=1.5, gamma_s=1.15):
    """
    Compute uniform load capacity (kN/m) for a simply supported,
    singly reinforced rectangular concrete beam using Eurocode-like design.
    Inputs:
      h, b, L, d, As  : geometry in mm (L = span in m)
      fck, fyk        : characteristic strengths in MPa (N/mm^2)
    Optional:
      alpha_cc, gamma_c, gamma_s : defaults 0.85, 1.5, 1.15 (Eurocode typical)
    Returns:
      w_design_kN_per_m : design uniform load in kN/m
    """
    from math import isfinite

    if not (h > 0 and b > 0 and L > 0 and d > 0 and As > 0):
        raise ValueError("All geometric inputs must be positive (in mm).")
    if not isfinite(fck) or not isfinite(fyk):
        raise ValueError("Material strengths must be finite numbers.")

    # Convert L to mm
    L = L*1000

    # Design strengths (N/mm^2)
    fcd = alpha_cc * fck / gamma_c   # concrete design compressive stress
    fyd = fyk / gamma_s              # steel design yield

    # Whitney rectangular stress block (Eurocode-like simple approach)
    a = As * fyd / (fcd * b)         # depth of equivalent rectangular block (mm)
    z = d - a / 2.0                  # internal lever arm (mm)
    if z <= 0:
        raise ValueError("Resulting lever arm z <= 0 (check As, d, fck, fyk).")

    # Moment capacity (N*mm -> kN*m)
    M_Nmm = As * fyd * z
    M_kNm = M_Nmm * 1e-6

    # Uniform load for simply supported beam: M = w * L^2 / 8
    L_m = L / 1000.0
    w_kN_per_m = (8.0 * M_kNm) / (L_m**2)

    return w_kN_per_m