#!/usr/bin/env python3
"""
Gemini Setup Helper
Helps you set up Google Gemini API for testing
"""

import os
import requests

def check_gemini_setup():
    """Check if Gemini is properly set up"""
    
    print("🔍 GEMINI SETUP CHECKER")
    print("=" * 40)
    
    # Check API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY not found!")
        print("\n📋 Setup Instructions:")
        print("1. Go to: https://aistudio.google.com/app/apikey")
        print("2. Sign in with your Google account")
        print("3. Click 'Create API Key'")
        print("4. Copy the API key")
        print("5. Set it in your environment:")
        print("   Windows: $env:GEMINI_API_KEY='your-key-here'")
        print("   Linux/Mac: export GEMINI_API_KEY='your-key-here'")
        return False
    
    print(f"✅ GEMINI_API_KEY found: {api_key[:8]}...{api_key[-4:]}")
    
    # Test API connection
    print("\n🔄 Testing Gemini API connection...")
    
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key={api_key}"
        
        payload = {
            "contents": [{
                "parts": [{
                    "text": "Hello, can you respond with just 'API test successful'?"
                }]
            }],
            "generationConfig": {
                "temperature": 0.1,
                "maxOutputTokens": 50
            }
        }
        
        response = requests.post(url, json=payload, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                response_text = result['candidates'][0]['content']['parts'][0]['text']
                print(f"✅ API test successful!")
                print(f"📝 Response: {response_text}")
                return True
            else:
                print("❌ No response from Gemini")
                return False
        else:
            print(f"❌ API error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return False

def show_gemini_info():
    """Show information about Gemini"""
    
    print("\n📊 GEMINI MODEL INFO")
    print("=" * 40)
    print("🤖 Model: gemini-2.5-flash-lite (Gemini 2.5 Flash-Lite)")
    print("🏢 Provider: Google")
    print("💰 Pricing: Free tier available")
    print("⚡ Speed: Very fast")
    print("🧠 Capabilities: Code generation, reasoning, analysis")
    print("📝 Context: 1M tokens")
    print("🔗 Documentation: https://ai.google.dev/")

def main():
    """Main function"""
    
    print("🚀 GEMINI SETUP & TEST")
    print("=" * 50)
    
    show_gemini_info()
    
    if check_gemini_setup():
        print("\n🎉 Gemini is ready to use!")
        print("\n📋 Next Steps:")
        print("1. Run a test workflow:")
        print("   cd workflows")
        print("   python run_gemini_workflow.py 1 3 3")
        print("\n2. This will test problems 1-3 with K=3")
        print("3. Results will be saved in generated/gemini_*/ folders")
    else:
        print("\n❌ Gemini setup incomplete")
        print("Please follow the setup instructions above")

if __name__ == "__main__":
    main()