from client import TieredMemoryManager

mem = TieredMemoryManager(working_limit=2)
mem.append_working("User is a senior software engineer")
mem.append_working("User prefers TypeScript and Python")
mem.append_working("User works at an AI research lab")

ctx = mem.get_context()
print("Active Working Memory:", ctx["working"])
print("Paged Archival Count:", ctx["archival_count"])
