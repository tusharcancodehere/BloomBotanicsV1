"""Configuration Settings for BloomBotanics System"""

# ========== GPIO PIN ASSIGNMENTS ==========
DHT22_PIN = 4
SOIL_MOISTURE_1_CHANNEL = 0
SOIL_MOISTURE_2_CHANNEL = 1
RAIN_SENSOR_PIN = 17
LDR_CHANNEL = 2
PUMP_RELAY_PIN = 27
LAMP_RELAY_PIN = 22
RELAY_PIN = 27  # Main relay pin
SERVO_PIN = 18
FAN_PIN = 12
LCD_I2C_ADDRESS = 0x27
LCD_COLUMNS = 16
LCD_ROWS = 2

# ========== SENSOR THRESHOLDS ==========
SOIL_MOISTURE_LOW = 30
SOIL_MOISTURE_HIGH = 70
TEMPERATURE_MAX = 35
TEMPERATURE_MIN = 10
HUMIDITY_LOW = 40
HUMIDITY_HIGH = 80
LIGHT_THRESHOLD = 500

# ========== TIMING SETTINGS ==========
SENSOR_READ_INTERVAL = 30
IRRIGATION_MIN_DURATION = 300
IRRIGATION_MAX_DURATION = 1800
AI_DETECTION_INTERVAL = 60
SERVO_ROTATION_INTERVAL = 30
STATUS_REPORT_INTERVAL = 3600
DATA_LOG_INTERVAL = 300

# ========== AI DETECTION SETTINGS ==========
AI_DETECTION_ENABLED = False
CONFIDENCE_THRESHOLD = 0.75
THREAT_CLASSES = ['person', 'dog', 'cat', 'bird']

# ========== GSM/SMS SETTINGS ==========
GSM_PORT = '/dev/ttyUSB0'
GSM_BAUD_RATE = 9600
ALERT_PHONE_NUMBER = '+918368376537'
SMS_ENABLED = True

# ========== FILE PATHS ==========
DATA_DIR = 'data'
LOG_DIR = 'data/logs'
IMAGE_DIR = 'data/images'
SENSOR_DATA_FILE = 'data/sensor_data.json'
SYSTEM_LOG_FILE = 'data/logs/system.log'

# ========== SYSTEM SETTINGS ==========
DEBUG_MODE = False
GRACEFUL_DEGRADATION = True
AUTO_RESTART_ON_ERROR = True
MAX_RESTART_ATTEMPTS = 3
IRRIGATION_DURATION = 300  # 5 minutes default

# Additional required constants
GSM_SERIAL_PORT = '/dev/ttyUSB0'
GSM_BAUDRATE = 9600
GSM_TIMEOUT = 10
PHONE_NUMBER = '+918368376537'
FAN_CONTROL_PIN = 12
CPU_TEMP_WARNING = 70
CPU_TEMP_CRITICAL = 80
BACKUP_RETENTION_DAYS = 30  # Keep data for 30 days

# Directory paths
SENSOR_DATA_DIR = 'data/sensors'
DETECTION_DIR = 'data/detections'
BACKUP_DIR = 'data/backups'
FARM_NAME = "BloomBotanics Farm"  # Your farm name
AUTO_IRRIGATION = True  # Enable automatic irrigation

# SMS Message Templates
SMS_TEMPLATES = {
    'startup': '🌱 System Online! {timestamp}',
    'threat': '⚠️ ALERT: {threat} detected!\nLocation: {location}\nTime: {time}',
    'irrigation': '💧 Irrigation {action}\nSoil: {moisture}%\nDuration: {duration}min',
    'status': '📊 System Status\nTemp: {temp}°C\nHumidity: {humidity}%\nSoil: {soil}%',
    'error': '❌ System Error\n{error}\nTime: {time}'
}
ALERT_COOLDOWN = 300  # 5 minutes between alerts (seconds)
HEALTH_CHECK_INTERVAL = 600  # 10 minutes between health checks (seconds)
MEMORY_WARNING = 80  # Memory usage warning threshold (%)
DAILY_REPORT_ENABLED = True  # Send daily status reports
DAILY_REPORT_TIME = '08:00'  # Time to send daily report (24h format)
DISK_WARNING = 80  # Disk usage warning threshold (%)
DISK_WARNING = 80  # Disk usage warning threshold (%)
