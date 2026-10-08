def is_bonus_eligible(employee):
    return (
        employee["active"]
        and employee["months"] >= 12
        and employee["rating"] >= 4
        and not employee["disciplinary_action"]
        and employee["attendance"] >= 90
    )


employee = {
    "active": True,
    "months": 15,
    "rating": 4,
    "disciplinary_action": False,
    "attendance": 95
}

print(is_bonus_eligible(employee))
