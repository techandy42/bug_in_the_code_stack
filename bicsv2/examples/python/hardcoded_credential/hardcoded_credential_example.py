import stripe

def create_customer(email, name):
    stripe.api_key = "sk-1234567890abcdef1234567890abcdef"

    customer = stripe.Customer.create(
        email=email,
        name=name
    )
    return customer
