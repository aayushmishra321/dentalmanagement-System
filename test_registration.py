#!/usr/bin/env python
"""
Test script to verify registration functionality
Run this after deployment to test if registration works
"""

import os
import sys
import django
from django.conf import settings

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dentalmanagement.settings')
django.setup()

from home.models import UserDetail

def test_registration():
    """Test user registration functionality"""
    print("Testing user registration...")
    
    # Test data
    test_user = {
        'name': 'Test User',
        'email': 'test@example.com',
        'contact': '1234567890',
        'dateofbirth': '1990-01-01',
        'gender': 'Male',
        'address': 'Test Address',
        'pincode': '123456',
        'password': 'testpass123'
    }
    
    try:
        # Check if user already exists
        if UserDetail.objects.filter(email=test_user['email']).exists():
            print("Test user already exists, deleting...")
            UserDetail.objects.filter(email=test_user['email']).delete()
        
        # Create new user
        user = UserDetail.objects.create(**test_user)
        print(f"✅ User created successfully: {user.name} ({user.email})")
        
        # Verify user exists
        retrieved_user = UserDetail.objects.get(email=test_user['email'])
        print(f"✅ User retrieved successfully: {retrieved_user.name}")
        
        # Clean up
        retrieved_user.delete()
        print("✅ Test user cleaned up")
        
        print("\n🎉 Registration test PASSED!")
        return True
        
    except Exception as e:
        print(f"❌ Registration test FAILED: {str(e)}")
        return False

def test_database_connection():
    """Test database connection"""
    print("Testing database connection...")
    
    try:
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"✅ Database connection successful: {result}")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("🔍 Running registration tests...\n")
    
    # Test database connection
    db_ok = test_database_connection()
    print()
    
    # Test registration if database is OK
    if db_ok:
        reg_ok = test_registration()
    else:
        print("❌ Skipping registration test due to database issues")
        reg_ok = False
    
    print("\n" + "="*50)
    if db_ok and reg_ok:
        print("🎉 ALL TESTS PASSED - Registration should work!")
    else:
        print("❌ TESTS FAILED - Check the issues above")
    print("="*50)