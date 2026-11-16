"""Checkout module for the online shopping application."""


def apply_student_discount(total, is_student):
    """Apply a 10% student discount when the customer is a student."""
    if is_student:
        return total * 0.90
    return total


def checkout(total, is_student=False):
    """Print the purchase total and return the amount to charge."""
    print(f"Original purchase total: GBP {total:.2f}")
    final = apply_student_discount(total, is_student)
    print(f"Final purchase total:   GBP {final:.2f}")
    return final
