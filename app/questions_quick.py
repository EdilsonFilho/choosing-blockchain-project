# app/questions_quick.py
from app.recommender import recommend_blockchain, recommendations
from app.utils import print_result , print_header, ask_yes_no

def run_quick_mode():
    print_header("Quick Mode")
    print("Answer 5 quick questions to get a blockchain recommendation.\n")

    # Ask the 5 quick yes/no questions
    q1 = ask_yes_no("1) Do you want your blockchain to be open and accessible to anyone?")
    q2 = ask_yes_no("2) Is high transaction speed more important than decentralization?")
    q3 = ask_yes_no("3) Will your project handle sensitive or private business data?")
    q4 = ask_yes_no("4) Do you plan to create or use tokens or NFTs?")
    q5 = ask_yes_no("5) Do you need compatibility with smart contracts?")

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
