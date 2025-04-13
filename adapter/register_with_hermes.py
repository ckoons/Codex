import os
import sys
import logging
import asyncio
import json
import uuid
import time
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("codex_registration")

async def register_codex_with_hermes():
    """
    Register Codex (Aider) with Hermes service registry.
    
    Returns:
        bool: Whether registration was successful
    """
    try:
        # Find the Tekton root directory
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tekton_root = os.path.dirname(current_dir)
        
        # Find Hermes directory
        hermes_dir = os.path.join(tekton_root, "Hermes")
        if not os.path.exists(hermes_dir):
            logger.error(f"Hermes directory not found at {hermes_dir}")
            return False
        
        # Create registrations directory if it doesn't exist
        registrations_dir = os.path.join(hermes_dir, "registrations")
        os.makedirs(registrations_dir, exist_ok=True)
        
        # Create registration data
        registration_data = {
            "service_id": "codex",
            "name": "Codex Aider",
            "version": "0.1.0",
            "endpoint": None,
            "capabilities": [
                "code_editing",
                "programming_assistance",
                "code_generation",
                "ai_pair_programming"
            ],
            "metadata": {
                "component_type": "tool",
                "description": "AI pair programming tool",
                "ui_enabled": True,
                "ui_component": "codex",
                "indicator": "green"  # Add the "little green button"
            },
            "instance_uuid": str(uuid.uuid4()),
            "registration_time": time.time(),
            "status": "active"
        }
        
        # Write registration to file
        registration_file = os.path.join(registrations_dir, "codex.json")
        with open(registration_file, "w") as f:
            json.dump(registration_data, f, indent=2)
        
        logger.info(f"Successfully registered Codex with Hermes at {registration_file}")
        return True
    
    except Exception as e:
        logger.error(f"Error registering Codex with Hermes: {e}")
        return False

async def main():
    """
    Main entry point for the registration script.
    """
    success = await register_codex_with_hermes()
    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)