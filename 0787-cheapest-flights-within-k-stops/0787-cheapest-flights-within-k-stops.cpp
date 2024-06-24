class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        constexpr int infinity = numeric_limits<int>::max();

        vector<int> prices(n, infinity);
        auto new_prices = prices;
        prices[src] = 0;

        for (size_t i=0; i<k+1; ++i) {
            for (const auto& row : flights) {
                const size_t a = row[0];
                const size_t b = row[1];
                const int cost = row[2];
                if (prices[a]==infinity) {
                    continue;
                }

                new_prices[b] = std::min(new_prices[b], prices[a]+cost);
            }
            prices = new_prices;
        }

        if (prices[dst] == infinity) return -1;
        return prices[dst];
    }
};