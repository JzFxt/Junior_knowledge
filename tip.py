def main():
    print("Thank you for stopping by and using our service!")
    total_bill = float(input("How much was the total bill? (Hint: its in your receipt!): "))
    tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
    
    tip_amount = total_bill * (tip_percentage / 100)
    total_amount = total_bill + tip_amount
    
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Total Amount to Pay: ${total_amount:.2f}")
main()

def optional():
    other_service = input("If you don't want to tip, we also offer a gift card option. Would you like that instead? (Y/N): ")
    if other_service.lower() == 'y':
        gift_card_amount = float(input("Enter the amount for the gift card: "))
        print(f"Gift Card Amount: ${gift_card_amount:.2f}")
    if other_service.lower() == 'n':
        print("No gift card selected. Thank you for your visit!")
    elif other_service.lower() != 'y' and other_service.lower() != 'n':
        print("Invalid answer. Please enter either 'Y' for Yes or 'N' for No.")
optional()
