import requests, os, pickle, json, binascii, time, urllib3, base64, ssl, aiohttp, asyncio
import DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2, sQ_pb2, devxt_count_pb2, dev_generator_pb2
from God_BlazexC4 import *
from xHeaders import *
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# =================== CONFIGURATION ======================
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

# =================== GLOBAL VARIABLES ===================
online_writer = None
whisper_writer = None
spammer_uid = None

status_response_cache = {} 
pending_status_requests = {}
room_info_cache = {}
last_status_packet = None
insquad = None 
joining_team = False 
online_writer = None 
whisper_writer = None 
last_bot_status_check = 0
senthi = False
bot_status_cache_time = 30
cached_bot_status = None
last_status_packet = None
START_SPAM_DURATION = 18     
WAIT_AFTER_MATCH_SECONDS = 20 
START_SPAM_DELAY = 0.2       
region = 'IN'
WHITELISTED_UIDS = {
    "537512413",
    "1136824736"
}
# ADMIN INFO FUNCTION FOR ADMIN COMMAND 
ADMIN_UID = "537512413"
ADMIN_UID_2 = "1136824736"
server2 = "BD"
key2 = "mg24"
BYPASS_TOKEN = "your_bypass_token_here"
WHITELIST_ONLY = False
bot_enabled = True
BOT_OWNER_UID = 537512413  
PLAYER_NAME_CACHE = {}
PLAYER_NAME_CACHE = 'name_cache.json'
# ========== NAME DISPLAY CONFIG ==========
NAME_DISPLAY_ENABLED = False   # True = নাম দেখাবে, False = শুধু "User" দেখাবে
freeze_running = False
freeze_task = None
FREEZE_EMOTES = [909052010, 909052010, 909052010]
FREEZE_DURATION = 10  # seconds
evo_emotes = {
    "1": "909000063",   # AK
    "2": "909000068",   # SCAR
    "3": "909000075",   # 1st MP40
    "4": "909040010",   # 2nd MP40
    "5": "909000081",   # 1st M1014
    "6": "909039011",   # 2nd M1014
    "7": "909000085",   # XM8
    "8": "909000090",   # Famas
    "9": "909000098",   # UMP
    "10": "909035007",  # M1887
    "11": "909042008",  # Woodpecker
    "12": "909041005",  # Groza
    "13": "909033001",  # M4A1
    "14": "909038010",  # Thompson
    "15": "909038012",  # G18
    "16": "909045001",  # Parafal
    "17": "909049010",  # P90
    "18": "909051003"   # m60
}
#------------------------------------------#

# Emote mapping for evo commands
EMOTE_MAP = {
    1: 909000063,
    2: 909000081,
    3: 909000075,
    4: 909000085,
    5: 909000134,
    6: 909000098,
    7: 909035007,
    8: 909051012,
    9: 909000141,
    10: 909034008,
    11: 909051015,
    12: 909041002,
    13: 909039004,
    14: 909042008,
    15: 909051014,
    16: 909039012,
    17: 909040010,
    18: 909035010,
    19: 909041005,
    20: 909051003,
    21: 909034001
}

# Badge values for s1 to s8 commands - using your exact values
BADGE_VALUES = {
    "s1": 1048576,    # Your first badge
    "s2": 32768,      # Your second badge  
    "s3": 2048,       # Your third badge
    "s4": 64,         # Your fourth badge
    "s5": 262144     # Your seventh badge
}

# Admin Functions
def is_admin(uid):
    return str(uid) == ADMIN_UID or str(uid) == ADMIN_UID_2

# Mute Functions 
def is_off():
    return not bot_enabled

def ff_num(val):
    return xMsGFixinG(str(val)) if val not in (None, "") else "N/A"

from datetime import datetime
from zoneinfo import ZoneInfo  # Python 3.9+

def human_time(ts):
    try:
        ts = int(ts)
        bd_time = datetime.fromtimestamp(ts, ZoneInfo("Asia/Dhaka"))
        return bd_time.strftime("%d %b %Y, %I:%M %p")
    except:
        return "N/A"

# ==================== API SERVER LAUNCHER ====================
import subprocess
import sys
import os
import time

def start_api_servers():
    """APIS ফোল্ডারের সব সাবফোল্ডারে app.py খুঁজে আলাদা প্রসেসে চালায়"""
    apis_dir = os.path.join(os.path.dirname(__file__), "APIS")
    if not os.path.exists(apis_dir):
        print("[ WARNING ] APIS folder not found. Skipping API server startup.")
        return []
    
    processes = []
    for item in os.listdir(apis_dir):
        item_path = os.path.join(apis_dir, item)
        if os.path.isdir(item_path):
            app_file = os.path.join(item_path, "app.py")
            if os.path.isfile(app_file):
                print(f"[ SYSTEM ] Starting API server from {app_file}...")
                proc = subprocess.Popen(
                    [sys.executable, app_file],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                processes.append(proc)
                print(f"[ SUCCESS ] Started {item} API with PID {proc.pid}")
            else:
                print(f"[ WARNING ] No app.py found in {item_path}, skipping.")
    
    if processes:
        print(f"[ SYSTEM ] Waiting 3 seconds for API servers to initialize...")
        time.sleep(3)
    return processes

def titles():
    """Return all titles instead of just one random"""
    titles_list = [
        905090075, 904990072, 904990069, 905190079
    ]
    return titles_list  # Return the full list instead of random.choice            
    
def create_credentials_template():
    """Create a template credentials file"""
    template = """# God Blaze Free Fire Bot Credentials
# Fill in your Free Fire account credentials below

# Format 1: Comma-separated (RECOMMENDED)
uid=YOUR_UID_HERE,password=YOUR_PASSWORD_HERE

# OR Format 2: Line-separated
# uid: YOUR_UID_HERE
# password: YOUR_PASSWORD_HERE

# Save this file and restart the bot
"""
    
    filename = "God_Blaze.txt"
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(template)
        print(f"📝 Created {filename} template file")
        print("✏️ Please edit it with your actual credentials")
        return False
    return True
    
da = 'f2212101'
dec = ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']
x_list = ['1','01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f']

def Decrypt_ID(da):
    """EXACT SAME as your code"""
    if da != None and len(da) == 10:
        w = 128
        xxx = len(da)/2 - 1
        xxx = str(xxx)[:1]
        for i in range(int(xxx)-1):
            w = w * 128
        x1 = da[:2]
        x2 = da[2:4]
        x3 = da[4:6]
        x4 = da[6:8]
        x5 = da[8:10]
        return str(w * x_list.index(x5) + (dec.index(x2) * 128) + dec.index(x1) + (dec.index(x3) * 128 * 128) + (dec.index(x4) * 128 * 128 * 128))

    if da != None and len(da) == 8:
        w = 128
        xxx = len(da)/2 - 1
        xxx = str(xxx)[:1]
        for i in range(int(xxx)-1):
            w = w * 128
        x1 = da[:2]
        x2 = da[2:4]
        x3 = da[4:6]
        x4 = da[6:8]
        return str(w * x_list.index(x4) + (dec.index(x2) * 128) + dec.index(x1) + (dec.index(x3) * 128 * 128))
    
    return None

def Encrypt_ID(x):
    """EXACT SAME as your code"""
    x = int(x)
    x = x / 128 
    if x > 128:
        x = x / 128
        if x > 128:
            x = x / 128
            if x > 128:
                x = x / 128
                strx = int(x)
                y = (x - int(strx)) * 128
                stry = str(int(y))
                z = (y - int(stry)) * 128
                strz = str(int(z))
                n = (z - int(strz)) * 128
                strn = str(int(n))
                m = (n - int(strn)) * 128
                return dec[int(m)] + dec[int(n)] + dec[int(z)] + dec[int(y)] + x_list[int(x)]
            else:
                strx = int(x)
                y = (x - int(strx)) * 128
                stry = str(int(y))
                z = (y - int(stry)) * 128
                strz = str(int(z))
                n = (z - int(strz)) * 128
                strn = str(int(n))
                return dec[int(n)] + dec[int(z)] + dec[int(y)] + x_list[int(x)]

def decrypt_api(cipher_text):
    """EXACT SAME as your code"""
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(bytes.fromhex(cipher_text)), AES.block_size)
    return plain_text.hex()

def encrypt_api(plain_text):
    """EXACT SAME as your code"""
    plain_text = bytes.fromhex(plain_text)
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher_text.hex()

def encrypt_message(plaintext_bytes):
    """EXACT SAME as your Flask API"""
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(plaintext_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded)
    return binascii.hexlify(encrypted).decode('utf-8')    

def create_uid_protobuf(uid):
    """EXACT SAME as your Flask API"""
    msg = dev_generator_pb2.dev_generator()
    msg.saturn_ = int(uid)
    msg.garena = 1
    return msg.SerializeToString()

def enc(uid):
    """EXACT SAME as your Flask API"""
    pb = create_uid_protobuf(uid)
    return encrypt_message(pb)

def decode_player_info(binary):
    """EXACT SAME as your Flask API"""
    info = devxt_count_pb2.xt()
    info.ParseFromString(binary)
    return info    
    
import requests
import json

def load_jwt_token():
    """Load token from /tmp/token.json"""
    try:
        with open("/tmp/token.json", "r") as f:
            data = json.load(f)
        token = data.get("token")
        if token:
            print(f"[ SUCCESS ] Loaded token: {token[:20]}...")
            return token
        else:
            print("[ ERROR ] No token found in /tmp/token.json")
            return None
    except Exception as e:
        print(f"[ ERROR ] Error loading token: {e}")
        return None

def load_tokens_ind():
    """Load bulk tokens from token_ind.json"""
    try:
        with open("token_ind.json", "r") as f:
            tokens = json.load(f)
        print(f"[ DATA ] Loaded {len(tokens)} tokens from token_ind.json")
        return tokens
    except:
        print("[ ERROR ] No tokens found in token_ind.json")
        return None


def get_region_from_token(token):
    try:
        parts = token.split('.')
        if len(parts) < 2:
            return None
        payload_b64 = parts[1] + '=' * (-len(parts[1]) % 4)
        import base64, json
        payload = json.loads(base64.urlsafe_b64decode(payload_b64).decode())
        return payload.get('lock_region', '').upper()
    except Exception as e:
        print(f"[ WARNING ] Token region decode error: {e}")
        return None

def get_player_info(uid):
    try:
        url = f"https://mg24-gamer-king.vercel.app/info/get?uid={uid}"
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            return None, f"API Error: {res.status_code}"

        data = res.json()

        # basic validation
        if "AccountInfo" not in data:
            return None, "Invalid API response"

        return data

    except requests.exceptions.Timeout:
        return None, "Request timeout"

    except Exception as e:
        return None, str(e)


def send_friend_request_single(uid, token, region="IND"):
    """EXACT SAME as your Flask function but single"""
    try:
        encrypted_id = Encrypt_ID(uid)
        payload = f"08a7c4839f1e10{encrypted_id}1801"
        encrypted_payload = encrypt_api(payload)
        
        # Determine URL based on region
        if region.lower() == "ind":
            url = "https://client.ind.freefiremobile.com/RequestAddingFriend"
        elif region.lower() == "bd":
            url = "https://client.bd.freefiremobile.com/RequestAddingFriend"
        else:
            url = "https://client.ind.freefiremobile.com/RequestAddingFriend"
        
        headers = {
            "Authorization": f"Bearer {token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB53",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0"
        }
        
        print(f"📤 Sending friend request to {uid}...")
        response = requests.post(url, data=bytes.fromhex(encrypted_payload), headers=headers, timeout=10, verify=False)
        
        if response.status_code == 200:
            print(f"✅ Success: Friend request sent to {uid}")
            return True
        else:
            print(f"❌ Failed: Status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False    
    
def start_autooo(self):    
    try:
        fields = {
            1: 9,
            2: {
                1: 12480598706,
            },
        }
        packet = create_protobuf_packet(fields).hex()
        header_length = len(encrypt_packet(packet, self.key, self.iv)) // 2
        header_length_final = dec_to_hex(header_length)
        if len(header_length_final) == 2:
            final_packet = "0515000000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 3:
            final_packet = "051500000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 4:
            final_packet = "05150000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 5:
            final_packet = "0515000" + header_length_final + self.nmnmmmmn(packet)
        return bytes.fromhex(final_packet)
    except exception as e:
        print(e)

def load_credentials_from_file(filename="God_Blaze.txt"):
    """
    Load UID and password from God_Blaze.txt file
    """
    try:
        if not os.path.exists(filename):
            print(f"[ ERROR ] {filename} not found!")
            create_credentials_template()
            return None, None  # Always return tuple of two values
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        uid = None
        password = None
        
        # Try to find uid and password using regex
        import re
        
        # Look for uid=value or uid: value
        uid_match = re.search(r'(?:uid\s*[=:]\s*)(\d+)', content, re.IGNORECASE)
        if uid_match:
            uid = uid_match.group(1)
        
        # Look for password=value or password: value
        pass_match = re.search(r'(?:password\s*[=:]\s*)([^\s\n\r]+)', content, re.IGNORECASE)
        if pass_match:
            password = pass_match.group(1)
        
        if not uid or not password:
            print(f"[ ERROR ] Could not find UID/password in {filename}")
            print("[ INFO ] Please make sure the file contains:")
            print("[ INFO ]    uid=YOUR_UID,password=YOUR_PASSWORD")
            print("[ INFO ]    OR")
            print("[ INFO ]    uid: YOUR_UID")
            print("[ INFO ]    password: YOUR_PASSWORD")
            return None, None  # Always return tuple
        
        print(f"[ SUCCESS ] Loaded credentials from {filename}")
        print(f"[ USER ] UID: {uid}")
        print(f"[ USER ] Password: {password}")
        
        return uid, password  # Return exactly two values
        
    except Exception as e:
        print(f"[ ERROR ] Error loading credentials: {e}")
        return None, None  # Always return tuple

# Load emotes from JSON file (your format)
def load_emotes_from_json():
    """Load emote IDs from emotes.json file with your exact format"""
    emotes_file = "emotes.json"
    
    try:
        with open(emotes_file, 'r') as f:
            emotes_data = json.load(f)
        
        # Access using your structure: data["EMOTES"]["numbers"] and data["EMOTES"]["names"]
        number_emotes = emotes_data.get("EMOTES", {}).get("numbers", {})
        name_emotes = emotes_data.get("EMOTES", {}).get("names", {})
        
        print(f"[ SUCCESS ] Loaded {len(number_emotes)} number emotes and {len(name_emotes)} named emotes")
        return {
            "numbers": number_emotes,
            "names": name_emotes
        }
        
    except Exception as e:
        print(f"[ ERROR ] Error loading {emotes_file}: {e}")
        # Return empty dictionaries as fallback
        return {"numbers": {}, "names": {}}

# Load emotes globally
EMOTES_DATA = load_emotes_from_json()
NUMBER_EMOTES = EMOTES_DATA["numbers"]
NAME_EMOTES = EMOTES_DATA["names"]

# Helper functions for ghost join
def dec_to_hex(decimal):
    """Convert decimal to hex string"""
    hex_str = hex(decimal)[2:]
    return hex_str.upper() if len(hex_str) % 2 == 0 else '0' + hex_str.upper()



async def encrypt_packet(packet_hex, key, iv):
    """Encrypt packet using AES CBC"""
    cipher = AES.new(key, AES.MODE_CBC, iv)
    packet_bytes = bytes.fromhex(packet_hex)
    padded_packet = pad(packet_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded_packet)
    return encrypted.hex()

async def nmnmmmmn(packet_hex, key, iv):
    """Wrapper for encrypt_packet"""
    return await encrypt_packet(packet_hex, key, iv)
    

def generate_random_hex_color():
    """Generate random hex color for messages"""
    return ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

def bunner_():
    """Generate random avatar ID"""
    return random.randint(100000000, 999999999)

# Add this function to your code
def Encrypt(number):
    """Encrypt function from your first TCP bot"""
    number = int(number)
    encoded_bytes = []
    
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number:
            break
    
    return bytes(encoded_bytes).hex()


async def send_working_join_request(target_uid, key, iv, region, LoGinDaTaUncRypTinG):
    """Send join request that actually works"""
    
    try:
        # Step 1: Reset bot to solo mode
        print("[ SYSTEM ] Resetting bot to solo mode...")
        await reset_bot_state(key, iv, region)
        await asyncio.sleep(1)
        
        # Step 2: Create bot's own squad (so it has context)
        print("[ SYSTEM ] Creating bot squad...")
        squad_packet = await OpEnSq(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', squad_packet)
        await asyncio.sleep(1)
        
        # Step 3: Send join request
        print(f"[ NETWORK ] Sending join request to {xMsGFixinG(target_uid)}...")
        join_packet = await create_working_join_request(target_uid, key, iv, region, LoGinDaTaUncRypTinG)
        
        if join_packet:
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            print(f"[ SUCCESS ] Bot join request sent! Player can now accept.")
            return True
        else:
            print(f"[ ERROR ] Failed to create join packet")
            return False
            
    except Exception as e:
        print(f"[ ERROR ] Error in working join request: {e}")
        return False
        
async def create_simple_start_packet(key, iv):
    """Create simple start match packet (00 00 00 d6)"""
    
    # This appears to be a minimal start packet
    # 00 00 00 d6 in hex = 214 in decimal (packet type?)
    
    fields = {
        1: 214,  # Packet type for start match (d6 hex = 214 decimal)
        2: {
            1: 1,  # Start match command
        }
    }
    
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Generate final packet
    final_packet = await GeneRaTePk(packet_hex, '0514', key, iv)  # Use appropriate packet type
    
    print(f"[ SUCCESS ] Simple start match packet created")
    return final_packet
    
async def create_detailed_start_packet(key, iv, region="IND"):
    """Create detailed start match packet with device info"""
    
    # Decoded from your hex: contains device info (vivo, arm64, etc.)
    
    fields = {
        1: 269,  # 0x10D = 269 decimal (detailed start packet)
        2: {
            1: 8,           # Unknown
            2: 8,           # Unknown
            3: 11,          # Unknown
            4: 1,           # Unknown
            5: "vivo",      # Device brand
            6: "130",       # Device model
            7: "arm64-v8a", # CPU architecture
            8: "f538dc9b-cec9-43cd-8125-95f7f4f1f7e3",  # Device ID
            9: "FFD58FB4F76F648C2A5E21EBCFA3AAE81B4C9B7D97",  # Unknown
            10: "voice",    # Audio type
            11: "V2059",    # Version
            12: "mt6785",   # Processor
            13: "AFFD58FB4F76F648C2A5E21EBCFA3AAE81B4C9B7D97",  # Unknown
            14: "IND_1999120752610979840",  # Region + timestamp
            15: 269         # Packet length?
        }
    }
    
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Determine packet type based on region
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    final_packet = await GeneRaTePk(packet_hex, packet_type, key, iv)
    
    print(f"[ SUCCESS ] Detailed start match packet created")
    return final_packet
        
async def generate_guest_accounts(count=1, name="BlackApis", password_prefix="FF"):
    """Generate guest accounts using the API"""
    api_url = f"https://gen-by-black-api.vercel.app/generate?name={name}&password_prefix={password_prefix}"
    
    accounts = []
    failed_attempts = 0
    max_retries = 10
    
    print(f"[ NETWORK ] Generating {count} guest accounts...")
    
    for i in range(count):
        retry_count = 0
        success = False
        
        while retry_count < max_retries and not success:
            try:
                print(f"[ SYSTEM ] Attempt {retry_count + 1}/{max_retries} for account {i + 1}/{count}...")
                
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=30)) as session:
                    async with session.get(api_url) as response:
                        
                        if response.status == 200:
                            data = await response.json()
                            
                            if data.get("success"):
                                account = {
                                    'uid': data.get('uid'),
                                    'password': data.get('password'),
                                    'name': data.get('name'),
                                    'timestamp': time.time()
                                }
                                accounts.append(account)
                                print(f"[ SUCCESS ] Account {i + 1}: {account['uid']}")
                                success = True
                                failed_attempts = 0  # Reset failed attempts counter
                                
                            else:
                                print(f"[ ERROR ] API error: {data.get('message', 'Unknown error')}")
                                retry_count += 1
                                await asyncio.sleep(2)
                                
                        elif response.status == 503:
                            print(f"[ WARNING ] Server busy (503), retrying in 3 seconds...")
                            retry_count += 1
                            await asyncio.sleep(3)
                            
                        else:
                            print(f"[ ERROR ] HTTP {response.status}, retrying...")
                            retry_count += 1
                            await asyncio.sleep(2)
                            
            except asyncio.TimeoutError:
                print(f"[ WARNING ] Timeout, retrying...")
                retry_count += 1
                await asyncio.sleep(2)
                
            except Exception as e:
                print(f"[ ERROR ] Error: {str(e)[:50]}...")
                retry_count += 1
                await asyncio.sleep(2)
        
        if not success:
            print(f"[ ERROR ] Failed to generate account {i + 1} after {max_retries} attempts")
            failed_attempts += 1
            
            # If too many failures in a row, stop
            if failed_attempts >= 3:
                print("[ ERROR ] Too many failures, stopping...")
                break
        
        # Small delay between accounts to avoid rate limiting
        if i < count - 1:
            await asyncio.sleep(1)
    
    return accounts

def save_guest_accounts(accounts, filename="guest_accounts.json"):
    """Save guest accounts to JSON file"""
    try:
        # Load existing accounts if file exists
        existing = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                existing = json.load(f)
        
        # Combine with new accounts
        all_accounts = existing + accounts
        
        # Save to file
        with open(filename, 'w') as f:
            json.dump(all_accounts, f, indent=2)
        
        print(f"[ DATA ] Saved {len(accounts)} accounts to {filename}")
        print(f"[ INFO ] Total accounts: {len(all_accounts)}")
        
        return True
    except Exception as e:
        print(f"[ ERROR ] Error saving accounts: {e}")
        return False


        print(f"[ ERROR ] Could not parse: {e}")
        


async def check_player_status(target_uid, key, iv, max_wait=3):
    """Direct function to check player status with proper waiting"""
    try:
        # Clear old cache
        if target_uid in status_response_cache:
            del status_response_cache[target_uid]
        
        # Send request
        status_packet = await createpacketinfo(target_uid, key, iv)
        if not status_packet:
            return None, "Failed to create packet"
        
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', status_packet)
        print(f"[ NETWORK ] Sent status request for {xMsGFixinG(target_uid)}")
        
        # Wait for response with polling
        start_time = time.time()
        while time.time() - start_time < max_wait:
            if target_uid in status_response_cache:
                cache_data = status_response_cache[target_uid]
                return cache_data, "Success"
            
            await asyncio.sleep(0.1)  # Short sleep
        
        return None, f"No response after {max_wait} seconds"
        
    except Exception as e:
        return None, f"Error: {str(e)}"

async def createpacketinfo(idddd, key, iv):
    """Create player status request packet - SAME as first TCP bot"""
    try:
        ida = Encrypt(idddd)
        packet = f"080112090A05{ida}1005"
        header_lenth = len(await encrypt_packet(packet, key, iv)) // 2
        header_lenth_final = dec_to_hex(header_lenth)
        
        if len(header_lenth_final) == 2:
            final_packet = "0F15000000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 3:
            final_packet = "0F1500000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 4:
            final_packet = "0F150000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 5:
            final_packet = "0F15000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        else:
            final_packet = "0F1500000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
            
        return bytes.fromhex(final_packet)
        
    except Exception as e:
        print(f"[ ERROR ] Error creating packet info: {e}")
        return None

def fix_num(number):
    """Format numbers with breaks - from first TCP"""
    fixed = ""
    count = 0
    num_str = str(number)
    
    for char in num_str:
        if char.isdigit():
            count += 1
        fixed += char
        if count == 3:
            fixed += "[c]"
            count = 0
    return fixed

def get_available_room(input_text):
    """Parse protobuf to JSON - from first TCP"""
    try:
        from protobuf_decoder.protobuf_decoder import Parser
        parsed_results = Parser().parse(input_text)
        parsed_results_objects = parsed_results
        parsed_results_dict = parse_results(parsed_results_objects)
        json_data = json.dumps(parsed_results_dict)
        return json_data
    except Exception as e:
        print(f"[ ERROR ] error {e}")
        return None

