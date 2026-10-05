def clean_amount(raw_amount):
    """Convert a raw amount value into a clean, non-negative float."""
    value = float(raw_amount)
    # BUG: the negative-value check was accidently removed
    return round(value, 2)


def total_revenue(amounts):
    """Sum a list of raw amounts, cleaning each one first."""
    return round(sum(clean_amount(a) for a in amounts), 2)