# app/questions_quick.py
from app.utils import ask_yes_no, print_header, print_result

def run_quick_mode():
    print_header("Quick Mode")
    print("Answer 5 quick questions to get a blockchain recommendation.\n")

    q1 = ask_yes_no("Do you want your blockchain to be open and accessible to anyone?")
    q2 = ask_yes_no("Is high transaction speed more important than decentralization?")
    q3 = ask_yes_no("Will your project handle sensitive or private business data?")
    q4 = ask_yes_no("Do you plan to create or use tokens or NFTs?")
    q5 = ask_yes_no("Do you need compatibility with smart contracts?")

    # Simple decision logic
    if q1 and not q3:
        if q4 and q5:
            print_result("Recommended Blockchain: Ethereum — Public, supports tokens and smart contracts.")
        elif not q4 and q2:
            print_result("Recommended Blockchain: Solana — Public, high performance, ideal for scalable apps.")
        else:
            print_result("Recommended Blockchain: Polygon — Public, EVM-compatible and cost-efficient.")
    else:
        if q3 and not q1:
            if q5:
                print_result("Recommended Blockchain: Hyperledger Besu — Private, permissioned, supports smart contracts.")
            else:
                print_result("Recommended Blockchain: Hyperledger Fabric — Private, modular, enterprise-grade.")
        else:
            print_result("Recommended Blockchain: Hybrid solution — consider Layer-2 or sidechain approaches.")

    print_header("End of Quick Mode")