async def ghost_pakcet(player_id , secret_code ,K , V):
    fields = {
        1: 61,
        2: {
            1: int(player_id),  
            2: {
                1: int(player_id),  
                2: int(time.time()),  
                3: "MR3SKR",
                5: 12,  
                6: 9999999,
                7: 1,
                8: {
                    2: 1,
                    3: 1,
                },
                9: 3,
            },
            3: secret_code,},}
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , K , V)

def parse_results(parsed_results):
    """Helper for get_available_room"""
    result_dict = {}
    for result in parsed_results:
        field_data = {}
        field_data["wire_type"] = result.wire_type
        if result.wire_type == "varint":
            field_data["data"] = result.data
        if result.wire_type == "string":
            field_data["data"] = result.data
        if result.wire_type == "bytes":
            field_data["data"] = result.data
        elif result.wire_type == "length_delimited":
            field_data["data"] = parse_results(result.data.results)
        result_dict[result.field] = field_data
    return result_dict  # ← ADD THIS LINE

def get_player_status(packet):
    """Get player status from packet"""
    json_result = get_available_room(packet)
    if not json_result:
        return "OFFLINE"
    
    parsed_data = json.loads(json_result)
    
    if "5" not in parsed_data or "data" not in parsed_data["5"]:
        return "OFFLINE"
    
    json_data = parsed_data["5"]["data"]
    
    if "1" not in json_data or "data" not in json_data["1"]:
        return "OFFLINE"
    
    data = json_data["1"]["data"]
    
    if "3" not in data:
        return "OFFLINE"
    
    status_data = data["3"]
    
    if "data" not in status_data:
        return "OFFLINE"
    
    status = status_data["data"]
    
    if status == 1:
        return "SOLO"
    if status == 2:
        if "9" in data and "data" in data["9"]:
            group_count = data["9"]["data"]
            countmax1 = data["10"]["data"]
            countmax = countmax1 + 1
            return f"INSQUAD ({group_count}/{countmax})"
        return "INSQUAD"
    if status in [3, 5]:
        return "INGAME"
    if status == 4:
        return "IN ROOM"
    if status in [6, 7]:
        return "IN SOCIAL ISLAND MODE"
    
    return "NOTFOUND"

def get_idroom_by_idplayer(packet):
    """Extract room ID from player info packet"""
    try:
        json_result = get_available_room(packet)
        parsed_data = json.loads(json_result)
        json_data = parsed_data["5"]["data"]
        data = json_data["1"]["data"]
        idroom = data['15']["data"]
        return idroom
    except Exception as e:
        print(f"[ ERROR ] Error extracting room ID: {e}")
        return None



def get_leader(packet):
    """Extract leader ID from squad packet"""
    try:
        json_result = get_available_room(packet)
        parsed_data = json.loads(json_result)
        json_data = parsed_data["5"]["data"]
        data = json_data["1"]["data"]
        leader = data['8']["data"]
        return leader
    except Exception as e:
        print(f"[ ERROR ] Error extracting leader: {e}")
        return None

# Add to your global variables

# Add near top with other globals
status_queue = asyncio.Queue()
cache_dict = {}

# In TcPOnLine, instead of caching directly:
async def handle_status_response(hex_data):
    """Process and queue status responses"""
    try:
        # ... parsing code ...
        
        # Put in queue instead of direct cache
        await status_queue.put({
            'player_id': player_id,
            'data': cache_entry
        })
        
        print(f"[ NETWORK ] Queued status for {xMsGFixinG(target_uid)}")
        
    except Exception as e:
        print(f"[ ERROR ] Queue error: {e}")

# In TcPChaT, add a queue consumer
async def cache_consumer():
    """Consume status responses from queue"""
    while True:
        try:
            item = await status_queue.get()
            player_id = item['player_id']
            cache_dict[player_id] = item['data']
            print(f"[ NETWORK ] Cache updated for {xMsGFixinG(target_uid)}")
            status_queue.task_done()
        except Exception as e:
            print(f"[ ERROR ] Consumer error: {e}")
        await asyncio.sleep(0.1)



# Start consumer in your main function
async def StarTinG():
    # Start consumer
    consumer_task = asyncio.create_task(cache_consumer())
    
    retry_delay = 120  # Start with 2 minutes (helps avoid rate limits)
    max_delay = 600  # Maximum 10 minutes
    consecutive_failures = 0
    
    while True:
        try:
            result = await asyncio.wait_for(MaiiiinE(), timeout = 7 * 60 * 60)
            
            # Reset delay on successful connection
            if result is not None:
                retry_delay = 5
                consecutive_failures = 0
            else:
                # Connection failed, apply backoff
                consecutive_failures += 1
                if consecutive_failures > 10:
                    print(f"[ ERROR ] Failed {consecutive_failures} times. Stopping bot.")
                    print("[ INFO ] Please check your credentials and try again later.")
                    break
                    
                print(f"[ SYSTEM ] Waiting {retry_delay} seconds before retry (Attempt {consecutive_failures}/10)...")
                await asyncio.sleep(retry_delay)
                
                # Exponential backoff
                retry_delay = min(retry_delay * 2, max_delay)
                
        except KeyboardInterrupt:
            consumer_task.cancel()
            break
        except asyncio.TimeoutError: 
            print("[ WARNING ] Token ExpiRed ! , ResTartinG")
            retry_delay = 5  # Reset on token expiry
        except Exception as e: 
            print(f"[ ERROR ] ErroR TcP - {e} => ResTarTinG ...")
            import traceback
            traceback.print_exc()
            
            consecutive_failures += 1
            if consecutive_failures > 10:
                print(f"[ ERROR ] Too many errors ({consecutive_failures}). Stopping bot.")
                break
                
            print(f"[ SYSTEM ] Waiting {retry_delay} seconds before retry...")
            await asyncio.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, max_delay)

import pickle
import os
import time

CACHE_FILE = 'status_cache.pkl'
CACHE_TIMEOUT = 30  # Cache entries expire after 30 seconds

def save_to_cache(player_id, data):
    """Save status to file cache with timestamp"""
    try:
        # Load existing cache
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'rb') as f:
                    cache = pickle.load(f)
            except:
                cache = {}
        else:
            cache = {}
        
        # Add timestamp
        data['saved_at'] = time.time()
        
        # Update cache
        cache[str(player_id)] = data
        
        # Save back
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump(cache, f)
        
        print(f"[ DATA ] Saved to file cache: {player_id}")
        return True
    except Exception as e:
        print(f"[ ERROR ] Cache save error: {e}")
        import traceback
        traceback.print_exc()
        return False

def load_from_cache(player_id):
    """Load status from file cache, check expiration"""
    try:
        if not os.path.exists(CACHE_FILE):
            return None
        
        with open(CACHE_FILE, 'rb') as f:
            cache = pickle.load(f)
        
        player_key = str(player_id)
        if player_key in cache:
            data = cache[player_key]
            
            # Check if cache is expired
            if 'saved_at' in data:
                if time.time() - data['saved_at'] > CACHE_TIMEOUT:
                    print(f"[ WARNING ] Cache expired for {player_id}")
                    del cache[player_key]
                    with open(CACHE_FILE, 'wb') as f:
                        pickle.dump(cache, f)
                    return None
            
            print(f"[ NETWORK ] Loaded from cache: {player_id}")
            return data
        
        return None
    except Exception as e:
        print(f"[ ERROR ] Cache load error: {e}")
        return None

def clear_cache_entry(player_id):
    """Clear specific cache entry"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            
            player_key = str(player_id)
            if player_key in cache:
                del cache[player_key]
                
            with open(CACHE_FILE, 'wb') as f:
                pickle.dump(cache, f)
            print(f"[ SYSTEM ] Cleared cache for {player_id}")
    except Exception as e:
        print(f"[ ERROR ] Clear cache error: {e}")

def debug_file_cache():
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            print(f"\n[ INFO ] FILE CACHE DEBUG:")
            print(f"[ INFO ] Size: {len(cache)} entries")
            for uid, data in cache.items():
                # আগে চেক করো data ডিকশনারি কিনা
                if isinstance(data, dict):
                    age = time.time() - data.get('saved_at', 0)
                    status = data.get('status', 'NO STATUS')
                else:
                    age = 0
                    status = str(data)
                print(f"[ INFO ]   {uid}: {status} (age: {age:.1f}s)")
            print("---\n")
            return cache
        else:
            print("[ INFO ] No cache file exists")
            return {}
    except Exception as e:
        print(f"[ ERROR ] Cache debug error: {e}")
        return {}

def load_from_cache(player_id):
    """Load status from file cache"""
    try:
        if not os.path.exists(CACHE_FILE):
            return None
        
        with open(CACHE_FILE, 'rb') as f:
            cache = pickle.load(f)
        
        if player_id in cache:
            return cache[player_id]
        return None
    except Exception as e:
        print(f"[ ERROR ] Cache load error: {e}")
        return None

def clear_cache_entry(player_id):
    """Clear specific cache entry"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            
            if player_id in cache:
                del cache[player_id]
                
            with open(CACHE_FILE, 'wb') as f:
                pickle.dump(cache, f)
    except:
        pass


    
    
    async def get_account_token(self, uid, password):
        """Get access token for a specific account"""
        try:
            url = "https://100067.connect.garena.com/oauth/guest/token/grant"
            headers = {
                "Host": "100067.connect.garena.com",
                "User-Agent": await Ua(),
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "close"
            }
            data = {
                "uid": uid,
                "password": password,
                "response_type": "token",
                "client_type": "2",
                "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
                "client_id": "100067"
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=data) as response:
                    if response.status == 200:
                        data = await response.json()
                        open_id = data.get("open_id")
                        access_token = data.get("access_token")
                        return open_id, access_token
            return None, None
        except Exception as e:
            print(f"[ ERROR ] Error getting token for {uid}: {e}")
            return None, None
    
    async def send_join_from_account(self, target_uid, account_uid, password, key, iv, region):
        """Send join request from a specific account"""
        try:
            # Get token for this account
            open_id, access_token = await self.get_account_token(account_uid, password)
            if not open_id or not access_token:
                return False
            
            # Create join packet using the account's credentials
            join_packet = await self.create_account_join_packet(target_uid, account_uid, open_id, access_token, key, iv, region)
            if join_packet:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                return True
            return False
            
        except Exception as e:
            print(f"[ ERROR ] Error sending join from {account_uid}: {e}")
            return False


    
async def leave_squad(key, iv, region):
    """Leave squad - converted from your old TCP leave_s()"""
    fields = {
        1: 7,
        2: {
            1: 12480598706  # Your exact value from old TCP
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)    
    
async def request_join_with_badge(target_uid, badge_value, key, iv, region="bd"):
    """Fixed badge spam function matching craftland_badge structure"""
    try:
        # Get random avatar
        avatar_id = int(await xBunnEr())
        
        fields = {
            1: 33,  # Packet type
            2: {
                1: int(target_uid),        # Target UID
                2: region.upper(),        # Country code
                3: 1,                     # Status 1
                4: 1,                     # Status 2
                5: bytes([1, 7, 9, 10, 11, 18, 25, 26, 32]),  # Numbers field
                6: "iG:[C][B][FF0000] God Blaze",  # Nickname
                7: 330,                   # Rank
                8: 1000,                  # Field 8
                10: region.upper(),       # Region code
                11: bytes([              # UUID
                    49, 97, 99, 52, 98, 56, 48, 101, 99, 102, 48, 52, 55, 56,
                    97, 52, 52, 50, 48, 51, 98, 102, 56, 102, 97, 99, 54, 49,
                    50, 48, 102, 53
                ]),
                12: 1,                    # Field 12
                13: int(target_uid),      # Repeated UID
                14: {                    # Field 14 (nested)
                    1: 2203434355,
                    2: 8,
                    3: b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
                },
                16: 1,                    # Field 16
                17: 1,                    # Field 17
                18: 312,                  # Field 18
                19: 46,                   # Field 19
                23: bytes([16, 1, 24, 1]), # Field 23
                24: avatar_id,            # Avatar ID
                26: {},                   # Empty field 26
                27: {                    # Field 27 (critical for badge!)
                    1: 11,               # Field 27.1
                    2: 13777711848,      # Field 27.2 (your bot UID)
                    3: 9999              # Field 27.3
                },
                28: {},                   # Empty field 28
                31: {                    # Field 31 (badge value here too)
                    1: 1,
                    2: int(badge_value)  # BADGE VALUE
                },
                32: int(badge_value),     # Field 32 (badge value again)
                34: {                    # Field 34
                    1: int(target_uid),  # Target UID again
                    2: 8,
                    3: b"\x0F\x06\x15\x08\x0A\x0B\x13\x0C\x11\x04\x0E\x14\x07\x02\x01\x05\x10\x03\x0D\x12"
                }
            },
            10: "en",                     # Language
            13: {                        # Field 13
                2: 1,
                3: 1
            }
        }
        
        # Convert to protobuf
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        # Determine packet type based on region
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        # Generate final encrypted packet
        final_packet = await GeneRaTePk(packet_hex, packet_type, key, iv)
        
        print(f"[ SUCCESS ] Created badge packet with value {badge_value} for UID {xMsGFixinG(target_uid)}")
        return final_packet
        
    except Exception as e:
        print(f"[ ERROR ] Error creating badge packet: {e}")
        import traceback
        traceback.print_exc()
        return None
    
async def reset_bot_state(key, iv, region):
    """Reset bot to solo mode before spam - Critical step from your old TCP"""
    try:
        # Leave any current squad (using your exact leave_s function)
        leave_packet = await leave_squad(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        await asyncio.sleep(0.5)
        
        print("[ SUCCESS ] Bot state reset - left squad")
        return True
        
    except Exception as e:
        print(f"[ ERROR ] Error resetting bot: {e}")
        return False    
    





    
    
    
async def auto_rings_emote_dual(uid, key, iv, region):
    """Send The Rings emote to both sender and bot for dual emote effect"""
    try:
        # The Rings emote ID
        rings_emote_id = 909050009
        
        # Get bot's UID
        bot_uid = 13601801571
        
        # Send emote to SENDER (person who invited)
        emote_to_sender = await Emote_k(int(uid), rings_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_sender)
        
        # Small delay between emotes
        await asyncio.sleep(0.5)
        
        # Send emote to BOT (bot performs emote on itself)
        emote_to_bot = await Emote_k(int(bot_uid), rings_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_bot)
        
        print(f"[ GAME ] Bot performed dual Rings emote with sender {uid} and bot {bot_uid}!")
        
    except Exception as e:
        print(f"[ ERROR ] Error sending dual rings emote: {e}")    
        
        
async def Room_Spam(Uid, Rm, Nm, K, V):
    fields = {
        1: 78,
        2: {
            1: int(Rm),  
            2: "iG:[C][B][FF0000]Black_Apis",  
            3: {
                2: 1,
                3: 1
            },
            4: 330,      
            5: 6000,     
            6: 201,      
            10: int(await xBunnEr()),  
            11: int(Uid), # Target UID
            12: 1,       
            15: {
                1: 1,
                2: 32768
            },
            16: 32768,    
            18: {
                1: 11481904755,  
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            
            31: {
                1: 1,
                2: 32768
            },
            32: 32768,    
            34: {
                1: int(Uid),   
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        }
    }
    
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0e15', K, V)
    

    
async def reject_spam_loop(target_uid, key, iv):
    """Send reject spam packets to target in background"""
    global reject_spam_running
    
    count = 0
    max_spam = 150
    
    while reject_spam_running and count < max_spam:
        try:
            # Send both packets
            packet1 = await banecipher1(target_uid, key, iv)
            packet2 = await banecipher(target_uid, key, iv)
            
            # Send to Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet1)
            await asyncio.sleep(0.1)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet2)
            
            count += 1
            print(f"[ NETWORK ] Sent reject spam #{count} to {xMsGFixinG(target_uid)}")
            
            # 0.2 second delay between spam cycles
            await asyncio.sleep(0.2)
            
        except Exception as e:
            print(f"[ ERROR ] Error in reject spam: {e}")
            break
    
    return count    
    
async def handle_reject_completion(spam_task, target_uid, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of reject spam and send final message"""
    try:
        spam_count = await spam_task
        
        # Send completion message
        if spam_count >= 150:
            completion_msg = f"""
[B][C][00FFFF]✦ REJECT SPAM COMPLETED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]PACKETS: [FFFFFF]{spam_count * 2}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        else:
            completion_msg = f"""
[B][C][00FFFF]✦ REJECT SPAM PARTIAL ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]PACKETS: [FFFFFF]{spam_count * 2}
[00FF00]STATUS : [FFFFFF]PARTIAL ⚠️
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv)
        
    except asyncio.CancelledError:
        print("[ INFO ] Reject spam was cancelled")
    except Exception as e:
        error_msg = f"""
[B][C][00FFFF]✦ REJECT SPAM ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv)    
    
    
    
async def banecipher(target_uid, key, iv):
    """Create reject spam packet 1 - Converted to new async format"""
    banner_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)

async def send_banner_message(client_id, key, iv):
    banner_text = """
[B][C][00FFFF]✦ GOD BLAZE BOT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]WELCOME TO God Blaze BOT !
[00FF00]UPDATE : [FFFFFF]NEW VERSION NEW FEATURES !
[00FF00]ACTION : [FFFFFF]ENJOY THE GAME!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)

async def banecipher1(client_id, key, iv):
    """Create reject spam packet 2 - Converted to new async format"""
    gay_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: int(client_id),
        2: 5,
        4: 50,
        5: {
            1: int(client_id),
            2: gay_text,
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)
    
async def get_colorful_message(message_text, message_number):
    """Generate message with different colors"""
    color_palette = ["FF0000", "00FF00", "0000FF", "FFFF00", "FF00FF", 
                     "00FFFF", "FFA500", "FF1493", "00FF7F", "7B68EE",
                     "FFD700", "00CED1", "FF69B4", "32CD32", "9370DB",
                     "FF4500", "1E90FF", "ADFF2F", "FF6347", "8A2BE2"]
    
    color_index = (message_number - 1) % len(color_palette)
    return f"[C][B][{color_palette[color_index]}]{message_text}"    

def get_random_avatar():
	avatar_list = [
         '902050001', '902050002', '902050003', '902039016', '902050004', 
        '902047011', '902047010', '902049015', '902050006', '902049020'
    ]
	random_avatar = random.choice(avatar_list)
	return  random_avatar

async def xSEndMsgsQQ(Msg , id , K , V):
    fields = {1: id , 2: id , 4: Msg , 5: 1756580149, 7: 2, 8: 904990072, 9: {1: "xBe4!sTo - C4", 2: int(get_random_avatar()), 4: 330, 5: 1001000001, 8: "xBe4!sTo - C4", 10: 1, 11: 1, 13: {1: 2}, 14: {1: 1158053040, 2: 8, 3: "\u0010\u0015\b\n\u000b\u0015\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"}}, 10: "en", 13: {2: 2, 3: 1}}
    Pk = (await CrEaTe_ProTo(fields)).hex()
    Pk = "080112" + await EnC_Uid(len(Pk) // 2, Tp='Uid') + Pk
    return await GeneRaTePk(Pk, '1201', K, V)     






        




async def create_training_start_packet(key, iv, region):
    """Create packet to start training mode in Free Fire"""
    
    try:
        # Decoded from your hex dump:
        # 62 27 01 01 28 00 01 00 00 00 00 00 79 2c 59 bf...
        # This appears to be a "start training" or "enter training ground" packet
        
        # Based on common Free Fire packet structure:
        # Packet type 0x27 = 39 decimal (training related)
        
        fields = {
            1: 39,  # Packet type for training (0x27 = 39)
            2: {
                1: 1,  # Action type (1 = start/enter)
                2: 1,  # Training mode type (1 = normal training)
                3: 0,  # Unknown flag
                4: 0,  # Unknown flag
                # The rest appears to be encrypted training data
                5: {
                    1: bytes.fromhex("79 2c 59 bf e0 5b be a6 00 ae 89 a5 26 4f 55 6f"),
                    2: bytes.fromhex("40 e5 e3 52 aa e2 46 26 ef e8 ac 5c 6c b1 db 9e"),
                    3: bytes.fromhex("87 09 4d aa ed c2 eb da")
                }
            }
        }
        
        # Alternative simpler structure (more likely):
        fields_simple = {
            1: 39,  # Training packet type
            2: {
                1: 1,   # Start training command
                2: 0,   # Training ground ID (0 = default)
                3: 1,   # Mode (1 = training)
                4: {    # Training settings
                    1: 1,  # Weapons enabled
                    2: 1,  # Bots enabled
                    3: 0,  # Unlimited ammo
                    4: 1,  # Health regen
                    5: 0   # God mode
                }
            }
        }
        
        # Let's try the simple structure first
        packet = await CrEaTe_ProTo(fields_simple)
        packet_hex = packet.hex()
        
        print(f"[ DATA ] Created training packet: {packet_hex[:50]}...")
        
        # Determine packet header based on region
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        # Generate final encrypted packet
        final_packet = await GeneRaTePk(packet_hex, packet_type, key, iv)
        
        print(f"[ SUCCESS ] Training start packet created")
        return final_packet
        
    except Exception as e:
        print(f"[ ERROR ] Error creating training packet: {e}")
        import traceback
        traceback.print_exc()
        return None




async def lag_team_loop(team_code, key, iv, region):
    """Rapid join/leave loop to create lag"""
    global lag_running
    count = 0
    
    while lag_running:
        try:
            # Join the team
            join_packet = await GenJoinSquadsPacket(team_code, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
            # Very short delay before leaving
            await asyncio.sleep(0.01)  # 10 milliseconds
            
            # Leave the team
            leave_packet = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            
            count += 1
            print(f"[ NETWORK ] Lag cycle #{count} completed for team: {team_code}")
            
            # Short delay before next cycle
            await asyncio.sleep(0.01)  # 10 milliseconds between cycles
            
        except Exception as e:
            print(f"[ ERROR ] Error in lag loop: {e}")
            # Continue the loop even if there's an error
            await asyncio.sleep(0.1)
 

import requests




# ADD FRIEND FUNCTION - BRIGHT RED/GREEN EDITION
def add_friend(target_uid):
    try:
        # Read credentials from God_Blaze.txt
        try:
            with open("God_Blaze.txt", 'r') as f:
                lines = f.read().strip().split('\n')
                uid = None
                password = None
                
                for line in lines:
                    line = line.strip()
                    if line.startswith("uid="):
                        uid = line.replace("uid=", "").strip()
                    elif line.startswith("password="):
                        password = line.replace("password=", "").strip()
                
                if not uid or not password:
                    return f"""
[B][C][00FFFF]✦ INVALID FILE FORMAT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS  : [FF0000]ERROR
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""
                    
        except FileNotFoundError:
            return f"""
[B][C][00FFFF]✦ FILE NOT FOUND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS  : [FF0000]ERROR
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""
        except Exception as e:
            return f"""
[B][C][00FFFF]✦ FILE ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS  : [FF0000]ERROR
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""

        # Use local API
        url = f"http://127.0.0.1:5005/adding_friend?uid={uid}&password={password}&friend_uid={target_uid}"

        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return f"""
[B][C][00FFFF]✦ API ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS  : [FF0000]ERROR
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""

        data = res.json()
        
        success = data.get("success", False)
        bot_name = data.get("bot_name", "Unknown")
        friend_name = data.get("friend_name", "Unknown")
        region = data.get("region", "N/A")
        bot_uid = data.get("bot_uid", uid)
        friend_uid = data.get("friend_uid", target_uid)
        status_code = data.get("status_code", "")
        error_msg = data.get("error", "")

        # Format names with xMsGFixinG
        formatted_bot_name = xMsGFixinG(bot_name) if bot_name != "Unknown" else bot_name
        formatted_friend_name = xMsGFixinG(friend_name) if friend_name != "Unknown" else friend_name
        formatted_bot_uid = xMsGFixinG(str(bot_uid))
        formatted_friend_uid = xMsGFixinG(str(friend_uid))

        if success:
            # SUCCESS - BRIGHT GREEN
            return f"""
[B][C][00FFFF]✦ FRIEND ADDED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]BOT NAME    : [00FF00]{formatted_bot_name}
[00FF00]BOT UID     : [00FF00]{formatted_bot_uid}
[00FF00]TARGET NAME : [00FF00]{formatted_friend_name}
[00FF00]TARGET UID  : [00FF00]{formatted_friend_uid}
[00FF00]REGION      : [00FF00]{region}
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""
        else:
            # ERROR - BRIGHT RED
            extra = ""
            if status_code:
                extra = f"\n[FFD700]STATUS CODE : [FF0000]{status_code}"
            elif error_msg:
                extra = f"\n[FFD700]ERROR       : [FF0000]{error_msg[:50]}"
            
            return f"""
[B][C][00FFFF]✦ FRIEND ADD FAILED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]BOT NAME    : [FF0000]{formatted_bot_name}
[00FF00]BOT UID     : [FF0000]{formatted_bot_uid}
[00FF00]TARGET NAME : [FF0000]{formatted_friend_name}
[00FF00]TARGET UID  : [FF0000]{formatted_friend_uid}
[00FF00]REGION      : [FF0000]{region}{extra}
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""

    except Exception as e:
        return f"""
