/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
* Time Complexity: O(n²) — for each of n elements, the inner loop scans the
 *   uniqueItems list which grows up to n, making membership check O(n) each time
 * Space Complexity: O(n) — uniqueItems holds up to n elements
 * Optimal Time Complexity: O(n) — use a Set for O(1) membership checks instead
 *   of scanning an array
 *
 * Refactor: a Set tracks what we've seen (O(1) lookup). We iterate once,
 * appending only items not yet in the Set. Same O(n) space as before, but
 * time drops from O(n²) to O(n).
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const seen = new Set();
  const uniqueItems = [];

  for (const item of inputSequence) {
    if (!seen.has(item)) {
      seen.add(item);
      uniqueItems.push(item);
    }
  }

  return uniqueItems;
}
