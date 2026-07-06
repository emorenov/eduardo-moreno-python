print("=" * 40)
print("   STREAMING SERVICE BUDGET CALCULATOR")
print("=" * 40)

name = input("What is your name? ")
print(f"\nHi {name}! Let's calculate your streaming budget.\n")

service_1_name = input("Enter your 1st streaming service: ")
service_1_cost = float(input(f"Monthly cost for {service_1_name}? $"))

service_2_name = input("Enter your 2nd streaming service: ")
service_2_cost = float(input(f"Monthly cost for {service_2_name}? $"))

service_3_name = input("Enter your 3rd streaming service: ")
service_3_cost = float(input(f"Monthly cost for {service_3_name}? $"))

months = int(input("\nHow many months do you want to calculate for? "))
budget_limit = 300

monthly_total = service_1_cost + service_2_cost + service_3_cost
grand_total = monthly_total * months
is_over_budget = grand_total > budget_limit

print()
print("=" * 40)
print(f"  {name}'s STREAMING BUDGET REPORT")
print("=" * 40)
print(f"{service_1_name}: ${service_1_cost:.2f} / mo")
print(f"{service_2_name}: ${service_2_cost:.2f} / mo")
print(f"{service_3_name}: ${service_3_cost:.2f} / mo")
print("-" * 40)
print(f"Monthly Total: ${monthly_total:.2f} / mo")
print(f"Total over {months} months: ${grand_total:.2f}")
print(f"Over ${budget_limit} budget? {is_over_budget}")
print("=" * 40)