[B][C][00FFFF]✦ UNEXPECTED ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS  : [FF0000]ERROR
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""


# REMOVE FRIEND FUNCTION - BRIGHT RED/GREEN EDITION
def remove_friend(target_uid):
    try:
        # Read credentials from God_Blaze.txt
        try:
            with open("God_Blaze.txt", 'r') as f:
                lines = f.read().strip().split('\n')
                uid = None
                password = None
                
                for line in lines:
                    line = line.strip()
                    if line.startswith("uid="):
                        uid = line.replace("uid=", "").strip()
                    elif line.startswith("password="):
                        password = line.replace("password=", "").strip()
                
                if not uid or not password:
                    return f"""
[B][C][00FFFF]✦ INVALID FILE FORMAT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS  : [FF0000]ERROR
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""
                    
        except FileNotFoundError:
            return f"""
[B][C][00FFFF]✦ FILE NOT FOUND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS  : [FF0000]ERROR
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""
        except Exception as e:
            return f"""
[B][C][00FFFF]✦ FILE ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS  : [FF0000]ERROR
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""

        # Use local API
        url = f"http://127.0.0.1:5005/remove_friend?uid={uid}&password={password}&friend_uid={target_uid}"

        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return f"""
[B][C][00FFFF]✦ API ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS  : [FF0000]ERROR
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""

        data = res.json()
        
        success = data.get("success", False)
        bot_name = data.get("bot_name", "Unknown")
        friend_name = data.get("friend_name", "Unknown")
        region = data.get("region", "N/A")
        bot_uid = data.get("bot_uid", uid)
        friend_uid = data.get("friend_uid", target_uid)
        status_code = data.get("status_code", "")
        error_msg = data.get("error", "")

        # Format names with xMsGFixinG
        formatted_bot_name = xMsGFixinG(bot_name) if bot_name != "Unknown" else bot_name
        formatted_friend_name = xMsGFixinG(friend_name) if friend_name != "Unknown" else friend_name
        formatted_bot_uid = xMsGFixinG(str(bot_uid))
        formatted_friend_uid = xMsGFixinG(str(friend_uid))

        if success:
            # SUCCESS - BRIGHT GREEN (remove success also green)
            return f"""
[B][C][00FFFF]✦ FRIEND REMOVED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]BOT NAME    : [00FF00]{formatted_bot_name}
[00FF00]BOT UID     : [00FF00]{formatted_bot_uid}
[00FF00]TARGET NAME : [00FF00]{formatted_friend_name}
[00FF00]TARGET UID  : [00FF00]{formatted_friend_uid}
[00FF00]REGION      : [00FF00]{region}
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""
        else:
            # ERROR - BRIGHT RED
            extra = ""
            if status_code:
                extra = f"\n[FFD700]STATUS CODE : [FF0000]{status_code}"
            elif error_msg:
                extra = f"\n[FFD700]ERROR       : [FF0000]{error_msg[:50]}"
            
            return f"""
[B][C][00FFFF]✦ FRIEND REMOVE FAILED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]BOT NAME    : [FF0000]{formatted_bot_name}
[00FF00]BOT UID     : [FF0000]{formatted_bot_uid}
[00FF00]TARGET NAME : [FF0000]{formatted_friend_name}
[00FF00]TARGET UID  : [FF0000]{formatted_friend_uid}
[00FF00]REGION      : [FF0000]{region}{extra}
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""

    except Exception as e:
        return f"""
[B][C][00FFFF]✦ UNEXPECTED ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS  : [FF0000]ERROR
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""

#Clan-info-by-clan-id
def Get_clan_info(clan_id):
    try:
        url = f"https://get-clan-info.vercel.app/get_clan_info?clan_id={clan_id}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            msg = f"""
[B][C][00FFFF]✦ GUILD DETAILS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]NAME       : [FFFFFF]{data['clan_name']}
[00FF00]ID         : [FFFFFF]{fix_num(data['id'])}
[00FF00]LEVEL      : [FFFFFF]{fix_num(data['level'])}
[00FF00]SCORE      : [FFFFFF]{fix_num(data['score'])}
[00FF00]RANK       : [FFFFFF]{fix_num(data['rank'])}
[00FF00]REGION     : [FFFFFF]{data['region']}
[00FF00]MEMBERS    : [FFFFFF]{fix_num(data['guild_details']['members_online'])}/{fix_num(data['guild_details']['total_members'])}
[00FF00]BALANCE    : [FFFFFF]{fix_num(data['balance'])}
[00FF00]XP         : [FFFFFF]{fix_num(data['xp'])}
[00FF00]WELCOME    : [FFFFFF]{data['welcome_message']}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            return msg
        else:
            msg = """
[B][C][00FFFF]✦ GUILD DETAILS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Failed to get info
[00FF00]ACTION : [FFFFFF]Please try again later!!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            return msg
    except:
        pass

def check_ban(uid):
    try:
        url = f"https://mg24-gamer-king.vercel.app/check/ban?uid={uid}"
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            return """
[B][C][00FFFF]✦ API ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS CODE : [FF0000]""" + str(res.status_code) + """
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""

        data = res.json()

        name = data.get("nickname", "Unknown")
        account_id = data.get("account_id", uid)
        region = data.get("region", "N/A")
        status = data.get("ban_status", "Unknown")
        period = data.get("ban_period") or "No Ban"

        status_lower = status.lower()

        # BAN CHECK - Green if not banned, Red if banned
        if "not" in status_lower or "no ban" in status_lower or "unbanned" in status_lower:
            main_color = "00FF00"  # Bright Green
            status_text = "NOT BANNED ✓"
        else:
            main_color = "FF0000"  # Bright Red
            status_text = "BANNED ✗"

        return f"""
[B][C][00FFFF]✦ BAN STATUS CHECK ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]NAME    : [{main_color}]{name}
[00FF00]UID     : [{main_color}]{xMsGFixinG(account_id)}
[00FF00]REGION  : [{main_color}]{region}
[00FF00]STATUS  : [{main_color}]{status_text}
[00FF00]PERIOD  : [{main_color}]{period}
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""

    except requests.exceptions.ConnectionError:
        return """
[B][C][00FFFF]✦ CONNECTION ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]MESSAGE : [FF0000]API SERVER OFFLINE
[00FF00]CHECK   : [FF0000]Port 5004 running?
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""
    except requests.exceptions.Timeout:
        return """
[B][C][00FFFF]✦ TIMEOUT ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]MESSAGE : [FF0000]API NOT RESPONDING
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""
    except Exception as e:
        return f"""
[B][C][00FFFF]✦ UNEXPECTED ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]ERROR : [FF0000]{str(e)[:50]}
[FFFFFF]━━━━━━━━━━━━━━━━━━
"""


        

 
Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB53"}

# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)
    
def get_random_evo_emote():
    """Return random evo emote ID"""
    evo_emotes = [
        909000063,  # AK
        909000068,  # SCAR  
        909000075,  # 1st MP40
        909040010,  # 2nd MP40
        909000081,  # 1st M1014
        909039011,  # 2nd M1014
        909000085,  # XM8
        909000090,  # Famas
        909000098,  # UMP
        909035007,  # M1887
        909042008,  # Woodpecker
        909041005,  # Groza
        909033001,  # M4A1
        909038010,  # Thompson
        909038012,  # G18
        909045001,  # Parafal
        909049010,  # P90
        909051003   # M60
    ]
    return random.choice(evo_emotes)
    
async def extract_uid_from_emote_packet(data_hex, key, iv):
    """Extract UID from emote packet (the sender)"""
    try:
        # Decrypt the packet
        packet = await DeCode_PackEt(data_hex[10:])
        packet_json = json.loads(packet)
        
        print(f"[ DATA ] Analyzing packet structure: {json.dumps(packet_json, indent=2)[:200]}...")
        
        # PATTERN 1: Your Emote_k() structure (Type 21)
        if packet_json.get('1') == 21:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '5' in packet_json['2']['data'] and 'data' in packet_json['2']['data']['5']):
                
                nested = packet_json['2']['data']['5']['data']
                if '1' in nested:
                    uid = nested['1']['data']
                    print(f"[ SUCCESS ] Extracted UID from pattern 21: {uid}")
                    return uid
        
        # PATTERN 2: Direct emote structure
        elif packet_json.get('1') == 26:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '1' in packet_json['2']['data']):
                
                uid = packet_json['2']['data']['1']['data']
                print(f"[ SUCCESS ] Extracted UID from pattern 26: {uid}")
                return uid
        
        # PATTERN 3: Try common paths
        for path in ['2/1', '5/1', '2/data/1', '5/data/1']:
            try:
                uid = get_nested_value(packet_json, path)
                if uid and str(uid).isdigit() and len(str(uid)) > 6:
                    print(f"[ SUCCESS ] Extracted UID from path {path}: {uid}")
                    return uid
            except:
                pass
        
        print(f"[ ERROR ] Could not extract UID from packet")
        return None
        
    except Exception as e:
        print(f"[ ERROR ] UID extraction error: {e}")
        return None

def get_nested_value(data, path):
    """Get value from nested JSON path like '2/5/1'"""
    keys = path.split('/')
    current = data
    
    for key in keys:
        if key.isdigit():
            key = str(key)  # JSON keys are strings
        
        if key in current and 'data' in current[key]:
            current = current[key]['data']
        else:
            return None
    
    return current

async def ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region):
    """Join team, authenticate chat, perform emote, and leave automatically"""
    try:
        # Step 1: Join the team
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
        print(f"[ SYSTEM ] Joined team: {team_code}")
        
        # Wait for team data and chat authentication
        await asyncio.sleep(1.5)  # Increased to ensure proper connection
        
        # Step 2: The bot needs to be detected in the team and authenticate chat
        # This happens automatically in TcPOnLine, but we need to wait for it
        
        # Step 3: Perform emote to target UID
        emote_packet = await Emote_k(int(target_uid), int(emote_id), key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
        print(f"[ GAME ] Performed emote {emote_id} to UID {xMsGFixinG(target_uid)}")
        
        # Wait for emote to register
        await asyncio.sleep(0.5)
        
        # Step 4: Leave the team
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print(f"[ SYSTEM ] Left team: {team_code}")
        
        return True, f"Quick emote attack completed! Sent emote to UID {xMsGFixinG(target_uid)}"
        
    except Exception as e:
        return False, f"Quick emote attack failed: {str(e)}"
        
        
async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload
    
async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, headers=headers, data=data, timeout=15) as response:
                if response.status != 200: 
                    print(f"[ ERROR ] Failed to get access token - Status: {response.status}")
                    return (None, None)
                data = await response.json()
                open_id = data.get("open_id")
                access_token = data.get("access_token")
                return (open_id, access_token) if open_id and access_token else (None, None)
        except asyncio.TimeoutError:
            print(f"[ ERROR ] Connection to Garena auth server timed out.")
            return (None, None)
        except aiohttp.ClientError as e:
            print(f"[ ERROR ] Network error connecting to Garena auth server: {e}")
            return (None, None)

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.123.1"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('[ WARNING ] Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
    

async def cHTypE(H):
    """Detect chat type including custom rooms"""
    if not H: 
        return 'Squid'
    elif H == 1: 
        return 'CLan'
    elif H == 2: 
        return 'PrivaTe'
    elif H == 3: 
        return 'CustomRoom'  # Custom room chat type
    else:
        return 'Squid'  # Default fallback
    
async def SEndMsG(H, message, Uid, chat_id, key, iv, region):
    """Send message to any chat type including custom rooms"""
    TypE = await cHTypE(H)
    
    if TypE == 'Squid': 
        msg_packet = await xSEndMsgsQ(message, chat_id, key, iv)
    elif TypE == 'CLan': 
        msg_packet = await xSEndMsg(message, 1, chat_id, chat_id, key, iv)
    elif TypE == 'PrivaTe': 
        msg_packet = await xSEndMsg(message, 2, Uid, Uid, key, iv)
    else:
        # Fallback to squad chat
        msg_packet = await xSEndMsgsQ(message, chat_id, key, iv)
        
    return msg_packet
    
    
async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):
    if TypE == 'ChaT' and ChaT: whisper_writer.write(PacKeT) ; await whisper_writer.drain()
    elif TypE == 'OnLine': online_writer.write(PacKeT) ; await online_writer.drain()
    else: return 'UnsoPorTed TypE ! >> ErrrroR (:():)' 

async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, max_retries=3, region="ind"):
    """Enhanced safe send message that works with custom rooms"""
    for attempt in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                
            print(f"[ SUCCESS ] Message sent successfully to chat type {chat_type} (attempt {attempt + 1})")
            return True
        except Exception as e:
            print(f"[ ERROR ] Failed to send message (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(0.5)
    return False

async def fast_emote_spam(uids, emote_id, key, iv, region):
    """Fast emote spam function that sends emotes rapidly"""
    global fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    while fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"[ ERROR ] Error in fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # 0.1 seconds interval between spam cycles

# NEW FUNCTION: Custom emote spam with specified times
async def custom_emote_spam(uid, emote_id, times, key, iv, region):
    """Custom emote spam function that sends emotes specified number of times"""
    global custom_spam_running
    count = 0
    
    while custom_spam_running and count < times:
        try:
            uid_int = int(uid)
            H = await Emote_k(uid_int, int(emote_id), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            count += 1
            await asyncio.sleep(0.0000001)  # 0.1 seconds interval between emotes
        except Exception as e:
            print(f"[ ERROR ] Error in custom_emote_spam for uid {uid}: {e}")
            break

async def create_level_up_bot_connection(key, iv, region):
    """Create a separate connection for level-up bot"""
    try:
        # This would use a different bot account
        # For now, we'll use the main bot
        print("[ SYSTEM ] Level-up bot connection initialized")
        return True
    except Exception as e:
        print(f"[ ERROR ] Level-up bot connection error: {e}")
        return False

async def level_up_join_team(team_code, key, iv, region):
    """Level-up bot joins the team"""
    try:
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
        print(f"[ SYSTEM ] Level-up bot joining team: {team_code}")
        await asyncio.sleep(2)
        return True
    except Exception as e:
        print(f"[ ERROR ] Level-up bot join error: {e}")
        return False

async def level_up_leave_team(key, iv):
    """Level-up bot leaves the team"""
    try:
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print("[ SYSTEM ] Level-up bot leaving team")
        await asyncio.sleep(1)
        return True
    except Exception as e:
        print(f"[ ERROR ] Level-up bot leave error: {e}")
        return False
        
async def level_up_loop(team_code, target_uid, key, iv, region, chat_type, chat_id):
    """Main level-up automation loop"""
    global level_up_running
    
    cycle_count = 0
    max_cycles = 1000  # Safety limit
    
    print(f"[ SYSTEM ] Starting level-up automation for team {team_code}")
    
    while level_up_running and cycle_count < max_cycles:
        try:
            cycle_count += 1
            print(f"[ SYSTEM ] Level-up cycle #{cycle_count}")
            
            # Step 1: Send instruction message
            instruction_msg = f"""
[B][C][00FFFF]✦ LEVEL-UP CYCLE #{cycle_count} ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]ACTION : [FFFFFF]Joining your team...
[00FF00]STATUS : [FFFFFF]Will start match
[00FF00]WAIT   : [FFFFFF]{level_up_wait_time} seconds after match
[00FF00]INFO   : [FFFFFF]Bot is working...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            await safe_send_message(chat_type, instruction_msg, target_uid, chat_id, key, iv)
            
            # Step 2: Join the team
            join_success = await level_up_join_team(team_code, key, iv, region)
            if not join_success:
                print("[ ERROR ] Failed to join team, retrying...")
                await asyncio.sleep(2)
                continue
            
            # Step 3: Send "ready" message
            ready_msg = f"""
[B][C][00FFFF]✦ BOT JOINED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]Starting match...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            await safe_send_message(chat_type, ready_msg, target_uid, chat_id, key, iv)
            
            # Step 4: Start the match (spam start packet)
            start_packet = await FS(key, iv)
            spam_duration = 10  # Spam for 10 seconds
            start_time = time.time()
            
            while time.time() - start_time < spam_duration and level_up_running:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
                await asyncio.sleep(0.2)  # 200ms delay between packets
            
            # Step 5: Wait for match to complete (simulate)
            waiting_msg = f"""
[B][C][00FFFF]✦ MATCH IN PROGRESS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]Waiting for match to complete...
[00FF00]NEXT   : [FFFFFF]Starts in {level_up_wait_time} seconds
[00FF00]INFO   : [FFFFFF]Bot remains in team
[00FF00]ACTION : [FFFFFF]Let the match complete normally!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            await safe_send_message(chat_type, waiting_msg, target_uid, chat_id, key, iv)
            
            # Step 6: Wait the specified time
            wait_count = 0
            while wait_count < level_up_wait_time and level_up_running:
                await asyncio.sleep(1)
                wait_count += 1
                
                # Progress update every 5 seconds
                if wait_count % 5 == 0:
                    progress_msg = f"""
[B][C][00FFFF]✦ LEVEL-UP PROGRESS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]WAITED : [FFFFFF]{wait_count}/{level_up_wait_time} seconds
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                    await safe_send_message(chat_type, progress_msg, target_uid, chat_id, key, iv)
            
            if not level_up_running:
                break
            
            # Step 7: Leave team
            leave_success = await level_up_leave_team(key, iv)
            
            if leave_success:
                leave_msg = f"""
[B][C][00FFFF]✦ BOT LEFT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]Left team to restart cycle...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                await safe_send_message(chat_type, leave_msg, target_uid, chat_id, key, iv)
            
            # Step 8: Small delay before next cycle
            await asyncio.sleep(2)
            
        except Exception as e:
            print(f"[ ERROR ] Error in level-up cycle: {e}")
            # Try to recover
            await level_up_leave_team(key, iv)
            await asyncio.sleep(3)
    
    print("[ SYSTEM ] Level-up automation stopped")

# NEW FUNCTION: Evolution emote spam with mapping
async def evo_emote_spam(uids, number, key, iv, region):
    """Send evolution emotes based on number mapping"""
    try:
        emote_id = EMOTE_MAP.get(int(number))
        if not emote_id:
            return False, f"Invalid number! Use 1-21 only."
        
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"[ ERROR ] Error sending evo emote to {uid}: {e}")
        
        return True, f"Sent evolution emote {number} (ID: {emote_id}) to {success_count} player(s)"
    
    except Exception as e:
        return False, f"Error in evo_emote_spam: {str(e)}"



# NEW FUNCTION: Fast evolution emote spam
async def evo_fast_emote_spam(uids, number, key, iv, region):
    """Fast evolution emote spam function"""
    global evo_fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    
    while evo_fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"[ ERROR ] Error in evo_fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"Completed fast evolution emote spam {count} times"
    
async def send_required_packets(key, iv, region, bot_uid):
    """Send packets required after connection"""
    try:
        # Packet 1: Client info
        fields1 = {
            1: 100,
            2: {
                1: bot_uid,
                2: "1.123.1",  # Game version
                3: "Android",
                4: "en",
            }
        }
        
        # Packet 2: Device info
        fields2 = {
            1: 101,
            2: {
                1: "vivo",
                2: "1901",
                3: "arm64-v8a",
                4: str(time.time()),
            }
        }
        
        packets = []
        for fields in [fields1, fields2]:
            if region.lower() == "ind":
                packet_type = '0514'
            elif region.lower() == "bd":
                packet_type = "0519"
            else:
                packet_type = "0515"
                
            packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
            packets.append(packet)
        
        return packets
        
    except Exception as e:
        print(f"[ ERROR ] Required packets error: {e}")
        return []



async def RejectMSGtaxt(squad_owner,uid, key, iv):
    random_banner = f"""
.
.
.









[00FF00]God Blaze TCP
WELCOME TO God Blaze TCP BOT



 """
    fields = {
    1: 5,
    2: {
        1: int(squad_owner),
        2: 1,
        3: int(uid),
        4: random_banner
    }
    }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , key, iv)

async def send_keep_alive(key, iv, region):
    """Send keep-alive packet to maintain connection"""
    try:
        fields = {
            1: 99,  # Keep-alive packet type
            2: {
                1: int(time.time()),
                2: 1,  # Keep-alive flag
            }
        }
        
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
        return packet
    except Exception as e:
        print(f"[ ERROR ] Keep-alive error: {e}")
        return None

async def ArohiAccepted(uid,code,K,V):
    fields = {
        1: 4,
        2: {
            1: uid,
            3: uid,
            8: 1,
            9: {
            2: 161,
            4: "y[WW",
            6: 11,
            8: "1.114.18",
            9: 3,
            10: 1
            },
            10: str(code),
        }
        }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , K , V)


async def new_lag(key , iv):
    fields = {
        1: 15,
        2: {
            1: 804266360,
            2: 1
        }
    }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , key , iv)


async def convert_kyro_to_your_system(target_uid, chat_id, key, iv, nickname="God Blaze", title_id=None):
    """EXACT conversion with customizable title ID"""
    try:
        # Use provided title_id or get random one
        if title_id is None:
            # Get a random title from the list
            available_titles = [905090075, 904990072, 904990069, 905190079]
            title_id = random.choice(available_titles)
        
        # Create fields dictionary with specific title_id
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"TitleID":{title_id},"type":"Title"}}',  # Use specific title ID
                # ... rest of your fields
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(await xBunnEr()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {
                        1: 2
                    },
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        
        # ... rest of your existing function
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        
        print(f"[ SUCCESS ] Created packet with Title ID: {title_id}")
        return final_packet
        
    except Exception as e:
        print(f"[ ERROR ] Conversion error: {e}")
        return None
        
def get_random_sticker():
    """
    Randomly select one sticker from available packs
    """

    sticker_packs = [
        # NORMAL STICKERS (1200000001-1 to 24)
        ("1200000001", 1, 24),

        # KELLY EMOJIS (1200000002-1 to 15)
        ("1200000002", 1, 15),

        # MAD CHICKEN (1200000004-1 to 13)
        ("1200000004", 1, 13),
    ]

    pack_id, start, end = random.choice(sticker_packs)
    sticker_no = random.randint(start, end)

    return f"[1={pack_id}-{sticker_no}]"
        
# Alternative: DIRECT port of your friend's function but with your UID
async def send_kyro_title_adapted(chat_id, key, iv, target_uid, nickname="God Blaze"):
    """Direct adaptation of your friend's working function"""
    try:
        # Import your proto file (make sure it's in the same directory)
        from kyro_title_pb2 import GenTeamTitle
        
        root = GenTeamTitle()
        root.type = 1
        
        nested_object = root.data
        nested_object.uid = int(target_uid)  # CHANGE: Use target UID
        nested_object.chat_id = int(chat_id)
        nested_object.title = f"{{\"TitleID\":{titles()},\"type\":\"Title\"}}"
        nested_object.timestamp = int(datetime.now().timestamp())
        nested_object.language = "en"
        
        nested_details = nested_object.field9
        nested_details.Nickname = f"[C][B][FF0000]{nickname}"  # CHANGE: Your nickname
        nested_details.avatar_id = int(await xBunnEr())  # Use your function
        nested_details.rank = 330
        nested_details.badge = 102000015
        nested_details.Clan_Name = "BOT TEAM"  # CHANGE: Your clan
        nested_details.field10 = 1
        nested_details.global_rank_pos = 1
        nested_details.badge_info.value = 2
        
        nested_details.prime_info.prime_uid = 1158053040
        nested_details.prime_info.prime_level = 8
        # IMPORTANT: This must be bytes, not string!
        nested_details.prime_info.prime_hex = b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
        
        nested_options = nested_object.field13
        nested_options.url_type = 2
        nested_options.curl_platform = 1
        
        nested_object.empty_field.SetInParent()
        
        # Serialize
        packet = root.SerializeToString().hex()
        
        # Use YOUR encryption function
        encrypted_packet = await encrypt_packet(packet, key, iv)
        
        # Calculate length
        packet_length = len(encrypted_packet) // 2
        
        # Convert to hex (4 characters with leading zeros)
        hex_length = f"{packet_length:04x}"
        
        # Build packet EXACTLY like your friend
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"[ ERROR ] Direct adaptation error: {e}")
        import traceback
        traceback.print_exc()
        return None

