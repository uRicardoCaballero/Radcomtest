# In app/utils.py (or a similar file)
from datetime import datetime

def aplicar_descuento(cliente):
    """Applies the special yearly discount if the client pays for the entire year early."""
    now = datetime.now()
    if cliente.es_libre():
        return 0
    
    # Special yearly discount logic
    if now.month == 1 or now.month == 2:  # January, pay 10 months
        return float(cliente.plan_pago) * (10 / 12)
    elif now.month == 3:  # March, pay 9 months
        return float(cliente.plan_pago) * (9 / 12)
    else:  # After March, no discounts, just pay the full remaining months
        return float(cliente.plan_pago)