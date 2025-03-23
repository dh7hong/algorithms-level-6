def solution(users, emoticons):
    # Discount rates we can apply
    discount_rates = [10, 20, 30, 40]
    
    # To store the best result: [max subscribers, max sales]
    best_result = [0, 0]
    
    # DFS to generate all combinations of discounts
    def dfs(idx, current_discounts):
        nonlocal best_result

        # Base case: all emoticons have a discount assigned
        if idx == len(emoticons):
            subscribers = 0
            total_sales = 0

            # Evaluate this discount combination for all users
            for discount_threshold, price_threshold in users:
                total_purchase = 0

                for i in range(len(emoticons)):
                    discount = current_discounts[i]
                    if discount >= discount_threshold:
                        price = emoticons[i] * (100 - discount) // 100
                        total_purchase += price

                # Decide if user subscribes or purchases
                if total_purchase >= price_threshold:
                    subscribers += 1
                else:
                    total_sales += total_purchase

            # Update the best result if it's better
            if subscribers > best_result[0]:
                best_result = [subscribers, total_sales]
            elif subscribers == best_result[0] and total_sales > best_result[1]:
                best_result = [subscribers, total_sales]
            return

        # Recursive step: try each discount rate at current index
        for rate in discount_rates:
            current_discounts.append(rate)
            dfs(idx + 1, current_discounts)
            current_discounts.pop()

    # Start DFS
    dfs(0, [])

    return best_result
