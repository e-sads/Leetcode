class Solution {

    public int maxArea(int[] height) {
       
        int max = 0;
        int val = 0;
        int left = 0;
        int right = height.length-1;
        if (height.length == 1){
            return 1;
        }

        while (right > left){
             
            val = Math.max(val, (right-left) * Math.min(height[left],height[right]));
            if (val > max){
                max = val;
            }
            if (height[left] > height[right]){
                right--;
            } else {
                left++;
            }
        }
        
        return max;
    }
}