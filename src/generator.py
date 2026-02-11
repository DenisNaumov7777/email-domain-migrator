import csv
import random
from pathlib import Path
from faker import Faker

fake = Faker()

def generate_fake_csv(path: Path, count: int = 20) -> None:
    """
    Generate a CSV file with fake names and a mix of targeted and random emails.
    """
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Full Name", "Email Address"])

        for _ in range(count):
            name = fake.name()
            # 50% chance to generate the target domain, otherwise a random one
            domain = "abc.edu" if random.choice([True, False]) else fake.domain_name()
            email = f"{fake.user_name()}@{domain}"
            writer.writerow([name, email])