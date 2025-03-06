    square_meters_to_be_greened = float(input())
    price_for_total_square_meters = square_meters_to_be_greened * 7.61
    discount = price_for_total_square_meters * 0.18
    final_price = price_for_total_square_meters - discount

    print(f"The final price is: {final_price} lv.")
    print(f"The discount is: {discount} lv.")