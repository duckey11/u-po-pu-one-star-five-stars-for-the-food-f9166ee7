import os

ENTRY = (
    "I queued 40 minutes for a food-truck taco, got sunburned through "
    "the atmosphere, and paid for water that falls from the sky, yet "
    "the cheese sauce alone was worth losing my return ticket."
)

# Bounty rules: exactly one sentence, 1-200 characters. Refuse to write
# an entry that breaks them instead of silently submitting an invalid file.
if not 1 <= len(ENTRY) <= 200:
    raise SystemExit(f"entry must be 1-200 chars, got {len(ENTRY)}")
if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
    raise SystemExit("entry must be exactly one sentence")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
