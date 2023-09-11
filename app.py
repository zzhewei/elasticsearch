from main import create_app

# if it needs test change controller to test
blueprints = [
    "main.controller:v1",
]
# need test change development to testing
app = create_app("development", blueprints)
