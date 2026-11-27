
def get_irrigation_decision(
    rainfall_deviation_pct,
    predicted_yield_current,
    predicted_yield_normal,
    dry_spell_days,
    soil_adequacy_index,
    crop_name="Rice"
):
    """
    Converts weather deficit + ML yield-drop risk into a 3-tier advisory:
    'Safe', 'Monitor', or 'Irrigate Now'.
    """
    # 1. Calculate % yield drop caused by current rainfall deficit
    if predicted_yield_normal > 0:
        yield_drop_pct = ((predicted_yield_normal - predicted_yield_current) / predicted_yield_normal) * 100.0
    else:
        yield_drop_pct = 0.0

    # 2. High water-sensitivity crops need earlier protection
    water_sensitive_crops = {"rice", "sugarcane", "banana", "potato", "cotton(lint)", "wheat"}
    is_sensitive = str(crop_name).strip().lower() in water_sensitive_crops

    # Adjust thresholds slightly if soil adequacy is poor (< 0.5)
    deficit_trigger = -18.0 if (is_sensitive or soil_adequacy_index < 0.5) else -22.0
    dry_spell_trigger = 12 if is_sensitive else 15

    # 3. Decision Logic (IMD Deficient = <= -20% rainfall deviation)
    if (rainfall_deviation_pct <= deficit_trigger) and (yield_drop_pct >= 10.0 or dry_spell_days >= dry_spell_trigger):
        status = "Irrigate Now"
        reason = (
            f"Genuine yield-threatening deficit: rainfall is {rainfall_deviation_pct:.1f}% below normal, "
            f"predicted yield drop is {yield_drop_pct:.1f}%, dry spell is {dry_spell_days} days."
        )
    elif (rainfall_deviation_pct <= -10.0) or (dry_spell_days >= 7 and yield_drop_pct >= 5.0):
        status = "Monitor"
        reason = (
            f"Moderate moisture watch: rainfall deviation {rainfall_deviation_pct:.1f}%, "
            f"predicted yield risk {yield_drop_pct:.1f}%. Hold irrigation and re-check in 3 days."
        )
    else:
        status = "Safe"
        reason = (
            f"Normal variability: rainfall deviation ({rainfall_deviation_pct:.1f}%) and "
            f"yield risk ({yield_drop_pct:.1f}%) are within safe bounds. No irrigation needed."
        )

    return {
        "decision": status,
        "yield_drop_pct": round(yield_drop_pct, 2),
        "reason": reason
    }
