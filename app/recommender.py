# app/recommender.py

# Centralized recommendation dictionary
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
    "polkadot": {
        "name": "Polkadot",
        "description": "Public blockchain platform designed for interoperability, connecting multiple chains (parachains) in a scalable ecosystem.",
        "website": "https://polkadot.network/"
    },
    "avalanche": {
        "name": "Avalanche",
        "description": "Public, scalable blockchain supporting custom subnetworks, high throughput, and low fees.",
        "website": "https://www.avax.network/"
    },
    "hybrid_layer2": {
        "name": "Hybrid / Layer-2 solutions",
        "description": "Use a combination of public and private blockchains. Layer-2 solutions like Rollups, sidechains, or hybrid setups allow scalability, privacy, and cost efficiency.",
        "website": "https://ethereum.org/en/developers/docs/scaling/"
    }
}

def recommend_blockchain(answers: list[bool]) -> str:
    score_public = sum(answers[i] for i in [0,4,5,7,13,15,23,24])
    score_private = sum(answers[i] for i in [1,2,6,9,18,20,27,29])
    score_defi = sum(answers[i] for i in [12,4,15])
    score_nft = sum(answers[i] for i in [5,16])

    if score_private > score_public:
        return "hyperledger_besu" if answers[7] else "hyperledger_fabric"

    if score_defi > 3:
        return "ethereum"

    if score_public > score_private and answers[3]:
        return "solana"

    if answers[10]:
        return "polkadot"

    if answers[5] or score_nft > 1:
        return "polygon"

    # fallback: if it is not clear → Hybrid / Layer-2
    return "hybrid_layer2"