async def send_all_titles_sequentially(uid, chat_id, key, iv, region, chat_type):
    """Send all titles one by one with 2-second delay"""
    
    # Get all titles
    all_titles = [
        905090075, 904990072, 904990069, 905190079
    ]
    
    total_titles = len(all_titles)
    
    # Send initial message
    start_msg = f"""
[B][C][00FFFF]✦ TITLE SEQUENCE ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(uid)}
[00FF00]TOTAL  : [FFFFFF]{total_titles}
[00FF00]DELAY  : [FFFFFF]2 seconds
[00FF00]STATUS : [FFFFFF]Sending titles now...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
    await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv)
    
    try:
        for index, title_id in enumerate(all_titles):
            title_number = index + 1
            
            # Create progress message
            progress_msg = f"""
[B][C][00FFFF]✦ SENDING TITLE ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TITLE  : [FFFFFF]{title_id}
[00FF00]PROGRESS: [FFFFFF]{title_number}/{total_titles}
[00FF00]NEXT   : [FFFFFF]2 seconds
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            await safe_send_message(chat_type, progress_msg, uid, chat_id, key, iv)
            
            # Send the actual title using your existing method
            # You'll need to use your existing title sending logic here
            # For example:
            title_packet = await convert_kyro_to_your_system(uid, chat_id, key, iv, nickname="God Blaze", title_id=title_id)
            
            if title_packet and whisper_writer:
                whisper_writer.write(title_packet)
                await whisper_writer.drain()
                print(f"[ SUCCESS ] Sent title {title_number}/{total_titles}: {title_id}")
            
            # Wait 2 seconds before next title (unless it's the last one)
            if title_number < total_titles:
                await asyncio.sleep(2)
        
        # Completion message
        completion_msg = f"""
[B][C][00FFFF]✦ TITLES COMPLETED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(uid)}
[00FF00]TOTAL  : [FFFFFF]{total_titles}
[00FF00]TIME   : [FFFFFF]{total_titles * 2} seconds
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, completion_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"""
[B][C][00FFFF]✦ TITLE ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def handle_all_titles_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    """Handle /alltitles command to send all titles sequentially"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        target_uid = uid
        target_name = "Yourself"
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
        target_name = f"UID {xMsGFixinG(target_uid)}"
    else:
        error_msg = f"""
[B][C][00FFFF]✦ ALLTITLES COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/alltitles [uid]
[00FF00]EX 1   : [FFFFFF]/alltitles
[00FF00]EX 2   : [FFFFFF]/alltitles 123456789
[00FF00]INFO   : [FFFFFF]Sends all 4 titles
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Start the title sequence in the background
    asyncio.create_task(
        send_all_titles_sequentially(target_uid, chat_id, key, iv, region, chat_type)
    )
    
    # Immediate response
    response_msg = f"""
[B][C][00FFFF]✦ TITLE SEQUENCE ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{target_name}
[00FF00]TOTAL  : [FFFFFF]4 titles
[00FF00]DELAY  : [FFFFFF]2 seconds each
[00FF00]STATUS : [FFFFFF]Running in background...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
    await safe_send_message(chat_type, response_msg, uid, chat_id, key, iv)


async def noob(target_uid, chat_id, key, iv, nickname="God Blaze", title_id=None):
    """EXACT conversion with customizable title ID"""
    try:
        # Use provided title_id or get random one
        if title_id is None:
            # Get a random title from the list
            available_titles = [904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072]
            title_id = random.choice(available_titles)
        
        # Create fields dictionary with specific title_id
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"TitleID":{title_id},"type":"Title"}}',
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(await xBunnEr()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {
                        1: 2
                    },
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        
        # ... rest of your existing function
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        
        print(f"[ SUCCESS ] Created packet with Title ID: {title_id}")
        return final_packet
        
    except Exception as e:
        print(f"[ ERROR ] Conversion error: {e}")
        return None
        

async def send_all_titles_sequentiallly(uid, chat_id, key, iv, region, chat_type):
    """Send all titles one by one with 2-second delay"""
    
    # Get all titles
    all_titles = [
        904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072
    ]
    
    total_titles = len(all_titles)
    
    # Send initial message
    start_msg = f"""
[B][C][00FFFF]✦ TITLE SEQUENCE ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Noobde God Blaze GAMER ya meku agar tu noob bolra toh tu g a y hai
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
    await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv)
    
    try:
        for index, title_id in enumerate(all_titles):
            title_number = index + 1
            

            
            # Send the actual title using your existing method
            # You'll need to use your existing title sending logic here
            # For example:
            title_packet = await noob(uid, chat_id, key, iv, nickname="God Blaze", title_id=title_id)
            
            if title_packet and whisper_writer:
                whisper_writer.write(title_packet)
                await whisper_writer.drain()
                print(f"[ SUCCESS ] Sent title {title_number}/{total_titles}: {title_id}")
            
            # Wait 2 seconds before next title (unless it's the last one)
            if title_number < total_titles:
                await asyncio.sleep(2)
        
        # Completion message
        completion_msg = f"""
[B][C][00FFFF]✦ TITLES COMPLETED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Noobde ab tu bta ye titles aur bol kon noob hai
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, completion_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"""
[B][C][00FFFF]✦ TITLE ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def handle_alll_titles_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    """Handle /alltitles command to send all titles sequentially"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        target_uid = uid
        target_name = "Yourself"
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
        target_name = f"UID {xMsGFixinG(target_uid)}"
    else:
        error_msg = f"""
[B][C][00FFFF]✦ ALLTITLES COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/alltitles [uid]
[00FF00]EX 1   : [FFFFFF]/alltitles
[00FF00]EX 2   : [FFFFFF]/alltitles 123456789
[00FF00]INFO   : [FFFFFF]Sends all 4 titles
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Start the title sequence in the background
    asyncio.create_task(
        send_all_titles_sequentiallly(target_uid, chat_id, key, iv, region, chat_type)
    )
    


async def RoomJoin(room_id, password, key, iv):
    """Join Free Fire custom room"""
    try:
        # Import your proto file
        from room_join_pb2 import join_room
        
        root = join_room()
        root.field_1 = 3  # Room join command
        
        # Nested object
        nested_object = root.field_2
        nested_object.field_1 = int(room_id)
        nested_object.field_2 = str(password)
        
        # Field 8
        nested_8 = nested_object.field_8
        nested_8.field_1 = "IDC3"
        nested_8.field_2 = 149
        nested_8.field_3 = "IND"
        
        # Other fields
        nested_object.field_9 = "\x01\x03\x04\x07\x09\x0a\x0b\x12\x0e\x16\x19\x20\x1d"  # Bytes, not string
        nested_object.field_10 = 1
        nested_object.field_12.SetInParent()  # Empty field
        nested_object.field_13 = 1
        nested_object.field_14 = 1
        nested_object.field_16 = "en"
        
        # Field 22
        nested_22 = nested_object.field_22
        nested_22.field_1 = 21
        
        # Serialize
        packet_hex = root.SerializeToString().hex()
        
        # Encrypt using your function
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        
        # Convert length to hex
        hex_length = dec_to_hex(packet_length)  # Use your existing function
        
        # Build packet header (type 0e15 for room join)
        if len(hex_length) == 2:
            header = "0e15000000"
        elif len(hex_length) == 3:
            header = "0e1500000"
        elif len(hex_length) == 4:
            header = "0e150000"
        elif len(hex_length) == 5:
            header = "0e15000"
        else:
            header = "0e150000"
        
        final_packet_hex = header + hex_length + encrypted_packet
        
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"[ ERROR ] Room join error: {e}")
        import traceback
        traceback.print_exc()
        return None
        

# Alternative: Using your fields dictionary format
async def RoomJoin_fields(room_id, password, key, iv):
    """Room join using your CrEaTe_ProTo format"""
    try:
        fields = {
            1: 3,  # Room join command
            2: {   # Nested object
                1: int(room_id),   # room_id
                2: str(password),  # password
                8: {  # field_8
                    1: "IDC3",
                    2: 149,
                    3: "IND"
                },
                9: b"\x01\x03\x04\x07\x09\x0a\x0b\x12\x0e\x16\x19\x20\x1d",  # Bytes!
                10: 1,
                12: {},  # Empty field
                13: 1,
                14: 1,
                16: "en",
                22: {  # field_22
                    1: 21
                }
            }
        }
        
        # Convert to protobuf
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        # Encrypt and build packet
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = dec_to_hex(packet_length)
        
        # Build header
        if len(hex_length) == 2:
            header = "0e15000000"
        elif len(hex_length) == 3:
            header = "0e1500000"
        elif len(hex_length) == 4:
            header = "0e150000"
        elif len(hex_length) == 5:
            header = "0e15000"
        else:
            header = "0e150000"
        
        final_packet_hex = header + hex_length + encrypted_packet
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"[ ERROR ] Room join fields error: {e}")
        return None

def remove_from_whitelist(uid_to_remove):
    """Remove UID from whitelist"""
    global WHITELISTED_UIDS
    
    uid_str = str(uid_to_remove)
    
    # Don't allow removing owner
    if uid_str == "":  # Your UID
        return False, "Cannot remove bot owner from whitelist!"
    
    if uid_str not in WHITELISTED_UIDS:
        return False, f"UID {uid_str} not in whitelist"
    
    WHITELISTED_UIDS.remove(uid_str)
    return True, f"✅ Removed {uid_str} from whitelist"

async def handle_room_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /room command with proper error handling"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 2:
        error_msg = f"""
[B][C][00FFFF]✦ ROOM COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/room (uid)
[00FF00]EX 1   : [FFFFFF]/room 537512413
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    target_uid = parts[1]
    
    try:
        # Step 1: Check player status
        status_result, status_message = await check_player_status(target_uid, key, iv)
        
        packet = None
        player_status = None
        
        # If live check failed, try cache
        if not status_result:
            # Check cache
            cached_data = load_from_cache(target_uid)
            if cached_data and 'packet' in cached_data:
                packet = cached_data['packet']
                player_status = cached_data.get('status', 'UNKNOWN')
                print(f"[ WARNING ] Using cached data for {xMsGFixinG(target_uid)}")
            else:
                error_msg = f"""
[B][C][00FFFF]✦ PLAYER NOT FOUND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]STATUS : [FFFFFF]FAILED ❌
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
                return
        else:
            # Use live data
            packet = status_result.get('packet', b'')
            player_status = get_player_status(packet)
        
        # Step 2: Check if player is in room
        if not player_status or "IN ROOM" not in player_status:
            info_msg = f"""
[B][C][00FFFF]✦ PLAYER STATUS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]STATUS : [FFFFFF]{player_status or 'UNKNOWN'}
[00FF00]INFO   : [FFFFFF]Not in custom room
[00FF00]ACTION : [FFFFFF]Player must join custom room first!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            await safe_send_message(chat_type, info_msg, uid, chat_id, key, iv)
            return
        
        # Step 3: Extract room ID
        room_id = get_idroom_by_idplayer(packet) if packet else None
        
        if not room_id:
            error_msg = f"""
[B][C][00FFFF]✦ ROOM ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Failed to extract room ID
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            return
        
        # Step 4: SUCCESS - Send room info
        success_msg = f"""
[B][C][00FFFF]✦ ROOM FOUND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]ROOM ID: [FFFFFF]{room_id}
[00FF00]STATUS : [FFFFFF]{player_status}
[00FF00]DATA   : [FFFFFF]{'CACHED' if not status_result else 'LIVE'}
[00FF00]ACTION : [FFFFFF]Quick join: /xjoin {room_id} 0000
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
        # Step 5: AUTO-SPAM (add this if you want spam)
        # Uncomment this section if you want auto-spam:
        
        spam_count = 5
        for i in range(spam_count):
            try:
                spam_packet = await Room_Spam(target_uid, room_id, f"Spam_{i+1}", key, iv)
                if spam_packet and online_writer:
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
                    await asyncio.sleep(0.2)
            except Exception as e:
                print(f"[ ERROR ] Spam error: {e}")
        
        spam_msg = f"""
[B][C][00FFFF]✦ ROOM SPAM ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Spammed {spam_count} invites!
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, spam_msg, uid, chat_id, key, iv)
        
        
    except Exception as e:
        print(f"[ ERROR ] Room command error: {e}")
        error_msg = f"""
[B][C][00FFFF]✦ ROOM ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)[:80]}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

# Room spam command (send multiple messages)
async def handle_room_spam_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /spamroom command to send room spam messages"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 4:
        error_msg = f"""
[B][C][00FFFF]✦ SPAMROOM COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/spamroom (room_id) (uid) (message)
[00FF00]EX 1   : [FFFFFF]/spamroom 123456 14010319252 Hello World!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    try:
        room_id = parts[1]
        target_uid = parts[2]
        message = ' '.join(parts[3:])
        
        # Validate inputs
        if not room_id.isdigit():
            error_msg = f"""
[B][C][00FFFF]✦ INVALID ROOM ID ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Room ID must be numbers only!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            return
            
        if not target_uid.isdigit():
            error_msg = f"""
[B][C][00FFFF]✦ INVALID UID ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]UID must be numbers only!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            return
        
        # Send initial message
        initial_msg = f"""
[B][C][00FFFF]✦ PREPARING ROOM SPAM ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]ROOM ID: [FFFFFF]{room_id}
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]MESSAGE: [FFFFFF]{message[:30]}...
[00FF00]STATUS : [FFFFFF]Creating packet...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        
        await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
        
        # Create and send the spam packet
        spam_packet = await SPam_Room(target_uid, room_id, message, key, iv)
        
        if spam_packet:
            # Send via Online connection (since it's room-related)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
            
            success_msg = f"""
[B][C][00FFFF]✦ ROOM SPAM SENT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]ROOM   : [FFFFFF]{room_id}
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]MESSAGE: [FFFFFF]{message[:40]}...
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        else:
            success_msg = f"""
[B][C][00FFFF]✦ ROOM SPAM FAILED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Failed to create spam packet!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"""
[B][C][00FFFF]✦ ROOM SPAM ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

