public class BinarySearch {
    
    public static void main(System[] args){


        int[] nums = {-1,0,3,5,9,12};
        int target = 9;

        int ans = search(nums,target);

        if (ans != -1){
            System.out.println(target + " exists in nums and its index is " + ans);
        } else {
            System.out.println(target + " does not exist in nums so return " + ans);

        }

    }


    public static int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;
        int ans = -1;
        while (left <= right){
            int mid = (left+right)/2;
            if (nums[mid] == target){
                ans = mid;
                break;
            } else if (nums[mid] < target) {
                left = mid+1;
            } else {
                right = mid-1;
            }
        }

        return ans;
    }
}
