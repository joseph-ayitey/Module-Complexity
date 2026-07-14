/**
 * Calculate the sum and product of integers in a list
 *
 * Note: the "sum" is every number added together
 * and the "product" is every number multiplied together
 * so for example: [2, 3, 5] would return
 * {
 *   "sum": 10, // 2 + 3 + 5
 *   "product": 30 // 2 * 3 * 5
 * }
 *
* Time Complexity: O(n) — two sequential loops, each visiting n elements once (O(2n) = O(n))
 * Space Complexity: O(1) — only two accumulator variables, regardless of input size
 * Optimal Time Complexity: O(n) — every element must be visited at least once; can't do better
 *
 * Refactor: collapsed two loops into one. Big O doesn't change (still O(n)), but the
 * constant factor halves — we visit each element once instead of twice.
 * 
 * @param {Array<number>} numbers - Numbers to process
 * @returns {Object} Object containing running total and product
 */
export function calculateSumAndProduct(numbers) {
  let sum = 0;
 

  let product = 1;
  
  for (const num of numbers) {
    sum += num;
    product *= num;
  }

  return {
     sum, product
  };
}