# Also create a shorter alias command handler
async def handle_sr_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /sr command (short version of /spamroom)"""
    await handle_room_spam_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type)
        
async def detect_emote_perfect(data_hex, key, iv):
    """100% ACCURATE emote detection using YOUR exact packet structure"""
    
    try:
        # Step 1: Decrypt using your EXACT method
        decrypted = await DeCode_PackEt(data_hex[10:])  # Use YOUR existing function
        packet_json = json.loads(decrypted)
        
        # Step 2: EXACT STRUCTURE MATCHING
        # Check for Type 21 (from your Emote_k function)
        if packet_json.get('1') == 21:
            # Check for the EXACT structure you use
            if '2' in packet_json and 'data' in packet_json['2']:
                emote_data = packet_json['2']['data']
                
                # Verify EXACT field structure matches Emote_k()
                if ('1' in emote_data and '2' in emote_data and 
                    '5' in emote_data and 'data' in emote_data['5']):
                    
                    nested = emote_data['5']['data']
                    
                    # THIS IS THE 100% ACCURATE DETECTION
                    # Matches EXACTLY what you send in Emote_k()
                    if '1' in nested and '3' in nested:
                        return {
                            'type': 'emote',
                            'packet_type': 21,  # ← EXACT MATCH
                            'identifier': emote_data.get('1', {}).get('data'),
                            'base_emote': emote_data.get('2', {}).get('data'),
                            'target_uid': nested.get('1', {}).get('data'),  # WHO received it
                            'emote_id': nested.get('3', {}).get('data'),
                            'confidence': 100.0,
                            'raw_packet': packet_json
                        }
        
        # ALTERNATIVE FORMAT: Direct to player
        elif packet_json.get('1') == 26:  # Another emote type
            # Add similar exact matching here
            pass
        
        return None
        
    except Exception as e:
        print(f"[ ERROR ] Perfect detection error: {e}")
        return None
        
async def detect_emote_with_sender(data_hex, key, iv):
    """Detect emote AND find who sent it"""
    
    try:
        # First, detect if it's an emote packet
        emote_info = await detect_emote_perfect(data_hex, key, iv)
        
        if not emote_info:
            return None
        
        # Now we need to find the SENDER's UID
        # Look for sender in different packet parts
        
        # METHOD 1: Check packet header for UID
        packet_header = data_hex[:20]
        
        # Look for UID patterns in hex (9-11 digits)
        import re
        uid_pattern = r'(\d{9,11})'
        
        # Search in entire packet
        all_uids = re.findall(uid_pattern, data_hex)
        
        if len(all_uids) >= 2:
            # We have at least 2 UIDs: sender and target
            # The target is already in emote_info['target_uid']
            target_uid = str(emote_info['target_uid'])
            
            # Find which UID is NOT the target
            for uid in all_uids:
                if uid != target_uid:
                    # This is likely the SENDER
                    emote_info['sender_uid'] = int(uid)
                    emote_info['detection_method'] = 'uid_pattern'
                    
                    print(f"[ SUCCESS ] SENDER FOUND: {xMsGFixinG(uid)} sent emote to {xMsGFixinG(target_uid)}")
                    return emote_info
        
        # METHOD 2: Look in packet structure
        packet_json = emote_info['raw_packet']
        
        # Search recursively for UID that's NOT the target
        def find_sender_in_json(obj, target_uid):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == 'data' and isinstance(v, (int, str)):
                        v_str = str(v)
                        if v_str.isdigit() and len(v_str) > 8:
                            if v_str != str(target_uid):
                                return int(v)
                    elif isinstance(v, dict):
                        result = find_sender_in_json(v, target_uid)
                        if result:
                            return result
            return None
        
        sender_uid = find_sender_in_json(packet_json, emote_info['target_uid'])
        if sender_uid:
            emote_info['sender_uid'] = sender_uid
            emote_info['detection_method'] = 'json_search'
            return emote_info
        
        # If we can't find sender, at least we detected the emote
        emote_info['sender_uid'] = None
        return emote_info
        
    except Exception as e:
        print(f"[ ERROR ] Sender detection error: {e}")
        return None


async def send_title_packet_direct(target_uid, chat_id, key, iv, region="ind"):
    """Send title packet directly without chat context - for auto-join"""
    try:
        print(f"[ SYSTEM ] Sending title to {xMsGFixinG(target_uid)} in chat {chat_id}")
        
        # Method 1: Using your existing function
        title_packet = await convert_kyro_to_your_system(target_uid, chat_id, key, iv)
        
        if title_packet and whisper_writer:
            # Send via Whisper connection
            whisper_writer.write(title_packet)
            await whisper_writer.drain()
            print(f"[ SUCCESS ] Title sent via Whisper to {xMsGFixinG(target_uid)}")
            return True
            
    except Exception as e:
        print(f"[ ERROR ] Error sending title directly: {e}")
        import traceback
        traceback.print_exc()
    
    return False

def extract_type_5(packet_json):
    """Extract from Type 5 packets"""
    if packet_json.get('1') == 5:
        try:
            if '2' in packet_json and 'data' in packet_json['2']:
                data = packet_json['2']['data']
                sender = data.get('1', {}).get('data')
                emote_id = data.get('4', {}).get('data')
                
                if sender:
                    return {
                        'sender_uid': sender,
                        'emote_id': emote_id or 909000063,  # Default if not found
                        'packet_type': 5,
                        'confidence': 'medium'
                    }
        except:
            pass
    return None

# Add these imports at the top with your other imports
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import json
import requests
import asyncio

# Add these constants with your other global variables
BIO_ENCRYPTION_KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
BIO_ENCRYPTION_IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
FREEFIRE_VERSION = "OB53"

def decode_jwt_noverify(token: str):
    """Decode JWT without verification"""
    try:
        parts = token.split(".")
        if len(parts) < 2:
            return None
        payload_b64 = parts[1] + "=" * (-len(parts[1]) % 4)
        payload = json.loads(base64.urlsafe_b64decode(payload_b64).decode())
        return payload
    except Exception:
        return None

# Add these global variables

async def is_bot_in_squad(bot_uid, key, iv):
    """Quick check if bot is in squad (with caching)"""
    global last_bot_status_check, cached_bot_status
    
    # Use cache if recent
    current_time = time.time()
    if (current_time - last_bot_status_check < bot_status_cache_time and 
        cached_bot_status is not None):
        return cached_bot_status
    
    try:
        # Send status request
        status_packet = await createpacketinfo(bot_uid, key, iv)
        if status_packet and online_writer:
            online_writer.write(status_packet)
            await online_writer.drain()
            
            # Wait for response
            await asyncio.sleep(2)
            
            # Check cache
            if bot_uid in status_response_cache:
                packet = status_response_cache[bot_uid].get('packet', b'')
                status = get_player_status(packet)
                
                in_squad = "INSQUAD" in status
                cached_bot_status = in_squad
                last_bot_status_check = current_time
                
                return in_squad
        
        return False
        
    except Exception as e:
        print(f"[ ERROR ] Squad check error: {e}")
        return False

def get_bio_server_url(lock_region: str):
    """Get bio endpoint based on region"""
    region = lock_region.upper()
    if region == "IND":
        return "https://client.ind.freefiremobile.com/UpdateSocialBasicInfo"
    elif region in {"BR", "US", "SAC", "NA"}:
        return "https://client.us.freefiremobile.com/UpdateSocialBasicInfo"
    elif region == "BD":
        return "https://client.bd.freefiremobile.com/UpdateSocialBasicInfo"
    elif region == "SG":
        return "https://client.sg.freefiremobile.com/UpdateSocialBasicInfo"
    else:
        return "https://clientbp.ggblueshark.com/UpdateSocialBasicInfo"

def create_bio_protobuf(bio_text):
    """Create protobuf message for bio update - EXACT SAME AS YOUR FLASK API"""
    # This creates the EXACT same protobuf structure as your Flask API
    
    # Protobuf structure from your API:
    # field_2: 17 (0x11)
    # field_5: EmptyMessage
    # field_6: EmptyMessage  
    # field_8: bio_text (string)
    # field_9: 1 (0x01)
    # field_11: EmptyMessage
    # field_12: EmptyMessage
    
    # Build protobuf manually (matching your exact structure)
    # Field 2: varint 17
    field_2 = b'\x08\x11'  # tag:1 type:varint value:17
    
    # Field 5: EmptyMessage (empty bytes)
    field_5 = b'\x2A\x00'  # tag:5 type:length-delimited length:0
    
    # Field 6: EmptyMessage (empty bytes)
    field_6 = b'\x32\x00'  # tag:6 type:length-delimited length:0
    
    # Field 8: bio text (string)
    bio_bytes = bio_text.encode('utf-8')
    bio_length = len(bio_bytes)
    field_8 = b'\x42' + bytes([bio_length]) + bio_bytes  # tag:8 type:string
    
    # Field 9: varint 1
    field_9 = b'\x48\x01'  # tag:9 type:varint value:1
    
    # Field 11: EmptyMessage
    field_11 = b'\x5A\x00'  # tag:11 type:length-delimited length:0
    
    # Field 12: EmptyMessage
    field_12 = b'\x62\x00'  # tag:12 type:length-delimited length:0
    
    # Combine all fields
    protobuf_data = field_2 + field_5 + field_6 + field_8 + field_9 + field_11 + field_12
    return protobuf_data

async def set_bio_directly_async_with_retry(jwt_token, bio_text, region="IND", max_retries=3, retry_delay=2):
    """Set bio with automatic retry logic"""
    
    for attempt in range(max_retries):
        try:
            print(f"[ SYSTEM ] Bio API attempt {attempt + 1}/{max_retries}")
            
            result = await set_bio_directly_async(jwt_token, bio_text, region)
            
            if result.get("success"):
                return result
            else:
                print(f"[ ERROR ] Bio update failed: {result.get('message')}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay)
                    
        except Exception as e:
            print(f"[ ERROR ] Bio attempt {attempt + 1} error: {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(retry_delay)
            continue
    
    # If all retries failed
    return {
        "success": False,
        "message": f"All {max_retries} attempts failed"
    }

async def set_bio_directly_async(jwt_token, bio_text, region="IND"):
    """Set bio directly - ASYNC version with better error handling"""
    try:
        # Decode JWT to get region
        payload = decode_jwt_noverify(jwt_token)
        if not payload:
            return {
                "success": False,
                "message": "Invalid JWT token"
            }
        
        lock_region = payload.get("lock_region", region).upper()
        url_bio = get_bio_server_url(lock_region)
        
        print(f"[ SYSTEM ] Setting bio for region: {lock_region}")
        print(f"[ DATA ] Bio text: {bio_text}")
        
        # Create protobuf message
        data_bytes = create_bio_protobuf(bio_text)
        print(f"[ DATA ] Protobuf created: {len(data_bytes)} bytes")
        
        # Encrypt using AES CBC
        cipher = AES.new(BIO_ENCRYPTION_KEY, AES.MODE_CBC, BIO_ENCRYPTION_IV)
        
        # Pad data to AES block size (16 bytes)
        padding_length = 16 - (len(data_bytes) % 16)
        if padding_length:
            data_bytes += bytes([padding_length] * padding_length)
        
        encrypted_data = cipher.encrypt(data_bytes)
        print(f"[ DATA ] Encrypted: {len(encrypted_data)} bytes")
        
        # Headers
        headers = {
            "Expect": "100-continue",
            "Authorization": f"Bearer {jwt_token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": FREEFIRE_VERSION,
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        
        print(f"[ NETWORK ] Sending to: {url_bio}")
        
        # Use aiohttp with timeout
        import level_result
        timeout = level_result.ClientTimeout(total=10)
        
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(url_bio, headers=headers, data=encrypted_data) as response:
                response_text = await response.text()
                
                print(f"[ NETWORK ] Response status: {response.status}")
                
                if response.status == 200:
                    return {
                        "success": True,
                        "message": "Bio updated successfully!",
                        "region": lock_region,
                        "bio": bio_text
                    }
                else:
                    return {
                        "success": False,
                        "message": f"Server error: {response.status} - {response_text[:100]}"
                    }
                
    except aiohttp.ClientError as e:
        print(f"[ ERROR ] Network error: {e}")
        return {
            "success": False,
            "message": f"Network error: {str(e)[:80]}"
        }
    except asyncio.TimeoutError:
        print(f"[ ERROR ] Request timeout")
        return {
            "success": False,
            "message": "Request timeout (10s)"
        }
    except Exception as e:
        print(f"[ ERROR ] Bio update error: {e}")
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "message": f"Error: {str(e)[:80]}"
        }

# Now add this command handler to your TcPChaT function
# Find where other commands are handled and add this:

def analyze_squad_packet(packet_json):
    """Analyze packet structure to find squad members"""
    
    print("\n[ SYSTEM ] ANALYZING SQUAD PACKET STRUCTURE")
    print("="*50)
    
    # Check if this is a squad data packet
    if '5' not in packet_json or 'data' not in packet_json['5']:
        print("[ ERROR ] Not a squad data packet")
        return None
    
    squad_data = packet_json['5']['data']
    
    # Look for fields that could contain multiple players
    candidate_fields = []
    
    for field_num in squad_data:
        field_info = squad_data[field_num]
        if 'data' not in field_info:
            continue
            
        data_value = field_info['data']
        
        # Check if it's a list (likely contains multiple players)
        if isinstance(data_value, list):
            print(f"[ SUCCESS ] Field {field_num}: LIST with {len(data_value)} items")
            candidate_fields.append((field_num, 'list', data_value))
            
            # Show first item structure
            if data_value and isinstance(data_value[0], dict):
                print(f"[ DATA ] First item keys: {list(data_value[0].keys())}")
                # Check if first item has UID (field 1)
                if '1' in data_value[0]:
                    uid = data_value[0]['1']['data']
                    print(f"[ DATA ] Contains UID: {uid}")
        
        # Check if it's a dict with numeric keys (0, 1, 2, 3...)
        elif isinstance(data_value, dict):
            keys = list(data_value.keys())
            numeric_keys = [k for k in keys if k.isdigit()]
            if len(numeric_keys) > 0:
                print(f"[ SUCCESS ] Field {field_num}: DICT with numeric keys {numeric_keys[:5]}...")
                candidate_fields.append((field_num, 'dict', data_value))
    
    print("\n[ SYSTEM ] MOST LIKELY SQUAD MEMBERS FIELDS:")
    for field_num, field_type, data in candidate_fields:
        print(f"[ DATA ] Field {field_num} ({field_type})")
        
        if field_type == 'list':
            # Try to extract UIDs from list
            uids = []
            for item in data[:5]:  # Check first 5 items
                if isinstance(item, dict) and '1' in item:
                    uid = item['1']['data']
                    uids.append(uid)
            if uids:
                print(f"[ DATA ] Found UIDs: {uids}")
        
        elif field_type == 'dict':
            # Try to extract UIDs from dict
            uids = []
            for key in list(data.keys())[:5]:  # Check first 5 keys
                item = data[key]
                if isinstance(item, dict) and '1' in item:
                    uid = item['1']['data']
                    uids.append(uid)
            if uids:
                print(f"[ DATA ] Found UIDs: {uids}")
    
    return candidate_fields

def generic_extract(packet_json):
    """Generic search for UID and emote ID"""
    uid = None
    emote_id = None
    
    # Recursively search for UID (long number)
    def search(obj):
        nonlocal uid, emote_id
        
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'data' and isinstance(v, (int, str)) and str(v).isdigit():
                    # Check if it looks like a UID (long number)
                    num = int(v)
                    if 1000000 < num < 99999999999:  # Reasonable UID range
                        if not uid:  # First found is likely sender
                            uid = num
                        # Check if it's an emote ID (starts with 909...)
                        elif str(v).startswith('909') and len(str(v)) >= 9:
                            emote_id = num
                
                elif isinstance(v, dict):
                    search(v)
                elif isinstance(v, list):
                    for item in v:
                        search(item)
    
    search(packet_json)
    
    if uid:
        return {
            'sender_uid': uid,
            'emote_id': emote_id or 909000063,  # Default AK emote
            'packet_type': 'generic',
            'confidence': 'medium'
        }
    
    return None
    
async def auto_reply_with_emote(emote_info, key, iv):
    """Automatically reply with same emote"""
    
    try:
        # Get bot's UID (you need to set this)
        bot_uid = 14010319252  # Replace with your bot's actual UID
        
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        
        # Send emote back to sender
        reply_packet = await Emote_k(sender_uid, emote_id, key, iv, region)
        
        if online_writer:
            online_writer.write(reply_packet)
            await online_writer.drain()
            
            print(f"[ SYSTEM ] Bot replied with emote {emote_id} to {sender_uid}")
            
    except Exception as e:
        print(f"[ ERROR ] Auto-reply error: {e}")

def extract_squad_members_correct(packet_json):
    """Extract squad members from FULL squad packet"""
    
    print("\n[ SYSTEM ] EXTRACTING SQUAD MEMBERS")
    print("="*50)
    
    try:
        if ('5' not in packet_json or 
            'data' not in packet_json['5'] or 
            '2' not in packet_json['5']['data']):
            print("[ ERROR ] Invalid packet structure")
            return []
        
        field2_data = packet_json['5']['data']['2']['data']
        
        squad_members = []
        
        # Field 2 has numeric keys: '1', '2', '3', '4', '5', etc.
        # Each key might be a squad member slot OR player data field
        
        # Let's check what each numeric key contains
        for key in field2_data:
            if not key.isdigit():
                continue
                
            item = field2_data[key]['data']
            print(f"\n[ DATA ] Key {key}: Type = {type(item)}")
            
            if isinstance(item, dict):
                # Check if this is a player object
                # Player objects usually have fields: 1=UID, 2=name, 4=rank, etc.
                if '1' in item and '2' in item:
                    try:
                        uid = item['1']['data']
                        name = item['2']['data']
                        
                        # Make sure it's a valid UID (not a small number)
                        if isinstance(uid, int) and uid > 1000000:
                            rank = item['4']['data'] if '4' in item else 0
                            
                            print(f"   [ SUCCESS ] PLAYER FOUND!")
                            print(f"      [ DATA ] UID: {uid}")
                            print(f"      [ DATA ] Name: {name}")
                            print(f"      [ DATA ] Rank: {rank}")
                            
                            squad_members.append({
                                'slot': key,
                                'uid': uid,
                                'name': name,
                                'rank': rank
                            })
                        else:
                            print(f"   [ WARNING ] Not a UID: {uid}")
                            
                    except Exception as e:
                        print(f"   [ ERROR ] Error extracting player: {e}")
                else:
                    print(f"   [ DATA ] Fields: {list(item.keys())[:5]}...")
            elif isinstance(item, (int, str)):
                print(f"   [ DATA ] Value: {item}")
        
        print(f"\n[ SUCCESS ] TOTAL SQUAD MEMBERS FOUND: {len(squad_members)}")
        for member in squad_members:
            print(f"  • Slot {member['slot']}: {member['name']} (UID: {member['uid']})")
        
        return squad_members
        
    except Exception as e:
        print(f"[ ERROR ] Extraction error: {e}")
        import traceback
        traceback.print_exc()
        return []
        
async def analyze_packet_structure(data_hex, key, iv):
    """Analyze and display packet structure"""
    
    print(f"\n[ SYSTEM ] PACKET ANALYSIS")
    print("="*50)
    
    # Basic info
    print(f"[ DATA ] Length: {len(data_hex)} characters")
    print(f"[ DATA ] Header: {data_hex[:10]}")
    
    # Try to decode
    try:
        if len(data_hex) > 20:
            decoded = await DeCode_PackEt(data_hex[10:])
            packet_json = json.loads(decoded)
            
            print(f"[ SUCCESS ] Successfully decoded!")
            print(f"[ DATA ] Packet type (field 1): {packet_json.get('1', 'Unknown')}")
            
            # Show structure
            print(f"\n[ SYSTEM ] PACKET STRUCTURE:")
            print(f"[ DATA ] Top-level fields: {list(packet_json.keys())}")
            
            # Show field 1 value
            if '1' in packet_json:
                print(f"  [ DATA ] Field 1: {packet_json['1']}")
            
            # Show if it contains emote ID patterns


            emote_patterns = re.findall(r'909[0-9a-f]{6}', data_hex)
            if emote_patterns:
                print(f"\n[ DATA ] EMOTE IDS FOUND IN HEX: {emote_patterns}")
            
            # Show UID patterns
            uid_patterns = re.findall(r'(\d{9,11})', data_hex)
            uids = [uid for uid in uid_patterns if not uid.startswith('909')]
            if uids:
                print(f"[ DATA ] UIDS FOUND IN HEX: {uids}")
            
            # Return the decoded structure
            return packet_json
            
        else:
            print("[ ERROR ] Packet too short to decode")
            return None
            
    except Exception as e:
        print(f"[ ERROR ] Decode error: {e}")
        return None

async def RedZed_SendInv(bot_uid, uid, key, iv):
    """Async version of send invite function"""
    try:
        fields = {
            1: 2, 
            2: {
                1: int(uid), 
                2: "IND", 
                3: 1, 
                4: 1, 
                6: "RedZedKing!!", 
                7: 330, 
                8: 1000, 
                9: 100, 
                10: "DZ", 
                12: 1, 
                13: int(uid), 
                16: 1, 
                17: {
                    2: 159, 
                    4: "y[WW", 
                    6: 11, 
                    8: "1.123.1", 
                    9: 3, 
                    10: 1
                }, 
                18: 306, 
                19: 18, 
                24: 902000306, 
                26: {}, 
                27: {
                    1: 11, 
                    2: int(bot_uid), 
                    3: 99999999999
                }, 
                28: {}, 
                31: {
                    1: 1, 
                    2: 32768
                }, 
                32: 32768, 
                34: {
                    1: bot_uid, 
                    2: 8, 
                    3: b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
                }
            }
        }
        
        # Convert bytes properly
        if isinstance(fields[2][34][3], str):
            fields[2][34][3] = b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
        
        # Use async versions of your functions
        packet = await CrEaTe_ProTo(fields)
        packet_hex = packet.hex()
        
        # Generate final packet
        final_packet = await GeneRaTePk(packet_hex, '0515', key, iv)
        
        return final_packet
        
    except Exception as e:
        print(f"[ ERROR ] Error in RedZed_SendInv: {e}")
        import traceback
        traceback.print_exc()
        return None
        
async def freeze_emote_spam(uid, key, iv, region, chat_type, chat_id, sender_uid):
    """Send 3 freeze emotes in 1-second cycles for 10 seconds"""
    global freeze_running
    
    try:
        cycles = 0
        max_cycles = FREEZE_DURATION  # 10 seconds
        
        while freeze_running and cycles < max_cycles:
            # Send all 3 emotes in sequence
            for i, emote_id in enumerate(FREEZE_EMOTES):
                if not freeze_running:
                    break
                    
                try:
                    # Send emote
                    emote_packet = await Emote_k(int(uid), emote_id, key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
                    
                    print(f"[ SYSTEM ] Freeze emote {i+1}/{len(FREEZE_EMOTES)} sent: {emote_id}")
                    
                    # Small delay between emotes (0.3 seconds)
                    await asyncio.sleep(0.3)
                    
                except Exception as e:
                    print(f"[ ERROR ] Error sending freeze emote {i+1}: {e}")
            
            cycles += 1
            print(f"[ SYSTEM ] Freeze cycle {cycles}/{max_cycles} completed")
            
            # Wait for next cycle (total 1 second per cycle)
            remaining_time = 1.0 - (0.3 * len(FREEZE_EMOTES))
            if remaining_time > 0:
                await asyncio.sleep(remaining_time)
        
        print(f"[ SUCCESS ] Freeze sequence completed: {cycles} cycles")
        return cycles
        
    except Exception as e:
        print(f"[ ERROR ] Freeze function error: {e}")
        return 0
        
async def handle_freeze_completion(freeze_task, uid, sender_uid, chat_id, chat_type, key, iv):
    """Handle freeze command completion"""
    try:
        cycles_completed = await freeze_task
        
        completion_msg = f"""
[B][C][00FFFF]✦ FREEZE COMPLETED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(uid)}
[00FF00]TIME   : [FFFFFF]{cycles_completed} seconds
[00FF00]EMOTES : [FFFFFF]{cycles_completed * 3}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv)
        
    except asyncio.CancelledError:
        print("[ SYSTEM ] Freeze command cancelled")
    except Exception as e:
        error_msg = f"""
[B][C][00FFFF]✦ FREEZE ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv)

async def test_emote_packet(target_uid, emote_id, key, iv, region="IND"):
    """Test if emote packet works and show structure"""
    
    print(f"\n[ SYSTEM ] TESTING EMOTE PACKET")
    print("="*50)
    
    # Create the packet using your function
    emote_packet = await Emote_k(target_uid, emote_id, key, iv, region)
    
    if not emote_packet:
        print("[ ERROR ] Failed to create packet")
        return False
    
    # Convert to hex for analysis
    packet_hex = emote_packet.hex()
    
    print(f"[ SUCCESS ] Packet created!")
    print(f"   [ DATA ] Length: {len(packet_hex)} characters")
    print(f"   [ DATA ] Header: {packet_hex[:20]}")
    
    # Try to decode it back
    try:
        if len(packet_hex) > 20:
            # Remove header (first 10 bytes = 20 hex chars)
            payload = packet_hex[20:]  # Skip header
            
            # Decrypt (you need to implement this)
            # For testing, let's see raw structure
            print(f"\n[ SYSTEM ] RAW PACKET STRUCTURE:")
            print(f"[ DATA ] Full hex (first 200 chars):")
            print(packet_hex[:200] + "...")
            
            # Look for the UID in hex

            uid_hex = hex(target_uid)[2:]
            if uid_hex in packet_hex:
                print(f"[ SUCCESS ] Target UID {xMsGFixinG(target_uid)} found in packet!")
            else:
                print(f"[ ERROR ] Target UID not found in hex")
            
            # Look for emote ID
            emote_hex = hex(emote_id)[2:]
            if emote_hex in packet_hex:
                print(f"[ SUCCESS ] Emote ID {emote_id} found in packet!")
            else:
                print(f"[ ERROR ] Emote ID not found in hex")
        
        print(f"\n[ SUCCESS ] Packet created successfully!")
        return True
        
    except Exception as e:
        print(f"[ ERROR ] Analysis error: {e}")
        return False
        
async def send_and_monitor_emote(target_uid, emote_id, key, iv, region, reader):
    """Send emote and monitor response - FIXED VERSION"""
    
    print(f"\n[ SYSTEM ] SENDING TEST EMOTE")
    print(f"   [ DATA ] Target: {xMsGFixinG(target_uid)}")
    print(f"   [ DATA ] Emote: {emote_id}")
    print("="*50)
    
    # 1. Create packet
    emote_packet = await Emote_k(target_uid, emote_id, key, iv, region)
    
    if not emote_packet:
        print("[ ERROR ] Failed to create packet")
        return
    
    # 2. Send it
    print("[ NETWORK ] Sending packet...")
    if online_writer:
        online_writer.write(emote_packet)
        await online_writer.drain()
        print("[ SUCCESS ] Packet sent!")
    else:
        print("[ ERROR ] No connection")
        return
    
    # 3. Wait for response (SHORTER - 2 seconds)
    print("\n[ SYSTEM ] Waiting for response (2 seconds)...")
    
    responses = []
    start_time = time.time()
    
    while time.time() - start_time < 2:  # Reduced from 5 to 2 seconds
        try:
            # Read any response
            if reader:
                response = await asyncio.wait_for(reader.read(9999), timeout=0.1)
                if response:
                    resp_hex = response.hex()
                    responses.append(resp_hex)
                    
                    # Quick analysis
                    print(f"[ NETWORK ] Got response #{len(responses)}")
                    print(f"   [ DATA ] Length: {len(resp_hex)} chars")
                    print(f"   [ DATA ] Header: {resp_hex[:10]}")
                    
                    # Check if it's the emote echo
                    if '909' in resp_hex:
                        print(f"   [ SUCCESS ] Contains emote ID!")
        except asyncio.TimeoutError:
            continue
        except Exception as e:
            # Silent error - don't print
            pass
    
    # 4. Summary
    print(f"\n[ SYSTEM ] RESPONSE SUMMARY")
    print(f"[ DATA ] Total responses: {len(responses)}")
    
    if len(responses) > 0:
        print("[ SUCCESS ] SUCCESS! Server accepted your emote packet!")
    else:
        print("[ WARNING ] No immediate response (might still be processing)")
        
async def start_auto_packet(key, iv, region):
    """Create start match packet"""
    fields = {
        1: 9,
        2: {
            1: 12480598706,
        },
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
        
async def KickTarget(target_uid, key, iv):
    fields = {1: 35, 2: {1: int(target_uid)}}
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0515' , key, iv)
            
def analyze_hex_packet(packet_hex):
    """Analyze hex packet structure"""
    
    print(f"\n[ SYSTEM ] HEX PACKET ANALYSIS")
    print("="*50)
    
    # Header analysis
    header = packet_hex[:10]
    print(f"[ DATA ] Header (first 5 bytes): {header}")
    
    # Common headers:
    # 0514 = IND online packet
    # 0519 = BD online packet  
    # 1215 = Whisper packet
    # 1200 = Chat packet
    
    if header.startswith('05'):
        print("[ NETWORK ] Online connection packet")
    elif header.startswith('12'):
        print("[ NETWORK ] Whisper/Chat packet")
    
    # Look for UIDs (9-11 digit numbers in hex)
    import re
    
    # Find all sequences of 9+ hex digits
    hex_patterns = re.findall(r'[0-9a-f]{9,12}', packet_hex.lower())
    
    print(f"\n[ DATA ] Hex sequences found:")
    for pattern in hex_patterns[:10]:  # Show first 10
        # Try to convert to decimal
        try:
            decimal = int(pattern, 16)
            if 1000000 < decimal < 99999999999:  # Reasonable UID range
                print(f"  [ DATA ] {pattern} → {decimal} (Possible UID)")
            elif decimal > 900000000:  # Emote ID range
                print(f"  [ DATA ] {pattern} → {decimal} (Possible emote ID)")
        except:
            print(f"  [ DATA ] {pattern}")
    
    # Show packet content (first 200 chars)
    print(f"\n[ DATA ] Packet preview (first 200 chars):")
    print(packet_hex[:200])
    
    if len(packet_hex) > 200:
        print(f"[ DATA ] ... and {len(packet_hex) - 200} more characters")
        
def append_to_whitelist(uid_to_add):
    """Simple function to add UID to whitelist"""
    global WHITELISTED_UIDS
    
    uid_str = str(uid_to_add)
    
    if uid_str in WHITELISTED_UIDS:
        return False, f"UID {uid_str} already in whitelist"
    
    WHITELISTED_UIDS.add(uid_str)
    return True, f"✅ Added {uid_str} to whitelist"
    
async def send_friend_request_async(target_uid: str, count: int = 1) -> dict:
    """
    Main function to send friend requests from TCP bot
    
    Args:
        target_uid: Target player UID
        count: Number of requests (1 for single, >1 for bulk)
    
    Returns:
        Dictionary with results
    """
    try:
        if count == 1:
            # Single request using /tmp/token.json
            token = load_jwt_token()
            if not token:
                return {"success": 0, "failed": 1, "error": "No token found"}
            
            success = send_friend_request_single(target_uid, token)
            
            if success:
                return {"success": 1, "failed": 0}
            else:
                return {"success": 0, "failed": 1}
                
        else:
            # Bulk requests using token_ind.json
            tokens = load_tokens_ind()
            if not tokens:
                return {"success": 0, "failed": 0, "error": "No tokens found"}
            
            max_count = min(count, len(tokens))
            results = {"success": 0, "failed": 0}
            
            print(f"[ NETWORK ] Sending {max_count} friend requests...")
            
            # Send requests sequentially (or use threading for faster)
            for i in range(max_count):
                token = tokens[i]['token']
                success = send_friend_request_single(target_uid, token)
                
                if success:
                    results["success"] += 1
                else:
                    results["failed"] += 1
                
                # Small delay to avoid rate limiting
                await asyncio.sleep(0.1)
            
            return results
            
    except Exception as e:
        print(f"[ ERROR ] Friend request error: {e}")
        return {"success": 0, "failed": 0, "error": str(e)}    

async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer, last_status_packet, status_response_cache, senthi
    global insquad, joining_team, whisper_writer, region
 
    bot_uid = 14010319252
 
    if insquad is not None:
        insquad = None
    if joining_team is True:
        joining_team = False
    
    online_writer = None
    whisper_writer = None
    
    while True:
        try:
            print(f"[ NETWORK ] Attempting to connect to {ip}:{port}...")
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            
            # --- AUTHENTICATION ---
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            print("[ SUCCESS ] Authentication token sent. Listening for emotes...")
            
            # --- READING LOOP ---
            while True:
                data2 = await reader.read(9999)
                    
                if not data2: 
                    print("[ WARNING ] Connection closed by the server.")
                    break
                    
                data_hex = data2.hex()

                # =================== AUTO ACCEPT HANDLING ===================
                
                # Case 1: Squad is cancelled or left (6, 7 are often status/exit codes)
                if data_hex.startswith('0500') and insquad is not None and joining_team == False:
                    try:
                        # Assuming DeCode_PackEt and json.loads are available and correct
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        # Validate packet structure
                        if isinstance(packet_json, dict) and packet_json.get('1') in [6, 7]: 
                             insquad = None
                             joining_team = False
                             print("[ SYSTEM ] Squad cancelled or exited (code 6/7).")
                             continue
                             
                    except (KeyError, ValueError, TypeError):
                        # Silently skip packets with unexpected structure
                        pass
                    except Exception as e:
                        # Only log unexpected errors
                        if "indices must be integers" not in str(e):
                            print(f"[ ERROR ] Error in auto-accept case 1: {e}")
                        pass
                
                # Case 2: Auto-accept for whitelisted users
                if data_hex.startswith("0500") and insquad is None and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        # Validate packet structure before accessing
                        if not isinstance(packet_json, dict):
                            continue
                            
                        if '5' not in packet_json or 'data' not in packet_json.get('5', {}):
                            continue
    
                        uid = packet_json['5']['data']['1']['data']
                        invite_uid = packet_json['5']['data']['2']['data']['1']['data']
                        squad_owner = packet_json['5']['data']['1']['data']  # Person inviting
                        code = packet_json['5']['data']['8']['data']
  

                        emote_id = 909050009
                        bot_uid = 14009897329
    
                        # Check if the squad owner is whitelisted
                        if str(squad_owner) in WHITELISTED_UIDS:
                            print(f"[ SUCCESS ] Whitelisted user {squad_owner} invited bot. Accepting...")
                        
                            SendInv = await RedZed_SendInv(bot_uid, invite_uid, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', SendInv)
                            inv_packet = await RejectMSGtaxt(squad_owner, uid, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', inv_packet)
        
                            print(f"[ NETWORK ] Received squad invite from {squad_owner}, accepting...")                  
                            Join = await ArohiAccepted(squad_owner, code, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', Join)
        
                            await asyncio.sleep(2)
                                                    
                            emote_to_sender = await Emote_k(int(uid), emote_id, key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_sender)
        
                            bot_emote = await Emote_k(int(bot_uid), emote_id, key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_emote)
                            
                            
            
                            # Set squad status
                            insquad = True
                            print(f"[ SYSTEM ] Bot joined squad of {squad_owner}")
        
        
        
                        else:
                            try:
                                print(f"[ WARNING ] Bot is private! Ignoring invite from {squad_owner}")
                                 # Send quick reject message
                                bot_uid = 13777711848
                                message_text = f" Can't accept Your request Talk to God Blaze"
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(squad_owner),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
                                print("[ DATA ] got it")

                                if private_msg_packet and whisper_writer:
                                    # Send via Whisper connection (chat connection)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
                                else:
                                    print("[ ERROR ] can't do it")
                    
                                    
                            except Exception as e:
                                print("[ ERROR ] got an error in can't accept")
    

                    except KeyError as e:
                        # Silently skip packets with unexpected structure
                        continue
                    except Exception as e:
                        # Only log unexpected errors
                        if "indices must be integers" not in str(e):
                            print(f"[ ERROR ] Error in auto-accept: {e}")
                        insquad = None
                        joining_team = False
                        continue
                
                # =================== HANDLE KICK/RECONNECT ===================
                # Case 3: Bot was kicked and needs to re-join chat
                if data_hex.startswith('0500') and len(data_hex) > 1000:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                    
                        packet_type = packet_json.get('1')
        
                        # Detect ALL kick/leave packets
                        if packet_type in [6, 7, 8, 9, 10, 11, 12]:
                            print(f"[ SYSTEM ] Kick/Leave packet detected (Type: {packet_type})")
            
                            # RESET SQUAD STATUS
                            insquad = None
                            joining_team = False
            
                            print(f"[ SUCCESS ] Bot reset after kick. Ready for new invites.")
                            
                            # Try to extract squad info for possible reconnection
                            try:
                                if '5' in packet_json and 'data' in packet_json['5']:
                                    OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet_json)
                                    print(f"[ SYSTEM ] Attempting reconnection to squad {SQuAD_CoDe}...")
                    
                                    # Re-authenticate chat
                                    JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', JoinCHaT)
                    
                                    print(f"[ SUCCESS ] Chat re-authenticated for reconnection")
                            except:
                                print("[ WARNING ] Could not extract squad info")
                                
                            continue  # Skip other handlers
        
                        # Also check for general squad data packets (for reconnection)
                        elif '5' in packet_json and 'data' in packet_json['5']:
                            try:
                                OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet_json)
                
                                # If we have squad data but insquad is None, try to reconnect
                                if insquad is None:
                                    print(f"[ SYSTEM ] Received squad data while not in squad. Attempting chat auth...")
                                    
                                    JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', JoinCHaT)
                    
                                    # Optional welcome back message
                                    welcome_msg = f"""
