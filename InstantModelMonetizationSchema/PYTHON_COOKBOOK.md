# Python Cookbook - Instant Model Monetization Schema 🍜

**Quick & Easy Python Recipes for Monetization** - Like instant ramen noodles, but for code!

## 🚀 Quick Start

This cookbook provides simple, ready-to-use Python examples for implementing the Instant Model Monetization Schema. No complex setup required - just copy, paste, and run!

## 📋 Table of Contents

1. [Basic Setup](#basic-setup)
2. [Creating Items](#creating-items)
3. [Managing Inventory](#managing-inventory)
4. [Processing Referrals](#processing-referrals)
5. [API Integration](#api-integration)

## Basic Setup

```python
# Simple monetization schema setup
import json
from datetime import datetime

class InstantMonetization:
    def __init__(self):
        self.items = []
        self.inventory = {}
        
    def add_item(self, name, price, quantity, description=""):
        item = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "description": description,
            "created_at": datetime.now().isoformat()
        }
        self.items.append(item)
        self.inventory[name] = quantity
        return item
```

## Creating Items

### Recipe 1: Add a Simple Item

```python
# Instant recipe - Add a product
monetization = InstantMonetization()

item = monetization.add_item(
    name="TastyTrade Referral",
    price=500.00,
    quantity=9999999,
    description="$500 per $5k funded account"
)

print(f"Added: {item['name']} - ${item['price']}")
```

### Recipe 2: Bulk Add Items

```python
# Add multiple items at once
items_to_add = [
    {"name": "Premium Referral", "price": 1000.00, "quantity": 100, "description": "Premium tier"},
    {"name": "Basic Referral", "price": 250.00, "quantity": 500, "description": "Basic tier"},
    {"name": "Starter Pack", "price": 50.00, "quantity": 1000, "description": "Entry level"}
]

for item_data in items_to_add:
    monetization.add_item(**item_data)
    
print(f"Added {len(items_to_add)} items to inventory")
```

## Managing Inventory

### Recipe 3: Check Inventory

```python
# Check current inventory levels
def check_inventory(monetization):
    print("\n📦 Current Inventory:")
    for name, quantity in monetization.inventory.items():
        status = "✅ In Stock" if quantity > 0 else "❌ Out of Stock"
        print(f"  {name}: {quantity} units - {status}")
```

### Recipe 4: Update Inventory

```python
# Update inventory after a sale
def process_sale(monetization, item_name, quantity_sold=1):
    if item_name in monetization.inventory:
        if monetization.inventory[item_name] >= quantity_sold:
            monetization.inventory[item_name] -= quantity_sold
            return True, f"✅ Sold {quantity_sold} x {item_name}"
        else:
            return False, "❌ Insufficient inventory"
    return False, "❌ Item not found"

# Example usage
success, message = process_sale(monetization, "TastyTrade Referral")
print(message)
```

## Processing Referrals

### Recipe 5: Referral Code Generator

```python
import random
import string

def generate_referral_code(length=10):
    """Generate a unique referral code"""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

# Generate referral codes
for i in range(3):
    code = generate_referral_code()
    print(f"Referral Code #{i+1}: {code}")
```

### Recipe 6: Track Referral Revenue

```python
class ReferralTracker:
    def __init__(self):
        self.referrals = []
        
    def add_referral(self, code, amount_funded, commission_rate=0.10):
        """Track a new referral"""
        commission = amount_funded * commission_rate
        referral = {
            "code": code,
            "funded_amount": amount_funded,
            "commission": commission,
            "timestamp": datetime.now().isoformat()
        }
        self.referrals.append(referral)
        return commission
    
    def total_earnings(self):
        """Calculate total earnings from all referrals"""
        return sum(r["commission"] for r in self.referrals)

# Example usage
tracker = ReferralTracker()
tracker.add_referral("HNFY4P46B2", 5000.00, 0.10)  # $5k funded = $500 commission
tracker.add_referral("ABC123DEF4", 10000.00, 0.10)  # $10k funded = $1000 commission

print(f"Total Earnings: ${tracker.total_earnings():.2f}")
```

## API Integration

### Recipe 7: Simple API Client

```python
import requests

class MonetizationAPI:
    def __init__(self, base_url="https://agentcies.replit.app"):
        self.base_url = base_url
        
    def get_inventory(self):
        """Fetch current inventory from API"""
        try:
            response = requests.get(f"{self.base_url}/api/inventory")
            return response.json()
        except Exception as e:
            return {"error": str(e)}
    
    def create_item(self, item_data):
        """Create a new item via API"""
        try:
            response = requests.post(
                f"{self.base_url}/api/items",
                json=item_data
            )
            return response.json()
        except Exception as e:
            return {"error": str(e)}

# Example usage (requires API to be running)
# api = MonetizationAPI()
# inventory = api.get_inventory()
# print(inventory)
```

### Recipe 8: Export to JSON

```python
def export_to_json(monetization, filename="monetization_data.json"):
    """Save monetization data to JSON file"""
    data = {
        "items": monetization.items,
        "inventory": monetization.inventory,
        "exported_at": datetime.now().isoformat()
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Data exported to {filename}")

# Export your data
export_to_json(monetization)
```

## 🎯 Quick Examples - Ready to Run

### Complete Example: TastyTrade Setup

```python
#!/usr/bin/env python3
"""
Complete example: Set up TastyTrade referral program
Run with: python3 tastytrade_setup.py
"""

from datetime import datetime
import json

class QuickMonetization:
    def __init__(self):
        self.store = {
            "name": "TastyTrade Referral Store",
            "items": [],
            "stats": {"total_revenue": 0, "items_sold": 0}
        }
    
    def add_product(self, name, price, inventory, description=""):
        product = {
            "id": len(self.store["items"]) + 1,
            "name": name,
            "price": price,
            "inventory": inventory,
            "description": description
        }
        self.store["items"].append(product)
        print(f"✅ Added: {name} (${price})")
        return product
    
    def sell(self, product_id, quantity=1):
        for item in self.store["items"]:
            if item["id"] == product_id:
                if item["inventory"] >= quantity:
                    item["inventory"] -= quantity
                    revenue = item["price"] * quantity
                    self.store["stats"]["total_revenue"] += revenue
                    self.store["stats"]["items_sold"] += quantity
                    print(f"💰 Sale complete! Revenue: ${revenue}")
                    return True
        return False
    
    def summary(self):
        print("\n📊 Store Summary:")
        print(f"  Total Revenue: ${self.store['stats']['total_revenue']}")
        print(f"  Items Sold: {self.store['stats']['items_sold']}")
        print(f"  Products: {len(self.store['items'])}")

# Quick setup
if __name__ == "__main__":
    store = QuickMonetization()
    
    # Add TastyTrade referral product
    store.add_product(
        name="TastyTrade $500 referral for $5k funded Acct.",
        price=500.00,
        inventory=9999999,
        description="Referral Code: HNFY4P46B2"
    )
    
    # Simulate some sales
    store.sell(1)  # First sale
    store.sell(1)  # Second sale
    
    # Show results
    store.summary()
```

## 🔥 Pro Tips

1. **Keep it simple**: Like instant ramen, the best code is simple and fast
2. **Error handling**: Always validate inputs before processing
3. **Logging**: Track all transactions for debugging
4. **Testing**: Test with small amounts first
5. **Backup**: Export data regularly with Recipe 8

## 📦 Requirements

```
# requirements.txt - if you need external packages
requests>=2.28.0  # For API calls
```

Install with:
```bash
pip install -r requirements.txt
```

## 🎉 That's It!

You now have instant, ready-to-use Python recipes for monetization. Just like instant ramen noodles - quick, easy, and satisfying!

**Remember**: This is a quick-start cookbook. Adapt these recipes to your specific needs.

---

*Made with ❤️ for instant results*
