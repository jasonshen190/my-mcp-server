#!/usr/bin/env python3
"""
Setup and run script for the my-mcp-server MCP Server
"""

import subprocess
import sys
import os


def install_dependencies():
    """Install required dependencies"""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "../requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False
    return True


def run_server():
    """Run the MCP server"""
    print("\nStarting the my-mcp-server MCP Server...")
    print("Press Ctrl+C to stop the server")
    try:
        subprocess.run([sys.executable, "demo_server.py"])
    except KeyboardInterrupt:
        print("\nServer stopped.")


def run_test_client():
    """Run the test client"""
    print("\nRunning test client...")
    try:
        subprocess.run([sys.executable, "test_client.py"])
    except subprocess.CalledProcessError as e:
        print(f"❌ Test client failed: {e}")


def main():
    """Main function"""
    print("my-mcp-server MCP Server Setup")
    print("=" * 30)
    
    # Check if we're in the right directory
    if not os.path.exists("demo_server.py"):
        print("❌ Please run this script from the src/ directory")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Ask user what they want to do
    print("\nWhat would you like to do?")
    print("1. Run the server")
    print("2. Run the test client")
    print("3. Run both (server in background, then test client)")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            run_server()
            break
        elif choice == "2":
            run_test_client()
            break
        elif choice == "3":
            print("\nStarting server in background...")
            # Start server in background
            server_process = subprocess.Popen([sys.executable, "demo_server.py"])
            try:
                # Wait a moment for server to start
                import time
                time.sleep(2)
                # Run test client
                run_test_client()
            finally:
                # Stop server
                server_process.terminate()
                server_process.wait()
            break
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
