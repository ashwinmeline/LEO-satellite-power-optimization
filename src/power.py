def calculate_required_capacity(eclipse_duration_s, p_payload_w, dod=0.3, eta=0.92):
    # Energy [Joules] = Power * Time
    energy_joules = (p_payload_w * eclipse_duration_s) / (dod * eta)
    return energy_joules / 3600  # Convert to Watt-hours