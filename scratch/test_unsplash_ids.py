import requests

# Test a list of authentic photo IDs on Unsplash
TEST_IDS = [
    # Electronics & Audio
    ("headphones", "photo-1505740420928-5e560c06d30e"), # Headphones
    ("soundbar", "photo-1545454675-3531b543be5d"), # Soundbar
    ("earbuds", "photo-1590658268037-6bf12165a8df"), # Earbuds
    ("microphone", "photo-1590602847861-f357a9332bbc"), # Microphone
    ("portable-speaker", "photo-1608043152269-423dbba4e7e1"), # Portable speaker
    ("turntable", "photo-1539185441755-769473a23570"), # Vinyl turntable
    ("audio-amp", "photo-1558089687-f282ffcbc126"), # Audio amp/mixer
    ("lavalier-mic", "photo-1598488035139-bdbb2231ce04"), # Audio gear
    ("dj-headphones", "photo-1484704849700-f032a568e944"), # DJ headphones
    ("mini-speaker", "photo-1543512214-318c7553f230"), # Small speaker

    # Smart Wearables
    ("smartwatch", "photo-1523275335684-37898b6baf30"), # Smartwatch
    ("fitness-band", "photo-1575311373937-040b8e1fd5b6"), # Fitness band
    ("rugged-watch", "photo-1522335789203-aabd1fc54bc9"), # Rugged watch
    ("smart-ring", "photo-1605100804763-247f67b3557e"), # Ring
    ("hybrid-watch", "photo-1524805444758-089113d48a6d"), # Classic watch
    ("watch-strap", "photo-1522335789203-aabd1fc54bc9"), # Watch band
    ("smart-scale", "photo-1576435728678-68d0fbf94e91"), # Digital scale
    ("sleep-mask", "photo-1541781774459-bb2af2f05b55"), # Sleep/relaxation

    # Laptops & Computers
    ("laptop", "photo-1496181133206-80ce9b88a853"), # Laptop
    ("keyboard", "photo-1587829741301-dc798b83add3"), # Keyboard
    ("mouse", "photo-1615663245857-ac93bb7c39e7"), # Mouse
    ("usb-hub", "photo-1625842268584-8f3296236761"), # USB hub
    ("monitor", "photo-1527443224154-c4a3942d3acf"), # Monitor
    ("webcam", "photo-1587826080692-f439cd0b70da"), # Webcam
    ("laptop-stand", "photo-1527864550417-7fd91fc51a46"), # Laptop desk setup
    ("external-ssd", "photo-1597872200969-2b65d56bd16b"), # SSD/hard drive
    ("lightbar", "photo-1517336714731-489689fd1ca8"), # Monitor desk setup

    # Mobiles & Accessories
    ("wall-charger", "photo-1583863788434-e58a36330cf0"), # Charger
    ("power-bank", "photo-1609081219090-a6d81d3085bf"), # Power bank
    ("phone-case", "photo-1585060544812-6b45742d762f"), # Phone case
    ("charging-cable", "photo-1586953208448-b95a79798f07"), # Braided cable
    ("car-mount", "photo-1511707171634-5f897ff02aa9"), # Mobile device
    ("screen-protector", "photo-1565849904461-04a58ad377e0"), # Phone screen
    ("phone-stand", "photo-1584438784894-089d6a62b8fa"), # Phone accessories

    # Bags & Travel Gear
    ("backpack", "photo-1553062407-98eeb64c6a62"), # Backpack
    ("duffel", "photo-1547949003-9792a18a2601"), # Duffel bag
    ("laptop-sleeve", "photo-1607604276583-eef5d076aa5f"), # Laptop sleeve
    ("sling-bag", "photo-1548036328-c9fa89d128fa"), # Sling / shoulder bag
    ("suitcase", "photo-1565026057447-bc90a3dceb87"), # Suitcase
    ("travel-pillow", "photo-1584100936595-c0654b55a2e2"), # Travel pillow
    ("umbrella", "photo-1517411032315-54ef2cb783bb"), # Umbrella

    # Home & Workspace Decor
    ("desk-lamp", "photo-1507473885765-e6ed057f782c"), # Desk lamp
    ("desk-mat", "photo-1527864550417-7fd91fc51a46"), # Desk mat
    ("oil-diffuser", "photo-1608571423902-eed4a5ad8108"), # Diffuser
    ("cushion", "photo-1584100936595-c0654b55a2e2"), # Pillow/cushion
    ("water-bottle", "photo-1602143407151-7111542de6e8"), # Water bottle
    ("air-purifier", "photo-1585771724684-38269d6639fd"), # Air purifier
    ("wall-clock", "photo-1563861826100-9cb868fdbe1c"), # Wall clock
    ("coffee-mug", "photo-1514432324607-a09d9b4aefdd"), # Coffee mug
    ("moon-lamp", "photo-1532767153582-b1a0e5145009"), # Moon lamp / glowing sphere

    # Gaming & Entertainment
    ("gaming-mouse", "photo-1615663245857-ac93bb7c39e7"), # Gaming mouse
    ("gaming-headset", "photo-1546435770-a3e426bf472b"), # Headset
    ("gamepad", "photo-1600080972464-8e5f35f63d08"), # Controller / gamepad
    ("mousepad", "photo-1527864550417-7fd91fc51a46"), # Mousepad
    ("keycaps", "photo-1587829741301-dc798b83add3"), # Keycaps
    ("laptop-cooler", "photo-1588872657578-7efd1f1555ed"), # Laptop cooler

    # Fashion & Lifestyle Essentials
    ("hoodie", "photo-1556905055-8f358a7a47b2"), # Hoodie
    ("tshirt", "photo-1521572267360-ee0c2909d518"), # T-Shirt
    ("sunglasses", "photo-1572635196237-14b3f281503f"), # Sunglasses
    ("wallet", "photo-1627123424574-724758594e93"), # Wallet
    ("dress-watch", "photo-1524805444758-089113d48a6d"), # Leather strap watch
    ("sneakers", "photo-1542291026-7eec264c27ff"), # Sneakers / shoes
    ("beanie", "photo-1576871337632-b9aef4c17ab9"), # Beanie
    ("baseball-cap", "photo-1588850561407-ed78c282e89b"), # Dad cap / baseball cap
    ("tote-bag", "photo-1544816155-12df9643f363"), # Canvas tote bag
    ("candle", "photo-1603006905003-be475563bc59"), # Scented candle
    ("belt", "photo-1624222247344-550fb60583dc"), # Leather/braided belt
]

print(f"Testing {len(TEST_IDS)} curated photo IDs...")
success = 0
for label, pid in TEST_IDS:
    url = f"https://images.unsplash.com/{pid}?w=400&q=70"
    try:
        r = requests.head(url, timeout=3)
        if r.status_code == 200:
            success += 1
        else:
            print(f"[FAIL {r.status_code}] {label}: {pid}")
    except Exception as e:
        print(f"[ERR] {label}: {e}")

print(f"Success: {success}/{len(TEST_IDS)} verified active Unsplash photo IDs")
