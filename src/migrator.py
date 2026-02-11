import re
import csv
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def contains_domain(address: str, domain: str) -> bool:
    """Check if the email address contains the exact domain."""
    pattern = rf"[\w\.-]+@{re.escape(domain)}$"
    return bool(re.match(pattern, address.strip()))

def replace_domain(address: str, old_domain: str, new_domain: str) -> str:
    """Replace the old domain with the new domain in the given email string."""
    pattern = rf"{re.escape(old_domain)}$"
    return re.sub(pattern, new_domain, address.strip())

def migrate_domains(input_csv: Path, output_csv: Path,
                    old_domain: str, new_domain: str) -> None:
    """
    Process the input CSV line by line to minimize memory usage,
    replace targeted domains, and write to the output CSV.
    """
    logging.info(f"Reading from {input_csv}")

    # Open both files simultaneously for stream processing
    with open(input_csv, "r", encoding="utf-8") as infile, \
         open(output_csv, "w", newline="", encoding="utf-8") as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        try:
            header = next(reader)
            writer.writerow(header)
            
            # Find the index dynamically to avoid hardcoding column positions
            email_index = next((i for i, col in enumerate(header) if 'Email Address' in col), None)
            if email_index is None:
                raise ValueError("Column 'Email Address' not found")
                
        except (StopIteration, ValueError) as e:
            logging.error(f"Invalid CSV format: {e}")
            return

        updated_count = 0
        for row in reader:
            if len(row) <= email_index:
                continue
                
            email = row[email_index].strip()

            if contains_domain(email, old_domain):
                new_email = replace_domain(email, old_domain, new_domain)
                logging.info(f"Migrated: {email} -> {new_email}")
                # Preserve a leading space if it matches the original format
                row[email_index] = f" {new_email}" if " " in row[email_index] else new_email
                updated_count += 1

            writer.writerow(row)

    logging.info(f"Successfully updated {updated_count} emails. Saved to {output_csv}")