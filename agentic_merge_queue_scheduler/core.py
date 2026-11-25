"""Core file-conflict graph coloring scheduler for parallel agent PR merge queues."""
from typing import Any, Dict, List, Set


class MergeQueueScheduler:
    """Partitions pending PRs into conflict-free merge waves via greedy graph coloring."""

    def schedule(self, prs: List[Dict[str, Any]], max_wave_size: int = 8) -> List[List[str]]:
        waves: List[Dict[str, Any]] = []
        ordered = sorted(prs, key=lambda p: (-p.get("priority", 0), p["pr_id"]))

        for pr in ordered:
            files: Set[str] = set(pr.get("files", []))
            placed = False
            for w in waves:
                if len(w["prs"]) < max_wave_size and files.isdisjoint(w["files"]):
                    w["prs"].append(pr["pr_id"])
                    w["files"].update(files)
                    placed = True
                    break
            if not placed:
                waves.append({"prs": [pr["pr_id"]], "files": set(files)})

        return [w["prs"] for w in waves]
