import math

def generate_frequencies():
    sum_freq = {}
    product_freq = {}
    combined_freq = {}

    for dice1 in range(1, 7):
        for dice2 in range(1, 7):
            sum_value = dice1 + dice2
            product_value = dice1 * dice2
            combined_identifier = f"{sum_value}-{product_value}"

            sum_freq[sum_value] = sum_freq.get(sum_value, 0) + 1
            product_freq[product_value] = product_freq.get(product_value, 0) + 1
            combined_freq[combined_identifier] = combined_freq.get(combined_identifier, 0) + 1

    return sum_freq, product_freq, combined_freq

def compute_entropy(distribution):
    total = sum(distribution.values())
    entropy_value = 0

    for freq in distribution.values():
        prob = freq / total
        entropy_value -= prob * math.log2(prob)

    return entropy_value

def main():
    sum_freq, product_freq, combined_freq = generate_frequencies()

    combined_entropy = compute_entropy(combined_freq)
    sum_entropy = compute_entropy(sum_freq)
    product_entropy = compute_entropy(product_freq)

    conditional_entropy = combined_entropy - sum_entropy
    mutual_info = product_entropy - conditional_entropy

    return [
        round(combined_entropy, 2),
        round(sum_entropy, 2),
        round(product_entropy, 2),
        round(conditional_entropy, 2),
        round(mutual_info, 2)
    ]


if __name__ == "__main__":
    results = main()
    print(results)
