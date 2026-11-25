import os

ENTRY = (
    "I queued 40 minutes for a food-truck taco, got sunburned through "
    "the atmosphere, and paid for water that falls from the sky, yet "
    "the cheese sauce alone was worth losing my return ticket over."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