[B][C][00FFFF]✦ BOT RECONNECTED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    P = await SEndMsG(0, welcome_msg, OwNer_UiD, OwNer_UiD, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                    
                            except:
                                pass  # Not a squad data packet
                
                    except Exception as e:
                        print(f"[ ERROR ] Kick/reconnect handler error: {e}")
                        pass
                
                # case 5
                if insquad == True:
                    try:
                        # Assuming DeCode_PackEt, json.loads, GeTSQDaTa, AutH_Chat, SEndPacKeT are available
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet_json)
                        
                        print(f"[ SYSTEM ] Received squad data for joining team, attempting chat auth for {OwNer_UiD}...")
                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)
                        
                        def get_random_color(): return "_" 
                        message = """[B][C][00FFFF]✦ GOD BLAZE BOT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]⚡ Status: Online 24/7
[FFD700]👑 Developer: God Blaze
[FFFFFF]━━━━━━━━━━━━━━━━━━
[FF00FF]Type /help for commands!"""
                        # In your auto-join (Old Handler) code, find this line:

                        P = await SEndMsG(0, message, OwNer_UiD, OwNer_UiD, key, iv, region)
                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        
                        joining_team = False
                        insquad = None
                            
                    except Exception as e:
                        print(f"[ ERROR ] Error in joining_team chat auth: {e}")
                        # Removed the redundant inner try/except block.
                        pass
                
                if "0600" in data2.hex()[0:4] and len(data2.hex()) > 700:
                    accept_packet = f'08{data2.hex().split("08", 1)[1]}'
                    kk = get_available_room(accept_packet)
                    parsed_data = json.loads(kk)
                    #logging.info(parsed_data)

                    senthi = True

                if senthi == True:
                    
                    def get_random_color(): return "_" 
                    message = """[B][C][00FFFF]✦ GOD BLAZE BOT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]⚡ Status: Online 24/7
[FFD700]👑 Developer: God Blaze
[FFFFFF]━━━━━━━━━━━━━━━━━━
[FF00FF]Type /help for commands!"""
                        # In your auto-join (Old Handler) code, find this line:

                    P = await SEndMsG(0, message, OwNer_UiD, OwNer_UiD, key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                    senthi = False

                # =================== STATUS HANDLER ===================
                if data_hex.startswith('0f00') and len(data_hex) > 100:
                    print(f"[ NETWORK ] Received status response packet")
    
                    try:
                        # Assuming the protocol structure: 0f00 + length bytes + 08 + actual proto data
                        # The split logic might need refinement based on the exact protocol
                        if '08' in data_hex:
                            proto_part = f'08{data_hex.split("08", 1)[1]}'
                        else:
                            print("[ WARNING ] Status packet structure missing '08' marker.")
                            continue
        
                        # Assuming get_available_room is available
                        parsed_data = get_available_room(proto_part)
                        if parsed_data:
                            parsed_json = json.loads(parsed_data)
            
                            # Check if it's field 15 (player info)
                            if "2" in parsed_json and parsed_json["2"]["data"] == 15:
                                # Get player ID
                                player_id = parsed_json["5"]["data"]["1"]["data"]["1"]["data"]
                
                                # Assuming get_player_status is available
                                player_status = get_player_status(proto_part) 
                                print(f"[ SUCCESS ] Parsed status for {xMsGFixinG(player_id)}: {player_status}")
                
                                # Create cache entry
                                cache_entry = {
                                    'status': player_status, 
                                    'packet': proto_part,
                                    'timestamp': time.time(),
                                    'full_packet': data_hex,
                                    'parsed_json': parsed_json
                                }
                
                                # --- SPECIAL CONDITION CHECK ---
                                try:
                                    StatusData = parsed_json
                                    if ("5" in StatusData and "data" in StatusData["5"] and 
                                        "1" in StatusData["5"]["data"] and "data" in StatusData["5"]["data"]["1"] and 
                                        "3" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["3"] and 
                                        StatusData["5"]["data"]["1"]["data"]["3"]["data"] == 1 and 
                                        "11" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["11"] and 
                                        StatusData["5"]["data"]["1"]["data"]["11"]["data"] == 1):
                
                                        print(f"[ SYSTEM ] SPECIAL CONDITION MET: Player {xMsGFixinG(target_uid)} is in SOLO mode with special flag 11=1")
                                        cache_entry['special_state'] = 'SOLO_WITH_FLAG_1'
                
                                except Exception as cond_error:
                                    print(f"[ WARNING ] Error checking special condition: {cond_error}")
                                # ------------------------------

                                # If in room, extract room ID
                                if "IN ROOM" in player_status:
                                    try:
                                        # Assuming get_idroom_by_idplayer is available
                                        room_id = get_idroom_by_idplayer(proto_part)
                                        if room_id:
                                            cache_entry['room_id'] = room_id
                                            print(f"[ DATA ] Room ID extracted: {room_id}")
                                    except Exception as room_error:
                                        print(f"[ ERROR ] Failed to extract room ID: {room_error}")
                
                                # If in squad, extract leader
                                elif "INSQUAD" in player_status:
                                    try:
                                        # Assuming get_leader is available
                                        leader_id = get_leader(proto_part)
                                        if leader_id:
                                            cache_entry['leader_id'] = leader_id
                                            print(f"[ DATA ] Leader ID: {leader_id}")
                                    except Exception as leader_error:
                                        print(f"[ ERROR ] Failed to extract leader: {leader_error}")
                
                                # Save to FILE cache (Assuming save_to_cache is available)
                                save_to_cache(player_id, cache_entry)
                                print(f"[ SUCCESS ] Saved to cache: {xMsGFixinG(target_uid)} = {player_status}")
                
                    except Exception as e:
                        print(f"[ ERROR ] Error parsing status: {e}")
                        import traceback
                        traceback.print_exc()
                
                # =================== END STATUS HANDLER ===================


            # --- CLEANUP AFTER INNER LOOP (Connection closed) ---
            if online_writer is not None:
                online_writer.close()
                await online_writer.wait_closed()
                online_writer = None
            
            if whisper_writer is not None:
                try:
                    whisper_writer.close()
                    await whisper_writer.wait_closed()
                except:
                    pass
                whisper_writer = None
                
            insquad = None
            joining_team = False
            
            print(f"[ SYSTEM ] Connection closed. Reconnecting in {reconnect_delay} seconds...")

        except ConnectionRefusedError:
            print(f"[ ERROR ] Connection refused by server at {ip}:{port}.")
        except asyncio.TimeoutError:
            print(f"[ ERROR ] Connection attempt to {ip}:{port} timed out.")
        except Exception as e:
            print(f"[ ERROR ] With {ip}:{port} - {e}")
            traceback.print_exc() 
            
            # --- CLEANUP AFTER EXCEPTION ---
            if online_writer is not None:
                try:
                    online_writer.close()
                    await online_writer.wait_closed()
                except:
                    pass
                online_writer = None
            if whisper_writer is not None:
                try:
                    whisper_writer.close()
                    await whisper_writer.wait_closed()
                except:
                    pass
                whisper_writer = None
                
            insquad = None
            joining_team = False
            
        await asyncio.sleep(reconnect_delay)

async def send_keep_alive(key, iv, region):
    """Send keep-alive packet to maintain connection"""
    try:
        fields = {
            1: 99,  # Keep-alive packet type
            2: {
                1: int(time.time()),
                2: 1,  # Keep-alive flag
            }
        }
        
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
        return packet
    except Exception as e:
        print(f"[ ERROR ] Keep-alive error: {e}")
        return None
        
                    

                            
async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(f"[ SYSTEM ] {region} TCP CHAT")

    global whisper_writer , spammer_uid , online_writer , chat_id , XX , uid , data2, fast_spam_running, fast_spam_task, custom_spam_running, custom_spam_task, spam_request_running, spam_request_task, reject_spam_running, reject_spam_task, bot_enabled
    # At the VERY TOP of your file, with other globals:
    status_response_cache = {}
    cache_lock = asyncio.Lock()  # For thread safety
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n[ SYSTEM ] Target Bot in Clan!')
                print(f'[ DATA ] Clan UID: {clan_id}')
                print(f'[ SUCCESS ] Bot connected with Clan Chat successfully!')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                        MsG = response.Data.msg.lower()

                    except:
                        response = None
                        
                        

                        



                    # ============ WHITELIST CHECK ============
                    # ============ WHITELIST CHECK ============
                    if response:
                        # Get data
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                        MsG = response.Data.msg.lower() # Added this to match your code

                        # ============ PUBLIC MODE ENABLED ============
                        # Maine yahan se Blocking Code hata diya hai.
                        # Ab bot check nahi karega, sab log commands use kar payenge.
                        
                        uid_str = str(uid)
                        print(f"[ COMMAND ] Received from: {uid_str} (Public Mode)")

                        # ... Yahan se niche commands shuru honge ...

                        # ========= BLOCK WHEN OFF (ONLY HERE) =========
                        if not bot_enabled:
                            await safe_send_message(response.Data.chat_type, "⛔ Bot is OFF", uid, chat_id, key, iv)
                            continue

    
# ================= BUNDLE COMMAND START =================
   # ================= FINAL BUNDLE COMMAND (FAST) =================
                        if inPuTMsG.strip().startswith('/bundle'):
                            print(f"[ COMMAND ] {inPuTMsG}")
                            
                            parts = inPuTMsG.strip().split()
                            
                            if len(parts) < 2:
                                bundle_list = """
[B][C][00FFFF]✦ BUNDLE LIST ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]• [FFFFFF]rampage
[00FF00]• [FFFFFF]cannibal
[00FF00]• [FFFFFF]devil
[00FF00]• [FFFFFF]scorpio
[00FF00]• [FFFFFF]frostfire
[00FF00]• [FFFFFF]paradox
[00FF00]• [FFFFFF]naruto
[00FF00]• [FFFFFF]aurora
[00FF00]• [FFFFFF]midnight
[00FF00]• [FFFFFF]itachi
[00FF00]• [FFFFFF]dreamspace
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, bundle_list, uid, chat_id, key, iv)
                            else:
                                bundle_name = parts[1].lower()
                                
                                # Real IDs
                                bundle_ids = {
                                    "rampage": "914000002", "cannibal": "914000003",
                                    "devil": "914038001", "scorpio": "914039001",
                                    "frostfire": "914042001", "paradox": "914044001",
                                    "naruto": "914047001", "aurora": "914047002",
                                    "midnight": "914048001", "itachi": "914050001",
                                    "dreamspace": "914051001"
                                }
                                
                                if bundle_name not in bundle_ids:
                                    error_msg = f"""
[B][C][00FFFF]✦ BUNDLE ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Invalid Name
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    bundle_id = bundle_ids[bundle_name]
                                    
                                    try:
                                        # Function call
                                        bundle_packet = await bundle_packet_async(bundle_id, key, iv, region)

                                        if bundle_packet and online_writer:
                                            # Packet Bhejo
                                            online_writer.write(bundle_packet)
                                            await online_writer.drain()
                                            
                                            success_msg = f"""
[B][C][00FFFF]✦ BUNDLE EQUIPPED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]BUNDLE : [FFFFFF]{bundle_name}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        else:
                                            print("[ ERROR ] Connection Lost")
                                    
                                    except Exception as e:
                                        print(f"[ ERROR ] Bundle command error: {e}")
                        # ===============================================================



                        # FREEZE COMMAND - /freeze [uid]
                        if inPuTMsG.strip().startswith('/freeze'):
                            print('[ COMMAND ] Processing freeze command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ FREEZE COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/freeze (uid)
[00FF00]EX 1   : [FFFFFF]/freeze me
[00FF00]EX 2   : [FFFFFF]/freeze 123456789
[00FF00]INFO   : [FFFFFF]Sends 3 ice/freeze emotes
[00FF00]ACTION : [FFFFFF]Use /stop_freeze to stop
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                
                                # Handle "me" or "self"
                                if target_uid.lower() in ['me', 'self', 'myself']:
                                    target_uid = str(response.Data.uid)
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {xMsGFixinG(target_uid)}"
                                
                                # Stop any existing freeze task
                                global freeze_running, freeze_task
                                if freeze_task and not freeze_task.done():
                                    freeze_running = False
                                    freeze_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Send initial message
                                initial_msg = f"""
[B][C][00FFFF]✦ FREEZE STARTED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{target_name}
[00FF00]TIME   : [FFFFFF]{FREEZE_DURATION} seconds
[00FF00]CYCLE  : [FFFFFF]1 second
[00FF00]STATUS : [FFFFFF]Starting sequence...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                # Start freeze task
                                freeze_running = True
                                freeze_task = asyncio.create_task(
                                    freeze_emote_spam(target_uid, key, iv, region, response.Data.chat_type, chat_id, uid)
                                )
        
                                # Handle completion
                                asyncio.create_task(
                                    handle_freeze_completion(freeze_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv)
                                )

                        if inPuTMsG.strip().startswith('/bio'):
                            print('[ COMMAND ] Processing bio change command')
    
                            parts = inPuTMsG.strip().split(maxsplit=1)
    
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ BIO COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/bio (text)
[00FF00]EX 1   : [FFFFFF]/bio Hello World
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                bio_text = parts[1]
                                
                                # Check length
                                if len(bio_text) > 50:
                                    error_msg = f"""
[B][C][00FFFF]✦ BIO ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Bio too long! Max 50 characters.
[00FF00]LENGTH : [FFFFFF]{len(bio_text)} chars
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                # Send initial message
                                initial_msg = f"""
[B][C][00FFFF]✦ UPDATING BIO ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]BIO    : [FFFFFF]{bio_text[:30]}...
[00FF00]STATUS : [FFFFFF]Please wait...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                # FIXED: Handle credentials properly
                                credentials = load_credentials_from_file("God_Blaze.txt")
                                if not credentials:
                                    error_msg = f"""
[B][C][00FFFF]✦ BIO ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Failed to load credentials from file!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
            
                                try:
                                    Uid, Pw = credentials
                                except:
                                    # If credentials returns more than 2 values, take first 2
                                    Uid = credentials[0] if isinstance(credentials, (list, tuple)) else None
                                    Pw = credentials[1] if isinstance(credentials, (list, tuple)) and len(credentials) > 1 else None
        
                                if not Uid or not Pw:
                                    error_msg = f"""
[B][C][00FFFF]✦ BIO ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Invalid credentials format!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                # Add retry logic for bio update
                                max_retries = 3
                                retry_delay = 2  # seconds
                                success = False
                                result = None
        
                                for attempt in range(max_retries):
                                    try:
                                        print(f"[ SYSTEM ] Bio update attempt {attempt + 1}/{max_retries}")
                
                                        # Get fresh token for each attempt
                                        open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
                                        if not open_id or not access_token:
                                            print(f"[ ERROR ] Failed to generate access token on attempt {attempt + 1}")
                                            await asyncio.sleep(retry_delay)
                                            continue
                
                                        PyL = await EncRypTMajoRLoGin(open_id, access_token)
                                        MajoRLoGinResPonsE = await MajorLogin(PyL)
                                        MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
                
                                        if not MajoRLoGinauTh or not MajoRLoGinauTh.token:
                                            print(f"[ ERROR ] No token received on attempt {attempt + 1}")
                                            await asyncio.sleep(retry_delay)
                                            continue
                
                                        token = MajoRLoGinauTh.token
                                        print(f"[ SUCCESS ] Using token: {token[:20]}...")
                
                                        # Call bio update with retry
                                        result = await set_bio_directly_async_with_retry(token, bio_text, region)
                                        
                                        if result.get("success"):
                                            success = True
                                            break
                                        else:
                                            print(f"[ ERROR ] Bio update failed on attempt {attempt + 1}: {result.get('message')}")
                                            if attempt < max_retries - 1:
                                                # Send progress update
                                                progress_msg = f"""
[B][C][00FFFF]✦ BIO RETRY ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Retrying... (Attempt {attempt + 2}/{max_retries})
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                                await safe_send_message(response.Data.chat_type, progress_msg, uid, chat_id, key, iv)
                                                await asyncio.sleep(retry_delay)
                        
                                    except Exception as e:
                                        print(f"[ ERROR ] Attempt {attempt + 1} error: {e}")
                                        if attempt < max_retries - 1:
                                            await asyncio.sleep(retry_delay)
                                        continue
        
                                # Send final result
                                if success:
                                    success_msg = f"""
[B][C][00FFFF]✦ BIO UPDATED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]BIO    : [FFFFFF]{bio_text}
[00FF00]REGION : [FFFFFF]{result.get('region', region)}
[00FF00]ATTEMPT: [FFFFFF]{attempt + 1}/{max_retries}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                else:
                                    success_msg = f"""
[B][C][00FFFF]✦ BIO FAILED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]BIO    : [FFFFFF]{bio_text}
[00FF00]ERROR  : [FFFFFF]{result.get('message', 'All attempts failed')}
[00FF00]ACTION : [FFFFFF]Try shorter text or wait 1 min
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
            

                        # QUICK EMOTE ATTACK COMMAND - /quick [team_code] [emote_id] [target_uid?]
                        if inPuTMsG.strip().startswith('/quick'):
                            print('[ COMMAND ] Processing quick emote attack command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 3:
                                error_msg = f"""
[B][C][00FFFF]✦ QUICK COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/quick (team_code) [emote_id] [target_uid]
[00FF00]EX 1   : [FFFFFF]/quick ABC123
[00FF00]EX 2   : [FFFFFF]/ghostquick ABC123
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
        
                                # Set default values
                                emote_id = parts[0]
                                target_uid = str(response.Data.uid)  # Default: Sender's UID
        
                                # Parse optional parameters
                                if len(parts) >= 3:
                                    emote_id = parts[2]
                                if len(parts) >= 4:
                                    target_uid = parts[3]
        
                                # Determine target name for message
                                if target_uid == str(response.Data.uid):
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {xMsGFixinG(target_uid)}"
        
                                initial_message = f"""
[B][C][00FFFF]✦ QUICK EMOTE ATTACK ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TEAM   : [FFFFFF]{team_code}
[00FF00]EMOTE  : [FFFFFF]{emote_id}
[00FF00]TARGET : [FFFFFF]{target_name}
[00FF00]STATUS : [FFFFFF]Executing sequence...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
                                try:
                                    # Try regular method first
                                    success, result = await ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region)
            
                                    if success:
                                        success_message = f"""
