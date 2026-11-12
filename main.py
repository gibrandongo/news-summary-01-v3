import os

SUMMARY = """World news, Wednesday 11 November 2026
1. Russia and Ukraine agreed the largest prisoner exchange of the war as US-mediated talks in Abu Dhabi ended with no ceasefire; the numbers, possibly 1,000 to 1,500 a side, are due Thursday. (AP)
2. Congo's Ebola outbreak passed 11,000 cases, with 11,042 infections and 5,387 deaths, making it the country's deadliest; the Bundibugyo virus has no approved vaccine or treatment. (AP)
3. The COP31 leaders' summit opened in Antalya, where UN chief Antonio Guterres warned slow climate action put the world on a path to destruction; 77 leaders were due to speak, with US, Chinese and Indian leaders absent. (AFP)
4. Iran designated Argentina's navy and air force terrorist organizations, retaliating for Buenos Aires designating the Revolutionary Guards in April; Argentina rejected the move. (Reuters)
5. US prosecutors charged three alleged Iran-backed operatives over nearly 20 plots in the US and Europe, including a September plot at RAF Fairford in England. (BBC)
6. NATO jets were scrambled twice overnight as suspected drones from Belarus crossed Lithuania, closing Vilnius and Kaunas airports; Latvia activated air defenses; the origin was unconfirmed. (LRT)
7. Democrat Scott Colom won Mississippi's US Senate race, beating Cindy Hyde-Smith by about 4,700 votes to become the state's first Black senator since 1881 and lift Democrats to 55 seats. (AP)
8. The US House voted 211-204 to send eight impeachment articles against Defense Secretary Pete Hegseth to committee, shelving it for this Congress. (BBC)
9. El Salvador said its forces and Haitian police destroyed the 400 Mawozo gang's headquarters in Haiti; the claim and a reported 20 dead were unverified. (BBC)
10. Asian shares fell after US October inflation rose 0.4%, above the 0.3% forecast, as Brent crude held near $92 amid tensions over Iran. (NDTV Profit)
11. Nine people were seriously hurt when a bus crashed into several vehicles in Seongnam, South Korea. (Yonhap)"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SUMMARY)


if __name__ == "__main__":
    main()
