// # Given an integer array nums, return true if any value appears at least twice in the array, 
// # and return false if every element is distinct.

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let seen = new Map();
    for (let num = 0; num < nums.length; num++) {
        if (seen.has(nums[num])) return true;
        seen.set(nums[num]);
    }
    return false;
    };