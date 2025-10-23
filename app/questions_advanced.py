# app/questions_advanced.py
from app.utils import ask_yes_no, print_header, print_result
from app.recommender import recommend_blockchain

def run_advanced_mode():
    print_header("Advanced Mode")
    print("Answer 30 technical questions to receive a detailed blockchain recommendation.\n")

    questions = [
        "Do you require your network to be fully decentralized?",
        "Will your participants be known and trusted entities?",
        "Do you plan to store private or confidential data?",
        "Is performance (transactions per second) a critical factor?",
        "Will your blockchain issue its own cryptocurrency or token?",
        "Do you need support for NFTs?",
        "Should your blockchain integrate easily with enterprise systems?",
        "Do you need smart contract functionality?",
        "Is on-chain governance important?",
        "Do you need a permissioned access model?",
        "Should your blockchain be interoperable with others?",
        "Will it operate across multiple legal jurisdictions?",
        "Do you plan to run DeFi applications?",
        "Do you require very low transaction costs?",
        "Do you prefer energy-efficient consensus mechanisms?",
        "Do you want a community-driven ecosystem?",
        "Is privacy-preserving computation (ZK proofs) important?",
        "Will you have identity management features?",
        "Do you plan to build enterprise-grade applications?",
        "Do you need high availability and scalability?",
        "Is regulatory compliance important?",
        "Do you need customizable consensus mechanisms?",
        "Will your project rely on oracles or external data?",
        "Do you need fast transaction finality?",
        "Do you want to support multiple smart contract languages?",
        "Do you prefer an EVM-compatible environment?",
        "Do you want open-source flexibility for custom modules?",
        "Will you use consortium-based governance?",
        "Is long-term stability more important than fast innovation?",
        "Do you require integration with IoT or supply chain systems?"
    ]

    answers = [ask_yes_no(q) for q in questions]
    result = recommend_blockchain(answers)
    print_result(result)
    print_header("End of Advanced Mode")
