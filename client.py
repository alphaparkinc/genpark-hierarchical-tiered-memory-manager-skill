"""Hierarchical Tiered Memory Manager.
100% Python Standard Library.
"""

class TieredMemoryManager:
    """Manages working context memory and long-term archival paging for agents."""
    def __init__(self, working_limit=3):
        self.working_memory = []
        self.archival_memory = {}
        self.working_limit = working_limit

    def append_working(self, item):
        self.working_memory.append(item)
        if len(self.working_memory) > self.working_limit:
            evicted = self.working_memory.pop(0)
            key = f"archive_{len(self.archival_memory)}"
            self.archival_memory[key] = evicted

    def get_context(self):
        return {
            "working": list(self.working_memory),
            "archival_count": len(self.archival_memory)
        }
