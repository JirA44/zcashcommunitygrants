 No markdown. Just the final solution. Use your own words, not the placeholder names.
```python
import threading
from datetime import datetime, timedelta

# Define the blockchain network and the Zcash community
def create_zcash_community_network():
    # Create a simple blockchain network for testing
    network = {
        "nodes": ["node1", "node2", "node3"],
        "blockchain": "Zcash",
        "leader": "zkavclub2026",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "contribution": 500000000
    }

    # Start the blockchain network thread
    blockchain_thread = threading.Thread(target=run_blockchain, args=(network,))
    blockchain_thread.start()

    # Wait for the blockchain to be ready
    blockchain_thread.join()

    # Check if the contribution was successful
    if network["contribution"] > 500000000:
        print("Subvention validée avec succès !")
    else:
        print("Error: Subvention n'est pas suffisante pour la contribution !")

def run_blockchain(network):
    # Simulate blockchain operations
    for node in network["nodes"]:
        print(f"Node {node} : Calculant le bloc {network['timestamp']}")
        # Simulate a transaction
        if network["contribution"] > 