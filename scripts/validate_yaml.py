#!/usr/bin/env python3
"""
YAML Validation Script for Paseo Action Submissions

This script validates YAML files in the repository, ensuring they have correct syntax
and proper structure for validator configurations.
"""

import yaml
import sys
import os
from pathlib import Path


def validate_validator_config(filepath):
    """Validate validator configuration files"""
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        
        # Check for required fields in validator configs
        if 'paseo-validators' in str(filepath):
            if not data:
                print(f"❌ {filepath}: Empty YAML file")
                return False
                
            # Check for required identity fields
            if 'identity' in data:
                identity = data['identity']
                required_identity_fields = ['display']
                for field in required_identity_fields:
                    if field not in identity:
                        print(f"❌ {filepath}: Missing required identity field: {field}")
                        return False
            
            # Check for accounts structure
            if 'accounts' in data:
                accounts = data['accounts']
                if not isinstance(accounts, list):
                    print(f"❌ {filepath}: 'accounts' should be a list")
                    return False
                
                for i, account in enumerate(accounts):
                    if not isinstance(account, dict):
                        print(f"❌ {filepath}: Account {i} should be a dictionary")
                        return False
                    if 'stash' not in account:
                        print(f"❌ {filepath}: Account {i} missing required 'stash' field")
                        return False
        
        # Check for required fields in system parachain configs
        elif any(chain in str(filepath) for chain in ['asset-hub', 'bridge-hub', 'coretime-chain', 'people-chain']):
            if not data:
                print(f"❌ {filepath}: Empty YAML file")
                return False
        
        # Check for required fields in additional services
        elif 'additional-services' in str(filepath):
            if not data:
                print(f"❌ {filepath}: Empty YAML file")
                return False
        
        print(f"✅ {filepath}: Valid")
        return True
        
    except yaml.YAMLError as e:
        print(f"❌ {filepath}: YAML parsing error - {e}")
        return False
    except Exception as e:
        print(f"❌ {filepath}: Validation error - {e}")
        return False


def main():
    """Main validation function"""
    print("🔍 Finding YAML files...")
    
    # Find all YAML files
    yaml_files = []
    for pattern in ['*.yml', '*.yaml']:
        yaml_files.extend(Path('.').rglob(pattern))
    
    print(f"Found {len(yaml_files)} YAML files")
    for yaml_file in sorted(yaml_files):
        print(f"  - {yaml_file}")
    
    print(f"\n📋 Validating {len(yaml_files)} YAML files...")
    
    all_valid = True
    for yaml_file in yaml_files:
        if not validate_validator_config(yaml_file):
            all_valid = False
    
    if not all_valid:
        print(f"\n❌ Validation failed! Some YAML files have errors.")
        sys.exit(1)
        
    print(f"\n🎉 All {len(yaml_files)} YAML files passed validation!")


if __name__ == "__main__":
    main()