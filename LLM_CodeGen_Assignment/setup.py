#!/usr/bin/env python3
"""
Setup script for the project - similar to package.json in Node.js
"""

from setuptools import setup, find_packages

setup(
    name="llm-codegen-evaluation",
    version="1.0.0",
    description="LLM Code Generation Evaluation with Coverage Analysis",
    packages=find_packages(),
    
    # Dependencies (like package.json dependencies)
    install_requires=[
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
        "coverage>=7.0.0",
    ],
    
    # Development dependencies
    extras_require={
        "dev": [
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ]
    },
    
    # Test configuration
    python_requires=">=3.8",
)