DEFAULT_PORT = 9080
NODE_ID_PROPERTY_KEY = 'node_id'
OWNER_PROPERTY_KEY = 'owner'
BUSINESS_PROPERTY_KEY = 'business'
LOCATION_PROPERTY_KEY = 'deploy_location'
INBOUND_TIMEOUT = 30  # seconds

RECORD = 'record'
VERIFICATION_RECORD = 'verification_record'
VERIFICATION_INFO = 'verification_info'

PHASE_1_NODE = 0b00001
PHASE_2_NODE = 0b00010
PHASE_3_NODE = 0b00100
PHASE_4_NODE = 0b01000
PHASE_5_NODE = 0b10000

DATABASE_NAME = os.environ.get('BLOCKCHAIN_DB_NAME')

CONFIG_FILE = '../configs/' + DATABASE_NAME + '.yml'

LOG_FILE = '../logs/' + DATABASE_NAME + '.log'


VALID_TXS = 'valid_txs'
INVALID_TXS = 'invalid_txs'
BUSINESS = 'business'
DEPLOY_LOCATION = 'deploy_location'

LOWER_PHASE_HASHES = 'lower_phase_hashes'
P2_COUNT = 'p2_count'
BUSINESS_LIST = 'business_list'
DEPLOY_LOCATION_LIST = 'deploy_location_list'

netNODE_ID = "node_id"
netHOST = "host"
netTWDC = "TWDC"
netPORT = "port"
netNODE_OWNER = "node_owner"
netPHASES = "phases"

#####################EOF##############################