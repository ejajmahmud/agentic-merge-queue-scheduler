"""Tests for Agentic Merge Queue Scheduler."""
import unittest
from agentic_merge_queue_scheduler.core import MergeQueueScheduler


class TestMergeQueueScheduler(unittest.TestCase):
    def test_groups_disjoint_prs_and_separates_conflicts(self):
        sched = MergeQueueScheduler()
        waves = sched.schedule([
            {"pr_id": "PR-1", "files": ["a.py", "b.py"]},
            {"pr_id": "PR-2", "files": ["c.py"]},
            {"pr_id": "PR-3", "files": ["b.py"]},
        ])
        self.assertEqual(waves, [["PR-1", "PR-2"], ["PR-3"]])

    def test_respects_max_wave_size(self):
        sched = MergeQueueScheduler()
        waves = sched.schedule([
            {"pr_id": "P1", "files": ["1.py"]},
            {"pr_id": "P2", "files": ["2.py"]},
            {"pr_id": "P3", "files": ["3.py"]},
        ], max_wave_size=2)
        self.assertEqual(len(waves), 2)
