import math

def i_beam_uniform_load_capacity(h, b, r, tw, tf, L, fy=250.0):
    """
    Calculate uniform load capacity (kN/m) of a symmetric steel I-beam on a simply supported span.
    Units:
      h, b, r, tw, tf: mm
      L: m
      fy: MPa (N/mm^2)
    Returns:
      { 'I_mm4': ..., 'S_mm3': ..., 'M_resisting_kNm': ..., 'w_allow_kN_per_m': ... }
    """
    # Basic checks
    if L <= 0:
        raise ValueError("Span L must be > 0 (m).")
    if any(x <= 0 for x in (h, b, tw, tf)):
        raise ValueError("h, b, tw, tf must be positive (mm).")

    # web clear height (approx) excluding flange thickness
    hw = h - 2.0 * tf
    if hw <= 0:
        raise ValueError("Web height hw = h - 2*tf <= 0. Check geometry.")

    # Areas
    A_flange = b * tf            # mm^2
    A_web = tw * hw              # mm^2

    # Second moment of area (about horizontal centroidal axis through mid-height)
    # flange contribution (about its own centroid): b*tf^3/12
    I_flange_about_centroid = b * tf**3 / 12.0  # mm^4
    # distance from flange centroid to neutral axis:
    dy = (h / 2.0) - (tf / 2.0)  # mm
    # Parallel axis
    I_flange_total_each = I_flange_about_centroid + A_flange * dy**2

    # web inertia about centroid (vertical rectangle)
    I_web = tw * hw**3 / 12.0    # mm^4

    # total I (two flanges + web)
    I_total = 2.0 * I_flange_total_each + I_web  # mm^4

    # Elastic section modulus S = I / (h/2)
    c = h / 2.0  # distance to extreme fiber (mm)
    S = I_total / c  # mm^3

    # Resisting moment (elastic) M = S * fy (fy in N/mm^2 => M in N*mm)
    # Convert to N*m (divide by 1e6) and to kN*m (divide by 1e6 then /1000 => /1e6 already gives N*m; convert to kN*m by /1000)
    M_resisting_Nmm = S * fy  # N*mm
    M_resisting_Nm = M_resisting_Nmm / 1e6  # N*m
    M_resisting_kNm = M_resisting_Nm / 1000.0  # kN*m

    # Uniform load capacity for simply supported beam: max moment = w*L^2/8 => w = 8*M / L^2
    # Use M in N*m to get w in N/m, then convert to kN/m
    w_allow_N_per_m = 8.0 * M_resisting_Nm / (L**2)  # N/m
    w_allow_kN_per_m = w_allow_N_per_m / 1000.0      # kN/m

    return {
        'I_mm4': I_total,
        'S_mm3': S,
        'M_resisting_kNm': M_resisting_kNm,
        'w_allow_kN_per_m': w_allow_kN_per_m,
        'area_flange_mm2': A_flange,
        'area_web_mm2': A_web,
        'hw_mm': hw
    }

# Example usage:
if __name__ == "__main__":
    # Example geometry (mm) and span (m)
    h = 300.0   # mm
    b = 150.0   # mm
    r = 10.0    # mm (ignored in inertia calc)
    tw = 8.0    # mm
    tf = 12.0   # mm
    L = 6.0     # m
    fy = 355.0  # MPa

    res = i_beam_uniform_load_capacity(h, b, r, tw, tf, L, fy=fy)
    print("I (mm^4):", round(res['I_mm4'], 2))
    print("S (mm^3):", round(res['S_mm3'], 2))
    print("Resisting moment M (kN·m):", round(res['M_resisting_kNm'], 3))
    print("Allowable uniform load w (kN/m):", round(res['w_allow_kN_per_m'], 3))
