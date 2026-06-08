class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const num_index_map = new Map();
        for (let i =0; i< nums.length; i++){
            const diff = target - nums[i];
            if(num_index_map.has(diff)){
                return [num_index_map.get(diff), i];
            }

            num_index_map.set(nums[i], i);
        }
    }
}
