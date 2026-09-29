import sys
import json
from client import TieredMemoryManager

mem = TieredMemoryManager()

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-hierarchical-tiered-memory-manager-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "append_agent_memory",
                        "description": "Add new item to working memory with automatic archival paging",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "item": {"type": "string", "description": "Memory item content"}
                            },
                            "required": ["item"]
                        }
                    },
                    {
                        "name": "get_memory_status",
                        "description": "Retrieve current working context and archival status",
                        "inputSchema": {"type": "object", "properties": {}}
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "append_agent_memory":
            it = args.get("item", "")
            mem.append_working(it)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": "Memory item stored"}]}}
        elif tool_name == "get_memory_status":
            ctx = mem.get_context()
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(ctx)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
