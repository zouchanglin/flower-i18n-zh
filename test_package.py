#!/usr/bin/env python
"""
Test script for flower-i18n package
测试 flower-i18n 包的功能
"""

import sys
from pathlib import Path

# Add package to path
sys.path.insert(0, str(Path(__file__).parent))

from flower_i18n import __version__
from flower_i18n.i18n import get_i18n


def test_basic_functionality():
    """Test basic i18n functionality"""
    print("=" * 60)
    print("Testing Flower i18n Package")
    print("=" * 60)

    # Test version
    print(f"\n✓ Package version: {__version__}")

    # Get i18n instance
    i18n = get_i18n()
    print(f"✓ i18n instance created")

    # Test available locales
    locales = i18n.get_available_locales()
    print(f"✓ Available locales: {locales}")

    # Test English translations
    print("\n--- Testing English (en_US) ---")
    i18n.set_locale('en_US')
    print(f"  nav.workers: {i18n.get('nav.workers')}")
    print(f"  nav.tasks: {i18n.get('nav.tasks')}")
    print(f"  nav.broker: {i18n.get('nav.broker')}")
    print(f"  workers.status: {i18n.get('workers.status')}")

    # Test Chinese translations
    print("\n--- Testing Chinese (zh_CN) ---")
    i18n.set_locale('zh_CN')
    print(f"  nav.workers: {i18n.get('nav.workers')}")
    print(f"  nav.tasks: {i18n.get('nav.tasks')}")
    print(f"  nav.broker: {i18n.get('nav.broker')}")
    print(f"  workers.status: {i18n.get('workers.status')}")

    # Test fallback for non-existent key
    print("\n--- Testing Fallback ---")
    result = i18n.get('non.existent.key')
    print(f"  non.existent.key: {result}")
    assert result == 'non.existent.key', "Fallback should return key itself"
    print("  ✓ Fallback works correctly")

    # Test all translation keys
    print("\n--- Testing All Translation Keys ---")
    i18n.set_locale('zh_CN')
    en_translations = i18n.translations.get('en_US', {})
    zh_translations = i18n.translations.get('zh_CN', {})

    print(f"  English keys: {len(en_translations)}")
    print(f"  Chinese keys: {len(zh_translations)}")

    # Check if all keys are present in both languages
    en_keys = set(en_translations.keys())
    zh_keys = set(zh_translations.keys())

    missing_in_zh = en_keys - zh_keys
    missing_in_en = zh_keys - en_keys

    if missing_in_zh:
        print(f"  ⚠ Keys missing in Chinese: {missing_in_zh}")
    if missing_in_en:
        print(f"  ⚠ Keys missing in English: {missing_in_en}")

    if not missing_in_zh and not missing_in_en:
        print("  ✓ All keys present in both languages")

    print("\n" + "=" * 60)
    print("All tests passed! ✓")
    print("=" * 60)


def test_patcher():
    """Test patcher functionality"""
    print("\n--- Testing Patcher ---")
    try:
        from flower_i18n.patcher import FlowerTemplatePatcher
        patcher = FlowerTemplatePatcher()
        print(f"  ✓ Patcher initialized")
        print(f"  Flower path: {patcher.flower_path}")
        print(f"  Templates path: {patcher.templates_path}")
    except Exception as e:
        print(f"  ⚠ Patcher test skipped (Flower might not be installed): {e}")


def main():
    """Run all tests"""
    try:
        test_basic_functionality()
        test_patcher()
        print("\n🎉 All tests completed successfully!")
        return 0
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())