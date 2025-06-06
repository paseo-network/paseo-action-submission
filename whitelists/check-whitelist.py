import os
from ruamel.yaml import YAML

validators_dir = "../paseo-validators/active"
whitelist_file = "whitelist.yml"

yaml = YAML()

# Load whitelist addresses, replacing tabs with spaces in-memory
with open(whitelist_file, "r") as f:
    whitelist_content = f.read().replace('\t', '  ')
whitelist_data = yaml.load(whitelist_content)
raw_whitelist = whitelist_data.get("whitelist", [])

# Extract only the address field from each mapping
whitelist = set(
    entry["address"] for entry in raw_whitelist
    if isinstance(entry, dict) and "address" in entry
)

# Collect all stash addresses from active validators
missing = []
reported_stashes = set()
for fname in os.listdir(validators_dir):
    if fname.endswith(".yml") or fname.endswith(".yaml"):
        with open(os.path.join(validators_dir, fname), "r") as f:
            data = yaml.load(f)
        accounts = data.get("accounts", [])
        if isinstance(accounts, dict):
            accounts = list(accounts.values())
        for account in accounts:
            stash = account.get("stash")
            if stash and stash not in whitelist and stash not in reported_stashes:
                missing.append({"file": fname, "stash": stash})
                reported_stashes.add(stash)

# Report missing addresses
if missing:
    print("Accounts not in whitelist:")
    for entry in missing:
        print(f"{entry['file']}: {entry['stash']}")
else:
    print("All accounts are whitelisted.")