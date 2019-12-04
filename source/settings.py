run_folder = './run/'
run_archive_folder = './run_archive/'

EPISODES = 10

start_points = [1000, 1000]

# Graph settings

# Value network settings
VALUE_HIDDEN_LAYERS_QUANTITY = 3
VALUE_NEURONS_QUANTITY = 100
VALUE_BATCH_SIZE = 1000
VALUE_ITERATIONS = 100
VALUE_DATASET_SIZE = 10000
VALUE_EPOCHS=10

# Policy network settings
POLICY_HIDDEN_LAYERS_QUANTITY = 7
POLICY_NEURONS_QUANTITY = 500