[B][C][00FFFF]✦ QUICK ATTACK SUCCESS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TEAM   : [FFFFFF]{team_code}
[00FF00]EMOTE  : [FFFFFF]{emote_id}
[00FF00]TARGET : [FFFFFF]{target_name}
[00FF00]STATUS : [FFFFFF]Bot joined → emoted → left! ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    else:
                                        success_message = f"""
[B][C][00FFFF]✦ QUICK ATTACK FAILED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{result}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print("[ ERROR ] Quick attack failed")
            

                        # /xjoin command removed
            
                        # PLAYER INVITE 
                        if inPuTMsG.strip().startswith('/inv'):
                            print('[ COMMAND ] Processing invite command')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ INVITE COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/inv (uid)
[00FF00]EX 1   : [FFFFFF]/inv 123456789
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"""
[B][C][00FFFF]✦ SENDING INVITE ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]STATUS : [FFFFFF]Sending Team Invite...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:

                                    V = await SEnd_InV(4, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                    await asyncio.sleep(0.3)

                                    # SUCCESS MESSAGE
                                    success_message = f"""
[B][C][00FFFF]✦ INVITE SENT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{target_uid}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    
                                except Exception as e:
                                    error_msg = f"""
[B][C][00FFFF]✦ INVITE ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/6")):
                            # Process /6 command - Create 4 player group
                            initial_message = f"""
[B][C][00FFFF]✦ 6-PLAYER GROUP ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]Creating group...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 4 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"""
[B][C][00FFFF]✦ GROUP CREATED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(uid)}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        # Add these lines to your existing command dispatcher:

                        if inPuTMsG.startswith('/spamroom ') or inPuTMsG == '/spamroom':
                            await handle_room_spam_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.startswith('/sr ') or inPuTMsG == '/sr':
                            await handle_sr_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.startswith('/title'):
                            await handle_all_titles_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                        # /sticker command removed



                                #GET PLAYER FAKE LIKE
                        # /fake_like command removed

                                #GET PLAYER SPAM
                        if inPuTMsG.strip().startswith('/spam_req'):
                            print('[ COMMAND ] Processing spam_req command')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ SPAM REQ COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/spam_req <uid>
[00FF00]EX 1   : [FFFFFF]/spam_req 14444444004
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"""
[B][C][00FFFF]✦ SPAM REQUEST ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]STATUS : [FFFFFF]Sending Spam Request...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                spam_result = spam_requests(target_uid)

                                await safe_send_message(response.Data.chat_type, spam_result, uid, chat_id, key, iv)



                                #GET PLAYER CHECK ID
                        if inPuTMsG.strip().startswith('/check'):
                            print('[ COMMAND ] Processing check command')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ CHECK COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/check <uid>
[00FF00]EX 1   : [FFFFFF]/check 14444444004
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"""
[B][C][00FFFF]✦ BAN STATUS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]STATUS : [FFFFFF]Checking Ban Status...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                ban_result = check_ban(target_uid)

                                await safe_send_message(response.Data.chat_type, ban_result, uid, chat_id, key, iv)


                        # Command handler for remove
                        if inPuTMsG.strip().startswith('/wlremove'):
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ WLREMOVE COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/wlremove (uid)
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
    
                            # Check owner
                            if str(response.Data.uid) != "537512413":
                                error_msg = f"""
[B][C][00FFFF]✦ PERMISSION DENIED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Only bot owner can remove from whitelist!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
                            
                            success, message = remove_from_whitelist(target_uid)
    
                            if success:
                                bot_uid = 13736023597
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                message_text = f"You Are Successfully Removed From Whitelist By {xMsGFixinG(uid)}"
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
                                result_msg = f"""
[B][C][00FFFF]✦ WHITELIST REMOVED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{message}
[00FF00]REMAIN : [FFFFFF]{len(WHITELISTED_UIDS)} UIDs
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            else:
                                result_msg = f"""
[B][C][00FFFF]✦ WHITELIST ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{message}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            
                            await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv)
                            
                        # Command to enable/disable whitelist only mode
                        if inPuTMsG.strip() == '/wlenable':
                            
                            WHITELIST_ONLY = True
                            msg = f"""
[B][C][00FFFF]✦ WHITELIST ENABLED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[00FF00]INFO   : [FFFFFF]Bot will only accept invites from whitelisted UIDs
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                        
                        if inPuTMsG.strip() == '/wldisable':

                            WHITELIST_ONLY = False
                            msg = f"""
[B][C][00FFFF]✦ WHITELIST DISABLED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[00FF00]INFO   : [FFFFFF]Bot will accept invites from anyone
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                            
                        # Add this command handler
                        if inPuTMsG.strip().startswith('/wladd'):
                            print('[ COMMAND ] Processing whitelist add command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ WLADD COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/wladd (uid) [note]
[00FF00]EX 1   : [FFFFFF]/wladd 123456789
[00FF00]EX 2   : [FFFFFF]/wladd 123456789 Friend
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
    
                            # Optional note
                            note = ""
                            if len(parts) > 2:
                                note = ' '.join(parts[2:])
    
                            # Check if sender is owner
                            if str(response.Data.uid) != "537512413":  # Replace with your actual UID
                                error_msg = f"""
[B][C][00FFFF]✦ PERMISSION DENIED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Only bot owner can add to whitelist!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Add to whitelist
                            success, message = append_to_whitelist(target_uid, note)
    
                            # Send result
                            if success:
                                bot_uid = 13736023597
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                message_text = f"You Are Successfully Added To Whitelist By {xMsGFixinG(uid)}"
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
        
                                if private_msg_packet and whisper_writer:
                                    # Send via Whisper connection (chat connection)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
                                success_msg = f"""
[B][C][00FFFF]✦ WHITELIST ADDED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]NOTE   : [FFFFFF]{note if note else 'None'}
[00FF00]TOTAL  : [FFFFFF]{len(WHITELISTED_UIDS)} UIDs
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            else:
                                success_msg = f"""
[B][C][00FFFF]✦ WHITELIST ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{message}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)    
                            
                        if inPuTMsG.strip() == '/wllist':
                            print('[ COMMAND ] Processing whitelist view command')
    
                            # Check if owner
                            if str(response.Data.uid) != "537512413":  # Your UID
                                error_msg = f"""
[B][C][00FFFF]✦ PERMISSION DENIED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Only bot owner can view whitelist!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Build whitelist message
                            total = len(WHITELISTED_UIDS)
    
                            whitelist_msg = f"""
[B][C][00FFFF]✦ WHITELIST INFO ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TOTAL  : [FFFFFF]{total} UIDs
[00FF00]ENABLED: [FFFFFF]{'YES' if WHITELIST_ONLY else 'NO'}
[00FF00]OWNER  : [FFFFFF]537512413
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
    
                            # Add first 20 UIDs (to avoid message too long)
                            count = 0
                            for uid in WHITELISTED_UIDS:
                                if uid != "537512413":  # Skip owner since already shown
                                    whitelist_msg += f"\n• {xMsGFixinG(uid)}"
                                    count += 1
                                    if count >= 20:
                                        remaining = total - 21  # -1 for owner, -20 shown
                                        if remaining > 0:
                                            whitelist_msg += f"\n... and {remaining} more"
                                        break
    
                            whitelist_msg += f"""

💡 Commands:
/wladd (uid) - Add to whitelist
/wlremove (uid) - Remove from whitelist
/wlenable - Enable whitelist only mode
/wldisable - Disable whitelist only mode
"""
    
                            await safe_send_message(response.Data.chat_type, whitelist_msg, uid, chat_id, key, iv)
                            

                        
                        # In your TcPChaT function, add this command handler:
                        if inPuTMsG.strip().startswith('/dm '):
                            print('[ COMMAND ] Processing private message command')
    
                            parts = inPuTMsG.strip().split(maxsplit=2)  # maxsplit=2 to keep message together
    
                            if len(parts) < 3:
                                error_msg = f"""
[B][C][00FFFF]✦ DM COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/dm (target_uid) (message)
[00FF00]EX 1   : [FFFFFF]/dm 123456789 Hello!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
                            message = parts[2]
                            message_text = f"[B]{message}"
                            
                            # Validate target UID
                            if not target_uid.isdigit() or len(target_uid) < 8:
                                error_msg = f"""
[B][C][00FFFF]✦ INVALID UID ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Invalid UID! Must be 8+ digits
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Validate message length
                            if len(message_text) > 100:
                                error_msg = f"""
[B][C][00FFFF]✦ MESSAGE ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Message too long! Max 100 characters
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Send initial confirmation
                            initial_msg = f"""
[B][C][00FFFF]✦ SENDING DM ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]MESSAGE: [FFFFFF]{message_text[:30]}...
[00FF00]STATUS : [FFFFFF]Sending...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
    
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
    
                            try:
                                # Get bot's UID from login data
                                bot_uid = 13777711848
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
        
                                if private_msg_packet and whisper_writer:
                                    # Send via Whisper connection (chat connection)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
            
                                    success_msg = f"""
[B][C][00FFFF]✦ DM SENT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]MESSAGE: [FFFFFF]{message_text}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    print(f"[ SUCCESS ] Private message sent to {xMsGFixinG(target_uid)}: {message_text}")
                                else:
                                    error_msg = f"""
[B][C][00FFFF]✦ DM ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Failed to create message packet!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
            
                            except Exception as e:
                                print(f"[ ERROR ] Private message error: {e}")
                                error_msg = f"""
[B][C][00FFFF]✦ DM ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)[:50]}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)



                        # Use the FINAL version
                        if inPuTMsG.strip().startswith('/kick'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ KICK COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/kick (uid)
[00FF00]EX 1   : [FFFFFF]/kick 123456789
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"""
[B][C][00FFFF]✦ KICKING PLAYER ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]STATUS : [FFFFFF]Kicking...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await KickTarget(target_uid, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(f"[ ERROR ] Kick error: {e}")

                                #GET PLAYER Add
                        if inPuTMsG.strip().startswith('/add'):
                            print('[ COMMAND ] Processing add command')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ ADD COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/add <uid>
[00FF00]EX 1   : [FFFFFF]/add 14444444004
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"""
[B][C][00FFFF]✦ ADDING FRIEND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]STATUS : [FFFFFF]Sending Requests...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                add_result = add_friend(target_uid)

                                await safe_send_message(response.Data.chat_type, add_result, uid, chat_id, key, iv)

                                #GET PLAYER REMOVE
                        if inPuTMsG.strip().startswith('/remove'):
                            print('[ COMMAND ] Processing remove command')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ REMOVE COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/remove <uid>
[00FF00]EX 1   : [FFFFFF]/remove 14444444004
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"""
[B][C][00FFFF]✦ REMOVING FRIEND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]STATUS : [FFFFFF]Removing Requests...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                remove_result = remove_friend(target_uid)

                                await safe_send_message(response.Data.chat_type, remove_result, uid, chat_id, key, iv)

                                    

                        if inPuTMsG.startswith(("/3")):
                            # Process /3 command - Create 3 player group
                            initial_message = f"""
[B][C][00FFFF]✦ 3-PLAYER GROUP ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]Creating group...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 6 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"""
[B][C][00FFFF]✦ GROUP CREATED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(uid)}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/4")):
                            # Process /3 command - Create 3 player group
                            initial_message = f"""
[B][C][00FFFF]✦ 4-PLAYER GROUP ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]Creating group...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 6 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(4, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(4, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"""
[B][C][00FFFF]✦ GROUP CREATED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(uid)}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        # In your TcPChaT function, look for the command handling section
                        # It might look something like this:

                        if inPuTMsG.startswith('/room '):
                            await handle_room_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)



                        if inPuTMsG.startswith(("/5")):
                            # Process /5 command in any chat type
                            initial_message = f"""
[B][C][00FFFF]✦ 5-PLAYER GROUP ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]Creating group...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)  # Reduced from 3 seconds
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"""
[B][C][00FFFF]✦ INVITATION SENT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(uid)}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)



                        # Add this with your other command handlers in the TcPChaT function
                        if inPuTMsG.strip().startswith('/multijoin'):
                            print('[ COMMAND ] Processing multi-account join request')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ MULTIJOIN COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/multijoin (uid)
[00FF00]EX 1   : [FFFFFF]/multijoin 123456789
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                if not target_uid.isdigit():
                                    error_msg = f"""
[B][C][00FFFF]✦ INVALID UID ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Please write a valid player ID!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                initial_msg = f"""
[B][C][00FFFF]✦ MULTIJOIN STARTED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]STATUS : [FFFFFF]Starting attack...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Try the fake multi-account method (more reliable)
                                    success_count, total_attempts = await real_multi_account_join(target_uid, key, iv, region)
            
                                    if success_count > 0:
                                        result_msg = f"""
[B][C][00FFFF]✦ MULTIJOIN COMPLETED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]SUCCESS: [FFFFFF]{success_count}
[00FF00]TOTAL  : [FFFFFF]{total_attempts}
[00FF00]INFO   : [FFFFFF]Check game for requests!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    else:
                                        result_msg = f"""
[B][C][00FFFF]✦ MULTIJOIN FAILED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]All join requests failed!
[00FF00]ACTION : [FFFFFF]Check bot connection.
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            
                                    await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    error_msg = f"""
[B][C][00FFFF]✦ MULTIJOIN ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)



                        # Update the command handler
                        if inPuTMsG.strip().startswith('/reject'):
                            print('[ COMMAND ] Processing reject spam command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ REJECT COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/reject (uid)
[00FF00]EX 1   : [FFFFFF]/reject 123456789
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Stop any existing reject spam
                                if reject_spam_task and not reject_spam_task.done():
                                    reject_spam_running = False
                                    reject_spam_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Send start message
                                start_msg = f"""
[B][C][00FFFF]✦ REJECT SPAM STARTED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]PACKETS: [FFFFFF]150 each type
[00FF00]DELAY  : [FFFFFF]0.2 seconds
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
        
                                # Start reject spam in background
                                reject_spam_running = True
                                reject_spam_task = asyncio.create_task(reject_spam_loop(target_uid, key, iv))
        
                                # Wait for completion in background and send completion message
                                asyncio.create_task(handle_reject_completion(reject_spam_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv))


                        if inPuTMsG.strip() == '/reject_stop':
                            if reject_spam_task and not reject_spam_task.done():
                                reject_spam_running = False
                                reject_spam_task.cancel()
                                stop_msg = f"""
[B][C][00FFFF]✦ REJECT SPAM STOPPED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, stop_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"""
[B][C][00FFFF]✦ REJECT SPAM ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]No active reject spam to stop!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                


                                    
                                                                                                     



                                                
                        # Add with other command handlers in TcPChaT                      
                                                                                          # FIXED JOIN COMMAND
                        if inPuTMsG.startswith('/join'):
                            # Process /join command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ JOIN COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/join (team_code)
[00FF00]EX 1   : [FFFFFF]/join ABC123
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                uid = response.Data.uid  # Get the UID of person who sent the command
        
                                initial_message = f"""
[B][C][00FFFF]✦ JOINING SQUAD ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]CODE   : [FFFFFF]{CodE}
[00FF00]STATUS : [FFFFFF]Joining...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
                                try:
                                    # Try using the regular join method first
                                    EM = await GenJoinSquadsPacket(CodE, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', EM)
            
                                    # Wait a bit for the join to complete
                                    await asyncio.sleep(2)
            
                                    # DUAL RINGS EMOTE - BOTH SENDER AND BOT
                                    try:
                                        await auto_rings_emote_dual(uid, key, iv, region)
                                    except Exception as emote_error:
                                        print(f"[ ERROR ] Dual emote failed but join succeeded: {emote_error}")
            
                                    # SUCCESS MESSAGE
                                    success_message = f"""
[B][C][00FFFF]✦ JOIN SUCCESS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]CODE   : [FFFFFF]{CodE}
[00FF00]STATUS : [FFFFFF]Joined squad!
[00FF00]INFO   : [FFFFFF]Dual Rings emote activated!
[00FF00]ACTION : [FFFFFF]Bot + You = 💕
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print(f"[ ERROR ] Regular join failed, trying ghost join: {e}")
                                    # If regular join fails, try ghost join
                                    try:
                                        # Get bot's UID from global context or login data
                                        bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                
                                        ghost_packet = await ghost_join_packet(bot_uid, CodE, key, iv)
                                        if ghost_packet:
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                    
                                            # Wait a bit for ghost join to complete
                                            await asyncio.sleep(2)
                    
                                            # DUAL RINGS EMOTE - BOTH SENDER AND BOT
                                            try:
                                                await auto_rings_emote_dual(uid, key, iv, region)
                                            except Exception as emote_error:
                                                print(f"[ ERROR ] Dual emote failed but ghost join succeeded: {emote_error}")
                    
                                            success_message = f"""
[B][C][00FFFF]✦ GHOST JOIN SUCCESS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]CODE   : [FFFFFF]{CodE}
[00FF00]STATUS : [FFFFFF]Ghost joined squad!
[00FF00]INFO   : [FFFFFF]Dual Rings emote activated!
[00FF00]ACTION : [FFFFFF]Bot + You = 💕
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                        else:
                                            error_msg = f"""
[B][C][00FFFF]✦ GHOST JOIN ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Failed to create ghost join packet.
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                    
                                    except Exception as ghost_error:
                                        print(f"[ ERROR ] Ghost join also failed: {ghost_error}")
                                        error_msg = f"""
[B][C][00FFFF]✦ JOIN ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(ghost_error)}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                
                
                        if inPuTMsG.strip().startswith('/ghost'):
                            # Process /ghost command in any chat type
                            print('[ COMMAND ] Processing ghost command')
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ GHOST COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/ghost (team_code)
[00FF00]EX 1   : [FFFFFF]/ghost ABC123
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                initial_message = f"""
[B][C][00FFFF]✦ GHOST JOINING ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]CODE   : [FFFFFF]{CodE}
[00FF00]STATUS : [FFFFFF]Ghost joining squad...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Get bot's UID from global context or login data
                                    bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                                    
                                    ghost_packet = await ghost_join_packet(bot_uid, CodE, key, iv)
                                    if ghost_packet:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                                        success_message = f"""
[B][C][00FFFF]✦ GHOST JOIN SUCCESS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]CODE   : [FFFFFF]{CodE}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                        await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    else:
                                        error_msg = f"""
[B][C][00FFFF]✦ GHOST JOIN ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Failed to create ghost join packet.
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        
                                except Exception as e:
                                    error_msg = f"""
[B][C][00FFFF]✦ GHOST JOIN ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)






                        if inPuTMsG.startswith('/exit'):
                            # Process /exit command in any chat type
                            initial_message = f"""
[B][C][00FFFF]✦ EXIT COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]Leaving current squad...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            leave = await ExiT(uid,key,iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , leave)
                            
                            # SUCCESS MESSAGE
                            success_message = f"""
[B][C][00FFFF]✦ EXIT SUCCESS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]Left the squad successfully!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)




                        

        



                        if inPuTMsG.strip().startswith('/e'):
                            print(f'[ COMMAND ] Processing emote command in chat type: {response.Data.chat_type}')
    
                            parts = inPuTMsG.strip().split()
    
                            # Check if user wants to list emotes or show help
                            if len(parts) == 1 or (len(parts) == 2 and parts[1].lower() == 'list'):
                                # Show available emotes
                                emote_list_msg = f"""
[B][C][00FFFF]✦ EMOTE SYSTEM ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATS  : [FFFFFF]1-{len(NUMBER_EMOTES)} numbers, {len(NAME_EMOTES)} names
[00FF00]USAGE 1: [FFFFFF]/e [number/name] (Self)
[00FF00]USAGE 2: [FFFFFF]/e [uid] [number/name] (Target)
[00FF00]USAGE 3: [FFFFFF]/e 9090xxxxx (Direct ID)
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        
                                popular_names = ["ak", "m60", "p90", "scar", "famas", "heart", "love", "dance", "hello", "money"]
                                line = ""
                                for name in popular_names:
                                    if name.lower() in NAME_EMOTES:
                                        line += f"[00FF00]{name}[FFFFFF], "
                                if line:
                                    emote_list_msg += "\n[00FF00]POPULAR: [FFFFFF]" + line.rstrip(", ")
        
                                emote_list_msg += f"""
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]EX 1   : [FFFFFF]/e ak
[00FF00]EX 2   : [FFFFFF]/e 123456789 heart
[00FF00]EX 3   : [FFFFFF]/e 123456789 1
[00FF00]EX 4   : [FFFFFF]/e ring
[00FF00]EX 5   : [FFFFFF]/e 909012345
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
        
                                await safe_send_message(response.Data.chat_type, emote_list_msg, uid, chat_id, key, iv)
                                continue
    
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ EMOTE COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/e [emote]
[00FF00]INFO   : [FFFFFF]Type /e list for help
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
    
                            initial_message = f"""
[B][C][00FFFF]✦ EMOTE SYSTEM ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]Preparing emote...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            target_uids = []
                            emote_key = None
    
                            try:
                                last_part = parts[-1].lower()
        
                                # Direct ID (9090xxxxx)
                                is_direct_id = last_part.isdigit() and len(last_part) == 9 and last_part.startswith("9090")
        
                                # Old checks
                                is_number = last_part.isdigit() and last_part in NUMBER_EMOTES
                                is_name = last_part in NAME_EMOTES
        
                                if is_direct_id or is_number or is_name:
                                    if len(parts) == 2:
                                        emote_key = last_part
                                        target_uids.append(int(response.Data.uid))
            
                                    elif len(parts) == 3:
                                        target_uids.append(int(parts[1]))
                                        emote_key = last_part
            
                                    else:
                                        for i in range(1, len(parts) - 1):
                                            target_uids.append(int(parts[i]))
                                        emote_key = last_part
                                else:
                                    error_msg = f"""
[B][C][00FFFF]✦ EMOTE ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Invalid emote: '{last_part}'
[00FF00]ACTION : [FFFFFF]Use number, name or 9090xxxxx ID
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
        
                                emote_id = None
                                emote_name_display = None
        
                                if is_direct_id:
                                    emote_id = int(emote_key)
                                    emote_name_display = f"ID:{emote_key}"
        
                                elif is_number:
                                    emote_id = NUMBER_EMOTES.get(emote_key)
                                    emote_name_display = f"#{emote_key}"
        
                                else:
                                    emote_id = NAME_EMOTES.get(emote_key)
                                    emote_name_display = emote_key
        
                                if not emote_id:
                                    error_msg = f"""
[B][C][00FFFF]✦ EMOTE ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Emote not found!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
        
                                success_count = 0
                                failed_uids = []
        
                                for target_uid in target_uids:
                                    try:
                                        H = await Emote_k(target_uid, int(emote_id), key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        success_count += 1
                                        await asyncio.sleep(0.1)
                                    except Exception as e:
                                        failed_uids.append(str(target_uid))
        
                                success_msg = f"""
[B][C][00FFFF]✦ EMOTE SENT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]EMOTE  : [FFFFFF]{emote_name_display}
[00FF00]SUCCESS: [FFFFFF]{success_count}/{len(target_uids)}
"""
        
                                if failed_uids:
                                    success_msg += f"[00FF00]FAILED : [FFFFFF]{', '.join(failed_uids)}\n"
                                
                                success_msg += "[FFFFFF]━━━━━━━━━━━━━━━━━━"
        
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    
                            except:
                                error_msg = f"""
[B][C][00FFFF]✦ EMOTE ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Invalid format!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)




# GLOBAL BLOCKED NAMES
                        BLOCKED_NAMES = ["maruf", "mg24", "mg-king", "mg_king", "mgking", "mg king"]  # Protected names

                        # GALi / JOKE MESSAGE
  


                        # Fast emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/fast'):
                            print('[ COMMAND ] Processing fast emote spam command')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"""
[B][C][00FFFF]✦ FAST COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/fast uid1 [uid2] [uid3] [uid4] emoteid
[00FF00]EX 1   : [FFFFFF]/fast 123456789 909000001
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and emoteid
                                uids = []
                                emote_id = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) > 3:  # Assuming UIDs are longer than 3 digits
                                            uids.append(part)
                                        else:
                                            emote_id = part
                                    else:
                                        break
                                
                                if not emote_id and parts[-1].isdigit():
                                    emote_id = parts[-1]
                                
                                if not uids or not emote_id:
                                    error_msg = f"""
[B][C][00FFFF]✦ FAST ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Invalid format!
[00FF00]USAGE  : [FFFFFF]/fast uid1 [uid2] [uid3] [uid4] emoteid
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    # Stop any existing fast spam
                                    if fast_spam_task and not fast_spam_task.done():
                                        fast_spam_running = False
                                        fast_spam_task.cancel()
                                    
                                    # Start new fast spam
                                    fast_spam_running = True
                                    fast_spam_task = asyncio.create_task(fast_emote_spam(uids, emote_id, key, iv, region))
                                    
                                    # SUCCESS MESSAGE
                                    success_msg = f"""
