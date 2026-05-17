import asyncio
import sys

async def main():
    process = await asyncio.create_subprocess_exec(
        "uv", "run", "mcp_server.py",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    try:
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=3.0)
    except asyncio.TimeoutError:
        process.kill()
        print("Server started OK (timed out waiting - this is expected)")
        return
    print(f"Exit code: {process.returncode}")
    print(f"STDOUT: {stdout.decode()}")
    print(f"STDERR: {stderr.decode()}")

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    asyncio.run(main())