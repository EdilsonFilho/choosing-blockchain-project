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
    }
}

def recommend_blockchain(answers: list[bool]) -> str:
    """
    Given a list of boolean answers, returns the key of the recommended blockchain.
    The key corresponds to the 'recommendations' dictionary.
    """

    # Basic scoring weights
    score_public = sum(answers[i] for i in [0, 4, 5, 7, 13, 15, 23, 24])
    score_private = sum(answers[i] for i in [1, 2, 6, 9, 18, 20, 27, 29])
    score_enterprise = sum(answers[i] for i in [6, 9, 18, 20, 27, 28, 29])
    score_defi = sum(answers[i] for i in [12, 4, 15])
    score_nft = sum(answers[i] for i in [5, 16])

    # Decision logic returns the key
    if score_private > score_public:
        if answers[7]:  # Smart contracts
            return "hyperledger_besu"
        else:
            return "hyperledger_fabric"

    if score_defi > 3:
        return "ethereum"

    if score_public > score_private and answers[3]:
        return "solana"

    if answers[10]:
        return "polkadot"

    if answers[5] or score_nft > 1:
        return "polygon"

    return "avalanche"