[B][C][00FFFF]✦ FAST SPAM STARTED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGETS: [FFFFFF]{len(uids)} players
[00FF00]EMOTE  : [FFFFFF]{emote_id}
[00FF00]TIMES  : [FFFFFF]25 times
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # Custom emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/p'):
                            print('[ COMMAND ] Processing custom emote spam command')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 4:
                                error_msg = f"""
[B][C][00FFFF]✦ P COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/p (uid) (emote_id) (times)
[00FF00]EX 1   : [FFFFFF]/p 123456789 909000001 10
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    target_uid = parts[1]
                                    emote_id = parts[2]
                                    times = int(parts[3])
                                    
                                    if times <= 0:
                                        error_msg = f"""
[B][C][00FFFF]✦ P ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Times must be greater than 0!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    elif times > 1000:
                                        error_msg = f"""
[B][C][00FFFF]✦ P ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Maximum 1000 times allowed for safety!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        # Stop any existing custom spam
                                        if custom_spam_task and not custom_spam_task.done():
                                            custom_spam_running = False
                                            custom_spam_task.cancel()
                                         
                                        
                                        # Start new custom spam
                                        custom_spam_running = True
                                        custom_spam_task = asyncio.create_task(custom_emote_spam(target_uid, emote_id, times, key, iv, region))
                                        
                                        # SUCCESS MESSAGE
                                        success_msg = f"""
[B][C][00FFFF]✦ CUSTOM SPAM STARTED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]EMOTE  : [FFFFFF]{emote_id}
[00FF00]TIMES  : [FFFFFF]{times}
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        
                                except ValueError:
                                    error_msg = f"""
[B][C][00FFFF]✦ P ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Invalid number format!
[00FF00]USAGE  : [FFFFFF]/p (uid) (emote_id) (times)
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"""
[B][C][00FFFF]✦ P ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                        # Spam request command - works in all chat types
                        # Spam request command - works in all chat types
                        if inPuTMsG.strip().startswith('/spam '):
                            print('[ COMMAND ] Processing spam request command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ SPAM COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/spam (uid)
[00FF00]EX 1   : [FFFFFF]/spam 123456789
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                if not target_uid.isdigit():
                                    error_msg = f"""
[B][C][00FFFF]✦ INVALID UID ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Please write a valid player ID!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                # Send initial message
                                initial_msg = f"""
[B][C][00FFFF]✦ SPAM STARTED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]STATUS : [FFFFFF]Loading accounts...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                # Check if accounts file exists
                                try:
                                    import os
                                    if not os.path.exists("vv.json"):
                                        error_msg = f"""
[B][C][00FFFF]✦ SPAM ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]vv.json file not found!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        return
                                except:
                                    pass
        
                                try:
                                    # Execute spam
                                    success_count, total_accounts = await multi_account_spam_request(target_uid, key, iv, region)
            
                                    if success_count > 0:
                                        result_msg = f"""
[B][C][00FFFF]✦ SPAM COMPLETED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]SUCCESS: [FFFFFF]{success_count}
[00FF00]TOTAL  : [FFFFFF]{total_accounts}
[00FF00]RATE   : [FFFFFF]{(success_count/total_accounts*100):.1f}%
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    else:
                                        result_msg = f"""
[B][C][00FFFF]✦ SPAM FAILED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]ACCOUNTS: [FFFFFF]{total_accounts}
[00FF00]INFO   : [FFFFFF]All requests failed!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
            
                                    await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print(f"[ ERROR ] Spam command error: {e}")
                                    import traceback
                                    traceback.print_exc()
                                    error_msg = f"""
[B][C][00FFFF]✦ SPAM ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)[:50]}...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)      

                        # Spam request command - works in all chat types
                        if inPuTMsG.strip().startswith('/spm_inv'):
                            print('[ COMMAND ] Processing spam invite with cosmetics')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ SPM_INV COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/spm_inv (uid)
[00FF00]EX 1   : [FFFFFF]/spm_inv 123456789
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Stop any existing spam request
                                if spam_request_task and not spam_request_task.done():
                                    spam_request_running = False
                                    spam_request_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Start new spam request WITH COSMETICS
                                spam_request_running = True
                                spam_request_task = asyncio.create_task(spam_request_loop_with_cosmetics(target_uid, key, iv, region))
        
                                # SUCCESS MESSAGE
                                success_msg = f"""
[B][C][00FFFF]✦ COSMETIC SPAM ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]REQUESTS: [FFFFFF]30
[00FF00]FEATURES: [FFFFFF]V-Badges + Cosmetics
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # Stop spam request command - works in all chat types
                        if inPuTMsG.strip() == '/stop spm_inv':
                            if spam_request_task and not spam_request_task.done():
                                spam_request_running = False
                                spam_request_task.cancel()
                                success_msg = f"""
[B][C][00FFFF]✦ SPAM STOPPED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"""
[B][C][00FFFF]✦ SPAM ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]No active spam request to stop!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

# In TcPChaT function, update /status command:
                        if inPuTMsG.strip().startswith('/status '):
                            print('[ COMMAND ] Processing status command')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ STATUS COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/status (player_uid)
[00FF00]EX 1   : [FFFFFF]/status 123456789
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return

                            target_uid = parts[1]

                            initial_msg = f"""
[B][C][00FFFF]✦ STATUS CHECK ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGET : [FFFFFF]{xMsGFixinG(target_uid)}
[00FF00]STATUS : [FFFFFF]Checking status...
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)

                            # Get player name
                            player_name = "Unknown"
                            try:
                                import requests
                                info_url = f"https://mg24-gamer-king.vercel.app/info/get?uid={target_uid}"
                                info_res = requests.get(info_url, timeout=5)

                                if info_res.status_code == 200:
                                    info_data = info_res.json()
                                    player_name = info_data.get("AccountInfo", {}).get("AccountName", "Unknown")

                            except Exception as e:
                                print(f"[ WARNING ] Could not fetch player name: {e}")

                            print(f"[ DATA ] Player Name: {player_name}")

                            print(f"\n[ SYSTEM ] BEFORE clearing cache:")
                            debug_file_cache()

                            clear_cache_entry(target_uid)

                            try:

                                status_packet = await createpacketinfo(target_uid, key, iv)

                                if not status_packet:
                                    error_msg = f"""
[B][C][00FFFF]✦ STATUS ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Failed to create status packet!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return

                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', status_packet)

                                print(f"[ NETWORK ] Sent status request for {xMsGFixinG(target_uid)}")

                                max_retries = 12
                                response_received = False

                                for attempt in range(max_retries):

                                    print(f"[ SYSTEM ] Checking file cache... attempt {attempt + 1}/{max_retries}")

                                    cache_data = load_from_cache(target_uid)

                                    if cache_data:

                                        print(f"[ SUCCESS ] FOUND in file cache! Status: {cache_data['status']}")
                                        response_received = True

                                        print(f"[ DATA ] Cache data keys: {list(cache_data.keys())}")

                                        status_msg = f"""
[B][C][00FFFF]✦ PLAYER STATUS ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]NAME   : [FFFFFF]{player_name}
[00FF00]UID    : [FFFFFF]{fix_num(target_uid)}
[00FF00]STATUS : [FFFFFF]{cache_data['status']}
"""

                                        if "IN ROOM" in cache_data['status']:

                                            if 'room_id' in cache_data:

                                                status_msg += f"[00FF00]ROOM ID: [FFFFFF]{fix_num(cache_data['room_id'])}\n"
                                                status_msg += f"[00FF00]ACTION : [FFFFFF]Use: /roomspam {xMsGFixinG(target_uid)}\n"

                                                room_id_msg = f"{fix_num(cache_data['room_id'])}"
                                                await safe_send_message(response.Data.chat_type, room_id_msg, uid, chat_id, key, iv)

                                            else:
                                                status_msg += f"[00FF00]ROOM ID: [FFFFFF]Not available\n"

                                        elif "INSQUAD" in cache_data['status']:

                                            if 'leader_id' in cache_data:

                                                leader_uid = cache_data['leader_id']
                                                leader_name = "Unknown"

                                                try:
                                                    leader_api = f"https://mg24-gamer-king.vercel.app/info/get?uid={leader_uid}"
                                                    leader_res = requests.get(leader_api, timeout=5)

                                                    if leader_res.status_code == 200:
                                                        leader_data = leader_res.json()
                                                        leader_name = leader_data.get("AccountInfo", {}).get("AccountName", "Unknown")

                                                except Exception as e:
                                                    print(f"[ WARNING ] Could not fetch leader name: {e}")

                                                status_msg += f"[00FF00]LEADER UID: [FFFFFF]{fix_num(leader_uid)}\n"
                                                status_msg += f"[00FF00]LEADER NAME: [FFFFFF]{leader_name}\n"

                                            try:

                                                if 'parsed_json' in cache_data:

                                                    parsed = cache_data['parsed_json']

                                                    if '5' in parsed and 'data' in parsed['5']:

                                                        squad_data = parsed['5']['data']['1']['data']

                                                        if '9' in squad_data and 'data' in squad_data['9']:

                                                            members = squad_data['9']['data']
                                                            max_members = squad_data['10']['data'] + 1

                                                            status_msg += f"[00FF00]SQUAD: [FFFFFF]{members}/{max_members}\n"

                                            except:
                                                pass

                                        elif "OFFLINE" in cache_data['status']:
                                            status_msg += f"[00FF00]INFO   : [FFFFFF]Player is offline\n"

                                        elif "INGAME" in cache_data['status']:
                                            status_msg += f"[00FF00]INFO   : [FFFFFF]Player is in a match\n"

                                        elif "SOLO" in cache_data['status']:
                                            status_msg += f"[00FF00]INFO   : [FFFFFF]Player is solo\n"

                                        status_msg += f"[FFFFFF]━━━━━━━━━━━━━━━━━━"

                                        await safe_send_message(response.Data.chat_type, status_msg, uid, chat_id, key, iv)

                                        print(f"\n[ SUCCESS ] AFTER successful response:")
                                        debug_file_cache()

                                        break

                                    await asyncio.sleep(0.5)

                                if not response_received:

                                    print(f"\n[ ERROR ] FAILED after {max_retries} tries")
                                    debug_file_cache()

                                    error_msg = f"""
[B][C][00FFFF]✦ STATUS ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]UID    : [FFFFFF]{fix_num(target_uid)}
[00FF00]INFO   : [FFFFFF]No response from server
[00FF00]ACTION : [FFFFFF]Try again in 10 seconds
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()

                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                            except Exception as e:

                                print(f"[ ERROR ] Status command error: {e}")

                                import traceback
                                traceback.print_exc()

                                error_msg = f"""
[B][C][00FFFF]✦ STATUS ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]{str(e)[:50]}
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/evo_fast '):
                            print('[ COMMAND ] Processing evo_fast command')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""
[B][C][00FFFF]✦ EVO FAST COMMAND ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]USAGE  : [FFFFFF]/evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)
[00FF00]EX 1   : [FFFFFF]/evo_fast 123456789 1
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"""
[B][C][00FFFF]✦ EVO FAST ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Invalid format!
[00FF00]USAGE  : [FFFFFF]/evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"""
[B][C][00FFFF]✦ EVO FAST ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Number must be between 1-21 only!
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            # Stop any existing evo_fast spam
                                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                                evo_fast_spam_running = False
                                                evo_fast_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_fast spam
                                            evo_fast_spam_running = True
                                            evo_fast_spam_task = asyncio.create_task(evo_fast_emote_spam(uids, number_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"""
[B][C][00FFFF]✦ EVO FAST STARTED ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]TARGETS: [FFFFFF]{len(uids)} players
[00FF00]EMOTE  : [FFFFFF]{number_int} (ID: {emote_id})
[00FF00]TIMES  : [FFFFFF]25 times
[00FF00]STATUS : [FFFFFF]SUCCESS ✅
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"""
[B][C][00FFFF]✦ EVO FAST ERROR ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]INFO   : [FFFFFF]Invalid number format! Use 1-21 only.
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)



                            
                        #==================≈===========  /HELP MENU COMMANDS ========================================
                        if inPuTMsG.strip().lower() in ("help", "/help", "menu", "/menu", "hi"):

                            # -------- ইউজারের নাম (NAME_DISPLAY_ENABLED অনুযায়ী) --------
                            player_name = "User"
                            if NAME_DISPLAY_ENABLED:
                                try:
                                    if str(uid) in PLAYER_NAME_CACHE:
                                        player_name = PLAYER_NAME_CACHE[str(uid)]
                                    else:
                                        # লোকাল Like API কল (পোর্ট 5017)
                                        url = f"http://127.0.0.1:5017/like?uid={uid}&server_name=bd"
                                        async with aiohttp.ClientSession() as session:
                                            async with session.get(url, timeout=5) as resp:
                                                if resp.status == 200:
                                                    data = await resp.json()
                                                    name = data.get('PlayerNickname')
                                                    if name:
                                                        player_name = name
                                                        PLAYER_NAME_CACHE[str(uid)] = name
                                                else:
                                                    print(f"[ WARNING ] Local API status: {resp.status}")
                                except Exception as e:
                                    print(f"[ WARNING ] Name fetch error: {e}")
                            # else: "User" ই থাকবে

                            # Header with player name
                            header = f"""
[B][C][00FFFF]✦ GOD BLAZE BOT ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]Hey {player_name}
[00FFFF]Welcome To God Blaze's BOT
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, header, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── Commands 1-10 ─────
                            help_1 = """
[B][C][00FFFF]✦ COMMANDS 1-10 ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]01. Equip Bundle [00FF00]/bundle [name]
[00FF00]02. Freeze Spam [00FF00]/freeze [uid]
[00FF00]03. Change Bio [00CCFF]/bio [text]
[00FF00]04. Quick Attack [00FF00]/quick [tc] [emote]
[00FF00]05. Player Invite [00CCFF]/inv [uid]
[00FF00]06. Spam Friend Req [00FF00]/spam_req [uid]
[00FF00]07. Check Player [FFFF00]/check [uid]
[00FF00]08. Add Whitelist [00CCFF]/wladd [uid]
[00FF00]09. View Whitelist [FFFF00]/wllist
[00FF00]10. Private Msg [FF0000]/dm [uid] [msg]
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, help_1, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── Commands 11-20 ─────
                            help_2 = """
[B][C][00FFFF]✦ COMMANDS 11-20 ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]11. Kick Player [FF6600]/kick [uid]
[00FF00]12. Add Friend [00FF00]/add [uid]
[00FF00]13. Remove Friend [FF00FF]/remove [uid]
[00FF00]14. Multi Join [00FF00]/multijoin [tc] [count]
[00FF00]15. Reject Spam [FFFFFF]/reject [uid]
[00FF00]16. Ghost Join [FFCC00]/ghost [tc]
[00FF00]17. Play Emote [FF0000]/e [uid] [emote]
[00FF00]18. Fast Emote [00FF00]/fast [uid] [emote]
[00FF00]19. Custom Emote [FF00FF]/p [uid] [emote] [count]
[00FF00]20. Spam Request [00CCFF]/spam [uid]
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, help_2, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # ───── Commands 21-23 ─────
                            help_3 = """
[B][C][00FFFF]✦ COMMANDS 21-23 ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]21. Spam Invite [00FFFF]/spm_inv [uid]
[00FF00]22. Player Status [00FF00]/status [uid]
[00FF00]23. Fast Evo Spam [00CCFF]/evo_fast [uid] [1-21]
[FFFFFF]━━━━━━━━━━━━━━━━━━
""".strip()
                            await safe_send_message(response.Data.chat_type, help_3, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            # Footer
                            footer = """[B][C][00FFFF]✦ BOT INFO ✦
[FFFFFF]━━━━━━━━━━━━━━━━━━
[00FF00]Developer    :: [FF1493]God Blaze
[00FF00]Status       :: [32CD32]ONLINE
[00FF00]Version      :: [1E90FF]ENHANCED V2
[FFFFFF]━━━━━━━━━━━━━━━━━━"""

                            await safe_send_message(response.Data.chat_type, footer, uid, chat_id, key, iv)
                        response = None

                            
            whisper_writer.close() ; await whisper_writer.wait_closed() ; whisper_writer = None
                    
                    	
                    	
        except Exception as e: print(f"ErroR {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)

async def MaiiiinE():
    # Load credentials from file
    print("[ SYSTEM ] Loading credentials from God_Blaze.txt...")
    credentials = load_credentials_from_file("God_Blaze.txt")
    
    if not credentials:
        print("[ ERROR ] Failed to load credentials!")
        print("[ INFO ] Please create God_Blaze.txt with your UID and password")
        print("[ INFO ] Format: uid=YOUR_UID,password=YOUR_PASSWORD")
        return None
    
    try:
        Uid, Pw = credentials
    except:
        # Handle case where credentials returns more than 2 values
        if isinstance(credentials, (list, tuple)) and len(credentials) >= 2:
            Uid = credentials[0]
            Pw = credentials[1]
        else:
            print("[ ERROR ] Invalid credentials format!")
            return None
    
    print("[ SUCCESS ] Credentials loaded successfully")
    
    # Get access token from Free Fire
    open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
    if not open_id or not access_token: 
        print("[ ERROR ] Could not authenticate (Rate limit or invalid credentials)")
        print("[ INFO ] If you see 429 errors, the API is rate limiting you. Wait a few minutes.")
        return None
    
    # Encrypt and send login request
    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE: 
        print("[ ERROR ] Target Account => Banned / Not Registered!") 
        return None
    
    # Decrypt login response
    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    
    # Get JWT token from response
    token = MajoRLoGinauTh.token
    if not token:
        print("[ ERROR ] No authentication token received!")
        return None
    
    # ✅ CRITICAL: SAVE TOKEN TO token.json FILE
    try:
        import json
        import time
        from datetime import datetime
        
        # Get region from login response
        region = getattr(MajoRLoGinauTh, 'region', 'IND')
        
        token_data = {
            "token": token,
            "saved_at": time.time(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "bot_uid": str(Uid),
            "region": region,
            "source": "main.py_bot_login"
        }
        
        with open("/tmp/token.json", "w") as f:
            json.dump(token_data, f, indent=2)
        
        print("[ SUCCESS ] Token saved to /tmp/token.json")
        print(f"[ DATA ] Token info: Region={region}, UID={Uid}")
        
    except Exception as e:
        print(f"[ WARNING ] Could not save token to file: {e}")
        import traceback
        traceback.print_exc()
    
    # Continue with normal bot setup
    UrL = MajoRLoGinauTh.url
    
    # Clear screen and show status
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("[ SYSTEM ] God Blaze BOT - INITIALIZING")
    print("=" * 50)
    print("[ SYSTEM ] Starting TCP Connections...")
    print("[ NETWORK ] Connecting to Free Fire servers...")
    print("[ SUCCESS ] Server connection established")
    
    region = getattr(MajoRLoGinauTh, 'region', 'IND')
    ToKen = token  # Use the saved token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp
    
    print(f"[ SUCCESS ] Authentication successful")
    print(f"[ DATA ] Account UID: {TarGeT}")
    print(f"[ DATA ] Region: {region}")
    print(f"[ DATA ] Token: {ToKen[:30]}...")
    
    # Get login data for server IPs
    LoGinDaTa = await GetLoginData(UrL, PyL, ToKen)
    if not LoGinDaTa: 
        print("[ ERROR ] Getting Ports From Login Data!") 
        return None
    
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    
    # Get server IPs and ports
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    
    print(f"[ NETWORK ] Online Server: {OnLinePorTs}")
    print(f"[ NETWORK ] Chat Server: {ChaTPorTs}")
    
    # Split IPs and ports (use rsplit to handle IPv6 addresses)
    OnLineiP, OnLineporT = OnLinePorTs.rsplit(":", 1)
    ChaTiP, ChaTporT = ChaTPorTs.rsplit(":", 1)
    
    # Get account name
    acc_name = LoGinDaTaUncRypTinG.AccountName
    print(f"[ SUCCESS ] Welcome, {acc_name}!")
    
    # Create authentication token for TCP connections
    AutHToKen = await xAuThSTarTuP(int(TarGeT), ToKen, int(timestamp), key, iv)
    
    # Create event for chat ready
    ready_event = asyncio.Event()
    
    # Start bot tasks
    print("\n[ SYSTEM ] Starting bot services...")
    
    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region))
    task2 = asyncio.create_task(TcPOnLine(OnLineiP, OnLineporT, key, iv, AutHToKen))  
 
    
    # Show loading animation
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[ SYSTEM ] God Blaze BOT - STARTING")
    print("=" * 50)
    
    for i in range(1, 4):
        dots = "." * i
        print(f"[ SYSTEM ] Loading{dots}")
        time.sleep(0.3)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[ SYSTEM ] God Blaze BOT - CONNECTING")
    print("=" * 50)
    print("┌────────────────────────────────────┐")
    print("│ ██████████████████████████████████ │")
    print("└────────────────────────────────────┘")
    
    # Wait for chat connection to be ready
    print("\n[ SYSTEM ] Waiting for chat connection...")
    try:
        await asyncio.wait_for(ready_event.wait(), timeout=10)
        print("[ SUCCESS ] Chat connection established!")
    except asyncio.TimeoutError:
        print("[ WARNING ] Chat connection timeout, continuing...")
    
    # Final status display
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("[ SYSTEM ] God Blaze BOT - ONLINE")
    print("=" * 50)
    print(f"[ DATA ] UID: {TarGeT}")
    print(f"[ DATA ] Name: {acc_name}")
    print(f"[ DATA ] Region: {region}")
    print(f"[ DATA ] Status: READY")
    print(f"[ DATA ] Chat Server: {ChaTiP}:{ChaTporT}")
    print(f"[ DATA ] Online Server: {OnLineiP}:{OnLineporT}")
    print("=" * 50)
    print("[ INFO ] Commands available in squad/guild chat")
    print("[ INFO ] Type /help for command list")
    print("=" * 50)
    
    # Test cache file write
    print("\n[ SYSTEM ] System Check:")
    print(f"[ DATA ] Working directory: {os.getcwd()}")
    print(f"[ DATA ] Cache file: {CACHE_FILE}")
    
    try:
        test_data = {'test': 'ok', 'timestamp': time.time()}
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump(test_data, f)
        print("[ SUCCESS ] Cache file write test: PASSED")
    except Exception as e:
        print(f"[ WARNING ] Cache file write test: {e}")
    
    # Check token.json exists
    if os.path.exists("/tmp/token.json"):
        print("[ SUCCESS ] /tmp/token.json file exists")
        try:
            with open("/tmp/token.json", "r") as f:
                token_info = json.load(f)
            age = time.time() - token_info.get('saved_at', 0)
            print(f"[ SUCCESS ] Token age: {age:.1f} seconds")
        except:
            print("[ WARNING ] Could not read /tmp/token.json")
    else:
        print("[ ERROR ] /tmp/token.json not found!")
    
    print("\n[ SYSTEM ] Bot is now running...")
    print("[ NETWORK ] Listening for commands and invitations")
    
    # Keep all tasks running
    try:
        await asyncio.gather(task1, task2)
    except asyncio.CancelledError:
        print("\n[ SYSTEM ] Bot tasks cancelled")
    except Exception as e:
        print(f"\n[ ERROR ] Error in bot tasks: {e}")
        import traceback
        traceback.print_exc()
    
    return None


if __name__ == '__main__':
    # সব এপিআই সার্ভার ব্যাকগ্রাউন্ডে চালু করুন
    api_processes = start_api_servers()
    try:
        asyncio.run(StarTinG())
    finally:
        # বট বন্ধ হলে এপিআই সার্ভারগুলোও বন্ধ করুন
        for proc in api_processes:
            proc.terminate()
    
  
