# genpark-hierarchical-tiered-memory-manager-skill

Agent Skill implementing **MemGPT-Inspired Hierarchical Tiered Memory & Context Paging** in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    NewItem["New Dialogue / Observation Event"] --> Working["Working Memory Window (Capacity L)"]
    Working --> OverCapacity{"Length > Capacity L?"}
    OverCapacity -->|Yes| Evict["Evict Oldest Context Item"]
    Evict --> Archival["Persist to Keyed Archival Memory Store"]
    OverCapacity -->|No| Ready["Active Prompt Working Context Ready"]
```
