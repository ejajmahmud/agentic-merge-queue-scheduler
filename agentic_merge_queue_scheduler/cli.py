"""CLI for Agentic Merge Queue Scheduler."""
import argparse
import json
from .core import MergeQueueScheduler


def main():
    parser = argparse.ArgumentParser(description="Agentic Merge Queue Scheduler CLI")
    parser.add_argument("--max-wave", type=int, default=4, help="Max PRs per parallel wave")
    args = parser.parse_args()

    sched = MergeQueueScheduler()
    prs = [
        {"pr_id": "PR-10", "files": ["auth.py"]},
        {"pr_id": "PR-11", "files": ["ui.py"]},
        {"pr_id": "PR-12", "files": ["auth.py", "db.py"]},
    ]
    print(json.dumps({"waves": sched.schedule(prs, max_wave_size=args.max_wave)}, indent=2))


if __name__ == "__main__":
    main()
