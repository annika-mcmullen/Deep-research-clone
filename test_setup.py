#!/usr/bin/env python3
"""
Test script to verify the Deep Research Clone setup
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import streamlit
        print(f"Streamlit {streamlit.__version__}")
    except ImportError as e:
        print(f"Streamlit import failed: {e}")
        return False
    
    try:
        import openai
        print(f"OpenAI {openai.__version__}")
    except ImportError as e:
        print(f"OpenAI import failed: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("python-dotenv")
    except ImportError as e:
        print(f"python-dotenv import failed: {e}")
        return False
    
    try:
        from research_engine import DeepResearchEngine
        print("research_engine module")
    except ImportError as e:
        print(f"research_engine import failed: {e}")
        return False
    
    return True

def test_environment():
    """Test environment variables"""
    print("\n🔍 Testing environment...")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key and api_key != 'your_openai_api_key_here':
        print("OpenAI API key found")
        return True
    else:
        print("OpenAI API key not set or using placeholder")
        print(" Please update the .env file with your actual API key")
        return False

def test_research_engine():
    """Test research engine initialization"""
    print("\n Testing research engine...")
    
    try:
        from research_engine import DeepResearchEngine
        engine = DeepResearchEngine()
        print("Research engine initialized successfully")
        return True
    except Exception as e:
        print(f"Research engine initialization failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Deep Research Clone - Setup Test")
    print("=" * 40)
    
    # Test Python version
    print(f"Python {sys.version}")
    
    # Run tests
    imports_ok = test_imports()
    env_ok = test_environment()
    engine_ok = test_research_engine()
    
    print("\n" + "=" * 40)
    print("Test Results:")
    print(f"   Imports: {'PASS' if imports_ok else 'FAIL'}")
    print(f"   Environment: {'PASS' if env_ok else 'WARNING'}")
    print(f"   Research Engine: {'PASS' if engine_ok else 'FAIL'}")
    
    if imports_ok and engine_ok:
        print("\n Setup looks good! You can now run:")
        print("   streamlit run app.py")
    else:
        print("\n Setup has issues. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 