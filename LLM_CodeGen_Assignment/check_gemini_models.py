#!/usr/bin/env python3
"""
Check available Gemini models
"""

import os
import google.generativeai as genai

# Configure Gemini
gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)

print("🔍 Available Gemini models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"  ✅ {model.name}")