"""
Simple setup script for the LLM Code Generation Evaluation system
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "google-generativeai>=0.8.0"
        ])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False

def check_api_key():
    """Check if API key is set"""
    api_key = os.getenv('GEMINI_API_KEY')
    
    if api_key:
        print(f"✅ API key found: {api_key[:10]}...")
        return True
    else:
        print("❌ GEMINI_API_KEY not set")
        print("\nTo set your API key:")
        print("$env:GEMINI_API_KEY='your-api-key-here'")
        return False

def main():
    """Setup the system"""
    print("LLM Code Generation Evaluation - Setup")
    print("=" * 40)
    
    # Install requirements
    if not install_requirements():
        return
    
    # Check API key
    if not check_api_key():
        print("\n⚠️  Please set your API key and run setup again")
        return
    
    print("\n🎉 Setup complete!")
    print("Run: python main_workflow.py")

if __name__ == "__main__":
    main()