# ===========================================================
# 🔮 ARBITRAGE CALCULATOR — LOOP EDITION FOR MONSEIGNEUR 👑
# Runs continuously until exit code is entered (default: 999)
# ===========================================================

def arbitrage_calc(yes1, yes2, total_capital):

    p1 = yes1 / 100
    p2 = yes2 / 100

    print("\n==========================================================")
    print(" 🔮  ARBITRAGE CALCULATION BETWEEN TWO MARKETS  🔮")
    print("==========================================================\n")

    # Price summary
    print("📊 PRICE SUMMARY")
    print("----------------------------------------------------------")
    print(f"   🟦 Market 1 YES price : {yes1:.2f}%")
    print(f"   🟥 Market 2 YES price : {yes2:.2f}%")
    print("----------------------------------------------------------\n")

    # Two possible combinations
    scenarios = [
        ("YES market 1", p1, "NO market 2", 1 - p2),
        ("YES market 2", p2, "NO market 1", 1 - p1),
    ]

    profitable = None
    for yes_desc, yes_price, no_desc, no_price in scenarios:
        if yes_price + no_price < 1:
            profitable = (yes_desc, yes_price, no_desc, no_price, yes_price + no_price)
            break

    if profitable is None:
        print("⚠️ No arbitrage opportunity exists.\n")
        return

    yes_desc, yes_price, no_desc, no_price, cost = profitable

    print("✅ PROFITABLE ARBITRAGE FOUND!")
    print(f"   ➝ Combination: {yes_desc} + {no_desc}")
    print(f"   ➝ Combined cost: {cost:.3f}\n")

    # Optimal stake split
    S_yes = total_capital * (yes_price / cost)
    S_no  = total_capital * (no_price  / cost)

    # Payouts
    gain_yes = S_yes * (1 / yes_price)
    gain_no  = S_no  * (1 / no_price)

    profit_yes = gain_yes - total_capital
    profit_no  = gain_no  - total_capital

    guaranteed_profit = min(profit_yes, profit_no)
    guaranteed_return_pct = (guaranteed_profit / total_capital) * 100

    print("==========================================================")
    print(" 💰 OPTIMAL STAKES")
    print("==========================================================")
    print(f"   🟦 {yes_desc:<18} : {S_yes:.2f} $")
    print(f"   🟥 {no_desc:<18}  : {S_no:.2f} $")
    print(f"\n   💵 Total capital used : {total_capital:.2f} $\n")

    print("==========================================================")
    print(" 🚀 GUARANTEED PROFIT & RETURN")
    print("==========================================================")
    print(f"   💵 Guaranteed Profit : +{guaranteed_profit:.2f} $")
    print(f"   🌟 GUARANTEED RETURN : {guaranteed_return_pct:.2f} % 🌟\n")

    print("==========================================================")
    print(" 📎 DETAILS (compact)")
    print("==========================================================")
    print("   Formula: payout = stake × (100 / price%)\n")

    print(f"   ➝ If YES wins:  profit = {S_yes:.2f} × (100 / {yes_price*100:.2f}) − {total_capital:.2f}")
    print(f"                     = {profit_yes:.2f} $\n")

    print(f"   ➝ If NO wins :  profit = {S_no:.2f} × (100 / {no_price*100:.2f}) − {total_capital:.2f}")
    print(f"                     = {profit_no:.2f} $\n")

    print("   (Guaranteed profit = minimum of the two outcomes)")
    print("==========================================================\n")


# ===========================================================
# 🔁 MAIN LOOP
# ===========================================================
EXIT_CODE = "999"

while True:
    print("\n🔢 Enter market parameters (type 999 to exit):\n")

    yes1_input = input(" 👉 YES price market 1 (%) : ")
    if yes1_input == EXIT_CODE:
        print("\n👋 Exiting program. Goodbye, Monseigneur 👑\n")
        break

    yes2_input = input(" 👉 YES price market 2 (%) : ")
    if yes2_input == EXIT_CODE:
        print("\n👋 Exiting program. Goodbye, Monseigneur 👑\n")
        break

    capital_input = input(" 💵 Total capital invested ($) : ")
    if capital_input == EXIT_CODE:
        print("\n👋 Exiting program. Goodbye, Monseigneur 👑\n")
        break

    yes1 = float(yes1_input)
    yes2 = float(yes2_input)
    total_capital = float(capital_input)

    arbitrage_calc(yes1, yes2, total_capital)
