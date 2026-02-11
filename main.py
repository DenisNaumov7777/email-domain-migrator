import argparse
from pathlib import Path
from src.migrator import migrate_domains
from src.generator import generate_fake_csv

def main():
    parser = argparse.ArgumentParser(description="A CLI tool to migrate email domains in a CSV file.")
    
    parser.add_argument("--input", type=Path, default=Path("data/user_emails.csv"),
                        help="Path to the input CSV file.")
    parser.add_argument("--output", type=Path, default=Path("data/updated_user_emails.csv"),
                        help="Path to the output CSV file.")
    parser.add_argument("--old-domain", type=str, default="abc.edu",
                        help="The old domain to search for (default: abc.edu).")
    parser.add_argument("--new-domain", type=str, default="xyz.edu",
                        help="The new domain to replace with (default: xyz.edu).")
    parser.add_argument("--generate", action="store_true",
                        help="Generate a fake CSV dataset if the input file does not exist.")
    parser.add_argument("--count", type=int, default=25,
                        help="Number of rows to generate if --generate is used (default: 25).")

    args = parser.parse_args()

    # Ensure directories exist
    args.input.parent.mkdir(parents=True, exist_ok=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    if not args.input.exists():
        if args.generate:
            print(f"Input file not found. Generating {args.count} fake records at {args.input}...")
            generate_fake_csv(args.input, count=args.count)
        else:
            print(f"Error: Target file '{args.input}' does not exist.")
            print("Tip: Run with --generate flag to create dummy data automatically.")
            return

    migrate_domains(args.input, args.output, args.old_domain, args.new_domain)

if __name__ == "__main__":
    main()