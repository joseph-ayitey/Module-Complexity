/**
 * Finds common items between two arrays.
 *
* Time Complexity: O(n × m) — filter visits each of n items in firstArray, and
 *   includes() scans up to m items in secondArray for each one
 * Space Complexity: O(n) — the Set holds at most n items (size of firstArray)
 * Optimal Time Complexity: O(n + m) — convert secondArray to a Set (O(m)), then
 *   each lookup is O(1) instead of O(m), reducing the total to one pass each
 *
 * Refactor: build a Set from secondArray once (O(m)), then filter firstArray
 * using Set.has() (O(1) per lookup) instead of Array.includes() (O(m) per lookup).
 * This changes the nested O(n × m) work into linear O(n + m).
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => {
  const secondSet = new Set(secondArray);
  return [...new Set(firstArray.filter((item) => secondSet.has(item)))];
};
