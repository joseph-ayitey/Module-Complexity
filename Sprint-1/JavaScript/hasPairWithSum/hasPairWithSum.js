/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: O(n²) — for each of n elements we scan up to n-1 remaining
 *   elements, checking every possible pair
 * Space Complexity: O(1) — no extra data structures, just two index variables
 * Optimal Time Complexity: O(n) — one pass: for each number check if its
 *   complement (target - number) has already been seen
 *
 * Refactor: walk the array once. For each number x, if (target - x) is already
 * in the seen Set, a valid pair exists. Otherwise record x and move on.
 * Trades O(1) space for O(n) space, but cuts time from O(n²) to O(n).
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
   const seen = new Set();
  for (const num of numbers) {
    if (seen.has(target - num)) return true;
    seen.add(num);
  }
  return false;
}
