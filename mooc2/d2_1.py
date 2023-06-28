def calculate_max_meals(N, M, ingredients):
    max_meals = 0

    for i in range(N):
        X, Y, Sm, Pm, Sv, Pv = ingredients[i]
        
        # 작은 포장과 큰 포장을 최대한 활용하여 재료 구매
        max_small_packs = min(Y // Sm, X)
        max_large_packs = min((M - Y) // Sv, (X - max_small_packs))
        
        # 구매한 작은 포장과 큰 포장의 개수에 따른 총 비용 계산
        total_cost = max_small_packs * Pm + max_large_packs * Pv
        
        # 최대 식사 준비량 갱신
        max_meals = max(max_meals, min(max_small_packs + max_large_packs, X))

    return max_meals

# 입력 받기
N, M = map(int, input().split())
ingredients = []

# 재료 정보 입력 받기
for _ in range(N):
    X, Y, Sm, Pm, Sv, Pv = map(int, input().split())
    ingredients.append((X, Y, Sm, Pm, Sv, Pv))

# 최대 식사 준비량 계산
max_meals = calculate_max_meals(N, M, ingredients)
print(max_meals)