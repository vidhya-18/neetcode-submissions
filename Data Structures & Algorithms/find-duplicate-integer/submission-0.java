

class Solution {
    public int findDuplicate(int[] nums) {
        HashMap<Integer, Integer> mpp = new HashMap<>();
        
        // Populate the map with frequencies
        for (Integer num : nums) {
            mpp.put(num, mpp.getOrDefault(num, 0) + 1);
        }

        // Find the duplicate
        for (Map.Entry<Integer, Integer> m : mpp.entrySet()) {
            if (m.getValue() > 1) {
                return m.getKey(); // No need for explicit casting as we use generics
            }
        }

        return -1;
    }
}
