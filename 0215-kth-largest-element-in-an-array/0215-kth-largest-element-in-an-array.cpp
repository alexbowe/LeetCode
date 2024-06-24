#include <random>
#include <tuple>

std::default_random_engine generator;

template <class T>
T random_index(T lo, T hi) {
    std::uniform_int_distribution<T> distribution(lo,hi);
    return distribution(generator);
}

std::tuple<int, int>
partition(vector<int>& nums, size_t lo, size_t hi, size_t pivot_idx) {
    const auto pivot = nums[pivot_idx];
    size_t eq = lo;
    while (eq <= hi) {
        if (nums[eq]<pivot) { std::swap(nums[lo++],nums[eq++]); }
        else if (nums[eq]==pivot) { eq++; }
        else if (nums[eq]>pivot) { std::swap(nums[eq],nums[hi--]); }
    }
    return {lo, hi};
}

int quickselect(vector<int>& nums, int k, size_t lo, size_t hi) {
    size_t pivot_idx = random_index(lo, hi);
    auto [start,end] = partition(nums, lo, hi, pivot_idx);
    if (k < start) { return quickselect(nums, k, lo, start-1); }
    if (k > end) { return quickselect(nums, k, end+1, hi); }
    return nums[k];
}

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return quickselect(nums, nums.size()-k, 0, nums.size()-1);
    }
};
