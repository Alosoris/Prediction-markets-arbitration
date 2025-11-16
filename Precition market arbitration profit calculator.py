def calcul_arbitrage(yes1, yes2, capital_total):
    """
    yes1, yes2 : cotes en % (prix du contrat YES sur chaque marché)
    capital_total : capital total disponible en dollars
    """

    # Conversion en prix décimaux (0-1)
    p1 = yes1 / 100
    p2 = yes2 / 100

    scenarios = [
        ("YES on market 1", p1, "NO on market 2", 1 - p2),
        ("YES on market 2", p2, "NO on market 1", 1 - p1)
    ]

    arbitrages = []

    for desc_yes, price_yes, desc_no, price_no in scenarios:
        total_cost = price_yes + price_no
        if total_cost < 1:
            profit_ratio = 1 - total_cost
            roi = profit_ratio / total_cost

            # Proportion optimale des mises
            # On répartit le capital proportionnellement aux coûts pour que le payout soit identique
            part_yes = price_yes / total_cost
            part_no = price_no / total_cost

            mise_yes = capital_total * part_yes
            mise_no = capital_total * part_no

            payout = capital_total / total_cost  # Montant récupéré garanti
            profit_total = payout - capital_total
            rendement_pct = (profit_total / capital_total) * 100

            arbitrages.append({
                "combo": f"{desc_yes} ({price_yes*100:.1f}%) + {desc_no} ({price_no*100:.1f}%)",
                "mise_yes": mise_yes,
                "mise_no": mise_no,
                "rendement_pct": rendement_pct,
                "profit": profit_total
            })

    # Affichage des résultats
    if not arbitrages:
        print("\n⚠️ No arbitration detected : the combinations cost ≥ 1 $.")
    else:
        print("\n=== POSSIBLE ARBITRATIONS ===")
        for arb in arbitrages:
            print(f"\nCombination : {arb['combo']}")
            print(f"→ Bet on the first market : {arb['mise_yes']:.2f} $")
            print(f"→ Bet on the second market : {arb['mise_no']:.2f} $")
            print(f"→ Profit : {arb['profit']:.2f} $")
            print(f"→ Return : {arb['rendement_pct']:.2f} %")
            print("!!! Verify that the platform fees are not too high and that the market has enough liquidity !!!")

# =====================
# Exemple d'utilisation
# =====================
yes1=0
while yes1!=2703:
    if yes1!=2703:
        yes1 = float(input("Enter the odds (%) of market 1 for 'YES' (enter 2703 to leave the program): "))
        yes2 = float(input("Enter the odds (%) of market 2 for 'YES' : "))
        capital_total = float(input("Betting amount ($) : "))

        calcul_arbitrage(yes1, yes2, capital_total)
    else:
        print("You left the program")
