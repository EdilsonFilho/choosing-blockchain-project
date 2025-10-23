# app/recommender.py

def recommend_blockchain(answers: list[bool]) -> str:
    """
    Given a list of boolean answers, returns a blockchain recommendation.
    """

    # Basic scoring weights
    score_public = sum(answers[i] for i in [0, 4, 5, 7, 13, 15, 23, 24])
    score_private = sum(answers[i] for i in [1, 2, 6, 9, 18, 20, 27, 29])
    score_enterprise = sum(answers[i] for i in [6, 9, 18, 20, 27, 28, 29])
    score_defi = sum(answers[i] for i in [12, 4, 15])
    score_nft = sum(answers[i] for i in [5, 16])

    # Decision logic
    if score_private > score_public:
        if answers[7]:  # Smart contracts
            return "Hyperledger Besu — Enterprise-focused, permissioned, and EVM-compatible."
        else:
            return "Hyperledger Fabric — Private, modular, and trusted for enterprise networks."

    if score_defi > 3:
        return "Ethereum — Public, decentralized, supports DeFi, tokens, and NFTs."

    if score_public > score_private and answers[3]:
        return "Solana — High performance, public, and suitable for large-scale apps."

    if answers[10]:
        return "Polkadot — Public, interoperable, and great for multi-chain ecosystems."

    if answers[5] or score_nft > 1:
        return "Polygon — EVM-compatible public chain, excellent for NFTs and scalability."

    return "Avalanche — Public, scalable, and supports multiple subnetworks and custom rules."
