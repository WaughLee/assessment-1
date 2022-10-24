from math import floor


def optimal_change(item_cost, amount_paid):
    if amount_paid < item_cost:
        return "Insufficient payment."
    elif item_cost == 0 or item_cost == amount_paid:
        return "No change due."

    # Change to cents in order to avoid decimal errors
    change_in_cents = (amount_paid * 100) - (item_cost * 100)

    # dictionary to store number of each currency to be given in change
    return_currencies = {}

    # Loop through currencies from highest to lowest.
    # The "floor" method is used to round numbers down to the nearest integer
    for x in currency_order:
        value = currency_amounts[x]
        num_to_give = floor(change_in_cents / value)
        remaining_change_due = change_in_cents % value
        if num_to_give >= 1:
            return_currencies[x] = num_to_give
            change_in_cents = remaining_change_due

    return final_text(item_cost, amount_paid, return_currencies)


currency_amounts = {
    '$100': 10000,
    '$50': 5000,
    '$20': 2000,
    '$10': 1000,
    '$5': 500,
    '$1': 100,
    'quarter': 25,
    'dime': 10,
    'nickel': 5,
    'penny': 1,
}

# Greatest to least amounts to cycle through.
currency_order = ['$100', '$50', '$20',
                  '$10', '$5', '$1', 'quarter', 'dime', 'nickel', 'penny']

# makes printed string with '$' and plural amounts when needed.


def final_text(item_cost, amount_paid, currency_map):
    result_message = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is"

    # separate coins from bills
    coins = ['quarter', 'dime', 'nickel', 'penny']

    for i in currency_order:
        if i in currency_map:
            number = currency_map[i]
            if i == 'penny' and number > 1:
                result_message += f" {number} pennies,"
            elif i in coins and number > 1:
                result_message += f" {number} {i}s,"
            elif number > 1:
                result_message += f" {number} {i} bills,"
            elif i in coins:
                result_message += f" {number} {i},"
            else:
                result_message += f" {number} {i} bill,"

    result_message = result_message[:-1] + "."
    # rfind to find the last occurrence of ',' if not found, returns -1
    index_last_comma = result_message.rfind(',')
    if index_last_comma > 0:
        result_message = result_message[0:index_last_comma +
                                        2] + "and " + result_message[index_last_comma + 2:]

    return result_message
