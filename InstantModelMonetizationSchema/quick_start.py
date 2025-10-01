#!/usr/bin/env python3
"""
🍜 Instant Model Monetization - Quick Start Example
Like instant ramen noodles - quick, easy, and ready in minutes!

Usage: python3 quick_start.py
"""

from datetime import datetime
import json


class InstantMonetization:
    """Simple monetization system - no complex setup required!"""
    
    def __init__(self, store_name="My Store"):
        self.store_name = store_name
        self.items = []
        self.inventory = {}
        self.sales = []
        print(f"🚀 {store_name} initialized!")
    
    def add_item(self, name, price, quantity, description=""):
        """Add an item to your store - instant and easy!"""
        item = {
            "id": len(self.items) + 1,
            "name": name,
            "price": float(price),
            "quantity": quantity,
            "description": description,
            "created_at": datetime.now().isoformat()
        }
        self.items.append(item)
        self.inventory[name] = quantity
        print(f"  ✅ Added: {name} - ${price} ({quantity} units)")
        return item
    
    def list_items(self):
        """Show all items in your store"""
        print(f"\n📦 {self.store_name} Inventory:")
        print("-" * 60)
        for item in self.items:
            stock_status = "✅ In Stock" if self.inventory[item['name']] > 0 else "❌ Out of Stock"
            print(f"  {item['id']}. {item['name']}")
            print(f"     Price: ${item['price']:.2f}")
            print(f"     Stock: {self.inventory[item['name']]} units - {stock_status}")
            if item['description']:
                print(f"     Description: {item['description']}")
        print("-" * 60)
    
    def sell(self, item_name, quantity=1):
        """Process a sale - instant revenue!"""
        if item_name not in self.inventory:
            print(f"  ❌ Error: {item_name} not found")
            return False
        
        if self.inventory[item_name] < quantity:
            print(f"  ❌ Error: Insufficient inventory for {item_name}")
            return False
        
        # Find the item to get price
        item = next((i for i in self.items if i['name'] == item_name), None)
        if not item:
            return False
        
        # Process the sale
        self.inventory[item_name] -= quantity
        revenue = item['price'] * quantity
        
        sale = {
            "item": item_name,
            "quantity": quantity,
            "revenue": revenue,
            "timestamp": datetime.now().isoformat()
        }
        self.sales.append(sale)
        
        print(f"  💰 Sale complete! {quantity} x {item_name} = ${revenue:.2f}")
        return True
    
    def summary(self):
        """Show store summary statistics"""
        total_revenue = sum(sale['revenue'] for sale in self.sales)
        total_items_sold = sum(sale['quantity'] for sale in self.sales)
        
        print(f"\n📊 {self.store_name} Summary:")
        print("=" * 60)
        print(f"  Total Products: {len(self.items)}")
        print(f"  Total Sales: {len(self.sales)}")
        print(f"  Items Sold: {total_items_sold}")
        print(f"  Total Revenue: ${total_revenue:.2f}")
        print("=" * 60)
    
    def export_json(self, filename="store_data.json"):
        """Export store data to JSON file"""
        data = {
            "store_name": self.store_name,
            "items": self.items,
            "inventory": self.inventory,
            "sales": self.sales,
            "exported_at": datetime.now().isoformat()
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\n💾 Data exported to {filename}")


def demo_tastytrade():
    """Demo: TastyTrade referral program setup"""
    print("\n" + "=" * 60)
    print("🍜 INSTANT MONETIZATION DEMO - TastyTrade Referrals")
    print("=" * 60)
    
    # Create store
    store = InstantMonetization("TastyTrade Referral Store")
    
    # Add TastyTrade referral products
    print("\n📦 Adding products...")
    store.add_item(
        name="TastyTrade $500 referral for $5k funded Acct.",
        price=500.00,
        quantity=9999999,
        description="Referral Code: HNFY4P46B2 | Link: https://open.tastytrade.com/signup?referralCode=HNFY4P46B2"
    )
    
    store.add_item(
        name="Premium Referral Package",
        price=1000.00,
        quantity=100,
        description="Premium tier with additional benefits"
    )
    
    store.add_item(
        name="Starter Referral Package",
        price=250.00,
        quantity=500,
        description="Entry-level referral package"
    )
    
    # Show inventory
    store.list_items()
    
    # Simulate some sales
    print("\n💰 Processing sales...")
    store.sell("TastyTrade $500 referral for $5k funded Acct.", 1)
    store.sell("Premium Referral Package", 2)
    store.sell("Starter Referral Package", 5)
    
    # Show summary
    store.summary()
    
    # Export data
    store.export_json("tastytrade_referrals.json")
    
    print("\n✨ Demo complete! Check tastytrade_referrals.json for exported data")


def demo_custom():
    """Demo: Create your own custom monetization setup"""
    print("\n" + "=" * 60)
    print("🍜 INSTANT MONETIZATION DEMO - Custom Store")
    print("=" * 60)
    
    store = InstantMonetization("AI Agent Store")
    
    print("\n📦 Setting up custom products...")
    store.add_item("AI Consultation Hour", 150.00, 20, "1-hour AI consulting session")
    store.add_item("API Access Key", 50.00, 100, "Monthly API access")
    store.add_item("Premium Support", 500.00, 10, "24/7 premium support package")
    
    store.list_items()
    
    print("\n💰 Processing sample transactions...")
    store.sell("AI Consultation Hour", 3)
    store.sell("API Access Key", 10)
    store.sell("Premium Support", 1)
    
    store.summary()


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════╗
║  🍜 Instant Model Monetization - Quick Start                 ║
║  Like instant ramen noodles - quick, easy, and satisfying!   ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Run TastyTrade demo
    demo_tastytrade()
    
    # Run custom store demo
    input("\n\nPress Enter to see custom store demo...")
    demo_custom()
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║  ✅ Quick Start Complete!                                     ║
║                                                               ║
║  Next steps:                                                  ║
║  1. Read PYTHON_COOKBOOK.md for more recipes                 ║
║  2. Customize the code for your needs                        ║
║  3. Check tastytrade_referrals.json for exported data        ║
║                                                               ║
║  Made with ❤️ for instant results!                           ║
╚══════════════════════════════════════════════════════════════╝
    """)
