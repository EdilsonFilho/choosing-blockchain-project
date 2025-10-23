# app/questions_advanced.py
from app.utils import ask_yes_no, print_header, print_result
from app.recommender import recommend_blockchain

def run_advanced_mode():
    print_header("Advanced Mode")
    print("Answer 30 technical questions to receive a detailed blockchain recommendation.\n")

    questions = [
        "1) Do you require your network to be fully decentralized?",
        "2) Will your participants be known and trusted entities?",
        "3) Do you plan to store private or confidential data?",
        "4) Is performance (transactions per second) a critical factor?",
        "5) Will your blockchain issue its own cryptocurrency or token?",
        "6) Do you need support for NFTs?",
        "7) Should your blockchain integrate easily with enterprise systems?",
        "8) Do you need smart contract functionality?",
        "9) Is on-chain governance important?",
        "10) Do you need a permissioned access model?",
        "11) Should your blockchain be interoperable with others?",
        "12) Will it operate across multiple legal jurisdictions?",
        "13) Do you plan to run DeFi applications?",
        "14) Do you require very low transaction costs?",
        "15) Do you prefer energy-efficient consensus mechanisms?",
        "16) Do you want a community-driven ecosystem?",
        "17) Is privacy-preserving computation (ZK proofs) important?",
        "18) Will you have identity management features?",
        "19) Do you plan to build enterprise-grade applications?",
        "20) Do you need high availability and scalability?",
        "21) Is regulatory compliance important?",
        "22) Do you need customizable consensus mechanisms?",
        "23) Will your project rely on oracles or external data?",
        "24) Do you need fast transaction finality?",
        "25) Do you want to support multiple smart contract languages?",
        "26) Do you prefer an EVM-compatible environment?",
        "27) Do you want open-source flexibility for custom modules?",
        "28) Will you use consortium-based governance?",
        "29) Is long-term stability more important than fast innovation?",
        "30) Do you require integration with IoT or supply chain systems?"
    ]

    answers = [ask_yes_no(q) for q in questions]
    result = recommend_blockchain(answers)
    print_result(result)
    print_header("End of Advanced Mode")
