import random
import csv

# Random text generation function
def random_text():
    texts = ["return policy", "payment options", "delivery options", "seller information",
             "buyer protection", "seller performance", "shipping cost", "item condition",
             "warranty information", "product description", "item location", "shipping time",
             "customer service", "feedback", "contact seller", "item specifics", "payment methods",
             "returns accepted", "taxes", "shipping and handling", "discounts", "offer and bidding",
             "auction style listings", "fixed price listings", "best offer", "counter offer",
             "private listings", "second chance offer", "shipping services", "package tracking",
             "delivery confirmation", "signature confirmation", "international shipping",
             "customs and import taxes", "return policy for sellers", "order tracking",
             "product details", "product specifications", "product compatibility", "warranty claim",
             "claim process", "resolution center", "cancellation policy", "refund process",
             "chargeback process", "payment disputes", "buyer requirements", "seller requirements",
             "site rules", "restricted items", "prohibited items", "reporting violations",
             "feedback removal", "feedback revision", "resolution services", "appeal process"]
    return random.choice(texts)

# Generate 50 random texts for each dataset
for i in range(1, 5):
    with open(f'dataset{i}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['text'])
        for j in range(50):
            writer.writerow([random_text()])
