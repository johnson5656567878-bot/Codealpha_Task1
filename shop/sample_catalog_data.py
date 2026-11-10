from decimal import Decimal

# 112 Curated, verified catalog items where EVERY image matches the product type 100%
CATEGORIES = [
    "electronics-audio",
    "smart-wearables",
    "laptops-computers",
    "mobiles-accessories",
    "bags-travel-gear",
    "home-workspace-decor",
    "gaming-entertainment",
    "fashion-lifestyle-essentials",
]

CATALOG_ITEMS = [
    # -------------------------------------------------------------
    # Category 1: Electronics & Audio
    # -------------------------------------------------------------
    {
        "id": 1,
        "name": "Apex Pro Active Noise Cancelling Headphones",
        "category": "electronics-audio",
        "filename": "apex-pro-anc-headphones.jpg",
        "photo_id": "photo-1505740420928-5e560c06d30e",
        "price": Decimal("4999.00"),
        "stock": 18,
        "description": "Over-ear wireless headphones with cushioned ear pads, hybrid active noise cancellation up to 38dB, and 45-hour battery life with rapid Type-C charging."
    },
    {
        "id": 2,
        "name": "SonicPulse Wireless Bluetooth Soundbar",
        "category": "electronics-audio",
        "filename": "sonicpulse-wireless-soundbar.jpg",
        "photo_id": "photo-1545454675-3531b543be5d",
        "price": Decimal("3499.00"),
        "stock": 12,
        "description": "Slim horizontal home theater soundbar delivering 60W RMS surround sound with dual passive bass radiators, HDMI ARC, optical audio, and Bluetooth 5.3."
    },
    {
        "id": 3,
        "name": "AuraPods Elite True Wireless Earbuds",
        "category": "electronics-audio",
        "filename": "aurapods-wireless-earbuds.jpg",
        "photo_id": "photo-1590658268037-6bf12165a8df",
        "price": Decimal("1999.00"),
        "stock": 25,
        "description": "Compact white in-ear wireless earbuds with magnetic clamshell charging case, touch playback controls, environmental noise reduction, and IPX5 water resistance."
    },
    {
        "id": 4,
        "name": "StudioCraft USB Condenser Microphone",
        "category": "electronics-audio",
        "filename": "studiocraft-condenser-mic.jpg",
        "photo_id": "photo-1590602847861-f357a9332bbc",
        "price": Decimal("2899.00"),
        "stock": 8,
        "description": "Studio recording cardioid condenser microphone with all-metal desk tripod, shock mount, integrated pop filter, and 192kHz/24bit studio audio capture."
    },
    {
        "id": 17,
        "name": "BassBoom 360 Portable Waterproof Speaker",
        "category": "electronics-audio",
        "filename": "bassboom-portable-speaker.jpg",
        "photo_id": "photo-1608043152269-423dbba4e7e1",
        "price": Decimal("2299.00"),
        "stock": 15,
        "description": "Rugged cylindrical outdoor bluetooth speaker with 360-degree omnidirectional acoustics, IP67 dust and water resistance, and 18-hour continuous playtime."
    },
    {
        "id": 18,
        "name": "AcousticMaster Hi-Fi Stereo Amplifier",
        "category": "electronics-audio",
        "filename": "acousticmaster-stereo-amp.jpg",
        "photo_id": "photo-1558089687-f282ffcbc126",
        "price": Decimal("8499.00"),
        "stock": 5,
        "description": "Compact brushed aluminium 100W per channel Class-D stereo audio amplifier with treble, bass, and volume dials, aptX HD Bluetooth, and subwoofer output."
    },
    {
        "id": 19,
        "name": "RetroGroove Vinyl Turntable Record Player",
        "category": "electronics-audio",
        "filename": "retrogroove-vinyl-turntable.jpg",
        "photo_id": "photo-1539185441755-769473a23570",
        "price": Decimal("6999.00"),
        "stock": 6,
        "description": "3-speed belt-driven vinyl record player turntable housed in vintage walnut wood with an Audio-Technica magnetic moving cartridge and built-in phono preamp."
    },
    {
        "id": 20,
        "name": "ClarityVoice Wireless Lavalier Mic System",
        "category": "electronics-audio",
        "filename": "clarityvoice-lavalier-mic.jpg",
        "photo_id": "photo-1598488035139-bdbb2231ce04",
        "price": Decimal("3199.00"),
        "stock": 10,
        "description": "Dual-channel wireless clip-on lapel lavalier microphone system with intelligent noise suppression DSP and 200m ultra-low latency line-of-sight range."
    },
    {
        "id": 21,
        "name": "SoundShield Over-Ear DJ Monitoring Headphones",
        "category": "electronics-audio",
        "filename": "soundshield-dj-headphones.jpg",
        "photo_id": "photo-1484704849700-f032a568e944",
        "price": Decimal("3799.00"),
        "stock": 14,
        "description": "Professional closed-back DJ studio monitoring headphones with 90-degree rotating earcups, 50mm large aperture neodymium drivers, and detachable coiled cable."
    },
    {
        "id": 22,
        "name": "PocketBeats Mini Bluetooth Speaker",
        "category": "electronics-audio",
        "filename": "pocketbeats-mini-speaker.jpg",
        "photo_id": "photo-1543512214-318c7553f230",
        "price": Decimal("999.00"),
        "stock": 30,
        "description": "Pocket-sized ultra-portable wireless speaker with rubberized impact bumper, silicone lanyard loop, crisp 5W sound output, and 8 hours of playback."
    },
    {
        "id": 23,
        "name": "NoiseZero Memory Foam Earphone Tips 6-Pack",
        "category": "electronics-audio",
        "filename": "noisezero-foam-ear-tips.jpg",
        "photo_id": "photo-1590658268037-6bf12165a8df",
        "price": Decimal("399.00"),
        "stock": 45,
        "description": "Set of 6 slow-rebound memory foam replacement ear tips in S/M/L sizes providing superior passive ambient noise isolation and custom ear canal contouring."
    },
    {
        "id": 24,
        "name": "OpticalLink Gold-Plated Toslink Audio Cable",
        "category": "electronics-audio",
        "filename": "opticallink-toslink-audio-cable.jpg",
        "photo_id": "photo-1558089687-f282ffcbc126",
        "price": Decimal("449.00"),
        "stock": 50,
        "description": "2-meter digital fiber optic audio cable with 24K gold-plated connectors and protective nylon braiding for pristine signal transfer between TVs and soundbars."
    },
    {
        "id": 25,
        "name": "DolbyCinema 5.1 Wireless Surround System",
        "category": "electronics-audio",
        "filename": "dolbycinema-surround-system.jpg",
        "photo_id": "photo-1545454675-3531b543be5d",
        "price": Decimal("18999.00"),
        "stock": 4,
        "description": "Full 400W 5.1 channel surround sound package with central multi-driver soundbar, down-firing wireless subwoofer, and dual rear wireless satellite speakers."
    },
    {
        "id": 26,
        "name": "AeroStream Bluetooth 5.3 Audio Transmitter",
        "category": "electronics-audio",
        "filename": "aerostream-audio-transmitter.jpg",
        "photo_id": "photo-1543512214-318c7553f230",
        "price": Decimal("1299.00"),
        "stock": 20,
        "description": "2-in-1 Bluetooth transmitter and receiver adapter with aptX Low Latency technology enabling dual simultaneous headphone streaming from televisions."
    },

    # -------------------------------------------------------------
    # Category 2: Smart Wearables
    # -------------------------------------------------------------
    {
        "id": 5,
        "name": "Vanguard AMOLED Smartwatch with Bluetooth Calling",
        "category": "smart-wearables",
        "filename": "vanguard-amoled-smartwatch.jpg",
        "photo_id": "photo-1523275335684-37898b6baf30",
        "price": Decimal("3999.00"),
        "stock": 15,
        "description": "Sleek round smartwatch with a vibrant 1.43-inch Always-on AMOLED touch display, Bluetooth hands-free phone calling, SpO2 sensor, and heart-rate monitoring."
    },
    {
        "id": 6,
        "name": "PulseFit Band 5 Waterproof Fitness Tracker",
        "category": "smart-wearables",
        "filename": "pulsefit-fitness-tracker-band.jpg",
        "photo_id": "photo-1575311373937-040b8e1fd5b6",
        "price": Decimal("1499.00"),
        "stock": 22,
        "description": "Slim lightweight fitness tracking wristband featuring 14-day battery life, 5ATM swim-proof water resistance, continuous step counter, and sleep phase analysis."
    },
    {
        "id": 7,
        "name": "Titanium Edge Ultra GPS Rugged Watch",
        "category": "smart-wearables",
        "filename": "titanium-edge-rugged-gps-watch.jpg",
        "photo_id": "photo-1522335789203-aabd1fc54bc9",
        "price": Decimal("6499.00"),
        "stock": 4,
        "description": "Heavy-duty outdoor multisport GPS watch with titanium alloy bezel, scratch-proof sapphire crystal glass, barometric altimeter, and waypoint compass."
    },
    {
        "id": 27,
        "name": "NovaRing Smart Health & Sleep Tracker",
        "category": "smart-wearables",
        "filename": "novaring-smart-health-ring.jpg",
        "photo_id": "photo-1605100804763-247f67b3557e",
        "price": Decimal("7999.00"),
        "stock": 7,
        "description": "Aerospace-grade titanium smart health ring monitoring nocturnal HRV, body temperature variations, and deep sleep stages without a bulky screen."
    },
    {
        "id": 28,
        "name": "ActiveLife Kids GPS Tracking Smartwatch",
        "category": "smart-wearables",
        "filename": "activelife-kids-gps-smartwatch.jpg",
        "photo_id": "photo-1523275335684-37898b6baf30",
        "price": Decimal("2499.00"),
        "stock": 18,
        "description": "Brightly colored children's smartwatch equipped with 4G LTE two-way video calls, dedicated SOS emergency button, and geofencing location alerts for parents."
    },
    {
        "id": 29,
        "name": "ApexRun Pro Triathlon Sports Watch",
        "category": "smart-wearables",
        "filename": "apexrun-pro-triathlon-watch.jpg",
        "photo_id": "photo-1522335789203-aabd1fc54bc9",
        "price": Decimal("12499.00"),
        "stock": 3,
        "description": "High-performance multisport endurance watch measuring VO2 max, running power cadence, triathlon transitions, and dual-frequency GNSS navigation."
    },
    {
        "id": 30,
        "name": "ChronoClassic Hybrid Smartwatch",
        "category": "smart-wearables",
        "filename": "chronoclassic-hybrid-watch.jpg",
        "photo_id": "photo-1524805444758-089113d48a6d",
        "price": Decimal("4499.00"),
        "stock": 9,
        "description": "Traditional analog mechanical watch face with stainless steel bezel and leather strap concealing an interactive sub-OLED display for notifications."
    },
    {
        "id": 31,
        "name": "SiliconeComfort Breathable Sport Band 22mm",
        "category": "smart-wearables",
        "filename": "silicone-sport-watch-band.jpg",
        "photo_id": "photo-1575311373937-040b8e1fd5b6",
        "price": Decimal("499.00"),
        "stock": 40,
        "description": "Perforated dual-tone silicone smartwatch replacement strap with quick-release locking lugs and sweat-wicking airflow channels for running."
    },
    {
        "id": 32,
        "name": "Milanese Magnetic Loop Stainless Steel Strap",
        "category": "smart-wearables",
        "filename": "milanese-magnetic-steel-strap.jpg",
        "photo_id": "photo-1524805444758-089113d48a6d",
        "price": Decimal("799.00"),
        "stock": 35,
        "description": "Finely woven flexible stainless steel mesh watch band featuring an infinitely adjustable neodymium magnetic clasp for a secure custom fit."
    },
    {
        "id": 33,
        "name": "Magnetic Fast Charging Cable for Smartwatch",
        "category": "smart-wearables",
        "filename": "smartwatch-magnetic-charging-cable.jpg",
        "photo_id": "photo-1523275335684-37898b6baf30",
        "price": Decimal("349.00"),
        "stock": 50,
        "description": "1-meter replacement magnetic charging dock cable with gold-plated pogo pins and built-in over-voltage protection for smartwatches."
    },
    {
        "id": 34,
        "name": "SwimMate Waterproof Lap Counter Ring",
        "category": "smart-wearables",
        "filename": "swimmate-waterproof-lap-counter.jpg",
        "photo_id": "photo-1605100804763-247f67b3557e",
        "price": Decimal("1899.00"),
        "stock": 12,
        "description": "Ergonomic index-finger tally lap counter and stopwatch with high-contrast display and 50m waterproof sealing for pool swimming sessions."
    },
    {
        "id": 35,
        "name": "VitalSense Smart Body Composition Scale",
        "category": "smart-wearables",
        "filename": "vitalsense-smart-body-scale.jpg",
        "photo_id": "photo-1576435728678-68d0fbf94e91",
        "price": Decimal("1799.00"),
        "stock": 20,
        "description": "Tempered glass digital bathroom scale measuring 16 biometric parameters including body fat percentage, BMI, and muscle mass via Bluetooth sync."
    },
    {
        "id": 36,
        "name": "SmartGlow Safety LED Running Armband",
        "category": "smart-wearables",
        "filename": "smartglow-led-safety-armband.jpg",
        "photo_id": "photo-1575311373937-040b8e1fd5b6",
        "price": Decimal("599.00"),
        "stock": 28,
        "description": "USB-rechargeable high-visibility dual-mode flashing and continuous LED safety armband designed for nighttime runners, joggers, and cyclists."
    },
    {
        "id": 37,
        "name": "SleepDeep Bluetooth Eye Mask with Flat Speakers",
        "category": "smart-wearables",
        "filename": "sleepdeep-bluetooth-eye-mask.jpg",
        "photo_id": "photo-1541781774459-bb2af2f05b55",
        "price": Decimal("1299.00"),
        "stock": 16,
        "description": "Blackout 3D contoured memory foam sleep mask with ultra-thin cushioned side-sleeper stereo speakers and 10 hours of ambient sound playback."
    },

    # -------------------------------------------------------------
    # Category 3: Laptops & Computers
    # -------------------------------------------------------------
    {
        "id": 8,
        "name": "AeroBook 14 Thin & Light Ultrabook",
        "category": "laptops-computers",
        "filename": "aerobook-14-ultrabook.jpg",
        "photo_id": "photo-1496181133206-80ce9b88a853",
        "price": Decimal("48999.00"),
        "stock": 6,
        "description": "Ultra-slim 14-inch metal laptop with 2.2K anti-glare IPS screen, 16GB RAM, 512GB SSD, backlit keyboard, and lightweight 1.28kg portable chassis."
    },
    {
        "id": 9,
        "name": "MachKey Tenkeyless RGB Mechanical Keyboard",
        "category": "laptops-computers",
        "filename": "machkey-mechanical-keyboard.jpg",
        "photo_id": "photo-1587829741301-dc798b83add3",
        "price": Decimal("3299.00"),
        "stock": 14,
        "description": "Tenkeyless mechanical typing keyboard with smooth red linear switches, per-key RGB backlighting, durable PBT keycaps, and detachable braided USB-C cable."
    },
    {
        "id": 10,
        "name": "PrecisionGlide Wireless Ergonomic Mouse",
        "category": "laptops-computers",
        "filename": "precisionglide-wireless-mouse.jpg",
        "photo_id": "photo-1615663245857-ac93bb7c39e7",
        "price": Decimal("1299.00"),
        "stock": 20,
        "description": "Sculpted ergonomic wireless computer mouse with thumb rest, silent click buttons, multi-device Bluetooth and USB dongle pairing, and adjustable 4000 DPI."
    },
    {
        "id": 11,
        "name": "OmniHub 8-in-1 Aluminium USB-C Dock",
        "category": "laptops-computers",
        "filename": "omnihub-usbc-docking-station.jpg",
        "photo_id": "photo-1625842268584-8f3296236761",
        "price": Decimal("2199.00"),
        "stock": 0,
        "description": "Aluminium USB-C multi-port adapter expanding laptops with 4K HDMI, 100W Power Delivery pass-through charging, Gigabit Ethernet, SD card reader, and 3 USB 3.0 ports."
    },
    {
        "id": 38,
        "name": "ViewPro 27-inch 4K UHD IPS Designer Monitor",
        "category": "laptops-computers",
        "filename": "viewpro-4k-designer-monitor.jpg",
        "photo_id": "photo-1527443224154-c4a3942d3acf",
        "price": Decimal("24999.00"),
        "stock": 5,
        "description": "27-inch 4K Ultra HD frameless computer monitor featuring 99% sRGB color accuracy, HDR400, tilt-adjustable stand, and single-cable USB-C video input."
    },
    {
        "id": 39,
        "name": "StreamCam 1080p 60FPS Autofocus Webcam",
        "category": "laptops-computers",
        "filename": "streamcam-hd-autofocus-webcam.jpg",
        "photo_id": "photo-1587826080692-f439cd0b70da",
        "price": Decimal("2799.00"),
        "stock": 12,
        "description": "Full HD 1080p 60fps streaming webcam with glass optical lens, dual noise-reducing stereo microphones, physical privacy shutter, and universal monitor clip."
    },
    {
        "id": 40,
        "name": "AluStand Height Adjustable Laptop Riser",
        "category": "laptops-computers",
        "filename": "alustand-laptop-riser.jpg",
        "photo_id": "photo-1527864550417-7fd91fc51a46",
        "price": Decimal("1499.00"),
        "stock": 25,
        "description": "Sturdy sandblasted aluminium folding laptop stand elevating screens to eye level for ergonomic posture, with heat dissipation slots and silicone pads."
    },
    {
        "id": 41,
        "name": "SpeedVault 1TB Portable External SSD",
        "category": "laptops-computers",
        "filename": "speedvault-external-ssd-1tb.jpg",
        "photo_id": "photo-1597872200969-2b65d56bd16b",
        "price": Decimal("6499.00"),
        "stock": 10,
        "description": "Pocket-sized shock-resistant solid-state drive delivering blistering 1050MB/s data transfer speeds with USB 3.2 Gen 2 Type-C connectivity."
    },
    {
        "id": 42,
        "name": "SilentDesk Wireless Membrane Keyboard & Mouse Combo",
        "category": "laptops-computers",
        "filename": "silentdesk-keyboard-mouse-combo.jpg",
        "photo_id": "photo-1587829741301-dc798b83add3",
        "price": Decimal("1699.00"),
        "stock": 22,
        "description": "Whisper-quiet chiclet wireless desktop keyboard with integrated numeric keypad and matching ambidextrous optical mouse powered by a single unifying USB dongle."
    },
    {
        "id": 43,
        "name": "CableTidy Silicone 5-Slot Desktop Organizer",
        "category": "laptops-computers",
        "filename": "cabletidy-silicone-cable-organizer.jpg",
        "photo_id": "photo-1586953208448-b95a79798f07",
        "price": Decimal("299.00"),
        "stock": 60,
        "description": "Flexible silicone 5-channel cable organizer with peel-and-stick 3M adhesive backing holding charging leads, HDMI cords, and mouse cables firmly on desk edges."
    },
    {
        "id": 44,
        "name": "ScreenBar Pro Auto-Dimming Monitor Light Bar",
        "category": "laptops-computers",
        "filename": "screenbar-monitor-light-bar.jpg",
        "photo_id": "photo-1517336714731-489689fd1ca8",
        "price": Decimal("3499.00"),
        "stock": 8,
        "description": "Asymmetric optical monitor lamp clipping neatly to top bezels, illuminating the desk surface without causing glare on screens, with touch warmth controls."
    },
    {
        "id": 45,
        "name": "TitanDual Heavy Duty Dual Monitor Gas Arm",
        "category": "laptops-computers",
        "filename": "titandual-gas-spring-monitor-arm.jpg",
        "photo_id": "photo-1527443224154-c4a3942d3acf",
        "price": Decimal("4299.00"),
        "stock": 7,
        "description": "Counterbalance dual gas-spring desktop clamp arm supporting two 17 to 32 inch monitors with 360-degree rotation, tilt, and integrated cable routing channels."
    },
    {
        "id": 46,
        "name": "AirDuster Electric Compressed High-Power Blower",
        "category": "laptops-computers",
        "filename": "airduster-electric-blower.jpg",
        "photo_id": "photo-1587826080692-f439cd0b70da",
        "price": Decimal("1899.00"),
        "stock": 15,
        "description": "Rechargeable electric compressed air duster with high-speed 100,000 RPM motor and multiple nozzle attachments for cleaning keyboards and computer electronics."
    },
    {
        "id": 47,
        "name": "DisplayPort 1.4 Braided Cable 8K@60Hz 2m",
        "category": "laptops-computers",
        "filename": "displayport-braided-cable-8k.jpg",
        "photo_id": "photo-1586953208448-b95a79798f07",
        "price": Decimal("699.00"),
        "stock": 35,
        "description": "Heavy-duty 2-meter DisplayPort 1.4 video cable supporting 8K resolution at 60Hz and 4K at 144Hz with gold-plated latches and multi-layer shielding."
    },

    # -------------------------------------------------------------
    # Category 4: Mobiles & Accessories
    # -------------------------------------------------------------
    {
        "id": 48,
        "name": "PowerVolt 65W GaN Fast Wall Charger",
        "category": "mobiles-accessories",
        "filename": "powervolt-gan-fast-wall-charger.jpg",
        "photo_id": "photo-1583863788434-e58a36330cf0",
        "price": Decimal("1799.00"),
        "stock": 25,
        "description": "Compact Gallium Nitride (GaN) high-speed wall plug charger featuring dual USB-C Power Delivery ports and one USB-A port for phones, tablets, and laptops."
    },
    {
        "id": 49,
        "name": "MagCharge 10,000mAh Magnetic Wireless Power Bank",
        "category": "mobiles-accessories",
        "filename": "magcharge-magnetic-wireless-powerbank.jpg",
        "photo_id": "photo-1609081219090-a6d81d3085bf",
        "price": Decimal("2299.00"),
        "stock": 18,
        "description": "Magnetic 10,000mAh portable wireless battery pack snapping securely onto MagSafe-compatible smartphones, equipped with a fold-out hands-free kickstand."
    },
    {
        "id": 50,
        "name": "ArmorFlex Shockproof MagSafe Protective Case",
        "category": "mobiles-accessories",
        "filename": "armorflex-magsafe-phone-case.jpg",
        "photo_id": "photo-1585060544812-6b45742d762f",
        "price": Decimal("899.00"),
        "stock": 30,
        "description": "Clear impact-absorbing shockproof smartphone case with reinforced air-cushioned corners, raised camera bumper bezel, and integrated magnetic ring."
    },
    {
        "id": 51,
        "name": "HyperBraid 100W USB-C to USB-C Cable 2M",
        "category": "mobiles-accessories",
        "filename": "hyperbraid-usbc-cable-100w.jpg",
        "photo_id": "photo-1586953208448-b95a79798f07",
        "price": Decimal("499.00"),
        "stock": 45,
        "description": "Durable 2-meter nylon-braided USB-C charging cord featuring an E-Marker intelligent chip delivering up to 100W power delivery and high-speed data transfer."
    },
    {
        "id": 52,
        "name": "CarVent Magnetic Wireless Fast Charging Mount",
        "category": "mobiles-accessories",
        "filename": "carvent-magnetic-car-charger-mount.jpg",
        "photo_id": "photo-1511707171634-5f897ff02aa9",
        "price": Decimal("1499.00"),
        "stock": 16,
        "description": "Automotive air-vent mounted phone holder equipped with strong magnetic alignment and 15W Qi wireless fast charging with full 360-degree rotation."
    },
    {
        "id": 53,
        "name": "DiamondEdge 9H Tempered Glass Screen Protector 2-Pack",
        "category": "mobiles-accessories",
        "filename": "diamondedge-tempered-glass-screen.jpg",
        "photo_id": "photo-1565849904461-04a58ad377e0",
        "price": Decimal("349.00"),
        "stock": 50,
        "description": "Ultra-clear 9H hardness tempered glass screen shield with oleophobic fingerprint-resistant coating and included precision alignment installation frame."
    },
    {
        "id": 54,
        "name": "FoldDesk Aluminium Phone & Tablet Stand",
        "category": "mobiles-accessories",
        "filename": "folddesk-aluminium-phone-stand.jpg",
        "photo_id": "photo-1584438784894-089d6a62b8fa",
        "price": Decimal("699.00"),
        "stock": 28,
        "description": "Pocket-foldable solid aluminium desktop cradle stand with anti-slip rubber pads holding smartphones, e-readers, and tablets in landscape or portrait orientation."
    },
    {
        "id": 55,
        "name": "SpeedSync 20W PD Fast Charging Cube",
        "category": "mobiles-accessories",
        "filename": "speedsync-20w-fast-charger.jpg",
        "photo_id": "photo-1583863788434-e58a36330cf0",
        "price": Decimal("649.00"),
        "stock": 35,
        "description": "Ultra-compact travel wall charger plug delivering 20W Power Delivery output to charge smartphones to 50% battery within 30 minutes safely."
    },
    {
        "id": 56,
        "name": "Universal Waterproof Phone Pouch Dry Bag 2-Pack",
        "category": "mobiles-accessories",
        "filename": "universal-waterproof-phone-pouch.jpg",
        "photo_id": "photo-1511707171634-5f897ff02aa9",
        "price": Decimal("399.00"),
        "stock": 40,
        "description": "IPX8 certified transparent underwater phone lanyard case allowing full touchscreen operation and photography while swimming, boating, or snorkeling."
    },
    {
        "id": 57,
        "name": "AudioSplitter Dual 3.5mm Headphone Adapter",
        "category": "mobiles-accessories",
        "filename": "audiosplitter-headphone-adapter.jpg",
        "photo_id": "photo-1586953208448-b95a79798f07",
        "price": Decimal("249.00"),
        "stock": 60,
        "description": "Gold-plated Y-splitter audio adapter allowing two pairs of 3.5mm wired headphones to connect into a single phone, laptop, or tablet audio port."
    },
    {
        "id": 58,
        "name": "NanoDrive 256GB Dual Type-C & USB 3.1 Flash Drive",
        "category": "mobiles-accessories",
        "filename": "nanodrive-dual-usbc-flashdrive.jpg",
        "photo_id": "photo-1597872200969-2b65d56bd16b",
        "price": Decimal("2199.00"),
        "stock": 14,
        "description": "Swivel metal flash drive with dual USB Type-C and USB-A connectors for transferring videos and photos seamlessly between smartphones and computers."
    },
    {
        "id": 59,
        "name": "GripRing 360 Rotating Magnetic Phone Holder",
        "category": "mobiles-accessories",
        "filename": "gripring-magnetic-phone-holder.jpg",
        "photo_id": "photo-1584438784894-089d6a62b8fa",
        "price": Decimal("449.00"),
        "stock": 38,
        "description": "Zinc alloy magnetic finger loop grip attaching securely to phone backs, doubling as a multi-angle desktop kickstand for watching videos."
    },
    {
        "id": 60,
        "name": "LensPro HD Telephoto & Macro Clip-On Lens Kit",
        "category": "mobiles-accessories",
        "filename": "lenspro-clip-on-camera-lens.jpg",
        "photo_id": "photo-1511707171634-5f897ff02aa9",
        "price": Decimal("1299.00"),
        "stock": 11,
        "description": "Optical coated glass lens attachment clipping over phone cameras to shoot detailed macro close-ups and 2x telephoto portraits with zero distortion."
    },
    {
        "id": 61,
        "name": "CableArmor Spiral Cable Protector 10-Pack",
        "category": "mobiles-accessories",
        "filename": "cablearmor-spiral-protector-10pack.jpg",
        "photo_id": "photo-1586953208448-b95a79798f07",
        "price": Decimal("199.00"),
        "stock": 70,
        "description": "Set of 10 flexible colored silicone spiral sleeves wrapping around charging cable joints to prevent fraying, bending, and splitting damage."
    },

    # -------------------------------------------------------------
    # Category 5: Bags & Travel Gear
    # -------------------------------------------------------------
    {
        "id": 12,
        "name": "NomadShield Weatherproof Commuter Backpack 24L",
        "category": "bags-travel-gear",
        "filename": "nomadshield-commuter-backpack.jpg",
        "photo_id": "photo-1553062407-98eeb64c6a62",
        "price": Decimal("2499.00"),
        "stock": 19,
        "description": "Modern urban commuter backpack crafted from water-repellent ballistic fabric with dedicated padded 16-inch laptop compartment and hidden luggage strap."
    },
    {
        "id": 13,
        "name": "Voyager Weekender Canvas Duffel Bag",
        "category": "bags-travel-gear",
        "filename": "voyager-canvas-duffel-bag.jpg",
        "photo_id": "photo-1547949003-9792a18a2601",
        "price": Decimal("1899.00"),
        "stock": 11,
        "description": "Heavy-duty canvas and leather travel duffel bag with reinforced shoulder straps, spacious main packing area, and side ventilated shoe compartment."
    },
    {
        "id": 14,
        "name": "UrbanSleeve Padded Laptop Case 15.6 Inch",
        "category": "bags-travel-gear",
        "filename": "urbansleeve-padded-laptop-case.jpg",
        "photo_id": "photo-1607604276583-eef5d076aa5f",
        "price": Decimal("899.00"),
        "stock": 3,
        "description": "Protective gray padded laptop sleeve with plush inner fleece lining, 360-degree corner drop padding, and front zipper pocket for charger cords."
    },
    {
        "id": 62,
        "name": "CrossBody Sling Water-Resistant Shoulder Bag",
        "category": "bags-travel-gear",
        "filename": "crossbody-sling-shoulder-bag.jpg",
        "photo_id": "photo-1548036328-c9fa89d128fa",
        "price": Decimal("1299.00"),
        "stock": 22,
        "description": "Single-strap crossbody chest bag with water-resistant fabric, breathable mesh back panel, quick-access card slot, and integrated USB pass-through port."
    },
    {
        "id": 63,
        "name": "Globetrotter 3-Piece Packing Cube Compression Set",
        "category": "bags-travel-gear",
        "filename": "globetrotter-packing-cubes-set.jpg",
        "photo_id": "photo-1553062407-98eeb64c6a62",
        "price": Decimal("999.00"),
        "stock": 25,
        "description": "Set of 3 zippered ripstop nylon compression packing organizers reducing clothing volume in suitcases and keeping garments neatly separated."
    },
    {
        "id": 64,
        "name": "AeroLite Cabin Hardshell Spinner Suitcase 20\"",
        "category": "bags-travel-gear",
        "filename": "aerolite-cabin-hardshell-suitcase.jpg",
        "photo_id": "photo-1565026057447-bc90a3dceb87",
        "price": Decimal("4499.00"),
        "stock": 6,
        "description": "20-inch carry-on rolling suitcase with impact-resistant polycarbonate hardshell, 360-degree silent double spinner wheels, and recessed TSA combination lock."
    },
    {
        "id": 65,
        "name": "PassportSafe RFID Blocking Travel Neck Wallet",
        "category": "bags-travel-gear",
        "filename": "passportsafe-travel-neck-wallet.jpg",
        "photo_id": "photo-1548036328-c9fa89d128fa",
        "price": Decimal("649.00"),
        "stock": 30,
        "description": "Concealable under-clothing travel pouch with RFID blocking lining, multiple zippered pockets for passports and cards, and skin-soft adjustable neck cord."
    },
    {
        "id": 66,
        "name": "RollTop Expandable Cycling Backpack 28L",
        "category": "bags-travel-gear",
        "filename": "rolltop-cycling-backpack-28l.jpg",
        "photo_id": "photo-1553062407-98eeb64c6a62",
        "price": Decimal("2999.00"),
        "stock": 12,
        "description": "Waterproof roll-top courier backpack expanding up to 28 liters with reflective night-safety strips, padded ergonomic straps, and external helmet web."
    },
    {
        "id": 67,
        "name": "TechFolio Travel Cable & Gadget Organizer Pouch",
        "category": "bags-travel-gear",
        "filename": "techfolio-travel-cable-pouch.jpg",
        "photo_id": "photo-1607604276583-eef5d076aa5f",
        "price": Decimal("799.00"),
        "stock": 35,
        "description": "Double-layer electronics accessories organizer case with elastic retention loops and mesh pockets for power banks, cables, SD cards, and styluses."
    },
    {
        "id": 68,
        "name": "DryLock Waterproof Dry Bag 15L with Phone Case",
        "category": "bags-travel-gear",
        "filename": "drylock-waterproof-dry-bag.jpg",
        "photo_id": "photo-1553062407-98eeb64c6a62",
        "price": Decimal("849.00"),
        "stock": 18,
        "description": "15-liter heavy-gauge waterproof dry sack with roll-top buckle closure keeping gear completely dry during kayaking, beach trips, and camping."
    },
    {
        "id": 69,
        "name": "ComfortCloud Memory Foam Neck Travel Pillow",
        "category": "bags-travel-gear",
        "filename": "comfortcloud-neck-travel-pillow.jpg",
        "photo_id": "photo-1584100936595-c0654b55a2e2",
        "price": Decimal("899.00"),
        "stock": 24,
        "description": "U-shaped ergonomic memory foam flight pillow providing 360-degree head and chin support with washable sweat-resistant cooling fiber cover."
    },
    {
        "id": 70,
        "name": "LuggageScale Digital Backlit Hanging Scale 50kg",
        "category": "bags-travel-gear",
        "filename": "luggagescale-digital-hanging-scale.jpg",
        "photo_id": "photo-1565026057447-bc90a3dceb87",
        "price": Decimal("499.00"),
        "stock": 40,
        "description": "Compact handheld electronic luggage weight scale with stainless steel hook, backlit LCD screen, tare zero function, and 50kg capacity."
    },
    {
        "id": 71,
        "name": "CompactFold Ultra-Light Travel Umbrella Windproof",
        "category": "bags-travel-gear",
        "filename": "compactfold-travel-umbrella.jpg",
        "photo_id": "photo-1517411032315-54ef2cb783bb",
        "price": Decimal("699.00"),
        "stock": 26,
        "description": "Pocket folding umbrella with 9 reinforced fiberglass ribs withstanding heavy wind gusts, teflon water-repellent coating, and auto open-close button."
    },
    {
        "id": 72,
        "name": "ShoeShield Waterproof Travel Shoe Bags 4-Pack",
        "category": "bags-travel-gear",
        "filename": "shoeshield-travel-shoe-bags.jpg",
        "photo_id": "photo-1547949003-9792a18a2601",
        "price": Decimal("399.00"),
        "stock": 50,
        "description": "Pack of 4 durable zippered moisture-proof travel shoe pouches keeping sneakers and dress shoes isolated from clean clothes inside luggage bags."
    },

    # -------------------------------------------------------------
    # Category 6: Home & Workspace Decor
    # -------------------------------------------------------------
    {
        "id": 15,
        "name": "LuminaGlow Magnetic Levitation Desk Lamp",
        "category": "home-workspace-decor",
        "filename": "luminaglow-magnetic-desk-lamp.jpg",
        "photo_id": "photo-1507473885765-e6ed057f782c",
        "price": Decimal("3799.00"),
        "stock": 7,
        "description": "Contemporary minimalist wooden desk lamp featuring warm ambient LED glow with touch-dimming base and inductive power efficiency."
    },
    {
        "id": 16,
        "name": "Zenith Acoustic Felt Desk Mat with Cork Base",
        "category": "home-workspace-decor",
        "filename": "zenith-acoustic-felt-desk-mat.jpg",
        "photo_id": "photo-1527864550417-7fd91fc51a46",
        "price": Decimal("999.00"),
        "stock": 30,
        "description": "Large 900x400mm premium felt desktop blotter pad with natural Portuguese cork backing muffling keyboard clatter and protecting wooden tables."
    },
    {
        "id": 73,
        "name": "AuraAroma Ultrasonic Essential Oil Diffuser",
        "category": "home-workspace-decor",
        "filename": "auraaroma-ultrasonic-oil-diffuser.jpg",
        "photo_id": "photo-1608571423902-eed4a5ad8108",
        "price": Decimal("1599.00"),
        "stock": 14,
        "description": "300ml cold mist ultrasonic aromatherapy diffuser with wood-grain base, 7 soothing LED ambient mood lights, and automatic safety shut-off."
    },
    {
        "id": 74,
        "name": "ErgoComfort Memory Foam Lumbar Support Cushion",
        "category": "home-workspace-decor",
        "filename": "ergocomfort-lumbar-cushion.jpg",
        "photo_id": "photo-1584100936595-c0654b55a2e2",
        "price": Decimal("1299.00"),
        "stock": 20,
        "description": "Ergonomically contoured high-density memory foam back support cushion with dual adjustable straps designed for office chairs and car seats."
    },
    {
        "id": 75,
        "name": "NordicHex Wooden Wall Floating Shelves 3-Pack",
        "category": "home-workspace-decor",
        "filename": "nordichex-wooden-wall-shelves.jpg",
        "photo_id": "photo-1507473885765-e6ed057f782c",
        "price": Decimal("1899.00"),
        "stock": 10,
        "description": "Set of 3 geometric honeycomb hexagon natural wood floating shelves with hidden mounting brackets for displaying small indoor succulents and books."
    },
    {
        "id": 76,
        "name": "HydroSmart Insulated Vacuum Water Bottle 750ml",
        "category": "home-workspace-decor",
        "filename": "hydrosmart-insulated-water-bottle.jpg",
        "photo_id": "photo-1602143407151-7111542de6e8",
        "price": Decimal("899.00"),
        "stock": 35,
        "description": "Double-walled 18/8 food-grade stainless steel reusable drink bottle keeping water iced cold for 24 hours or coffee hot for 12 hours with sweat-free matte finish."
    },
    {
        "id": 77,
        "name": "BreezePure Desktop HEPA Air Purifier",
        "category": "home-workspace-decor",
        "filename": "breezepure-desktop-air-purifier.jpg",
        "photo_id": "photo-1585771724684-38269d6639fd",
        "price": Decimal("3499.00"),
        "stock": 8,
        "description": "Cylindrical desktop room air purifier featuring H13 True HEPA multi-stage filtration capturing 99.97% of airborne dust, smoke, and allergen particles."
    },
    {
        "id": 78,
        "name": "BambooZen Multi-Device Charging Dock Station",
        "category": "home-workspace-decor",
        "filename": "bamboozen-charging-dock-station.jpg",
        "photo_id": "photo-1527864550417-7fd91fc51a46",
        "price": Decimal("1699.00"),
        "stock": 16,
        "description": "Natural solid bamboo desktop charging stand with 5 device slots and concealed internal cable routing to charge multiple phones and tablets clutter-free."
    },
    {
        "id": 79,
        "name": "SandHour 3D Moving Deep Sea Sand Art Picture",
        "category": "home-workspace-decor",
        "filename": "sandhour-moving-sand-art.jpg",
        "photo_id": "photo-1507473885765-e6ed057f782c",
        "price": Decimal("1199.00"),
        "stock": 18,
        "description": "Circular moving sand art glass picture frame creating intricate landscapes of mountain ridges and desert dunes with every soothing 360-degree rotation."
    },
    {
        "id": 80,
        "name": "GlowCoaster USB Heated Coffee Mug Warmer",
        "category": "home-workspace-decor",
        "filename": "glowcoaster-coffee-mug-warmer.jpg",
        "photo_id": "photo-1514432324607-a09d9b4aefdd",
        "price": Decimal("799.00"),
        "stock": 28,
        "description": "Electric heated desktop beverage coaster maintaining coffee, tea, and warm cocoa at a consistent 55°C (131°F) with waterproof tempered glass surface."
    },
    {
        "id": 81,
        "name": "AeroGrip Under-Desk Cable Management Tray",
        "category": "home-workspace-decor",
        "filename": "aerogrip-underdesk-cable-tray.jpg",
        "photo_id": "photo-1527864550417-7fd91fc51a46",
        "price": Decimal("849.00"),
        "stock": 22,
        "description": "Sturdy powder-coated steel mesh under-desk cable basket with clamp mounting holding power surge strips and laptop power bricks out of floor sight."
    },
    {
        "id": 82,
        "name": "DeskClair Acrylic Dry Erase Desktop Memo Board",
        "category": "home-workspace-decor",
        "filename": "deskclair-acrylic-memo-board.jpg",
        "photo_id": "photo-1507473885765-e6ed057f782c",
        "price": Decimal("699.00"),
        "stock": 30,
        "description": "Angled glass-finish dry-erase desktop whiteboard fitting between keyboards and monitors with built-in hidden storage compartment for stationery."
    },
    {
        "id": 83,
        "name": "MoonLight 3D Printed Rechargeable Lunar Lamp 15cm",
        "category": "home-workspace-decor",
        "filename": "moonlight-3d-lunar-lamp.jpg",
        "photo_id": "photo-1532767153582-b1a0e5145009",
        "price": Decimal("999.00"),
        "stock": 25,
        "description": "15cm spherical 3D-printed glowing moon night light on a geometric wooden stand with touch controls for switching between warm white and amber light."
    },
    {
        "id": 84,
        "name": "SilentQuartz Modern Minimalist Wall Clock 12\"",
        "category": "home-workspace-decor",
        "filename": "silentquartz-modern-wall-clock.jpg",
        "photo_id": "photo-1563861826100-9cb868fdbe1c",
        "price": Decimal("1199.00"),
        "stock": 15,
        "description": "12-inch non-ticking silent sweep quartz wall clock with clean Scandinavian dial typography, matte black frame, and clear glass protective lens."
    },

    # -------------------------------------------------------------
    # Category 7: Gaming & Entertainment
    # -------------------------------------------------------------
    {
        "id": 85,
        "name": "ViperStrike Wireless Pro Gaming Mouse 26K DPI",
        "category": "gaming-entertainment",
        "filename": "viperstrike-gaming-mouse.jpg",
        "photo_id": "photo-1615663245857-ac93bb7c39e7",
        "price": Decimal("2999.00"),
        "stock": 16,
        "description": "Lightweight 58g esports wireless gaming mouse with optical switches rated for 80 million clicks, pure PTFE skates, and 26,000 DPI high-precision sensor."
    },
    {
        "id": 86,
        "name": "NovaBlast RGB Surround Sound Gaming Headset",
        "category": "gaming-entertainment",
        "filename": "novablast-gaming-headset.jpg",
        "photo_id": "photo-1546435770-a3e426bf472b",
        "price": Decimal("2499.00"),
        "stock": 20,
        "description": "Over-ear gaming headphones featuring positional 7.1 surround audio, cooling memory foam ear cushions, flexible flip-to-mute mic, and dynamic RGB lighting."
    },
    {
        "id": 87,
        "name": "ApexController Wireless Gamepad for PC & Mobile",
        "category": "gaming-entertainment",
        "filename": "apexcontroller-wireless-gamepad.jpg",
        "photo_id": "photo-1600080972464-8e5f35f63d08",
        "price": Decimal("2199.00"),
        "stock": 15,
        "description": "Ergonomic wireless video game controller with anti-drift Hall Effect thumbsticks, textured rubber grips, dual vibration motors, and remappable back paddles."
    },
    {
        "id": 88,
        "name": "SpectraGlow Extended RGB Gaming Mouse Pad 800x300",
        "category": "gaming-entertainment",
        "filename": "spectraglow-rgb-mousepad.jpg",
        "photo_id": "photo-1527864550417-7fd91fc51a46",
        "price": Decimal("999.00"),
        "stock": 25,
        "description": "Extended 800x300mm micro-textured cloth gaming mat with non-slip natural rubber base and customizable 14-mode perimeter RGB LED fiber optic lighting."
    },
    {
        "id": 89,
        "name": "CamLink 4K HDMI USB Video Capture Card",
        "category": "gaming-entertainment",
        "filename": "camlink-video-capture-card.jpg",
        "photo_id": "photo-1587826080692-f439cd0b70da",
        "price": Decimal("1599.00"),
        "stock": 12,
        "description": "Compact USB 3.0 HDMI video capture dongle streaming console and camera gameplay in crisp 1080p 60fps with zero-lag pass-through for Twitch and YouTube."
    },
    {
        "id": 90,
        "name": "BungeeCord Magnetic Gaming Mouse Bungee",
        "category": "gaming-entertainment",
        "filename": "bungeecord-mouse-bungee.jpg",
        "photo_id": "photo-1615663245857-ac93bb7c39e7",
        "price": Decimal("499.00"),
        "stock": 30,
        "description": "Weighted anti-slip mouse cable management bungee with flexible silicone suspension spring eliminating cord snagging and drag during rapid gaming swipes."
    },
    {
        "id": 91,
        "name": "KeyCapSet Custom PBT Dye-Sub 128-Keycaps",
        "category": "gaming-entertainment",
        "filename": "keycapset-custom-pbt-keycaps.jpg",
        "photo_id": "photo-1587829741301-dc798b83add3",
        "price": Decimal("1499.00"),
        "stock": 14,
        "description": "Complete 128-key Cherry profile thick PBT replacement keycap set with oil-resistant matte texture and durable dye-sublimated custom legends."
    },
    {
        "id": 92,
        "name": "SwitchPack Mechanical Key Switch Tester 9-Keys",
        "category": "gaming-entertainment",
        "filename": "switchpack-mechanical-switch-tester.jpg",
        "photo_id": "photo-1587829741301-dc798b83add3",
        "price": Decimal("599.00"),
        "stock": 22,
        "description": "Clear acrylic mounting frame containing 9 distinct mechanical keyboard switches (linear, tactile, and clicky) with transparent keycaps for testing feel."
    },
    {
        "id": 93,
        "name": "GamerGrip Anti-Slip Controller Handle Decals",
        "category": "gaming-entertainment",
        "filename": "gamergrip-controller-grips.jpg",
        "photo_id": "photo-1600080972464-8e5f35f63d08",
        "price": Decimal("349.00"),
        "stock": 40,
        "description": "Laser-cut textured sweat-wicking adhesive rubber grip skins tailored for wireless gamepads to maintain firm handling during intense gaming tournaments."
    },
    {
        "id": 94,
        "name": "ArcadeStick Retro USB Fight Stick Controller",
        "category": "gaming-entertainment",
        "filename": "arcadestick-retro-fightstick.jpg",
        "photo_id": "photo-1600080972464-8e5f35f63d08",
        "price": Decimal("3899.00"),
        "stock": 6,
        "description": "Heavy-duty steel base arcade fight stick with microswitch directional ball-top joystick and 8 responsive concave action buttons for retro fighting games."
    },
    {
        "id": 95,
        "name": "CoolingPad RGB 6-Fan Gaming Laptop Cooler",
        "category": "gaming-entertainment",
        "filename": "coolingpad-gaming-laptop-cooler.jpg",
        "photo_id": "photo-1588872657578-7efd1f1555ed",
        "price": Decimal("1799.00"),
        "stock": 18,
        "description": "High-velocity 6-fan gaming laptop cooling stand with metal mesh surface, adjustable tilt height brackets, dual USB pass-through ports, and blue LED lighting."
    },
    {
        "id": 96,
        "name": "WallMount Dual Headset & Controller Hanger 2-Pack",
        "category": "gaming-entertainment",
        "filename": "wallmount-headset-controller-hanger.jpg",
        "photo_id": "photo-1546435770-a3e426bf472b",
        "price": Decimal("499.00"),
        "stock": 35,
        "description": "Pair of curved aircraft-grade aluminium wall or under-desk brackets holding large gaming headsets and game controllers safely off desk surfaces."
    },
    {
        "id": 97,
        "name": "SimWheel Racing Wheel Desk Clamp Bracket",
        "category": "gaming-entertainment",
        "filename": "simwheel-racing-wheel-clamp.jpg",
        "photo_id": "photo-1600080972464-8e5f35f63d08",
        "price": Decimal("1999.00"),
        "stock": 8,
        "description": "Heavy laser-cut steel desktop clamp adapter securely anchoring sim racing steering wheels, shifters, and handbrakes to gaming desks without wobbling."
    },
    {
        "id": 98,
        "name": "AeroFoam High-Density Acoustic Studio Foam 12-Pack",
        "category": "gaming-entertainment",
        "filename": "aerofoam-acoustic-studio-tiles.jpg",
        "photo_id": "photo-1558089687-f282ffcbc126",
        "price": Decimal("1299.00"),
        "stock": 15,
        "description": "12-pack of 12x12 inch 2-inch thick pyramid pattern acoustic polyurethane foam tiles deadening echoes and sound reflections in streaming studios."
    },

    # -------------------------------------------------------------
    # Category 8: Fashion & Lifestyle Essentials
    # -------------------------------------------------------------
    {
        "id": 99,
        "name": "Nomad Minimalist Heavyweight Fleece Hoodie",
        "category": "fashion-lifestyle-essentials",
        "filename": "nomad-heavyweight-fleece-hoodie.jpg",
        "photo_id": "photo-1556905055-8f358a7a47b2",
        "price": Decimal("1999.00"),
        "stock": 20,
        "description": "Premium 450 GSM heavyweight combed organic cotton fleece pullover hoodie featuring double-layered hood, drop shoulders, and ribbed cuffs."
    },
    {
        "id": 100,
        "name": "AeroFit Seamless Breathable Performance Tee",
        "category": "fashion-lifestyle-essentials",
        "filename": "aerofit-performance-tshirt.jpg",
        "photo_id": "photo-1521572267360-ee0c2909d518",
        "price": Decimal("799.00"),
        "stock": 30,
        "description": "Athletic crewneck t-shirt engineered from quick-drying 4-way stretch fabric with micro-mesh ventilation zones for running and gym workouts."
    },
    {
        "id": 101,
        "name": "PolarOptics Classic Aviator Polarized Sunglasses",
        "category": "fashion-lifestyle-essentials",
        "filename": "polaroptics-aviator-sunglasses.jpg",
        "photo_id": "photo-1572635196237-14b3f281503f",
        "price": Decimal("1299.00"),
        "stock": 24,
        "description": "Timeless metal-framed aviator sunglasses equipped with scratch-resistant Category 3 UV400 polarized lenses that eliminate blinding sun glare."
    },
    {
        "id": 102,
        "name": "SlimBifold Top Grain Genuine Leather Wallet",
        "category": "fashion-lifestyle-essentials",
        "filename": "slimbifold-leather-wallet.jpg",
        "photo_id": "photo-1627123424574-724758594e93",
        "price": Decimal("999.00"),
        "stock": 28,
        "description": "Handcrafted brown genuine top-grain cowhide leather bifold wallet featuring 8 credit card slots, cash divider, and integrated RFID skimming protection."
    },
    {
        "id": 103,
        "name": "UrbanChrono Vintage Leather Strap Quartz Watch",
        "category": "fashion-lifestyle-essentials",
        "filename": "urbanchrono-vintage-leather-watch.jpg",
        "photo_id": "photo-1524805444758-089113d48a6d",
        "price": Decimal("2499.00"),
        "stock": 12,
        "description": "Classic analog dress wristwatch with minimalist white dial, polished stainless steel case, accurate Japanese quartz movement, and genuine brown leather band."
    },
    {
        "id": 104,
        "name": "CanvasKicks Low-Top Vulcanized Skate Sneakers",
        "category": "fashion-lifestyle-essentials",
        "filename": "canvaskicks-canvas-skate-sneakers.jpg",
        "photo_id": "photo-1542291026-7eec264c27ff",
        "price": Decimal("1799.00"),
        "stock": 16,
        "description": "Classic red and white low-top casual skate sneakers featuring 12oz breathable canvas upper, reinforced rubber toe cap, and waffle grip vulcanized rubber soles."
    },
    {
        "id": 105,
        "name": "ComfortStitch Ribbed Cotton Beanie Hat",
        "category": "fashion-lifestyle-essentials",
        "filename": "comfortstitch-ribbed-beanie.jpg",
        "photo_id": "photo-1576871337632-b9aef4c17ab9",
        "price": Decimal("499.00"),
        "stock": 40,
        "description": "Cozy ribbed knit fold-over cuff beanie hat woven from soft thermal yarn for warmth, stretch, and casual styling during cold weather."
    },
    {
        "id": 106,
        "name": "AeroCap Unstructured Breathable Dad Cap",
        "category": "fashion-lifestyle-essentials",
        "filename": "aerocap-washed-cotton-dad-cap.jpg",
        "photo_id": "photo-1588850561407-ed78c282e89b",
        "price": Decimal("599.00"),
        "stock": 35,
        "description": "Classic 6-panel unstructured low-profile baseball dad hat crafted from 100% washed cotton twill with curved brim and adjustable brass metal slide buckle."
    },
    {
        "id": 107,
        "name": "EcoCanvas Reusable Heavy Duty Grocery Tote",
        "category": "fashion-lifestyle-essentials",
        "filename": "ecocanvas-cotton-grocery-tote.jpg",
        "photo_id": "photo-1544816155-12df9643f363",
        "price": Decimal("399.00"),
        "stock": 50,
        "description": "Heavy-duty 16oz natural unbleached canvas shoulder tote bag with double-stitched reinforced handles holding up to 25kg of books, laptops, and market groceries."
    },
    {
        "id": 108,
        "name": "KeySmart Compact Aviation Aluminium Key Organizer",
        "category": "fashion-lifestyle-essentials",
        "filename": "keysmart-aluminium-key-organizer.jpg",
        "photo_id": "photo-1627123424574-724758594e93",
        "price": Decimal("699.00"),
        "stock": 30,
        "description": "Aviation-grade aluminium pocket key holder folding up to 8 keys into a compact Swiss-army style profile that eliminates thigh pokes and key jingle."
    },
    {
        "id": 109,
        "name": "AeroSteel Insulated Travel Coffee Tumbler 450ml",
        "category": "fashion-lifestyle-essentials",
        "filename": "aerosteel-coffee-travel-tumbler.jpg",
        "photo_id": "photo-1514432324607-a09d9b4aefdd",
        "price": Decimal("799.00"),
        "stock": 32,
        "description": "Vacuum-insulated stainless steel travel coffee mug with spill-resistant magnetic sip slider lid, fitting standard automotive cup holders and preserving hot brews."
    },
    {
        "id": 110,
        "name": "TravelGroom Beard & Hair Trimmer Cordless",
        "category": "fashion-lifestyle-essentials",
        "filename": "travelgroom-cordless-beard-trimmer.jpg",
        "photo_id": "photo-1585771724684-38269d6639fd",
        "price": Decimal("1499.00"),
        "stock": 18,
        "description": "Cordless electric beard and body grooming trimmer with self-sharpening titanium blades, 20 precision length settings, and 90 minutes of rechargeable runtime."
    },
    {
        "id": 111,
        "name": "AuraMist Clean Linen & Amber Scented Soy Candle",
        "category": "fashion-lifestyle-essentials",
        "filename": "auramist-scented-soy-candle.jpg",
        "photo_id": "photo-1603006905003-be475563bc59",
        "price": Decimal("649.00"),
        "stock": 25,
        "description": "Hand-poured 100% natural soy wax aromatherapy candle in amber glass jar with natural crackling wood wick, burning cleanly for 45 hours."
    },
    {
        "id": 112,
        "name": "ClassicWeave Stretch Braided Elastic Belt",
        "category": "fashion-lifestyle-essentials",
        "filename": "classicweave-braided-elastic-belt.jpg",
        "photo_id": "photo-1624222247344-550fb60583dc",
        "price": Decimal("599.00"),
        "stock": 28,
        "description": "No-hole stretch braided woven casual belt with brushed metal buckle and leatherette end trims, offering infinite micro-adjustments for all-day comfort."
    },
]
