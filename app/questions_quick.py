# app/questions_quick.py
from app.recommender import recommend_blockchain, recommendations
from app.utils import print_result , print_header, ask_yes_no

# Mapping of quick mode recommendations with description and official sites
recommendations = {
    "ethereum": {
        "name": "Ethereum",
        "description": "Public blockchain, highly decentralized, supports smart contracts, tokens, and DeFi/NFT applications.",
        "website": "https://ethereum.org/"
    },
    "solana": {
        "name": "Solana",
        "description": "High-performance public blockchain ideal for fast transactions and scalable applications, especially for DeFi and apps requiring low latency.",
        "website": "https://solana.com/"
    },
    "polygon": {
        "name": "Polygon",
        "description": "EVM-compatible public blockchain with low fees and high scalability, ideal for NFTs and Layer-2 solutions.",
        "website": "https://polygon.technology/"
    },
    "hyperledger_fabric": {
        "name": "Hyperledger Fabric",
        "description": "Private, modular, enterprise-grade blockchain for confidential business processes. Highly customizable and permissioned.",
        "website": "https://www.hyperledger.org/use/fabric"
    },
    "hyperledger_besu": {
        "name": "Hyperledger Besu",
        "description": "Enterprise-focused permissioned blockchain with EVM compatibility. Supports private transactions and smart contracts.",
        "website": "https://www.hyperledger.org/use/besu"
    },
    "hybrid_layer2": {
        "name": "Hybrid / Layer-2 solutions",
        "description": "Use a combination of public and private blockchains. Layer-2 solutions like Rollups, sidechains, or hybrid setups allow scalability, privacy, and cost efficiency.",
        "website": "https://ethereum.org/en/developers/docs/scaling/"
    }
}

def run_quick_mode():
    print_header("Quick Mode")
    print("Answer 5 quick questions to get a blockchain recommendation.\n")

    # Ask the 5 quick yes/no questions
    q1 = ask_yes_no("Do you want your blockchain to be open and accessible to anyone?")
    q2 = ask_yes_no("Is high transaction speed more important than decentralization?")
    q3 = ask_yes_no("Will your project handle sensitive or private business data?")
    q4 = ask_yes_no("Do you plan to create or use tokens or NFTs?")
    q5 = ask_yes_no("Do you need compatibility with smart contracts?")

    # Determine recommendation key based on answers
    if q1 and not q3:
        if q4 and q5:
            key = "ethereum"
        elif not q4 and q2:
            key = "solana"
        else:
            key = "polygon"
    else:
        if q3 and not q1:
            if q5:
                key = "hyperledger_besu"
            else:
                key = "hyperledger_fabric"
        else:
            key = "hybrid_layer2"

    # Print enriched recommendation
    print_result(key)
    print_header("End of Quick Mode")
